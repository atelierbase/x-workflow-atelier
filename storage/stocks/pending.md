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
## 2026-07-02-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-02（木）
- 軸: サブ軸1 / 自分の実例
- ソース: https://arxiv.org/abs/2606.26959
- 画像プロンプト: Create a Japanese X post summary card as a landscape PNG, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: When delegating longer tasks to Codex or AI agents, decide the expected endpoint before starting, otherwise the work becomes hard to review. Use ONLY these exact 5 Japanese text blocks as visible text. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「任せる前に出口を決める」 2. Small subtitle: 「長い依頼ほど迷子になる」 3. Label: 「完了条件」 4. Label: 「確認方法」 5. Label: 「次の一手」 Visual structure: a Before/After style flow, not a fixed 3-column academic layout. Left side: tangled stack of task cards entering a messy path, implying longer AI-agent work gets confusing. Center: a clear decision gate/checkpoint with two concise labels 「完了条件」 and 「確認方法」 as the anchor. Right side: a clean action path leading to a small checklist card labeled 「次の一手」. Use arrows and a subtle bottleneck-to-clear-path transformation. Style: modern Japanese business infographic, clean off-white background, deep charcoal headline, blue task cards, amber caution accent near the messy path, green confirmation accent near the clean path. Large typography, generous spacing, maximum 5 text blocks, readable on mobile. Professional and practical, reader-first. Avoid: generic AI atmosphere, random laptop, robot mascot, decorative-only scene, research paper card, source/date labels, tiny explanatory text, extra captions, distorted or garbled Japanese text, inserted spaces inside Japanese labels, misspellings in 「任せる前に出口を決める」「長い依頼ほど迷子になる」「完了条件」「確認方法」「次の一手」.
- 画像ファイル: storage/images/2026-07-02-702.png
- 文面:

AIに長い仕事を任せるほど、先に出口を決める方が大事です。出口が曖昧だと、あとでレビューが詰まります。

6/25公開のCodex分析では、人なら8時間超のタスク依頼が年初から約10倍に増えていました。AIエージェントは、自分の代わりに手順を進めるAIです。

私も最近、任せる前に完了条件と確認方法を短く書くようにしています。今日の依頼だけ、出口を書いてから投げてみてください。

- ステータス: pending

---
