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
## 2026-07-06-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-06（月）
- 軸: サブ軸1 / 自分の実例
- ソース: https://arxiv.org/abs/2607.01418
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card for @AtelierBase_own Primary request: Create one landscape PNG summary card, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: AI coding agents such as Codex and Claude Code do not spread just because a company installs them. Adoption improves when actual peer usage is visible. A recent Microsoft field study found adopters of CLI coding agents merged roughly 24% more pull requests, but the practical takeaway is to show one real PR/workflow example so teammates can copy it. Visible text: Use ONLY these exact 5 Japanese text blocks. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「導入より見える化」 2. Small subtitle: 「AIエージェントは真似できる例で広がる」 3. Label: 「入れただけ」 4. Label: 「横で使う」 5. Label: 「PRを1本見せる」 Visual structure: a problem-to-action flow, not a fixed 3-column academic layout. Left side shows a muted blocked state: a tool installed but unused, represented by a small closed toolbox and quiet team area. Middle shows peer visibility: one developer workflow card being shown to teammates with a clear spotlight/arrow. Right side shows the practical action: a single pull request card with a check mark and a small +24% badge as a visual motif. Use stepped arrows from left to middle to right, with the right action area slightly larger and more concrete. Avoid equal columns; use an asymmetrical flow with a strong main headline. Style/medium: modern Japanese business infographic, polished editorial card, flat vector-like shapes rendered as a high-quality raster image. Composition/framing: large headline at top-left or top-center; flow across the middle; generous spacing; readable on mobile; maximum 5 text blocks total. Color palette: clean off-white background, deep charcoal headline, muted teal and blue-gray workflow shapes, warm amber highlight for visibility, green check accent. Avoid one-note purple/blue gradient. Constraints: Japanese text must be crisp and exactly spelled. Do not insert spaces inside Japanese labels. Do not add source names, dates, paper labels, paragraphs, tiny captions, screenshots, code snippets, laptops, robots, mascots, product logos, decorative-only elements, random terminal text, or extra words. Avoid generic AI atmosphere, random laptop, decorative-only scene, research summary card, source/date labels, distorted or garbled Japanese text, misspellings in 「導入より見える化」「AIエージェントは真似できる例で広がる」「入れただけ」「横で使う」「PRを1本見せる」.
- 画像ファイル: storage/images/2026-07-06-702.png
- 文面:

AI開発エージェントは、入れるだけでは定着しません。横で誰がどう使ったかを見える化する方が効きます。

CLI型エージェントは、ターミナルからAIに作業を任せる道具です。Microsoftの社内調査では、利用者のmerged PRが約24%増。

私なら、ツール配布より先に「Codexで通したPR」を1本だけ見せます。数字より、真似できる形が残るのがいいですね。

- ステータス: pending

---
