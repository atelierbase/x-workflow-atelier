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
## 2026-07-03-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-03（金）
- 軸: サブ軸1 / 自分の実例
- ソース: https://www.businessinsider.com/openai-codex-usage-limit-warroom-fix-issue-2026-6
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card for @AtelierBase_own Primary request: Create a landscape PNG summary card, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: Before delegating a long Codex / AI coding agent task, decide the stopping point, checkpoint timing, and usage check first. AI agent work can continue in the background through reviews and sub-tasks, so practical users should start small and inspect usage before scaling. Visible text: Use ONLY these exact 5 Japanese text blocks. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「任せる前に上限を決める」 2. Small subtitle: 「AI作業は裏側でも進む」 3. Label: 「小さく依頼」 4. Label: 「途中確認」 5. Label: 「使用量を見る」 Visual structure: a practical flow card, not a fixed 3-column academic layout. Show a task request entering a controlled gate on the left, then a winding path through small task cards and a usage meter, then a calm checkpoint panel on the right. The flow should communicate: start small -> check midway -> inspect usage. Include a subtle background layer showing faint behind-the-scenes activity cards moving in the back, but with no extra text. Use arrows, a visible limit gauge, and a checklist/checkpoint motif. Avoid equal three columns; use a diagonal or curved flow from lower-left to upper-right. Style/medium: modern Japanese business infographic, polished editorial card, flat vector-like shapes rendered as a high-quality raster image. Composition/framing: large headline at top-left or top-center, action flow across the middle, generous spacing, readable on mobile. Maximum 5 text blocks. Color palette: clean off-white background, deep charcoal headline, blue-gray task cards, amber limit/checkpoint accent, green usage-confirmation accent, small muted red warning accent only around unchecked background activity. Constraints: Japanese text must be crisp and exactly spelled. Do not insert spaces inside Japanese labels. Do not add source names, dates, paper labels, paragraphs, tiny captions, screenshots, code snippets, laptops, robots, mascots, logos, or decorative-only elements. Avoid: generic AI atmosphere, random laptop, decorative-only scene, research summary card, source/date labels, distorted or garbled Japanese text, misspellings in 「任せる前に上限を決める」「AI作業は裏側でも進む」「小さく依頼」「途中確認」「使用量を見る」.
- 画像ファイル: storage/images/2026-07-03-702.png
- 文面:

AIに長めの作業を任せる時は、先に「どこで止めるか」を決めた方がいいです。便利さの裏で、レビューやサブタスクが想像以上に走ることがあります。

Codexでも使用量が早く減る問題が報告され、原因の一つは自動レビューやsubagentの動きすぎでした。

私も長時間タスクは、小さく切って途中で使用量を見る運用に変えています。今日の一回だけ、依頼前に上限と確認タイミングを決めてみてください。

- ステータス: pending

---
