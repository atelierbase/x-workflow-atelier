"""Manual additions must select one ID without resending an earlier post."""

import contextlib
import io
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import scheduled_poster as poster


class ManualDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.pending = root / "pending.md"
        self.posted = root / "posted.md"
        self.pending.write_text("# queue\n\n" + "\n".join(
            f"## 2030-01-01-{n}\n- 投稿想定時刻: 夜\n- 種類: 画像付き\n"
            f"- 文面:\n\n{text}\n\n- ステータス: pending\n\n---\n"
            for n, text in [(703, "FIRST"), (704, "SECOND")]
        ))
        self.posted.write_text("# posted\n")
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        for name, value in [("PENDING", self.pending), ("POSTED", self.posted)]:
            self.stack.enter_context(patch.object(poster, name, value))
        self.stack.enter_context(patch.object(poster, "log"))
        self.stack.enter_context(patch.object(poster, "load_env_file"))
        self.stack.enter_context(patch.object(poster, "already_posted", return_value=True))
        self.stack.enter_context(patch.object(poster, "resolve_image", return_value=Path("image.png")))
        self.stack.enter_context(patch.object(poster, "load_credentials", side_effect=AssertionError("No live auth in tests")))
        self.stack.enter_context(patch.dict("os.environ", {"POST_SLOT": "夜", "SKIP_JITTER": "1"}))

    def test_normal_dispatch_still_respects_the_daily_slot(self):
        with self.assertRaises(SystemExit) as result:
            poster.main()
        self.assertEqual(result.exception.code, 0)

    def test_explicit_id_previews_only_the_requested_post(self):
        before = self.pending.read_text()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            poster.main(dry_run=True, requested_post_id="2030-01-01-704")
        self.assertIn("SECOND", output.getvalue())
        self.assertNotIn("FIRST", output.getvalue())
        self.assertEqual(self.pending.read_text(), before)

    def test_same_id_cannot_be_sent_twice(self):
        self.posted.write_text("## 2030-01-01-704（自動配信 / GitHub Actions）\n")
        with self.assertRaises(SystemExit) as result:
            poster.main(requested_post_id="2030-01-01-704")
        self.assertEqual(result.exception.code, 0)

    def test_missing_id_does_not_fall_back_to_another_post(self):
        with self.assertRaises(SystemExit) as result:
            poster.main(dry_run=True, requested_post_id="2030-01-01-705")
        self.assertEqual(result.exception.code, 2)

    def test_wrong_slot_does_not_send_the_requested_id(self):
        with patch.dict("os.environ", {"POST_SLOT": "朝"}):
            with self.assertRaises(SystemExit) as result:
                poster.main(dry_run=True, requested_post_id="2030-01-01-704")
        self.assertEqual(result.exception.code, 2)

    def test_sending_first_post_keeps_next_post_dispatchable(self):
        self.pending.write_text(self.pending.read_text().replace("# queue\n\n", "# queue\n\n---\n", 1))
        root = self.pending.parent
        (root / "config").mkdir()
        (root / "config" / "account.json").write_text('{"user_id":"123"}')
        tweepy = MagicMock()
        client = tweepy.Client.return_value
        client.get_me.return_value = SimpleNamespace(data=SimpleNamespace(id="123", username="test"))
        client.create_tweet.side_effect = [SimpleNamespace(data={"id": "one"}), SimpleNamespace(data={"id": "two"})]
        tweepy.API.return_value.media_upload.return_value = SimpleNamespace(media_id_string="image")
        creds = dict.fromkeys(("consumer_key", "consumer_secret", "access_token", "access_token_secret"), "test")
        with patch.dict(sys.modules, {"tweepy": tweepy}), \
             patch.object(poster, "SKILL_DIR", root), \
             patch.object(poster, "load_credentials", return_value=creds), \
             patch.object(poster, "mark_posted"):
            poster.main(requested_post_id="2030-01-01-703")
            self.assertIn("\n## 2030-01-01-704\n", self.pending.read_text())
            poster.main(requested_post_id="2030-01-01-704")
        self.assertEqual([call.kwargs["text"] for call in client.create_tweet.call_args_list], ["FIRST", "SECOND"])
        self.assertNotIn("## 2030-01-01-", self.pending.read_text())


if __name__ == "__main__":
    unittest.main()
