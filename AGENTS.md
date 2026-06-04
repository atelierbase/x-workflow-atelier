# AGENTS.md — X 直投稿ルーチン（Codex クラウド用・@AtelierBase_own）

> **このファイルは Codex への指示書**（Codexクラウドルーチンが repo を clone するとこれを読む）。
> 役割：**発火時に「今のスロット用の投稿を1本」生成し、必要なら GPT 画像も作り、X に投稿してリポジトリを更新する**。
> アカウント：**ひろ｜AI実業家**（X=@AtelierBase_own / 屋号 Atelier Base）。背骨＝「20億円の事業を作ってきた実業家が、今は Claude Code / Codex を相棒に楽しくWebサービスを作る」。

このルーチンは**生成も送信もすべて Codex が行う**（Claude ルーチンは無効化済み）。Codexは GPT-Image で画像も作れるので、**画像付き投稿もこのルーチンだけで完結**できる。

---

## 0. 必要な認証（Codexクラウドの環境変数に設定。リポジトリには絶対に置かない）

| 環境変数 | 用途 |
|---|---|
| `X_CONSUMER_KEY` / `X_CONSUMER_SECRET` | X API（OAuth1.0a）App キー |
| `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` | X API ユーザートークン（App権限は **Read and Write**） |
| `OPENAI_API_KEY` | GPT-Image 画像生成（画像付き投稿を作る時のみ） |

> キーの取得方法は `skill/references/08-api-setup.md`（Developer Portal / Free Tier / 4キー / Read-Write権限）。
> **キーをコミットしない**（public repo）。Codexの環境変数で渡す。

依存：`pip install tweepy requests openai`（poster は tweepy、画像生成は openai を使う）。

---

## 1. 今のスロットを決める
JST 現在時刻から：**6:00–10:59=朝 / 11:00–14:59=昼 / それ以外=夜**。
`TZ=Asia/Tokyo date +%H` で時を取り `SLOT`（朝/昼/夜）を決める。

## 2. 投稿文を生成（1本だけ・このスロット用）
書く前に必ず読む（このリポジトリ内）：
- `skill/references/00-context.md`（背景・軸）/ `skill/templates/voice-guide.md`（口調 v3.2）/ `skill/references/02-generate.md`
- `storage/analytics/learnings.md`（効くルールを反映＝学習の複利）
- 型は `skill/agents/writer.md` / `skill/templates/single-post-templates.md`

ネタは **WebSearch等で直近1週間の海外 Claude Code / Codex 情報**（発表時期を確認）。一人称「私」／絵文字0〜1個／**280字以内**。
投稿タイプ：`単発` を基本、たまに `コメント仕込み`（出典URLはセルフリプライのコメントへ／本文中で `--- コメント1 ---` 区切り）。**画像付き**は §3 のとおり時々入れてよい（CodexのGPT-Image活用）。

## 3.（画像付きにする場合）GPT-Image で画像生成
1. 画像プロンプトを作り、**`gpt-image-1`** で **PNG・横長 `1536x1024`・5MB以下**を生成（文字は入れない／クリーンな構図）。詳細規約は §画像の参考として `../codex-image-task.md` と同方針。
2. 保存先＝**`storage/images/<投稿ID>.png`**（ファイル名は投稿IDと完全一致・小文字 `.png`）。
3. 本文ブロックに **`- 画像ファイル: storage/images/<投稿ID>.png`** 行を必ず入れる。
   - ※X はローカルPNGを `media_upload` で添付するので、X単体なら事前pushは不要（poster がローカルファイルを読む）。

## 4. pending.md に1件だけ追記
`storage/stocks/pending.md` 末尾に1件 append（フォーマット厳守。既存は消さない＝基本ヘッダのみで空のはず）：

```
## {ID}
- 種類: 単発            # または「コメント仕込み」「画像付き」
- 投稿想定時刻: {SLOT}（自動・直投稿）
- 想定日: {YYYY-MM-DD（曜）}
- 軸: {軸}
- ソース: {一次ソースURL}
- 画像ファイル: storage/images/{ID}.png   # 画像付きのときだけ入れる
- 文面:

{本文}

- ステータス: pending

---
```
- **ID** = `YYYY-MM-DD-NNN`、NNN は **朝=701 / 昼=702 / 夜=703**（日付プレフィックスで一意）。
- `投稿想定時刻:` は先頭が `朝`/`昼`/`夜`（送信側が前方一致で拾う）。

## 5. 自己チェック（必須・在庫が無いぶんの唯一の安全網）
全部満たすか確認。1つでもNGなら §2 へ戻って作り直す（最大2回）：
- [ ] 280字以内（コメント仕込みは各セグメントも）
- [ ] 一人称「私」／絵文字0〜1個／楽しく前向き／実務フィルター
- [ ] **禁止語なし**：本名「石井」「ミライ塾」「アトリエの店主」その他個人特定
- [ ] 直近1週間のフレッシュネタ・一次ソースと矛盾しない
- [ ] （画像付きなら）画像が壊れていない・本文と整合
- 2回ダメ → **投稿せず** `storage/analytics/routine.log` に `skip: <理由>` を残して正常終了。

## 6. 送信（= 既存 poster を実行。これが X API 記載元）
**`scripts/scheduled_poster.py` を実行する。** これが X API の実装（tweepy OAuth1.0a・`create_tweet`・画像は `media_upload`・コメントはセルフリプライ・一過性403/429/5xxリトライ・冪等ガード）。

```bash
cd <repo>
SKIP_JITTER=1 python scripts/scheduled_poster.py
```
- 認証は §0 の環境変数から自動取得。`SKIP_JITTER=1` で遅延を切る（時刻はルーチンが持つ）。
- poster は pending の該当スロット1件を **X に投稿** → `posted.md` に移動 → `pending.md` から削除 → `post-state.json` に投稿済みマーク。
- dry-run で文面確認したい時は `python scripts/scheduled_poster.py --dry-run`（投稿しない）。

## 7. 結果を commit & push
```bash
git add storage/stocks/pending.md storage/stocks/posted.md storage/images storage/analytics/scheduler.log storage/analytics/post-state.json storage/analytics/routine.log
git commit -m "post: sent X {SLOT} {ID}"
git push
```
- ※poster が pending を空に戻すので、push しても GitHub Actions 側の送信ワークフローは**起動しない/起動しても空で no-op**（二重投稿しない）。GitHub Actions は予備の送信経路として残してあるだけ。

---

## API 記載元（このリポジトリ内）
| 何 | ファイル |
|---|---|
| **X API の実装そのもの**（OAuth1.0a・投稿・画像・リプライ・リトライ） | **`scripts/scheduled_poster.py`** |
| X API キーの取得・権限設定（Developer Portal / Read-Write） | `skill/references/08-api-setup.md` |
| 口調・型・軸・テンプレ | `skill/templates/voice-guide.md` / `skill/agents/writer.md` / `skill/references/*` |
| 学習ルール（毎回反映） | `storage/analytics/learnings.md` |

## 鉄則
- 完全無人。人間に承認を求めない（クラウド実行・止まると失敗）。
- 自己チェックに通らなければ**投稿しない**（事故より1本落とす方がマシ）。
- キーをコミットしない。`pending.md` を壊さない。エラー時も log に残して終了。
- 在庫は溜めない（pending は1本だけ）。X用画像を threads repo に置かない。
