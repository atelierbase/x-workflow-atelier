# ANALYSIS — X 週次分析（ローカル実行）

> **これは Analyst ロールのローカル実行プレイブック。**
> 分析は **grok-search を使うためクラウドルーティンにできない**。このMac上で週1回走らせる。

## いつ走るか

- 週1回（例: 毎週金 or 土の夜）
- ローカル cron（CronCreate）or 「Xの分析して」で秘書が手動起動

## 何をするか

`skill/agents/analyst.md` の手順に従う。要約：

1. `storage/stocks/posted.md` の直近7日を一覧化
2. **grok-search** で `@AtelierBase_own` の反応・数字を取得
   （例: 「@AtelierBase_own の直近7日の投稿で反応が多かった/少なかったものを、いいね・引用の中身とともに」）
3. オーナーが数字スクショを貼っていればそれを優先
4. 伸びた/伸びなかったに「なぜ？」の仮説 → 反証で潰す → 効くルールに蒸留
5. **`storage/analytics/learnings.md` に追記**
6. commit & push（→ 次回クラウドの Writer が learnings を読む）

```bash
cd ~/atlier-base-v1/products/x-workflow-repo
git add storage/analytics/learnings.md
git commit -m "analysis: weekly learnings update (X)"
git push
```

## データ源（ハイブリッド）

| 源 | 取得 | 備考 |
|---|---|---|
| grok-search | いいね/リプ/インプ傾向＋反応の中身 | 主役・ローカルのみ |
| 手動フィード | オーナーがスクショ/数字 | 最優先データ |
| X API Free | like/reply/repost count | 取れれば補助 |

## ループの閉じ方

ローカル Analyst が learnings.md 更新 → push → クラウドの Writer が次回参照。
**補充＝クラウド / 分析＝ローカル**の役割分担で複利が回る。
