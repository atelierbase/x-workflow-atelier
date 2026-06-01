# 01-neta: ネタ仕入れ（v3.1 / 海外バズ翻訳パイプライン）

このフェーズの目的は、**直近1週間の海外バズ情報**を中心に、当週分の投稿ネタリスト（21本分）を作ること。

## 重要な前提

このアカウント「ひろ｜AI実業家」は **Claude Code / Codex 特化のニッチ専門アカウント**。
ネタの中心は **海外で先行している AI 開発情報の日本語翻訳**。
ローカル日記や抽象論ではなく、**最新かつ実用的な専門情報** が伸びる。

## 入力

なし（オーナーから「ストック作って」「次の3本」「次の1週間分」など）

## 出力

ネタ候補リスト（次フェーズ「生成」への入力）。
**1週間分なら 21本**（朝7・昼7・夜7）。

## 鉄則：直近1週間に絞る

**過去の有名な話題ではなく、本当に直近1週間の新着情報**を中心にすること。

| ❌ NG（古い・抽象的） | ◎ OK（直近の具体的新着） |
|---|---|
| 「Karpathy が AI コーディングの罠を指摘」（2026年1月） | 「Lars Faye のバイラル批判記事が今週HN1位」（直近） |
| 「Plan Mode の使い方」（汎用Tips） | 「Anthropic Routines for Claude Code Automation」（今週リリース） |
| 「Multiagent Orchestration」（5/7発表） | 「KPMG × Anthropic 276,000人提携」（5/19発表） |

**WebSearch のクエリには必ず「past week」「this week」「May 19-26 2026」など期間を絞る**。

## ステップ

### Step 1. 海外ソースを並列で巡回（WebSearch + grok-search）

以下のクエリを **並列で実行**（4並列推奨）：

#### 必須クエリ4本（毎週）

1. `Anthropic Claude announcement news this week [今週の日付範囲]`
2. `Claude Code update feature release past week [今月]`
3. `OpenAI Codex GPT update news this week [今週の日付範囲]`
4. `Hacker News top AI coding agent trending this week [今月]`

#### 補助クエリ（深掘りしたい時）

- `Anthropic [新機能名] release announcement [今月]`
- `[製品名] vs [競合] 2026`
- `[トピック] best practices [今月]`

#### grok-search（X バズ取得）

- `Claude Code [トピック] lang:ja min_faves:100 within_time:7d`（日本語圏）
- `claude code OR codex AI coding lang:en min_faves:500 within_time:7d`（英語圏バズ）

### Step 2. 直近1週間のフレッシュネタを選別

WebSearch / grok-search の結果から、以下の基準で選別：

✅ **採用**:
- 直近1週間以内の発表・リリース
- 中級者にとって価値ある（実際の業務に使える）
- ニッチで競合の少ない情報
- 数字や具体的事例を含む

❌ **除外**:
- 過去発表の汎用Tips（「Plan Mode の使い方」など、いつでも書ける話題）
- 抽象的すぎる予測・哲学（読者が「で？」となる）
- 競合礼賛・他者攻撃
- 政治・宗教・性別系の話題

### Step 3. ネタを 21 本に配分

1週間分なら 7日 × 3 = 21 本。

**配分目標**:
- 朝（07-09）: 7本 / **主軸（海外翻訳）が中心**
- 昼（12-13）: 7本 / サブ軸1（自分の実例）が中心
- 夜（19-22）: 7本 / 主軸（解説）・サブ軸2（実業家視点）が混在

**軸別目標**:
- 主軸（海外翻訳・解説）: **50%（10-11本）**
- サブ軸1（自分の Claude Code/Codex 実例）: **30%（6-7本）**
- サブ軸2（AI実業家視点・思考）: **20%（4-5本）**

### Step 4. 各ネタにメタ情報をつける

各ネタは以下の構造で記録：

```
- トピック: [何の話か]
- ソース: [どこから取った情報か：URL/媒体名]
- 直近性: [いつ発表されたか・◯月◯日]
- ターゲット価値: [中級者にとってなぜ価値があるか]
- 想定軸: 主軸 / サブ軸1 / サブ軸2
- 想定時間帯: 朝 / 昼 / 夜
- ひろの実体験フック: [自分の使用例とどう繋げられるか]
```

## 主要ソース一覧

| ソース | URL | 特徴 |
|---|---|---|
| **Anthropic News** | https://www.anthropic.com/news | Claude / Claude Code の公式発表 |
| **OpenAI News** | https://openai.com/news/ | GPT / Codex の公式発表 |
| **Claude Code Docs / Changelog** | https://code.claude.com/docs/en/whats-new | Claude Code リリースノート |
| **Codex Changelog** | https://developers.openai.com/codex/changelog | Codex リリースノート |
| **Hacker News** | https://news.ycombinator.com/ | 開発者の議論・バイラル記事 |
| **Reddit r/ClaudeAI** | https://reddit.com/r/ClaudeAI | Claude 周辺コミュニティ |
| **Reddit r/OpenAI** | https://reddit.com/r/OpenAI | OpenAI 周辺コミュニティ |
| **GitHub trending** | https://github.com/trending | OSS の話題 |
| **Indie Hackers** | https://www.indiehackers.com/ | 個人開発者の事例 |
| **Releasebot** | https://releasebot.io/updates/anthropic | 自動集約された変更ログ |

## 出力フォーマット

ネタ仕入れの結果は以下の形式でまとめる。次フェーズ「生成」がこれを入力として使う：

```markdown
# ネタリスト YYYY-MM-DD（直近1週間: YYYY-MM-DD 〜 YYYY-MM-DD）

## A. 主軸候補（海外翻訳・10-11本）

1. **[トピック名]**
   - ソース: [URL/媒体]
   - 直近性: ◯月◯日発表
   - 想定時間帯: 朝
   - 想定価値: [中級者になぜ刺さるか]
   - ひろの実体験フック: [自分の使用例ヒント]

2. ...

## B. サブ軸1候補（自分の実例・6-7本）

...

## C. サブ軸2候補（実業家視点・4-5本）

...
```

## 後処理

ネタリストを `~/atlier-base-v1/projects/sns-auto-post/x/storage/stocks/drafts.md` に「ネタ起案」セクションとして追記。
次フェーズ「生成」では、このネタリストから21本に絞り込んで投稿文を作成する。

## よくある失敗パターン（v3.1 改訂時に学んだ）

1. **「過去の有名な話題」を新着と混同して入れてしまう**
   - → 必ず WebSearch のクエリに期間を入れる（"this week" "past week" "May 19-26 2026"）
2. **発表時期を確認せず、有名トピックだから採用してしまう**
   - → 「Karpathy 144k stars」「Multiagent Orchestration」など、有名でも数ヶ月前のものは除外
3. **抽象的な思考・哲学を主軸に入れてしまう**
   - → 主軸（朝枠）は必ず「直近の海外具体ニュース」。思考は夜のサブ軸2に
4. **ソースを記録し忘れる**
   - → 必ずネタ1つにつきソースURLを残す（後で投稿に出典を入れる時に必要）

## 注意

- ネタを集めすぎない。**21本 = 21トピックで十分**
- 1つのトピックで複数本書くと薄まる
- 翻訳元の英文を投稿に「直訳」しない。要点を抽出して「私」の言葉に
- 著作権配慮：要点抽出＋出典明示はOK、丸ごと翻訳引用はNG

## 履歴

- v1（廃止）: ローカル活動ログ起点（「アトリエの店主」キャラ）
- **v3.1（現行）**: 海外バズ翻訳パイプライン起点（「ひろ｜AI実業家」キャラ、直近1週間に絞る）
