#!/usr/bin/env python3
"""Queue one image2-generated SNS post in pending.md.

This script does not generate images and does not post. It validates that a
Codex/image2-created PNG exists in storage/images/<POST_ID>.png, then appends a
single image-backed post to storage/stocks/pending.md for GitHub Actions to send
at the matching slot.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent
PENDING = REPO_DIR / "storage" / "stocks" / "pending.md"
IMAGES_DIR = REPO_DIR / "storage" / "images"
JST = timezone(timedelta(hours=9))
WEEKDAYS = "月火水木金土日"
FORBIDDEN = ("石井", "ミライ塾", "アトリエの店主")
PNG_MAX_BYTES = 5 * 1024 * 1024


def today_label() -> str:
    now = datetime.now(JST)
    return f"{now:%Y-%m-%d}（{WEEKDAYS[now.weekday()]}）"


def read_text_arg(value: str | None) -> str:
    if not value or value == "-":
        return sys.stdin.read()
    return Path(value).read_text(encoding="utf-8")


def parse_segments(raw_text: str) -> list[str]:
    return [
        segment.strip()
        for segment in re.split(r"\n-{2,}\s*コメント\s*\d*\s*-{2,}\s*\n", raw_text)
        if segment.strip()
    ]


def validate_png(path: Path, post_id: str) -> list[str]:
    errors: list[str] = []
    expected = IMAGES_DIR / f"{post_id}.png"
    if path != expected:
        errors.append(f"image path must be storage/images/{post_id}.png")
    if not path.exists():
        errors.append(f"image file does not exist: {path.relative_to(REPO_DIR)}")
        return errors
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append("image file is not a PNG")
    if len(data) > PNG_MAX_BYTES:
        errors.append(f"image file is too large: {len(data)} bytes")
    return errors


def validate_post(args: argparse.Namespace, text: str, image_prompt: str) -> list[str]:
    errors: list[str] = []
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{3}", args.post_id):
        errors.append("post-id must match YYYY-MM-DD-NNN")
    if args.slot not in ("朝", "昼", "夜"):
        errors.append("slot must be 朝, 昼, or 夜")
    if not text.strip():
        errors.append("post text is empty")
    for word in FORBIDDEN:
        if word in text or word in image_prompt:
            errors.append(f"forbidden word appears: {word}")
    for i, segment in enumerate(parse_segments(text), 1):
        if len(segment) > 280:
            errors.append(f"text segment {i} exceeds 280 chars: {len(segment)}")

    rel_image = Path(args.image)
    if rel_image.is_absolute():
        image_path = rel_image
    else:
        image_path = (REPO_DIR / rel_image).resolve()
    errors.extend(validate_png(image_path, args.post_id))

    pending_text = PENDING.read_text(encoding="utf-8") if PENDING.exists() else ""
    if f"## {args.post_id}\n" in pending_text:
        errors.append(f"pending already contains {args.post_id}")
    if not args.allow_existing_slot and f"投稿想定時刻: {args.slot}" in pending_text:
        errors.append(f"pending already contains a post for slot {args.slot}")
    return errors


def append_pending(args: argparse.Namespace, text: str, image_prompt: str) -> None:
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    if not PENDING.exists():
        PENDING.write_text("# 受け渡しキュー（image2生成済み画像 / 定期投稿）\n\n---\n", encoding="utf-8")

    prompt_line = re.sub(r"\s+", " ", image_prompt).strip()
    image_prompt_block = f"- 画像プロンプト: {prompt_line}\n" if prompt_line else ""
    block = f"""
## {args.post_id}
- 種類: 画像付き
- 投稿想定時刻: {args.slot}（image2生成済み・GitHub Actions配信）
- 想定日: {args.date_label or today_label()}
- 軸: {args.axis}
- ソース: {args.source}
{image_prompt_block}- 画像ファイル: storage/images/{args.post_id}.png
- 文面:

{text.strip()}

- ステータス: pending

---
""".lstrip()
    current = PENDING.read_text(encoding="utf-8")
    if not current.endswith("\n"):
        current += "\n"
    PENDING.write_text(current + block, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--post-id", required=True)
    parser.add_argument("--slot", required=True, choices=("朝", "昼", "夜"))
    parser.add_argument("--axis", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--text-file", required=True, help="Use '-' to read from stdin")
    parser.add_argument("--image-prompt-file")
    parser.add_argument("--date-label")
    parser.add_argument("--allow-existing-slot", action="store_true")
    args = parser.parse_args()

    text = read_text_arg(args.text_file)
    image_prompt = read_text_arg(args.image_prompt_file) if args.image_prompt_file else ""
    errors = validate_post(args, text, image_prompt)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    append_pending(args, text, image_prompt)
    print(f"queued image2 post {args.post_id} for slot {args.slot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
