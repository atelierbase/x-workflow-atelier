# 07-setup: 初期セットアップ

このフェーズの目的は、x-workflow を実運用可能な状態にすること。新規アカウント立ち上げ時の1回だけ実行する。

## 前提

- Xアカウント（@AtelierBase_own）が作成済み（か、作成する直前）
- LINE「アトリエ店主の部屋」が作成済み（か、URL確定済み）
- ミライ塾・物販スクール・他サービスの整理ができている

## ステップ

### Step 1. config.json の作成

`config.json.example` をコピーして `config.json` を作成。

```bash
cp ~/.claude/skills/x-workflow/config.json.example ~/.claude/skills/x-workflow/config.json
```

内容を編集：

```json
{
  "account": {
    "handle": "@AtelierBase_own",
    "display_name": "アトリエの店主",
    "brand": "Atelier Base",
    "community": "ミライ塾"
  },
  "line": {
    "name": "アトリエ店主の部屋",
    "url": "https://lin.ee/xxxxx"
  },
  "posting_mode": "manual",
  "scheduler": {
    "provider": null,
    "api_key": null,
    "timezone": "Asia/Tokyo"
  },
  "api": {
    "tier": "free",
    "mcp_server": null,
    "monthly_post_limit": 100
  },
  "posting_schedule": {
    "morning": "07:00-09:00",
    "noon": "12:00-13:00",
    "evening": "19:00-22:00"
  },
  "reference_accounts": [],
  "content_balance": {
    "main": 0.6,
    "sub1": 0.25,
    "sub2": 0.15
  }
}
```

config.json は `.gitignore` 推奨（API key を後で入れる）。

### Step 2. ストックファイルの初期化

```bash
mkdir -p ~/.claude/skills/x-workflow/storage/stocks
touch ~/.claude/skills/x-workflow/storage/stocks/pending.md
touch ~/.claude/skills/x-workflow/storage/stocks/posted.md
touch ~/.claude/skills/x-workflow/storage/stocks/drafts.md
```

それぞれにヘッダーを書く：

`pending.md`:
```markdown
# ストック（未投稿）

最終更新: YYYY-MM-DD HH:MM

---
```

`posted.md`:
```markdown
# 投稿済みログ

---
```

`drafts.md`:
```markdown
# 起案中・没・メモ

---

## 起案中（要オーナー承認）

---

## 没（参考用に残す）

---

## ネタメモ（未着手）

---
```

### Step 3. プロフィール文の確定

`templates/profile.md` を読み込み、@ID 確定後の最終版を作る。

確認項目：
- 表示名: 「アトリエの店主」
- ID: @AtelierBase_own（空き確認後に確定）
- 自己紹介文（150文字以内）: アカウント世界観 + LINEリンク
- 場所: 任意（屋号「Atelier Base」関連でもOK）
- ウェブサイト: Atelier Base のHP URL（要確認）

オーナーと一緒に最終版を確定し、`templates/profile.md` を更新する。

### Step 4. 固定ポストの確定

`templates/pinned-post.md` を読み込み、最終版を作る。
立ち上げ後、最初の投稿として実行し、Xアプリでピン留め設定する。

### Step 5. LINE 動線の検証

- LINEリンクが正しく動くか
- 登録後のアンケート（3-4問）が表示されるか
- セグメントタグが正しく付くか
- ステップ配信が動くか

LINE運用ツール（L Step / プロラインフリー / LINE公式）の設定はここで行う。

### Step 6. 参考アカウントの登録

`config.json` の `reference_accounts` に、観察したいアカウントを登録：

```json
"reference_accounts": [
  "@example_account_1",
  "@example_account_2"
]
```

これは `references/01-neta.md` のフェーズ①で使う。

### Step 7. 初回投稿の準備

立ち上げの「最初の3-5本」を `/x-workflow 生成` で起案する。
特に最初の自己紹介スレッドは丁寧に作る：

- ポスト1: 「アトリエの店主と申します」自己紹介
- ポスト2: なぜこのアカウントを作ったか
- ポスト3: 何を発信するか
- ポスト4: どんな人に来てほしいか
- ポスト5: LINEへのCTA

これを最初の数日で投稿し、固定ポストに設定する（固定は自己紹介スレ or LINE誘導ポスト、どちらでも）。

### Step 8. 運用ペースの確認

- 1日3本投稿（Free枠制限内）
- 朝・昼・夜の時間帯を意識
- ストック残10本を最低ライン
- 週1回の分析タイミングを決める（例: 金曜夜）

## チェックリスト

- [ ] config.json 作成・編集済み
- [ ] storage/stocks/ 配下のファイル初期化済み
- [ ] プロフィール文確定・X側にも反映
- [ ] 固定ポスト確定・X側にもピン留め
- [ ] LINE登録〜セグメント振り分けまで動作確認済み
- [ ] LINE運用ツール選定済み（L Step / プロラインフリー / LINE公式）
- [ ] 参考アカウントを config.json に登録
- [ ] 初回スレッド（自己紹介）作成済み
- [ ] 週次分析タイミングをカレンダーに登録

## 次のアクション

セットアップ完了後は：
1. 初回投稿（自己紹介スレ＋単発1-2本）を流す
2. 1週間後に最初の分析タイミング
3. 4週後にPhase 2移行（scheduled or api 検討）

このセットアップは1回きり。以降は `/x-workflow ネタ` → `/x-workflow 生成` → `/x-workflow 配信` の3コマンドで回す。
