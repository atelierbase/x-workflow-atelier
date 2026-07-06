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
## 2026-07-06-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-06（月）
- 軸: サブ軸2 / 実業家視点
- ソース: OpenAI Developers Codex shortcuts teaser via The Verge (2026-06-29): https://www.theverge.com/ai-artificial-intelligence/959174/openai-codex-hardware-work-louder
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card for @AtelierBase_own Primary request: Create one landscape PNG summary card, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: Before adding Codex shortcut hardware or more buttons, decide the one recurring task worth delegating. OpenAI has teased a Codex shortcut device, but the practical business judgment is that the workflow must come before the button. Visible text: Use ONLY these exact 5 Japanese text blocks. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「押す前に手順を決める」 2. Small subtitle: 「Codexは反復タスクで効く」 3. Label: 「毎回迷う」 4. Label: 「手順化」 5. Label: 「1つだけ押す」 Visual structure: a decision flow, not a fixed 3-column academic layout. Left side shows messy repeated choices as stacked task cards and small tangled arrows. Center shows a clean checklist being narrowed to one repeatable workflow. Right side shows a single calm shortcut button connected to a PR description card with a check mark. Use an asymmetrical flow: left is cluttered, center is narrowing, right is calm and larger. The main headline should dominate. Do not make a device product render the hero; the hero is the practical decision. Style/medium: modern Japanese business infographic, polished editorial card, crisp vector-like shapes rendered as high-quality raster image, readable on mobile. Composition/framing: landscape 1536x1024, large headline top-left or top-center, generous spacing, maximum 5 text blocks total, sub-elements limited to three, no dense paragraphs. Color palette: clean off-white background, deep charcoal headline, restrained teal and blue-gray workflow shapes, warm amber highlight for the selected task, small green check accent. Avoid dominant purple/blue gradients and avoid beige-only palette. Constraints: Japanese text must be crisp and exactly spelled. Do not insert spaces inside Japanese labels. Do not add source names, dates, paper labels, paragraphs, tiny captions, screenshots, code snippets, laptops, robots, mascots, product logos, decorative-only elements, random terminal text, or extra words. Avoid: generic AI atmosphere, random laptop, decorative-only scene, research summary card, source/date labels, distorted or garbled Japanese text, misspellings in 「押す前に手順を決める」「Codexは反復タスクで効く」「毎回迷う」「手順化」「1つだけ押す」.
- 画像ファイル: storage/images/2026-07-06-703.png
- 文面:

ショートカットを増やす前に、Codexへ任せる反復タスクを1つ決めた方がいいです。

OpenAIがCodex向けの小型ショートカット端末を予告しました。便利そうですが、押す先の手順が曖昧だと、結局また迷います。

私なら、まずPR説明文づくりだけを固定化します。ワクワクする道具ほど、先に用途を細く決めたいです。今日できるのは、毎週くり返す作業を1つメモすることです。

- ステータス: pending

---
