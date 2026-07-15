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
## 2026-07-15-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-15（水）
- 軸: サブ軸2 / 実業家視点
- ソース: Claude Code v2.1.208 official release notes https://github.com/anthropics/claude-code/releases/tag/v2.1.208
- 画像プロンプト: Use case: infographic-diagram. Asset type: X post summary card, landscape PNG, 1536x1024 composition. Primary request: Create a clean Japanese social post summary card about a practical lesson for Claude Code / Codex-like coding agents: connecting too many MCP tools can make agent work feel heavy, so reduce tools before adding more. This is NOT a release-note card, NOT a research-card, and NOT a source summary. It should feel immediately personal to a builder who lets AI development agents use external tools. Core message: Before adding more tools, narrow the tool scope. The viewer should understand the conclusion, background pain, and practical action from the image alone. Visible text: use ONLY these exact Japanese text blocks, no other readable text, no English, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「つなぐ前に減らす」 2. Small pain label: 「MCPが多い」 3. Small problem label: 「処理が重い」 4. Small action label: 「使う分だけ」 5. Small routine label: 「週1で棚卸し」 Visual structure: a left-to-right clutter-to-focus flow, NOT three columns and NOT three side-by-side panels. Left side: many small connected tool nodes crowding around an AI-agent work queue, creating visual congestion, labeled 「MCPが多い」 and 「処理が重い」. Center: a simple narrowing filter/funnel that removes unused tool nodes. Right side: a smaller clean tool set connected to a clear task path, with check chips labeled 「使う分だけ」 and 「週1で棚卸し」. The headline sits across the upper-left/center with lots of negative space and should dominate the card. Use simple node lines, small toolbox icons with no letters, check marks, blank terminal-like rectangles with no text, and abstract symbols only. Style: modern Japanese business infographic, high readability, off-white background, deep charcoal headline, muted gray for clutter, calm green/teal for focused tools, small amber caution accent. Professional but warm, bold typography, generous spacing. Maximum 5 text blocks total. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense UI, research paper layout, release notes layout, any fixed 3-column layout, three rectangular panels, purple-blue gradient dominance, beige/brown dominance, watermarks, logos, malformed Japanese, extra readable text, English letters, command prompts, code snippets. Ensure Japanese text is correctly spelled with no garbling, especially 「つなぐ前に減らす」「MCPが多い」「処理が重い」「使う分だけ」「週1で棚卸し」.
- 画像ファイル: storage/images/2026-07-15-703.png
- 文面:

MCPを増やすほど、AIが賢くなるとは限りません。

Claude Codeの直近リリースでは、多数のMCPツールがある環境でツール処理が最大7倍軽くなる改善が入りました。MCPはAIに外部ツールをつなぐ仕組みです。

私の実務判断は、追加より棚卸し。今日、使っていないMCPを1つ外してから、Claude CodeやCodexに小さな作業を渡すと安心です。すぐ試せます。

- ステータス: pending

---
