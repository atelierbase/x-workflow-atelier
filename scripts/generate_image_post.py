#!/usr/bin/env python3
"""
Generate one image-backed SNS post and queue it in pending.md.

This is built for GitHub Actions. It researches fresh Claude Code / Codex news
with the OpenAI Responses web_search tool, writes one Japanese post, generates a
visual-summary PNG, and appends a single image post to storage/stocks/pending.md.
The platform poster then sends it with REQUIRE_IMAGE=1.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shlex
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import requests


REPO_DIR = Path(__file__).resolve().parent.parent
PENDING = REPO_DIR / "storage" / "stocks" / "pending.md"
POSTED = REPO_DIR / "storage" / "stocks" / "posted.md"
IMAGES_DIR = REPO_DIR / "storage" / "images"
LOG_DIR = REPO_DIR / "storage" / "analytics"
ROUTINE_LOG = LOG_DIR / "routine.log"
STATE = LOG_DIR / "post-state.json"
ENV_FILE = Path.home() / ".config" / "sns-auto-post" / "env"

JST = timezone(timedelta(hours=9))
FORBIDDEN = ("石井", "ミライ塾", "アトリエの店主")
SLOT_BASE = {"朝": 701, "昼": 702, "夜": 703}
WEEKDAYS = "月火水木金土日"

PLATFORM = "threads" if (REPO_DIR / "scripts" / "threads_poster.py").exists() else "x"


CONFIG: dict[str, Any] = {
    "x": {
        "account": "X @AtelierBase_own",
        "platform_note": "Xは280字以内。URLは本文に入れず、実務で使う視点を短く強く出す。",
        "char_min": 80,
        "char_max": 280,
        "image_size": "1536x1024",
        "image_focus": "何が新しいか、何が変わるか、実務上どう効くか",
        "context_files": [
            "skill/references/00-context.md",
            "skill/templates/voice-guide.md",
            "skill/templates/single-post-templates.md",
            "skill/agents/writer.md",
            "storage/analytics/learnings.md",
        ],
    },
    "threads": {
        "account": "Threads @atelierbase_own",
        "platform_note": "Threadsは200-400字目安、最大500字。私の体験や気づきを主役にして、必ず問いかけで締める。",
        "char_min": 150,
        "char_max": 500,
        "image_size": "1024x1024",
        "image_focus": "何が新しいか、何に気づいたか、読者に何を問いかけているか",
        "context_files": [
            "skill/references/00-context.md",
            "skill/templates/voice-guide.md",
            "skill/agents/writer.md",
            "storage/analytics/learnings.md",
        ],
    },
}


def log(message: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = f"{datetime.now(JST).isoformat()} [generate-image-post] {message}"
    with ROUTINE_LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


def load_env_file() -> None:
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
            os.environ.setdefault(key, value)


def current_slot() -> str:
    hour = datetime.now(JST).hour
    if 6 <= hour <= 10:
        return "朝"
    if 11 <= hour <= 14:
        return "昼"
    return "夜"


def today_label() -> str:
    now = datetime.now(JST)
    return f"{now:%Y-%m-%d}（{WEEKDAYS[now.weekday()]}）"


def today_key() -> str:
    return datetime.now(JST).strftime("%Y-%m-%d")


def load_state() -> dict[str, Any]:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def already_posted(slot: str) -> bool:
    return slot in load_state().get(today_key(), [])


def pending_has_slot(slot: str) -> bool:
    if not PENDING.exists():
        return False
    return f"投稿想定時刻: {slot}" in PENDING.read_text(encoding="utf-8")


def read_context(config: dict[str, Any]) -> str:
    chunks: list[str] = []
    for rel in config["context_files"]:
        path = REPO_DIR / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        chunks.append(f"\n\n--- {rel} ---\n{text[:4500]}")
    return "".join(chunks)


def used_ids() -> set[str]:
    found: set[str] = set()
    for path in (PENDING, POSTED):
        if path.exists():
            found.update(re.findall(r"## (\d{4}-\d{2}-\d{2}-\d{3})", path.read_text(encoding="utf-8")))
    if IMAGES_DIR.exists():
        for img in IMAGES_DIR.glob("*.png"):
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{3}", img.stem):
                found.add(img.stem)
    return found


def next_post_id(slot: str) -> str:
    prefix = today_key()
    existing = used_ids()
    for suffix in range(SLOT_BASE[slot], 1000):
        candidate = f"{prefix}-{suffix:03d}"
        if candidate not in existing:
            return candidate
    raise RuntimeError(f"No available post id for {prefix}")


def openai_post(path: str, payload: dict[str, Any], timeout: int = 180) -> dict[str, Any]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    resp = requests.post(
        f"https://api.openai.com/v1/{path}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )
    if not resp.ok:
        body = resp.text[:1200]
        raise RuntimeError(f"OpenAI API error {resp.status_code}: {body}")
    return resp.json()


def response_text(data: dict[str, Any]) -> str:
    if isinstance(data.get("output_text"), str):
        return data["output_text"]
    texts: list[str] = []
    for item in data.get("output", []):
        for content in item.get("content", []):
            if isinstance(content.get("text"), str):
                texts.append(content["text"])
    return "\n".join(texts).strip()


def parse_json_object(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    decoder = json.JSONDecoder()
    for i, ch in enumerate(cleaned):
        if ch != "{":
            continue
        try:
            obj, _ = decoder.raw_decode(cleaned[i:])
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    raise ValueError(f"No JSON object found in model output: {text[:500]}")


def generate_post(slot: str, post_id: str, config: dict[str, Any]) -> dict[str, Any]:
    text_model = os.environ.get("OPENAI_TEXT_MODEL", "gpt-5-mini")
    context = read_context(config)
    prompt = f"""
