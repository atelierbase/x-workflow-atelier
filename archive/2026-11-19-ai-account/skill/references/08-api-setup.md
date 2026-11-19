# 08-api-setup: X API 契約・MCP 接続のセットアップ

`config.json` の `posting_mode` を `"api"` に切り替えて自動投稿する前に、以下の準備が必要。

## ステップ概要

```
1. @ID の空き確認・アカウント開設
2. X Developer Portal 登録（Free Tier）
3. App 作成 + API key 取得
4. 認証情報を安全に保存
5. X MCP サーバーを Claude Code に接続
6. スキルの config.json 編集
7. 動作テスト（仮投稿1本）
```

## Step 1: @ID 空き確認 + アカウント開設

### 候補

- `@atelier_base`
- `@atelier_master`
- `@atelier_owner`
- `@ab_store`

### 確認方法

ブラウザで `https://x.com/{候補のID}` にアクセス。
「アカウントが見つかりません」が表示されたら空き。

### 開設手順

1. https://x.com で「サインアップ」
2. メールアドレスまたは電話番号で登録
3. @ID と表示名（「アトリエの店主」）を設定
4. プロフィール文を `templates/profile.md` の採用版から貼り付け
5. アイコン設定（似顔絵・別途用意）
6. 固定ポスト（`templates/pinned-post.md` から選択）を投稿してピン留め

## Step 2: X Developer Portal 登録（Free Tier）

1. https://developer.x.com/en にアクセス
2. 右上「Sign Up」→ 作成したXアカウントで認証
3. 用途アンケートに回答（正直に「個人事業の運営アカウント自動化」と書いてOK）
4. **Free Tier** を選択（月100投稿 = 1日3投稿 = 立ち上げ初期に十分）

### 注意

- 申請から承認まで数時間〜数日かかる場合あり
- 承認はメールで通知される
- 内容によっては追加質問が来る → 正直に答える

## Step 3: App 作成 + API key 取得

Developer Portal 承認後：

1. 「Projects & Apps」→「Create App」
2. App 名を決める（例: `atelier-shop-master`）
3. 必要なキー4種を取得・保存：

| キー名 | 説明 |
|---|---|
| API Key（Consumer Key） | アプリ識別子 |
| API Key Secret（Consumer Secret） | 上記のシークレット |
| Access Token | ユーザー権限のトークン |
| Access Token Secret | 上記のシークレット |

4. **アプリ権限を「Read and Write」に変更**（重要：これがないと投稿できない）
   - 設定画面 → User authentication settings → App permissions → Read and write を選択

## Step 4: 認証情報を安全に保存

ホームディレクトリ配下に専用フォルダを作って、JSON で保存。

```bash
mkdir -p ~/.config/x-workflow
chmod 700 ~/.config/x-workflow
```

`~/.config/x-workflow/x-credentials.json` を作成：

```json
{
  "consumer_key": "ここにAPI Key",
  "consumer_secret": "ここにAPI Key Secret",
  "access_token": "ここにAccess Token",
  "access_token_secret": "ここにAccess Token Secret"
}
```

```bash
chmod 600 ~/.config/x-workflow/x-credentials.json
```

これで他のユーザーから読めなくなる。

**※ 絶対に Git にコミットしないこと。`.gitignore` 推奨**

## Step 5: X MCP サーバーを Claude Code に接続

選定: **`EnesCinr/twitter-mcp`**（npm パッケージ: `@enescinar/twitter-mcp`）
- npm 一発で動く
- 投稿（post_tweet）と検索（search_tweets）対応
- 立ち上げ初期はこれで十分。フル機能が必要になったら `rafaljanicki/x-twitter-mcp-server`（Python）に乗り換え

ターミナルで以下を実行：

```bash
claude mcp add x-twitter \
  -e API_KEY="$(jq -r .consumer_key ~/.config/x-workflow/x-credentials.json)" \
  -e API_SECRET_KEY="$(jq -r .consumer_secret ~/.config/x-workflow/x-credentials.json)" \
  -e ACCESS_TOKEN="$(jq -r .access_token ~/.config/x-workflow/x-credentials.json)" \
  -e ACCESS_TOKEN_SECRET="$(jq -r .access_token_secret ~/.config/x-workflow/x-credentials.json)" \
  -- npx -y @enescinar/twitter-mcp
```

※ `jq` が無い場合は `brew install jq` で入れる、もしくは値を直接書く
※ MCP接続名（`x-twitter`）は自由に変えられるが、スキル内ドキュメントとは合わせる

### 接続確認

Claude Code を起動して `/mcp` コマンドでリスト表示。
`x-twitter` が一覧に出ていればOK。

