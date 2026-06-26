# 09-github-actions: GitHub Actions 自動配信運用

このスキルは GitHub Actions で X 自動投稿を実行する設計（Phase 3 / 2026-05-26 移行）。
PC の起動状態に関係なく、クラウド側で 24 時間動く。

## アーキテクチャ

```
[ローカル: Claude セッション]
   ↓ /x-workflow ネタ → /x-workflow 生成
[Claude が pending.md にストック追加]
   ↓ git push（私が代行 or オーナーが実行）
┌──────────────────────────────────────┐
│ GitHub: atelierbase/x-workflow-atelier │
│  pending.md ← 真実のソース             │
└──────────────────────────────────────┘
   ↓ オーナーが GitHub UI で内容確認・編集（任意）
   ↓ 毎日 JST 07:00 / 12:00 / 19:00
[GitHub Actions ワークフロー実行]
   ↓ scripts/scheduled_poster.py
[X API v2 で投稿]
   ↓ commit & push
[posted.md 更新、pending.md から削除]
```

## 主要設定値

| 項目 | 値 |
|---|---|
| リポジトリ | https://github.com/atelierbase/x-workflow-atelier |
| ワークフロー | `.github/workflows/scheduled-post.yml` |
| 投稿スクリプト | `scripts/scheduled_poster.py` |
| Secrets | `X_CONSUMER_KEY` / `X_CONSUMER_SECRET` / `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` |
| スケジュール | JST 07:00 / 12:00 / 19:00（cron UTC 22:00, 03:00, 10:00） |
| ジッター | ±15分 |
| Free Tier 上限 | 月100投稿 |

## オーナーと秘書（Claude）の役割分担

| ステップ | 秘書（Claude） | オーナー |
|---|---|---|
| 1. ネタ仕入れ | ◯（morning-trends + grok-search + 活動ヒアリング） | 素材提供 |
| 2. 投稿生成 | ◯（21本など、まとめて） | - |
| 3. ストック追加（pending.md） | ◯（ローカル → git push） | - |
| 4. **内容確認** | （提示） | ◯ **GitHub UI で見る** |
| 5. **編集・微調整** | リライト提案 | ◯ **GitHub UI で直接編集** |
| 6. 配信実行 | - | GitHub Actions が自動 |
| 7. 数値分析 | ◯（週次） | データ提供 |

## 運用サイクル

### 7日ごと（ストック切れ前 = 6/2 のような日）

1. 残ストック数を確認（pending.md のエントリ数）
2. オーナーから「最近の活動・気づき・撤退話」をヒアリング
3. 21本（1日3本 × 7日）を生成
4. ローカルの `~/atlier-base-v1/projects/sns-auto-post/x/storage/stocks/pending.md` に追記
5. `git push` で GitHub に反映
6. オーナーが **GitHub UI で内容確認 → 必要なら直接編集 → commit**

### 毎日（自動）

- JST 07:00 朝枠投稿（±15分のジッター）
- JST 12:00 昼枠投稿
- JST 19:00 夜枠投稿
- 各時間帯ごとに pending.md の該当ストックを1本消費

### 週次（金 or 土）

- posted.md で振り返り
- 伸びた投稿の特徴抽出
- 次の生成方針に反映（templates/voice-guide.md の「良い例」も更新）

## ファイル管理 - Single Source of Truth

| データ | 真のソース | 役割 |
|---|---|---|
| **ストック（pending.md）** | **GitHub** | GitHub Actions が直接読む |
| **投稿済みログ（posted.md）** | **GitHub** | コミット履歴で追跡可能 |
| voice-guide / templates / references | ローカル `~/.claude/skills/x-workflow/` | スキル定義 |
| config.json | ローカル + GitHub Secrets | 認証情報 |
| 投稿生成のドラフト | ローカル（作業バッファ） | 私が書いて push する |

**重要**：ローカルの `~/.claude/skills/x-workflow/storage/stocks/pending.md` は作業バッファに過ぎない。GitHub に push されて初めて投稿対象になる。

### 同期コマンド

