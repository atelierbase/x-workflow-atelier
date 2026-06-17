# AGENTS.md - X image2 queue automation (@AtelierBase_own)

このrepoでのCodex Automationの役割は、**投稿を生成してimage2画像を作り、GitHub Actionsが投稿できる状態でcommit & pushすること**。
Codex Automation自身はXへ投稿しない。配信は `.github/workflows/scheduled-post.yml` が定刻に行う。

アカウント: **ひろ｜AI実業家**（X=@AtelierBase_own / 屋号 Atelier Base）
背骨: 20億円の事業を作ってきた実業家が、今はClaude Code / Codexを相棒に楽しくWebサービスを作る。

## 実行タイミング

推奨Automation発火:

| 投稿枠 | Codex Automation目安 | GitHub Actions投稿 |
|---|---:|---:|
| 朝 | 06:30 JST | 07:05 JST |
| 昼 | 11:30 JST | 12:05 JST |
| 夜 | 18:30 JST | 19:05 JST |

JST現在時刻からスロットを決める:

- 06:00-10:59 = 朝
- 11:00-14:59 = 昼
- それ以外 = 夜

## 絶対ルール

- 画像生成は **Codexのimage2のみ**。OpenAI Images API、Canva、HTML/CSS、SVG、ダミー画像は使わない。
- Codex Automationは **Xへ直接投稿しない**。`scripts/scheduled_poster.py` も実行しない。
- やることは `storage/images/<ID>.png` と `storage/stocks/pending.md` を作ってcommit & pushするところまで。
- 画像生成・保存・検査に失敗したら `pending.md` に積まない。
- 本文のみ投稿は禁止。`pending.md` に積む投稿は必ず `種類: 画像付き`。
- 本名「石井」「ミライ塾」「アトリエの店主」は出さない。
- X用画像をthreads repoへ置かない。

## 1. 文脈を読む

必ず読む:

- `skill/references/00-context.md`
- `skill/templates/voice-guide.md`
- `skill/templates/single-post-templates.md`
- `skill/agents/writer.md`
- `storage/analytics/learnings.md`

ネタはWebSearch等で、直近1週間の海外Claude Code / Codex / AI開発エージェント関連情報を確認する。一次ソース・公式発表・公式docsを優先する。

## 2. 投稿IDを決める

形式: `YYYY-MM-DD-NNN`

| 投稿枠 | suffix |
|---|---:|
| 朝 | 701 |
| 昼 | 702 |
| 夜 | 703 |

同じIDの画像やpending/postedが既にあれば、704以降へ1つずつずらす。

## 3. 投稿文を作る

- 280字以内。コメント仕込みの場合は各セグメント280字以内。
- 一人称「私」。
- 絵文字0-1個。
- 実務フィルターを入れる。
- 出典URLを本文に直接入れすぎない。コメント仕込みにする場合は本文ブロック内で `--- コメント1 ---` 区切り。
- 投稿タイプは常に `画像付き`。

## 4. image2で画像を作る

image2に渡す画像プロンプトには以下を必ず含める:

- 一目で伝える主張
- 視覚構造（比較、3ステップ、Before/After、因果フローなど）
- 具体要素（機能名、変化、数字、実務効果）
- 避けるもの（generic AI atmosphere, random laptop, decorative-only scene）

画像仕様:

- PNG
- 推奨サイズ: 横長 `1536x1024`
- 5MB以下
- 保存先: `storage/images/<ID>.png`
- 日本語テキストを入れる場合は短いラベルだけ。長文は禁止。

## 5. queueスクリプトでpendingに積む

本文を一時ファイルに保存し、必要なら画像プロンプトも一時ファイルに保存してから実行する。

```bash
python scripts/queue_image2_post.py \
  --post-id "<ID>" \
  --slot "<朝|昼|夜>" \
  --axis "<軸>" \
  --source "<一次ソースURLまたはタイトル>" \
  --image "storage/images/<ID>.png" \
  --text-file "/tmp/x-post.txt" \
  --image-prompt-file "/tmp/x-image-prompt.txt"
```

このスクリプトが検査するもの:

- ID形式
- 画像パスが `storage/images/<ID>.png`
- PNG実在、PNG形式、5MB以下
- X文字数
- 禁止語
- 同じslotがpendingに重複していないこと

## 6. 最終確認

```bash
git diff -- storage/stocks/pending.md
python scripts/queue_image2_post.py --help >/dev/null
```

`pending.md` に1件だけ追加され、画像ファイルが存在することを確認する。

## 7. commit & push

投稿はしない。GitHubへ積むだけ。

```bash
git add storage/stocks/pending.md storage/images/<ID>.png
git commit -m "queue: X <SLOT> image2 post <ID>"
git push origin main
```

GitHub Actionsが投稿時刻に `pending.md` を読み、`REQUIRE_IMAGE=1` で画像付き投稿する。投稿後はActionsが `posted.md` へ移動してcommitする。

## 失敗時

失敗したら本文だけを積まない。可能なら `storage/analytics/routine.log` に理由を追記してcommitする。

例:

```text
2026-06-17T18:30:00+09:00 [codex-image2-queue] skip: image2 generation failed for <ID>
```