接続できていない場合：

```bash
claude mcp logs x-twitter
```

でログを確認する。

## Step 6: スキルの config.json を編集

```bash
cp ~/.claude/skills/x-workflow/config.json.example ~/.claude/skills/x-workflow/config.json
```

エディタで `~/.claude/skills/x-workflow/config.json` を開いて、以下を編集：

```json
{
  "account": {
    "handle": "@実際の取得したID",
    "display_name": "アトリエの店主",
    "brand": "Atelier Base"
  },
  "line": {
    "name": "アトリエ店主の部屋",
    "url": "https://lin.ee/実際のURL"
  },
  "posting_mode": "api",
  "api": {
    "tier": "free",
    "mcp_server": "rafaljanicki/x-twitter-mcp-server",
    "monthly_post_limit": 100,
    "credentials_path": "~/.config/x-workflow/x-credentials.json"
  },
  ...
}
```

### config.json も Git にコミットしない

LINE URL や @ID は機密ではないが、念のため `.gitignore` 推奨。

## Step 7: 動作テスト（仮投稿1本）

### 7-1. ストック初期化

```bash
mkdir -p ~/.claude/skills/x-workflow/storage/stocks
echo "# ストック（未投稿）" > ~/.claude/skills/x-workflow/storage/stocks/pending.md
echo "# 投稿済みログ" > ~/.claude/skills/x-workflow/storage/stocks/posted.md
echo "# 起案中・没・メモ" > ~/.claude/skills/x-workflow/storage/stocks/drafts.md
```

### 7-2. テスト用の仮投稿を pending.md に追加

`storage/stocks/pending.md` に以下を追記：

```markdown
## test-001
- 種類: 単発
- 投稿想定時刻: 任意
- 文面:

アトリエの店主、はじめます。
これからどうぞよろしくお願いします☺️

- ステータス: pending
```

### 7-3. 配信実行

Claude Code で：

```
/x-workflow 配信
```

スキルが MCP 経由で投稿を実行する。

### 7-4. 確認

- Xアプリで投稿が反映されているか
- `posted.md` に記録されているか
- `pending.md` から削除されているか

## トラブルシューティング

| エラー | 原因 | 対処 |
|---|---|---|
| `401 Unauthorized` | API key が間違っている / 権限不足 | キー再確認、App権限「Read and Write」を確認 |
| `403 Forbidden` | アカウントが凍結 | Xサポートに連絡 |
| `429 Too Many Requests` | Free枠（月100投稿）超過 | 翌月まで manual モード or Basic 契約 |
| `MCP connection failed` | MCP サーバー起動失敗 | `claude mcp logs x-twitter` で確認 |
| `tweet text too long` | 280文字超過 | 文字数チェック、スレッド分割 |

## 凍結リスク回避（重要）

1. **投稿時刻に ±15分のジッター** を入れる（config.json の `posting_schedule.jitter_minutes`）
2. 同じ文面・同じURLの連投を避ける
3. 短時間に複数投稿しない（30分以上の間隔）
4. リプ・いいね・引用RT は **100% 手動**
5. **最初の2週間は手動投稿も混ぜる**（API比率50%以下推奨）
6. 投稿内容を1日3本ジャストで固定しない（時々2本、時々3本）

## 完了チェックリスト

セットアップが完了したら、以下をひとつずつチェック：

- [ ] @ID 確定・アカウント開設済み
- [ ] プロフィール文（`templates/profile.md` 採用版）反映済み
- [ ] 固定ポスト（`templates/pinned-post.md`）反映済み・ピン留め済み
- [ ] 似顔絵アイコン設定済み
- [ ] X Developer Portal 登録・Free Tier 承認済み
- [ ] App 作成・API key 4種取得済み
- [ ] App 権限「Read and Write」設定済み
- [ ] `~/.config/x-workflow/x-credentials.json` 保存済み（chmod 600）
- [ ] X MCP サーバーを Claude Code に接続済み（`/mcp` で表示確認）
- [ ] スキルの `config.json` 編集済み
- [ ] `storage/stocks/` 配下のファイル初期化済み
- [ ] 仮投稿1本で動作テスト成功
- [ ] LINE「アトリエ店主の部屋」開設済み
- [ ] LINE 運用ツール選定・アンケート設定済み

## 次のステップ

すべてチェックがついたら：

1. 初期ストックを7本作る（最初の1週間分）→ `/x-workflow ネタ` → `/x-workflow 生成`
2. Day 1 から朝/昼/夜の3投稿を回す
3. 1週間後に `/x-workflow 分析` で振り返り
4. 4週目あたりで Basic Tier 検討
