# x-workflow-atelier

X (旧 Twitter) アカウント **@AtelierBase_own**（アトリエの店主）の自動投稿パイプライン。

GitHub Actions が毎日 **JST 07:00 / 12:00 / 19:00** に起動し、`storage/stocks/pending.md` から該当時間帯のストックを取り出して X に投稿、`posted.md` に移動する。

## アーキテクチャ

```
[GitHub Actions schedule (cron)]
        ↓
[checkout repo]
        ↓
[setup Python + tweepy]
        ↓
[scripts/scheduled_poster.py 実行]
        ↓
[X API v2 経由で投稿]
        ↓
[pending.md / posted.md を更新してコミット&プッシュ]
```

## ディレクトリ構造

```
.
├── .github/workflows/
│   └── scheduled-post.yml      # GitHub Actions ワークフロー
├── scripts/
│   └── scheduled_poster.py     # 投稿スクリプト
└── storage/
    ├── stocks/
    │   ├── pending.md          # 未投稿ストック
    │   └── posted.md           # 投稿済みログ
    └── analytics/
        └── scheduler.log       # 実行ログ
```

## 認証情報の管理

- GitHub Secrets に 4 種類の API key を登録:
  - `X_CONSUMER_KEY`
  - `X_CONSUMER_SECRET`
  - `X_ACCESS_TOKEN`
  - `X_ACCESS_TOKEN_SECRET`
- ローカル実行時は `~/.config/x-workflow/x-credentials.json` から自動で読む

## 手動実行

GitHub の Actions タブ → "Scheduled X Post" → "Run workflow"

または、ローカル:

```bash
~/.config/x-workflow/venv/bin/python scripts/scheduled_poster.py --dry-run
```

## ストック追加

`storage/stocks/pending.md` を編集してコミット&プッシュするだけ。
スキル `x-workflow` （`~/.claude/skills/x-workflow/`）で生成された投稿候補を貼り付ける。

## 関連

- Skill: `~/.claude/skills/x-workflow/`（コンセプト・口調ガイド・テンプレ・各 references）
- アカウント: [@AtelierBase_own](https://twitter.com/AtelierBase_own)
