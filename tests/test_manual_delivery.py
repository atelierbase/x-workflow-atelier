"""Manual additions must select one ID without resending an earlier post."""

import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
