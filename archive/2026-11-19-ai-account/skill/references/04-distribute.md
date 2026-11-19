# 04-distribute: 配信

このフェーズの目的は、ストックから取り出した投稿を実際にXに流すこと。

## モード切替

`~/.claude/skills/x-workflow/config.json` の `posting_mode` で挙動が変わる：

| モード | 挙動 | 推奨フェーズ |
|---|---|---|
| `manual` | コピペ用テキストを出力するだけ | Phase 1（立ち上げ初期） |
| `scheduled` | スケジューラAPI経由で予約 | Phase 2（4週目〜） |
| `api` | X MCPサーバー経由で直接投稿 | Phase 3（伸び確認後） |

初期は `manual` 推奨。

## manual モードの挙動

### Step 1. ストックから取り出し

`storage/stocks/pending.md` の先頭1件、または時刻タグが「朝」「昼」「夜」のうち現在時刻に近いものを選ぶ。

### Step 2. 整形して出力

以下の形式で、人間がそのままコピペできるテキストを出力する：

```
━━━━━━━━━━━━━━━━━━━━━━━━━
  📤 投稿コピー用（手動配信）
━━━━━━━━━━━━━━━━━━━━━━━━━

種類: 単発
ID: 2026-05-27-001

【投稿本文 ↓ ここから ↓】
[全文]
【ここまで ↑】

文字数: ◯◯文字
画像添付: なし / あり（パス）
リンク短縮: 不要 / lin.ee/xxx

投稿後、`/x-workflow 配信完了 2026-05-27-001` で記録します。

━━━━━━━━━━━━━━━━━━━━━━━━━
```

スレッドの場合はポストごとに区切って出力。

### Step 3. 投稿完了の記録

オーナーが投稿完了を宣言したら（「投稿した」「完了」「配信完了 ID」など）、
- `pending.md` から該当エントリを削除
- `posted.md` に追加（投稿日時を記録）

数値は後日反映する（24h後・7d後のタイミングで取りに行く）。

## scheduled モードの挙動（Phase 2 で実装）

Buffer / Typefully / SocialDog 等のAPIに予約POST。
将来実装予定。今ターンでは仕様だけ：

- config.json に `scheduler.provider` `scheduler.api_key` `scheduler.timezone` を持つ
- 配信完了の確認はWebhook or 定期チェック

## api モードの挙動

X MCP サーバー経由で直接POST。

**選定 MCP**: `EnesCinr/twitter-mcp`（npm パッケージ: `@enescinar/twitter-mcp`）
- シンプルな投稿・検索専用。新規アカウント運用の最小構成として適切
- 将来分析・タイムライン取得まで自動化したくなったら `rafaljanicki/x-twitter-mcp-server`（Python）に乗り換え可能

**提供ツール**:
- `mcp__x_twitter__post_tweet`: 投稿
- `mcp__x_twitter__search_tweets`: 検索（ネタ仕入れにも使える）

**接続前提**:
- X API 契約（Free Tier = 月100ポスト / Basic Tier = 月10,000ポスト）
- OAuth キー（API Key/Secret、Access Token/Secret）取得済み
- Claude Code に MCP 接続済み（`claude mcp add x-twitter ...`）
- スキルの `config.json` で `posting_mode: "api"` 設定

セットアップ手順の詳細は **`references/08-api-setup.md`** を参照。

### Step 1: pending.md から取り出し

`config.json` の `posting_schedule` を参考に、現在時刻に最も近い時間帯のストックを取り出す。

例: 現在が 07:30 → `morning` 帯（07:00-09:00）のストックから1本

### Step 2: 投稿時刻にジッター

凍結リスク回避のため、投稿時刻に **±15分のランダムな遅延**（`config.json.posting_schedule.jitter_minutes`）を入れる。

```python
# 擬似コード
import random, time
time.sleep(random.uniform(-15, 15) * 60)
```

毎日きっかり同じ時刻に投稿しないことが、ボット判定回避の基本。

### Step 3: MCP 経由で投稿

x-twitter MCP の `post_tweet` ツールを呼ぶ：

```
mcp__x_twitter__post_tweet(text="<投稿本文>")
```

