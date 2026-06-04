# ROUTINE — X（@AtelierBase_own / ひろ｜AI実業家）ストック自動補充

> ⚠️ **2026-06-04 廃止（DEPRECATED）**: 在庫補充モデルは終了。現在は**直投稿アーキ**。
> Routine は各スロットに `.claude/skills/x-post-now/SKILL.md` を発動し、1本生成→push→送信専用Actionsが配信する。
> この補充手順は使わない（参考保存）。最新は repo直下の README / ハブの CLAUDE.md・ROUTINE-SETUP.md を見ること。

> **Claude Code の Routines（クラウド・スケジュール実行）が無人で実行する標準指示書。**
> 必要な知識はすべてこの repo 内（`skill/` 配下）に同梱。ローカルのスキルや grok には依存しない。

## 役割

**「ストック補充マシン」**。Researcher → Writer の2役割を回し、`storage/stocks/pending.md` を補充して push する。
**配信は GitHub Actions（毎日 JST 07:05 / 12:05 / 19:05）が担当**。このルーティンは投稿しない。
（分析＝Analyst は別立て・ローカル。`ANALYSIS.md` 参照）

## 設定

| キー | 値 | 意味 |
|---|---|---|
| `TARGET_BUFFER` | **9** | pending がこの本数以上なら今回は生成せずスキップ |
| `MAX_PER_RUN` | **6** | 1回の実行で生成する最大本数 |
| `POST_CHAR_LIMIT` | **280** | 1投稿の文字数上限 |

## 手順

### Step 1. 残量チェック
`storage/stocks/pending.md` の `## YYYY-MM-DD-NNN` 見出し数を数える。
- **9以上** → 生成不要。`storage/analytics/routine.log` に `skip: pending=N` を追記して **commit & push して終了**。
- **9未満** → 不足分 `(9 - 現在数)`（上限 `MAX_PER_RUN`）を生成する。

### Step 2. Researcher を実行（ネタ仕入れ）
`skill/agents/researcher.md` の定義に従う。**WebSearch のみ**（grok不可）、直近1週間の Claude Code / Codex 情報を集めて選別 → ネタリスト。
（サブエージェントに委譲してもよい。クラウドで Task/サブエージェントが使えない場合はメインが直接実行）

### Step 3. Writer を実行（投稿生成）
`skill/agents/writer.md` の定義に従う。書く前に必ず読む：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md`（v3.2）/ `skill/references/02-generate.md`
- **`storage/analytics/learnings.md`**（効くルールを毎回反映＝学習の複利）

不足本数を生成。軸比率 主軸50%/サブ軸1 30%/サブ軸2 20%、足りない時間帯（朝/昼/夜）を優先。
**投稿タイプは3種を均等に（各1/3）**。1回の生成でも全体でも、なるべく各1/3になるよう配分する（例：3本なら各1本）：
- `単発`
- `コメント仕込み`（メイン＋セルフリプライ。出典URLはコメントへ）
- `画像付き`（画像プロンプト＋画像ファイルパスを記載。下記 Step 5 の画像指示を必ず出す）

### Step 4. pending.md へ追記
`skill/agents/writer.md` のフォーマットで末尾に追記（既存は消さない）。
キー `## ID` / `投稿想定時刻: 朝|昼|夜` / `- ステータス: pending` は崩さない。

### Step 5. 画像付きを生成した場合（重要）
画像はオーナーが ChatGPT(image) で手動生成する（Path B）。ルーティンは **オーナー向け画像指示**を `storage/analytics/image-requests.md` に追記し、ログにも出す：
```
## [投稿ID] 画像リクエスト（YYYY-MM-DD）
- 投稿プレビュー: [本文の冒頭]
- GPTに投げるプロンプト: [画像プロンプト全文]
- 保存先: storage/images/[投稿ID].png   ← この名前で保存してコミット
```
画像が未配置でも配信は本文のみでフォールバックするので、ルーティンは止まらない。

### Step 6. ログ → commit & push
1. `storage/analytics/routine.log` に `YYYY-MM-DD HH:MM JST | generated N | pending 旧→新` を追記
2. `git add -A && git commit -m "routine: stock +N (auto-refill)" && git push`

## 完全無人の原則
- 途中で人間に承認を求めない（クラウド実行なので止まる）
- 生成0でも routine.log を残して push する
- エラー時は routine.log にエラーを残して終了。pending.md は壊さない

## チェックリスト（push 前）
- [ ] 全投稿が一人称「私」・絵文字0〜1個・280字以内
- [ ] 直近1週間のフレッシュネタ（発表時期を確認）
- [ ] learnings.md の効くルールを反映した
- [ ] フォーマットのキーが崩れていない／既存を消していない
- [ ] 画像付きがあれば image-requests.md に指示を追記した
- [ ] routine.log を更新した
