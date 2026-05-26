#!/usr/bin/env python3
"""
Threads Scheduled Poster

pending_threads.md から該当時間帯のストックを取り出して Threads に投稿し、
posted.md に移動する。GitHub Actions / ローカル両対応。

認証情報の取得順:
  1. 環境変数（THREADS_ACCESS_TOKEN / THREADS_USER_ID）→ GitHub Actions 用
  2. ~/.config/threads-workflow/threads-credentials.json → ローカル用

Usage:
    python3 threads_poster.py [--dry-run] [--skip-jitter]

Threads API:
    https://graph.threads.net/v1.0/{user-id}/threads (コンテナ作成)
    https://graph.threads.net/v1.0/{user-id}/threads_publish (公開)
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

import requests


# === パス定義（環境によって自動切替）===
if os.getenv("GITHUB_ACTIONS"):
    REPO_DIR = Path(__file__).resolve().parent.parent
else:
    REPO_DIR = Path.home() / "atlier-base-v1" / "x-workflow-repo"

PENDING = REPO_DIR / "storage" / "stocks" / "pending_threads.md"
POSTED = REPO_DIR / "storage" / "stocks" / "posted.md"
CREDS = Path.home() / ".config" / "threads-workflow" / "threads-credentials.json"
LOG_DIR = REPO_DIR / "storage" / "analytics"
LOG = LOG_DIR / "scheduler_threads.log"

JST = timezone(timedelta(hours=9))
THREADS_TEXT_LIMIT = 500


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = f"{datetime.now(JST).isoformat()} [threads] {msg}"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


def load_credentials() -> dict:
    if os.getenv("THREADS_ACCESS_TOKEN"):
        log("credentials: env vars")
        return {
            "access_token": os.environ["THREADS_ACCESS_TOKEN"],
            "user_id": os.environ["THREADS_USER_ID"],
        }
    log(f"credentials: file {CREDS}")
    with open(CREDS, encoding="utf-8") as f:
        return json.load(f)


def current_slot() -> str:
    hour = datetime.now(JST).hour
    if 6 <= hour < 11:
        return "朝"
    elif 11 <= hour < 15:
        return "昼"
    else:
        return "夜"


def post_to_threads(text: str, access_token: str, user_id: str) -> str:
    """Threads API でテキスト投稿。投稿IDを返す。"""
    base_url = f"https://graph.threads.net/v1.0/{user_id}"

    # Step 1: Media Container 作成
    container_resp = requests.post(
        f"{base_url}/threads",
        data={
            "media_type": "TEXT",
            "text": text,
            "access_token": access_token,
        },
        timeout=30,
    )
    if not container_resp.ok:
        log(f"Container creation failed: {container_resp.status_code} {container_resp.text}")
        container_resp.raise_for_status()
    container_id = container_resp.json()["id"]
    log(f"container_id={container_id}")

    # Meta 推奨: コンテナが処理されるのを少し待つ
    time.sleep(3)

    # Step 2: 公開
    publish_resp = requests.post(
        f"{base_url}/threads_publish",
        data={
            "creation_id": container_id,
            "access_token": access_token,
        },
        timeout=30,
    )
    if not publish_resp.ok:
        log(f"Publish failed: {publish_resp.status_code} {publish_resp.text}")
        publish_resp.raise_for_status()
    thread_id = publish_resp.json()["id"]
    return thread_id


def main(dry_run: bool = False, skip_jitter: bool = False) -> None:
    slot = current_slot()
    log(f"START slot={slot} dry_run={dry_run} skip_jitter={skip_jitter}")

    # ジッター
    if not dry_run and not skip_jitter and not os.getenv("SKIP_JITTER"):
        jitter = random.randint(0, 15 * 60)
        log(f"jitter={jitter}s")
        time.sleep(jitter)

    # 認証情報
    try:
        creds = load_credentials()
    except Exception as e:
        log(f"FAILED to load credentials: {e}")
        sys.exit(1)

    # pending_threads.md
    if not PENDING.exists():
        log(f"pending_threads.md がありません: {PENDING}")
        sys.exit(0)

    with open(PENDING, encoding="utf-8") as f:
        content = f.read()

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

    text = match.group(1).strip()
    log(f"Text preview: {text[:30]}... ({len(text)} chars)")

    if len(text) > THREADS_TEXT_LIMIT:
        log(f"WARNING: text exceeds 500 char limit ({len(text)} chars)")

    if dry_run:
        log("DRY RUN - skipping actual post")
        print(f"\n--- DRY RUN: would post to Threads ---\n{text}\n---")
        return

    # 投稿
    try:
        thread_id = post_to_threads(text, creds["access_token"], creds["user_id"])
        log(f"POSTED thread_id={thread_id}")
    except Exception as e:
        log(f"POST FAILED: {e}")
        sys.exit(1)

    # posted.md に追記
    id_match = re.search(r"## (\d{4}-\d{2}-\d{2}-\d{3})", target_post)
    post_id = id_match.group(1) if id_match else "unknown"

    runner = "GitHub Actions" if os.getenv("GITHUB_ACTIONS") else "ローカル"
    posted_entry = f"""
## {post_id}（Threads自動配信 / {runner}）
- プラットフォーム: Threads
- 投稿日時: {datetime.now(JST).isoformat()}
- thread_id: {thread_id}
- URL: https://www.threads.com/@atelierbase_own/post/{thread_id}
- 文面:

{text}

- ステータス: posted

---
"""

    with open(POSTED, "a", encoding="utf-8") as f:
        f.write(posted_entry)

    # pending_threads.md から該当エントリ削除
    posts.pop(target_idx)
    new_content = header + "\n".join(posts) if posts else header
    with open(PENDING, "w", encoding="utf-8") as f:
        f.write(new_content)

    log(f"DONE moved {post_id} to posted")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="投稿せずに動作確認")
    parser.add_argument("--skip-jitter", action="store_true", help="ジッター遅延スキップ")
    args = parser.parse_args()
    main(dry_run=args.dry_run, skip_jitter=args.skip_jitter)
