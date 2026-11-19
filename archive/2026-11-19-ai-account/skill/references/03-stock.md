# 03-stock: ストック管理

このフェーズの目的は、生成 → 承認された投稿を**配信タイミングまで安全に保管**し、**配信状況を追跡可能**にすること。

## ファイル構造とデータの真実のソース

**重要**: 現運用（GitHub Actions）では、**真実のソースは GitHub 上**にある。

| 場所 | パス | 役割 |
|---|---|---|
| **GitHub（真実のソース）** | `atelierbase/x-workflow-atelier/storage/stocks/` | GitHub Actions が直接読む |
| ローカル（作業バッファ） | `~/atlier-base-v1/projects/sns-auto-post/x/storage/stocks/` | 私が生成 → push する場所 |
| スキル内（履歴・参考） | `~/.claude/skills/x-workflow/storage/stocks/` | スキル定義の一部・参考 |

### 各ファイル

```
storage/stocks/
├── pending.md  # 承認済み・未投稿（GitHub Actions が消費）
├── posted.md   # 投稿済み + 数値ログ（GitHub Actions が追記）
└── drafts.md   # 起案中・没・ネタメモ（ローカル管理）
```

### 編集フロー

- **秘書（Claude）が新規生成**: ローカル `x-workflow-repo/storage/stocks/pending.md` に追加 → `git push`
- **オーナーが微調整**: **GitHub UI** で直接編集 → "Commit changes"
- **投稿実行**: GitHub Actions が pending.md を読んで → posted.md に移動 → コミット & プッシュ

詳細は `references/09-github-actions.md` 参照。

## pending.md フォーマット

```markdown
# ストック（未投稿）

最終更新: YYYY-MM-DD HH:MM

---

## 2026-05-26-001
- 種類: 単発
- 投稿想定時刻: 朝7-9
- 想定日: 2026-05-27
- ネタ元: secretary/notes/2026-05-25-...
- 文面:

[投稿全文]

- 補足: [画像必要 / リンク添付 / 引用元URL など]
- ステータス: pending

---

## 2026-05-26-002
- 種類: スレッド（5ポスト）
- 投稿想定時刻: 夜19-22
- 想定日: 2026-05-28
- 文面:

ポスト1:
[全文]

ポスト2:
[全文]

...

- ステータス: pending

---
```

ID命名規則: `YYYY-MM-DD-NNN`（同日内の通番）

## posted.md フォーマット

```markdown
# 投稿済みログ

---

## 2026-05-26-001
- 種類: 単発
- 投稿日時: 2026-05-27 08:15
- 配信モード: manual / scheduled / api
- 文面:

[全文]

- 数値（24h時点）: impressions xxx / likes xxx / RT xxx / reply xxx / プロフクリック xxx
- 数値（7d時点）: impressions xxx / likes xxx / RT xxx / reply xxx / プロフクリック xxx / LINE登録寄与 推定◯人
- 所感: [伸びた / 普通 / 不調] - [理由仮説]

---
```

数値は手動 or X API経由で記録する。手動の場合は朝のルーティンで前日分を入力する習慣を作る。

## drafts.md フォーマット

```markdown
# 起案中・没・メモ

---

## 起案中（要オーナー承認）

### draft-001
- 種類: 単発
- 文面:
[全文]
- ステータス: 要承認

---

## 没（参考用に残す）

### killed-001
- 没理由: 「教える」トーンになりすぎ
- 文面（参考）:
[全文]

---

## ネタメモ（未着手）

- [メモ1]
- [メモ2]

---
```

## 操作

### ストック残量確認

`pending.md` のエントリ数をカウント。

- 残10本以上: 余裕
- 残5-9本: 通常
- 残3-4本: 注意。次回ネタ仕入れを推奨
- 残2本以下: ⚠️ 緊急。即ネタ仕入れ＋生成

### ストック追加

新規ストックは `pending.md` の末尾に追加。IDは当日の通番。

### ストックから取り出し（配信時）

`pending.md` の先頭から1つ取り出して、配信処理（→ `references/04-distribute.md`）。
配信完了したら `posted.md` に移動し、pending.md からは削除。

### リライト

`pending.md` のエントリを直接編集してOK。ただし削除はしない（履歴が消える）。

### 緊急差し込み

トレンド乗りなどで即時投稿したいときは、`pending.md` の先頭に挿入。

## ストック健全性ルール

1. **同日に種類が偏らない**: 単発ばかり、スレッドばかりは避ける
2. **時間帯がバラける**: 朝・昼・夜が混ざるように
3. **テーマ配分（主軸60% / サブ25% / サブ15%）を維持**: ストック内訳を時々チェック
4. **ストック0は絶対避ける**: 残3本切ったらアラート
5. **古すぎるストックは見直し**: 2週間以上未投稿のものは、文脈ズレで没になる可能性

## storage の初期化

初回利用時は `references/07-setup.md` の手順で初期化する。
`pending.md` / `posted.md` / `drafts.md` が存在しない場合は、ヘッダーだけのファイルを作成。

## 注意

- ファイルは Markdown のまま管理（DB化しない）。シンプルさ優先
- ストック内のURL短縮は配信時に決定（事前にやらない）
- ストックが「埃かぶってる」と感じたら、適度に没にしてリフレッシュ
