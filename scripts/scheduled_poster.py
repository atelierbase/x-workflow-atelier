#!/usr/bin/env python3
"""
Atelier Base / ひろ｜AI実業家 - Scheduled X Poster

pending.md から現在の時間帯に該当する次の投稿を取り出して X に投稿し、
posted.md に移動する。

対応する投稿タイプ:
  - 単発: 文面を1本投稿
  - コメント仕込み: メイン投稿 → セルフリプライでコメントを連投
  - 画像付き: 画像ファイルがあれば添付
    - REQUIRE_IMAGE=1 の場合、画像を添付できなければ投稿せず失敗する

GitHub Actions / ローカル launchd / cron / 手動実行 すべてに対応。

認証情報の取得順:
  1. 環境変数（X_CONSUMER_KEY 等）→ GitHub Actions 用
  2. ~/.config/x-workflow/x-credentials.json → ローカル用

Usage:
    python3 scheduled_poster.py [--dry-run]
"""

import argparse
import json
import os
import random
import re
import shlex
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path


# === パス定義 ===
# GitHub Actions / ローカル / Codex worktree のどこで実行しても、このスクリプトが
# 置かれているリポジトリを正とする。
SKILL_DIR = Path(__file__).resolve().parent.parent

PENDING = SKILL_DIR / "storage" / "stocks" / "pending.md"
POSTED = SKILL_DIR / "storage" / "stocks" / "posted.md"
CREDS = Path.home() / ".config" / "x-workflow" / "x-credentials.json"
ENV_FILE = Path.home() / ".config" / "sns-auto-post" / "env"
LOG_DIR = SKILL_DIR / "storage" / "analytics"
LOG = LOG_DIR / "scheduler.log"
# 日×枠ごとの投稿済みマーカー（冗長クロンの二重投稿を防ぐ冪等ガード用）
STATE = LOG_DIR / "post-state.json"

# === タイムゾーン: JST 固定 ===
JST = timezone(timedelta(hours=9))


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(JST).isoformat()
    line = f"{now} {msg}"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


def _today() -> str:
    return datetime.now(JST).strftime("%Y-%m-%d")


def load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def already_posted(slot: str) -> bool:
    """この日×この枠が既に投稿済みなら True（冗長クロンの二重投稿を防ぐ）。"""
    return slot in load_state().get(_today(), [])


def mark_posted(slot: str) -> None:
    """この日×この枠を投稿済みとして記録。直近14日分のみ保持。"""
    st = load_state()
    st.setdefault(_today(), [])
    if slot not in st[_today()]:
        st[_today()].append(slot)
    for k in sorted(st.keys())[:-14]:
        del st[k]
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")


def err_detail(e: Exception) -> str:
    """例外から X API の生レスポンス本文を取り出す（403 の本当の理由を残すため）。"""
    resp = getattr(e, "response", None)
    if resp is None:
        return ""
    try:
        return f" status={resp.status_code} body={resp.text[:500]}"
    except Exception:
        return ""


def is_transient(e: Exception) -> bool:
    """一過性（リトライする価値あり）のエラーか。429/5xx と、今朝のような瞬間的 403 を含む。"""
    status = getattr(getattr(e, "response", None), "status_code", None)
    return status in (403, 429, 500, 502, 503, 504)


def post_main_with_retry(make_call, attempts: int = 3):
    """メイン投稿を一過性エラーに対して指数バックオフでリトライする。"""
    for i in range(1, attempts + 1):
        try:
            return make_call()
        except Exception as e:
            log(f"main post attempt {i}/{attempts} failed: {e}{err_detail(e)}")
            if i < attempts and is_transient(e):
                time.sleep(min(60, 10 * i))
                continue
            raise


def load_env_file() -> None:
    """ローカルAutomation用の非公開envファイルを読む。既存の環境変数は上書きしない。"""
    if not ENV_FILE.exists():
        return
    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            parts = shlex.split(line, comments=True, posix=True)
        except ValueError:
            continue
        if parts and parts[0] == "export":
            parts = parts[1:]
        for part in parts:
            if "=" not in part:
                continue
            key, value = part.split("=", 1)
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                os.environ.setdefault(key, value)


def load_credentials() -> dict:
    """環境変数優先、なければファイルから読む"""
    if os.getenv("X_CONSUMER_KEY"):
        log("credentials: env vars")
        return {
            "consumer_key": os.environ["X_CONSUMER_KEY"],
            "consumer_secret": os.environ["X_CONSUMER_SECRET"],
            "access_token": os.environ["X_ACCESS_TOKEN"],
            "access_token_secret": os.environ["X_ACCESS_TOKEN_SECRET"],
        }
    log(f"credentials: file {CREDS}")
    with open(CREDS, encoding="utf-8") as f:
        return json.load(f)


