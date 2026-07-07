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
## 2026-07-08-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-08（水）
- 軸: 主軸 / 海外翻訳
- ソース: https://arxiv.org/abs/2607.01418
- 画像プロンプト: Create a landscape PNG infographic card for an X post, 1536x1024. Japanese text must be clear, short, and accurate. This is a practical summary card, not a research card and not an atmosphere image. Main message in large bold Japanese headline: 「配るだけでは定着しない」 Subheadline, smaller: 「AI開発エージェントは“見える成功例”から広がる」 Visual structure: Before/After + small action flow. Left side is muted gray Before panel labeled「Before」with one short label「ライセンス配布だけ」and a small warning icon. Right side is bright calm blue/green After panel labeled「After」with three compact blocks max: 1. 「1人で試す」 2. 「Before/Afterを見せる」 3. 「小さく横展開」 Add one small supporting metric badge, not dominant: 「PRマージ 約24%増」 Footer tiny source note only, not prominent: 「Microsoft大規模調査 / Claude Code・Copilot CLI」 Design style: clean modern business infographic, high contrast, readable Japanese typography, restrained palette white / charcoal / blue-green accents, no decorative-only scene, no laptop stock photo, no generic AI atmosphere, no random code background. Maximum 5 text blocks total. Make it feel immediately relevant to a solo founder or small business operator deciding how to introduce AI coding agents. Avoid making source name, date, or research label the hero.
- 画像ファイル: storage/images/2026-07-08-701.png
- 文面:

AI開発エージェントは、配るだけだと定着しません。

Microsoftの大規模調査では、初回利用は同僚の利用が見えるほど広がり、利用者はPRマージが約24%増えていました。PRはコード変更をレビューして取り込む単位です。

私の実務判断は、ライセンス配布より「隣の成功例」を先に作ること。

今日、1人だけ選んで1タスクのBefore/Afterを共有してみてください。

- ステータス: pending

---