**スレッドの場合**: `EnesCinr/twitter-mcp` の `post_tweet` 単体ではスレッド対応が限定的（in_reply_to_tweet_id パラメータの有無は要確認）。スレッド機能が必要になったら `rafaljanicki/x-twitter-mcp-server` か OpenTweet 系に乗り換え検討。

立ち上げ初期は **スレッドは手動投稿** で運用するのが安全：
- 各ポストを `manual` モード相当でコピペ出力
- 人間がXアプリで連投実行

または、スレッドを1ポストに圧縮した **要約版** を `post_tweet` で出してもOK。

### Step 4: 投稿成功時の処理

成功（200 OK / tweet_id 取得）した場合：

1. `pending.md` から該当エントリを削除
2. `posted.md` に追加。記録項目：
   - 投稿日時（実際の投稿時刻）
   - 種類（単発/スレッド/引用RT）
   - tweet_id（X側のID）
   - 文面（全文）
   - 配信モード（"api"）
3. 月の投稿カウント（`storage/analytics/monthly_count.json`）をインクリメント

### Step 5: 失敗時の処理

| エラー | 対処 |
|---|---|
| `401 Unauthorized` | 認証情報を再確認、`config.json` の `credentials_path` を確認 |
| `403 Forbidden` | アカウント凍結の可能性 → オーナーに通知、配信停止 |
| `429 Too Many Requests` | レート制限。5分後にリトライ（1回まで） |
| `tweet text too long` | 280文字超過 → drafts.md に戻して通知 |
| `connection error` | 5分後にリトライ（1回まで） |

リトライしても失敗する場合：
- エラーログを `storage/analytics/errors.md` に記録
- 該当エントリは `pending.md` に戻す
- オーナーに通知（次の対話で「⚠️ 配信エラー」を冒頭に表示）

### レート制限の管理

`config.json.api.monthly_post_limit` で月の上限を管理：

- **残10本以下**: 「⚠️ 今月の投稿枠が残り少ないです」と通知
- **残0本**: 自動投稿を停止し、`posting_mode` を一時的に `manual` に切替
- 翌月の1日に自動でリセット → `api` モードに復帰

### 凍結リスク回避（全項目）

新規アカウントは特に注意：

1. **投稿時刻にジッター ±15分**（前述）
2. **同じ文面の連投NG**（過去30日の posted.md と類似度チェック推奨）
3. **同じURLの連投も避ける**（短縮URLを微妙に変える）
4. **短時間に複数投稿しない**（最小間隔は30分以上）
5. **エンゲ（リプ・いいね・引用RT）は100%手動**
6. **最初の2週間は手動投稿も混ぜる**（API比率50%以下）
   - これは config.json の `mixed_mode_until` で日付指定可能（次の拡張で実装）

## モード自動切替

config.json の `posting_mode` を「自動切替」にしたい場合の挙動（将来拡張）：

- 月の枠を超えたら自動で `manual` に
- 認証エラーが3回連続したら自動で `manual` に + オーナー通知
- 安定運用が継続したら `manual` → `scheduled` → `api` と段階上げ

現状は手動切替（オーナーが `config.json` を編集）。

## 凍結リスク回避（全モード共通）

1. **新規アカウント初期の投稿時刻にバラつき**
   - 毎日きっかり9:00に投稿しない
   - ±15分程度のジッターを入れる
2. **API投稿は全体の50%以下に抑える（最初の2週間）**
   - 残りは手動投稿で人間味を出す
3. **エンゲ（リプ・いいね・引用RT）は100%手動**
   - ボット判定の最大要因
4. **同じ文面・同じURLの連投を避ける**
   - 短縮URLは毎回微妙に変えるなど

## 投稿後の最低限の動き

投稿後30分〜2時間：
- 反応が来たリプに**手動で**返信する
- いいね・RTしてくれた人を時々（毎回じゃなく）フォロー or プロフ確認
- 反応が良い投稿はピン留め切り替えも検討

これは「フェーズ④ エンゲ補助」（`references/05-engage.md`、次ターン作成）でも扱う。

## 注意

- Free枠（月100ポスト）を意識。1日3本上限
- 「配信予約したから安心」で放置すると、文脈変化に追従できない
- 撤退判断は数値ベースで（reach・LINE誘導CVR）
