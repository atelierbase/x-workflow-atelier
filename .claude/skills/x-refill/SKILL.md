---
name: x-refill
description: X（@AtelierBase_own / ひろ｜AI実業家）のストック自動補充スキル。pending.md が9本未満なら researcher→writer を回して不足分を生成し pending.md へ追記、routine.log を更新して commit & push する。クラウドルーチンが無人実行する用。トリガー：「Xストック補充」「x-refill」または /x-refill。
---

# x-refill — X ストック自動補充（無人）

このスキルは X アカウント @AtelierBase_own（「ひろ｜AI実業家」/ 屋号 Atelier Base）の**ストック補充マシン**。
Researcher → Writer の2役割を回して `storage/stocks/pending.md` を補充し、commit & push する。
**配信は GitHub Actions（JST 07:05/12:05/19:05）が担当。このスキルは投稿しない。** 分析（Analyst）は別立て・ローカル。

> 詳細仕様はリポジトリの `ROUTINE.md` が正。このスキルはその実行手順をスキルとして発動可能にしたもの。

## 完全無人の原則
- 途中で人間に承認を求めない（クラウド実行なので止まると失敗扱い）
- 生成0でも `storage/analytics/routine.log` を残して push する
- エラー時も `pending.md` は壊さず log に残して終了

## 設定
| キー | 値 | 意味 |
|---|---|---|
| TARGET_BUFFER | 9 | pending がこの本数以上ならスキップ |
| MAX_PER_RUN | 6 | 1回の生成上限 |
| POST_CHAR_LIMIT | 280 | 1投稿の文字数上限 |

## 手順

### Step 1. 残量チェック
`storage/stocks/pending.md` の `## YYYY-MM-DD-NNN` 見出し数を数える。
- **9以上** → 生成不要。`storage/analytics/routine.log` に `skip: pending=N` を追記して **commit & push して終了**。
- **9未満** → 不足分 `(9 - 現在数)`（上限 `MAX_PER_RUN`）を生成。

### Step 2. Researcher（ネタ仕入れ）
**`researcher` サブエージェントが使えるなら Task で委譲**、使えなければメインが直接実行する。
`skill/agents/researcher.md` の定義に従い、**WebSearch のみ**（grok・ローカルスキル不可）で直近1週間の海外 Claude Code / Codex 情報を収集・選別 → ネタリスト。

### Step 3. Writer（投稿生成）
**`writer` サブエージェントが使えるなら Task で委譲**、使えなければメインが直接実行する。
書く前に必ず読む：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md`（v3.2）/ `skill/references/02-generate.md`
- **`storage/analytics/learnings.md`**（効くルールを毎回反映＝学習の複利）

不足本数を生成。一人称「私」/ 絵文字0〜1個 / 280字以内。軸比率 主軸50%/サブ軸1 30%/サブ軸2 20%、足りない時間帯（朝/昼/夜）を優先。
**投稿タイプを混ぜる**：基本=`単発` / `コメント仕込み`を1日1本目安（出典URLはコメントへ）/ `画像付き`を時々。

### Step 4. pending.md へ追記
`skill/agents/writer.md` のフォーマットで末尾に追記（既存は消さない）。
キー `## ID` / `投稿想定時刻: 朝|昼|夜` / `- ステータス: pending` は崩さない。
画像付きを作った場合は本文ブロックに `- 画像ファイル: storage/images/<投稿ID>.png` を必ず入れる。

### Step 5. 画像付きを生成した場合
`storage/analytics/image-requests.md` にオーナー向け画像指示を追記（投稿ID・本文プレビュー・GPTプロンプト全文・保存先 `storage/images/<投稿ID>.png`）。
画像未配置でも配信は本文のみでフォールバックするので止まらない。

### Step 6. ログ → commit & push
1. `storage/analytics/routine.log` に `YYYY-MM-DD HH:MM JST | generated N | pending 旧→新` を追記
2. `git add -A && git commit -m "routine: stock +N (auto-refill)" && git push`

## チェックリスト（push 前）
- [ ] 全投稿が一人称「私」・絵文字0〜1個・280字以内
- [ ] 直近1週間のフレッシュネタ（発表時期を確認）
- [ ] learnings.md の効くルールを反映した
- [ ] フォーマットのキーが崩れていない／既存を消していない
- [ ] 画像付きがあれば image-requests.md に指示を追記＋本文に画像ファイル行を入れた
- [ ] routine.log を更新した