あなたは日本語SNS編集者です。{config['account']} のために、今すぐ投稿する画像付き投稿を1本だけ作ってください。

今日: {today_label()}
投稿スロット: {slot}
投稿ID: {post_id}
方針: 20億円の事業を作ってきた実業家が、今はClaude Code / Codexを相棒に楽しくWebサービスを作る。
制約: {config['platform_note']}

必ずやること:
- web_searchで、直近7日以内に公開または更新された海外のClaude Code / Codex / AI開発エージェント関連情報を調べる。
- 一次ソース、公式発表、公式docs、信頼できる発表記事を優先する。
- 投稿は翻訳ではなく、「私が実務でどう見るか」を入れる。
- 本名「石井」「ミライ塾」「アトリエの店主」は絶対に出さない。
- 種類は必ず「画像付き」。
- 画像は装飾アイキャッチではなく、文章を読まない人にも内容が分かる視覚要約にする。
- 画像だけ見ても「{config['image_focus']}」が分かる構図にする。

出力はJSONのみ:
{{
  "source_title": "出典タイトル",
  "source_url": "https://...",
  "freshness_date": "YYYY-MM-DD",
  "axis": "主軸 / 海外翻訳 ・ サブ軸1 / 自分の実例 ・ サブ軸2 / 実業家視点",
  "post_text": "投稿本文",
  "image_prompt": "GPT Imageに渡す画像生成プロンプト。日本語の視覚要約カードとして、画面内に入れる短い日本語見出しやラベルも明示する"
}}

参考ルール:
{context}
""".strip()
    data = openai_post(
        "responses",
        {
            "model": text_model,
            "input": prompt,
            "tools": [{"type": "web_search"}],
            "max_output_tokens": 3000,
        },
    )
    return parse_json_object(response_text(data))


def repair_post(post: dict[str, Any], errors: list[str], config: dict[str, Any]) -> dict[str, Any]:
    text_model = os.environ.get("OPENAI_TEXT_MODEL", "gpt-5-mini")
    prompt = f"""
次のJSON投稿案を、エラーだけ直してJSONのみで返してください。
エラー: {errors}
制約: {config['platform_note']}
禁止語: {', '.join(FORBIDDEN)}

JSON:
{json.dumps(post, ensure_ascii=False)}
""".strip()
    data = openai_post(
        "responses",
        {
            "model": text_model,
            "input": prompt,
            "max_output_tokens": 1600,
        },
    )
    return parse_json_object(response_text(data))


def validate_post(post: dict[str, Any], config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("source_title", "source_url", "axis", "post_text", "image_prompt"):
        if not str(post.get(key, "")).strip():
            errors.append(f"{key} is empty")
    source_url = str(post.get("source_url", ""))
    if not source_url.startswith(("https://", "http://")):
        errors.append("source_url must be an http URL")
    text = str(post.get("post_text", "")).strip()
    if len(text) > config["char_max"]:
        errors.append(f"post_text is too long: {len(text)} chars")
    if len(text) < config["char_min"]:
        errors.append(f"post_text is too short: {len(text)} chars")
    if PLATFORM == "threads" and not text.endswith(("?", "？")):
        errors.append("Threads post_text must end with a question")
    for word in FORBIDDEN:
        if word in text or word in str(post.get("image_prompt", "")):
            errors.append(f"forbidden word appears: {word}")
    if "- ステータス:" in text:
        errors.append("post_text contains pending.md control marker")
    return errors


def build_image_prompt(post: dict[str, Any], config: dict[str, Any]) -> str:
    return f"""
{post['image_prompt']}