ローカル → GitHub（私が生成した後）：
```bash
cd /Users/hirotomo.ishii/atlier-base-v1/projects/sns-auto-post/x
# pending.md を更新
git add storage/stocks/pending.md
git commit -m "stock: 7日分の新規生成"
git push
```

GitHub → ローカル（オーナーが UI 編集した分を取り込む）：
```bash
cd /Users/hirotomo.ishii/atlier-base-v1/projects/sns-auto-post/x
git pull
```

## オーナー向け：内容確認・編集の手順

### 配信待ちストックを見る

🔗 https://github.com/atelierbase/x-workflow-atelier/blob/main/storage/stocks/pending.md

### 投稿済みを見る

🔗 https://github.com/atelierbase/x-workflow-atelier/blob/main/storage/stocks/posted.md

### GitHub UI で編集

1. pending.md をブラウザで開く
2. 右上の **✏️ 鉛筆アイコン** をクリック
3. 編集
4. ページ下の "**Commit changes**" → コミットメッセージ入力（"edit post" 程度でOK）→ "Commit changes"

これで次回の自動配信から反映される。

### 編集時の制約

- ストックの ID フォーマット `## YYYY-MM-DD-NNN` は変えない
- `投稿想定時刻: 朝/昼/夜` は保持（スクリプトの判定キー）
- `- ステータス: pending` の行は消さない
- 本文は 280 文字以内
- 一人称・口調は `templates/voice-guide.md` v2（優しいですます調）を維持

### 緊急で投稿を入れたい

ストックは ID 順に消費されるので、緊急投稿は ID を当日付＋大きな番号で先頭に：

```markdown
## 2026-05-26-999
- 種類: 単発
- 投稿想定時刻: 夜（19:00-22:00）
- 文面:

緊急投稿の本文...

- ステータス: pending

---
```

これを pending.md の先頭エントリの直前に挿入してコミットすれば、次の「夜」枠で最優先で投稿される。

## トラブルシューティング

### 投稿されなかった

1. **Actions タブで失敗していないか**
   - https://github.com/atelierbase/x-workflow-atelier/actions
   - 赤い ✗ なら失敗、緑の ✓ なら成功

2. **scheduler.log を確認**
   - https://github.com/atelierbase/x-workflow-atelier/blob/main/storage/analytics/scheduler.log

3. **よくある原因**
   - 該当時間帯のストックがない → pending.md に「朝/昼/夜」のいずれかが切れた
   - 文字数オーバー（280超） → 編集時に増やしすぎた
   - API key 期限切れ・revoke → 再発行 → Secrets 更新

### 二重投稿が起きた

- 配信元は GitHub Actions のみ。古いローカル launchd は廃止済み。
- 念のため、古い launchd 設定が残っていないか確認:
  ```bash
  launchctl list | grep atelierbase
  ```
- 動いていたら停止し、`~/Library/LaunchAgents/` から該当 plist を退避:
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.atelierbase.x-workflow.scheduled-poster.plist
  ```

### Free Tier 月100投稿の上限が近い

- 月の中盤で残20本切ったら、配信ペースを落とすか、Basic Tier ($200/月) を検討
- もしくは、特定時間帯（例：昼）の自動化を一時停止 → workflow YAML から該当の cron を一時的に削除

### ストックが切れた / 切れそう

- 残5本以下になったら、Claude に「ストック生成して」と依頼
- 21本まとめて生成、ローカル → GitHub にプッシュ

## ワークフロー手動トリガー

緊急で投稿したいときや、テストしたいとき：

ターミナル：
```bash
gh workflow run scheduled-post.yml -R atelierbase/x-workflow-atelier
```

または、Actions タブで「Run workflow」ボタン。

## 関連ファイル

- `references/04-distribute.md` — 配信モード詳細
- `references/02-generate.md` — 生成フロー
- `references/03-stock.md` — ストック管理
- `templates/voice-guide.md` — 口調ガイド（v2）

## 履歴

- 2026-05-26: GitHub Actions 移行（launchd から）。アカウント `atelierbase` で運用開始