def current_slot() -> str:
    """JST の時間帯を判定"""
    hour = datetime.now(JST).hour
    if 6 <= hour < 11:
        return "朝"
    elif 11 <= hour < 15:
        return "昼"
    else:
        return "夜"


def parse_main_and_comments(raw_text: str):
    """文面を「メイン」と「コメント群」に分割する。

    区切りは `--- コメント1 ---` `--- コメント ---` のような行。
    コメント仕込みでない場合は comments=[] を返す。
    """
    segments = re.split(r"\n-{2,}\s*コメント\s*\d*\s*-{2,}\s*\n", raw_text)
    main = segments[0].strip()
    comments = [s.strip() for s in segments[1:] if s.strip()]
    return main, comments


def resolve_image(target_post: str):
    """画像ファイルパスを解決する。存在しなければ None（フォールバック）。"""
    m = re.search(r"-\s*画像ファイル:\s*(\S+)", target_post)
    if not m:
        return None
    rel = m.group(1).strip()
    path = (SKILL_DIR / rel).resolve()
    if path.exists():
        return path
    log(f"画像ファイル指定あり ({rel}) だが未配置")
    return None


def main(dry_run: bool = False) -> None:
    load_env_file()

    # POST_SLOT（起動cronから決まる固定スロット）があれば優先。
    # 無い時（手動dispatch等）のみ実行時刻から判定する。
    # → GitHub Actions の発火時刻ズレで「夜投稿が朝に出る」のを防ぐ。
    slot = os.getenv("POST_SLOT") or current_slot()
    log(f"START slot={slot} (source={'POST_SLOT' if os.getenv('POST_SLOT') else 'clock'}) dry_run={dry_run} pending={PENDING}")

    # 冪等ガード: 同じ日×同じ枠が既に投稿済みなら何もしない。
    # → 冗長クロン（各枠を複数回発火させてドロップ対策）でも二重投稿しない。
    if not dry_run and not os.getenv("ALLOW_DUPLICATE_SLOT") and already_posted(slot):
        log(f"SKIP slot={slot} は本日すでに投稿済み（冗長クロンの重複起動）")
        sys.exit(0)

    # ジッター（凍結リスク回避のため 0〜15 分のランダム遅延）
    # SKIP_JITTER=1 ならスキップ（直投稿モード=Routineが正確な時刻で発火するので不要）。
    if not dry_run and not os.getenv("SKIP_JITTER"):
        jitter = random.randint(0, 15 * 60)
        log(f"jitter={jitter}s")
        time.sleep(jitter)

    # 認証情報読み込み
    try:
        creds = load_credentials()
    except Exception as e:
        log(f"FAILED to load credentials: {e}")
        sys.exit(1)

    # pending.md 読み込み
    try:
        with open(PENDING, encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        log(f"FAILED to read pending: {e}")
        sys.exit(1)

    # ストックエントリーを分割
    parts = re.split(r"\n(?=## \d{4}-\d{2}-\d{2}-\d{3})", content)
    if len(parts) < 2:
        log("No pending posts.")
        if os.getenv("REQUIRE_PENDING") == "1":
            log("REQUIRE_PENDING=1; failing because the generation queue is empty")
            sys.exit(2)
        sys.exit(0)

    header = parts[0]
    posts = parts[1:]

    # 該当時間帯のストックを探す
    target_idx = None
    for i, post in enumerate(posts):
        if f"投稿想定時刻: {slot}" in post:
            target_idx = i
            break

    if target_idx is None:
        log(f"No pending post for slot={slot}")
        if os.getenv("REQUIRE_PENDING") == "1":
            log(f"REQUIRE_PENDING=1; failing because no post is queued for slot={slot}")
            sys.exit(2)
        sys.exit(0)

    target_post = posts[target_idx]

    # 文面抽出
    match = re.search(
        r"- 文面:\s*\n+(.+?)\n+- ステータス:", target_post, re.DOTALL
    )
    if not match:
        log("Failed to parse text from post")
        sys.exit(1)

    type_match = re.search(r"-\s*種類:\s*(\S+)", target_post)
    post_type = type_match.group(1) if type_match else "単発"

    raw_text = match.group(1).strip()
    main_text, comments = parse_main_and_comments(raw_text)
    image_path = resolve_image(target_post)
    require_image = os.getenv("REQUIRE_IMAGE") == "1" or post_type == "画像付き"
    log(
        f"Tweet preview: {main_text[:30]}... ({len(main_text)} chars), "
        f"comments={len(comments)}, image={'yes' if image_path else 'no'}"
    )

    if require_image and not image_path:
        log("REQUIRE_IMAGE=1 but no usable image file was found; aborting before post")
        sys.exit(1)

    if dry_run:
        log("DRY RUN - skipping actual post")
        print(f"\n--- DRY RUN: would post ---\n[MAIN]\n{main_text}")
        for i, c in enumerate(comments, 1):
            print(f"[COMMENT {i}]\n{c}")
        if image_path:
            print(f"[IMAGE] {image_path}")
        print("---")
        return

    # 投稿実行
    try:
        import tweepy
    except ImportError:
        log("ERROR: tweepy not installed. Run: pip install tweepy")
        sys.exit(1)

    try:
        client = tweepy.Client(
            consumer_key=creds["consumer_key"],
            consumer_secret=creds["consumer_secret"],
            access_token=creds["access_token"],
            access_token_secret=creds["access_token_secret"],
        )

        # 画像があれば v1.1 media/upload でアップロードする。
        # REQUIRE_IMAGE=1 の場合、失敗時に本文のみ投稿へフォールバックしない。
        media_ids = None
        if image_path:
            try:
                auth = tweepy.OAuth1UserHandler(
                    creds["consumer_key"],
                    creds["consumer_secret"],
                    creds["access_token"],
                    creds["access_token_secret"],
                )
                api_v1 = tweepy.API(auth)
                media = api_v1.media_upload(filename=str(image_path))
                media_ids = [media.media_id_string]
                log(f"media uploaded id={media.media_id_string}")
            except Exception as e:
                if require_image:
                    log(f"media upload failed and REQUIRE_IMAGE=1; aborting: {e}")
                    sys.exit(1)
                log(f"media upload failed, posting text-only: {e}")
                media_ids = None

        # メイン投稿（一過性エラーはリトライ）
        response = post_main_with_retry(
            lambda: client.create_tweet(text=main_text, media_ids=media_ids)
        )
        tweet_id = response.data["id"]
        log(f"POSTED main tweet_id={tweet_id}")
    except Exception as e:
        # メイン投稿が出ていない＝この枠は未消費。次の冗長クロンが再試行する。
        log(f"POST FAILED (main): {e}{err_detail(e)}")
        sys.exit(1)

    # ここから先はメイン投稿成功済み。コメントが失敗しても枠は消費して確定させる
    # （でないと次の冗長クロンがメインを二重投稿してしまう）。
    reply_to = tweet_id
    comment_ids = []
    for i, comment in enumerate(comments, 1):
        try:
            time.sleep(2)
            cresp = client.create_tweet(text=comment, in_reply_to_tweet_id=reply_to)
            cid = cresp.data["id"]
            comment_ids.append(cid)
            reply_to = cid
            log(f"POSTED comment {i} tweet_id={cid}")
        except Exception as e:
            log(f"COMMENT {i} FAILED (本文は投稿済み・続行): {e}{err_detail(e)}")
            break

    # この日×この枠を投稿済みとして記録（冪等ガード用）
    mark_posted(slot)

    # posted.md に追記
    id_match = re.search(r"## (\d{4}-\d{2}-\d{2}-\d{3})", target_post)
    post_id = id_match.group(1) if id_match else "unknown"
    runner = "GitHub Actions" if os.getenv("GITHUB_ACTIONS") else "ローカル"
    extra = ""
    if comment_ids:
        extra += "- comment_ids: " + ", ".join(comment_ids) + "\n"
    if image_path:
        extra += f"- 画像: {image_path.name}\n"
    posted_entry = f"""
## {post_id}（自動配信 / {runner}）
- 種類: {post_type}
- 投稿日時: {datetime.now(JST).isoformat()}
- 配信モード: api（{runner} + tweepy）
- tweet_id: {tweet_id}
- URL: https://twitter.com/AtelierBase_own/status/{tweet_id}
{extra}- 文面:

{raw_text}

- ステータス: posted

---
"""

    with open(POSTED, "a", encoding="utf-8") as f:
        f.write(posted_entry)

    # pending.md から該当エントリを削除
    posts.pop(target_idx)
    new_content = header + "\n".join(posts) if posts else header
    with open(PENDING, "w", encoding="utf-8") as f:
        f.write(new_content)

    log(f"DONE moved {post_id} to posted (type={post_type})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="投稿せずに動作確認")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