重要:
- これはSNS投稿用の日本語「視覚要約」画像です。雰囲気だけのアイキャッチは禁止。
- キャプションを読まない人にも、1) ニュース、2) 変化、3) 実務で効くこと が数秒で伝わる構図。
- 画面内テキストは大きく短く。小さい文章を詰め込まない。最大3ブロック。
- 架空のUIスクリーンショット、偽ロゴ、QRコード、人物写真風は避ける。
- 清潔で実務的、でも少し楽しいAtelier Baseらしい情報カード。
- 投稿本文の要旨: {post['post_text']}
- 出典: {post['source_title']}
""".strip()


def generate_image(post: dict[str, Any], post_id: str, config: dict[str, Any]) -> Path:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    image_path = IMAGES_DIR / f"{post_id}.png"
    if image_path.exists():
        return image_path

    requested = os.environ.get("OPENAI_IMAGE_MODEL")
    models = [requested] if requested else ["gpt-image-1.5", "gpt-image-1"]
    prompt = build_image_prompt(post, config)
    last_error: Optional[Exception] = None
    for model in models:
        if not model:
            continue
        try:
            data = openai_post(
                "images/generations",
                {
                    "model": model,
                    "prompt": prompt,
                    "size": config["image_size"],
                    "quality": os.environ.get("OPENAI_IMAGE_QUALITY", "medium"),
                    "output_format": "png",
                    "n": 1,
                },
                timeout=300,
            )
            item = data.get("data", [{}])[0]
            b64 = item.get("b64_json")
            if not b64:
                raise RuntimeError("OpenAI image response did not include b64_json")
            image_path.write_bytes(base64.b64decode(b64))
            return image_path
        except Exception as exc:  # Try older GPT Image model if the newest is unavailable.
            last_error = exc
            if requested:
                break
    raise RuntimeError(f"Image generation failed: {last_error}")


def append_pending(post: dict[str, Any], post_id: str, slot: str, image_path: Path) -> None:
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    if not PENDING.exists():
        PENDING.write_text("# 受け渡しキュー\n\n---\n", encoding="utf-8")
    rel_image = image_path.relative_to(REPO_DIR)
    image_prompt = re.sub(r"\s+", " ", str(post["image_prompt"])).strip()
    block = f"""
## {post_id}
- 種類: 画像付き
- 投稿想定時刻: {slot}（GitHub Actions・画像付き）
- 想定日: {today_label()}
- 軸: {post['axis']}
- ソース: {post['source_title']} {post['source_url']}
- 画像プロンプト: {image_prompt}
- 画像ファイル: {rel_image}
- 文面:

{str(post['post_text']).strip()}

- ステータス: pending

---
""".lstrip()
    current = PENDING.read_text(encoding="utf-8")
    if f"## {post_id}\n" in current:
        log(f"pending already contains {post_id}; skip append")
        return
    if not current.endswith("\n"):
        current += "\n"
    PENDING.write_text(current + block, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slot", choices=("朝", "昼", "夜"), default=os.environ.get("POST_SLOT") or current_slot())
    parser.add_argument("--force", action="store_true", help="Generate even if today's slot is already marked posted.")
    args = parser.parse_args()

    load_env_file()
    config = CONFIG[PLATFORM]
    slot = args.slot

    if already_posted(slot) and not args.force and os.environ.get("ALLOW_DUPLICATE_POST") != "1":
        log(f"skip: {PLATFORM} {slot} already posted today")
        return 0
    if pending_has_slot(slot):
        log(f"skip generation: pending already has a {slot} post; poster will consume it")
        return 0

    post_id = next_post_id(slot)
    log(f"start generation platform={PLATFORM} slot={slot} id={post_id}")
    post = generate_post(slot, post_id, config)
    errors = validate_post(post, config)
    if errors:
        log(f"repairing post: {errors}")
        post = repair_post(post, errors, config)
        errors = validate_post(post, config)
    if errors:
        raise RuntimeError(f"Generated post failed validation: {errors}")

    image_path = generate_image(post, post_id, config)
    append_pending(post, post_id, slot, image_path)
    log(f"queued {post_id} image={image_path.relative_to(REPO_DIR)}")
    print(f"GENERATED_POST_ID={post_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
