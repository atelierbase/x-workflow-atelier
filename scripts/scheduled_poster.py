#!/usr/bin/env python3
"""
Atelier Base / アトリエの店主 - Scheduled X Poster

pending.md から現在の時間帯に該当する次の投稿を取り出して X に投稿し、
posted.md に移動する。

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
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path


# === パス定義（環境によって自動切替）===
if os.getenv("GITHUB_ACTIONS"):
    # GitHub Actions: リポジトリルートを起点に
    SKILL_DIR = Path(__file__).resolve().parent.parent
else:
    # ローカル: ~/.claude/skills/x-workflow/
    SKILL_DIR = Path.home() / ".claude" / "skills" / "x-workflow"

PENDING = SKILL_DIR / "storage" / "stocks" / "pending.md"
POSTED = SKILL_DIR / "storage" / "stocks" / "posted.md"
CREDS = Path.home() / ".config" / "x-workflow" / "x-credentials.json"
LOG_DIR = SKILL_DIR / "storage" / "analytics"
LOG = LOG_DIR / "scheduler.log"

# === タイムゾーン: JST 固定 ===
JST = timezone(timedelta(hours=9))


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(JST).isoformat()
    line = f"{now} {msg}"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


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


def main(dry_run: bool = False) -> None:
    slot = current_slot()
    log(f"START slot={slot} dry_run={dry_run} pending={PENDING}")

    # ジッター（凍結リスク回避のため 0〜15 分のランダム遅延）
    if not dry_run:
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
        sys.exit(0)

    target_post = posts[target_idx]

    # 文面抽出
    match = re.search(
        r"- 文面:\s*\n+(.+?)\n+- ステータス:", target_post, re.DOTALL
    )
    if not match:
        log("Failed to parse text from post")
        sys.exit(1)

    tweet_text = match.group(1).strip()
    log(f"Tweet preview: {tweet_text[:30]}... ({len(tweet_text)} chars)")

    if dry_run:
        log("DRY RUN - skipping actual post")
        print(f"\n--- DRY RUN: would post ---\n{tweet_text}\n---")
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
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data["id"]
        log(f"POSTED tweet_id={tweet_id}")
    except Exception as e:
        log(f"POST FAILED: {e}")
        sys.exit(1)

    # posted.md に追記
    id_match = re.search(r"## (\d{4}-\d{2}-\d{2}-\d{3})", target_post)
    post_id = id_match.group(1) if id_match else "unknown"

    runner = "GitHub Actions" if os.getenv("GITHUB_ACTIONS") else "ローカル"
    posted_entry = f"""
## {post_id}（自動配信 / {runner}）
- 種類: 単発
- 投稿日時: {datetime.now(JST).isoformat()}
- 配信モード: api（{runner} + tweepy）
- tweet_id: {tweet_id}
- URL: https://twitter.com/status/{tweet_id}
- 文面:

{tweet_text}

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

    log(f"DONE moved {post_id} to posted")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="投稿せずに動作確認")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
