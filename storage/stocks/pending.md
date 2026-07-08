# 受け渡しキュー（image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで X へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- 2026-06-29 の伸び悩み対応で、古い未消化キューは `archive/pending-stale-growth-reset-2026-06-29.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-07-08-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-08（水）
- 軸: サブ軸1 / 自分の実例
- ソース: https://arxiv.org/abs/2607.01418
- 画像プロンプト: Create a landscape PNG infographic card for an X post, 1536x1024. Japanese text must be clear, short, and accurate. This is a practical post summary card, not a research card and not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Main headline, large bold Japanese: 「全員配布より頻度で選ぶ」 Small subheadline: 「AI開発エージェントは“使う場面”が多い人から残る」 Visual structure: a branching decision flow, not a fixed three-column card. Start at the left with a simple decision sign labeled 「導入先を決める」. Split into two paths: top muted gray path labeled 「熱量で選ぶ」 ending in a small fading card; bottom bright blue-green path labeled 「作業頻度で選ぶ」 leading to a clear action card. On the action card, show exactly two compact checks: 「週1タスク」 and 「小さくAI化」. Add one small supporting badge, not dominant: 「継続利用の差」. Use only these visible Japanese text blocks: 「全員配布より頻度で選ぶ」, 「AI開発エージェントは“使う場面”が多い人から残る」, 「導入先を決める」, 「熱量で選ぶ」, 「作業頻度で選ぶ」, 「週1タスク」, 「小さくAI化」, 「継続利用の差」. Keep labels short and legible. Design style: modern Japanese business infographic, high contrast, off-white background, deep charcoal headline, muted gray for the weak path, calm blue-green for the practical path, small amber accent on the supporting badge. Make it feel immediately relevant to a solo founder or small business operator deciding where to introduce Claude Code / Codex / CLI coding agents. Avoid generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense code background, research paper layout, source/date label as hero, or fixed three-column layout. Maximum 5 visual text zones even if labels are grouped. Ensure Japanese spelling is correct with no garbling, especially 「全員配布より頻度で選ぶ」「作業頻度で選ぶ」「週1タスク」「小さくAI化」.
- 画像ファイル: storage/images/2026-07-08-702.png
- 文面:

AI開発エージェントは、全員に同じ温度で配らなくていいです。

Microsoftの大規模調査では、継続利用は年齢や属性より「普段どれだけコードを書くか」と強く結びついていました。使う場面が多い人ほど残りやすい、という話です。

私の実務判断は、最初の配布先を熱量ではなく作業頻度で選ぶこと。

今日、週1で繰り返す開発タスクを1つだけAI化してみてください。

- ステータス: pending

---
