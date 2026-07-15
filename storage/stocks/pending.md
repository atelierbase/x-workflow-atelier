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
## 2026-07-15-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-15（水）
- 軸: サブ軸1 / 自分の実例
- ソース: Claude Code v2.1.210 official release notes https://github.com/anthropics/claude-code/releases/tag/v2.1.210
- 画像プロンプト: Use case: infographic-diagram. Asset type: X post summary card, landscape PNG, 1536x1024 composition. Primary request: Create a clean Japanese social post summary card about a practical lesson for Claude Code / Codex-like coding agents: before delegating work to an agent, confirm where it will edit. This is NOT a release-note card, NOT a research-card, and NOT a source summary. It should feel immediately personal to a builder who lets AI development agents edit code. Core message: Do not hand off work until the edit location is visible. The viewer should understand the conclusion, background risk, and practical action from the image alone. Visible text: use ONLY these exact Japanese text blocks, no other readable text, no English, no letters on icons, no code snippets, no file-extension labels, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「任せる前に場所を見る」 2. Small risk label: 「本体に触る？」 3. Small action label: 「作業場所を分ける」 4. Small check label: 「git status確認」 5. Small action label: 「小さく任せる」 Visual structure: one continuous diagonal flow from bottom-left to top-right, NOT three columns and NOT three side-by-side panels. Start with a crowded main repository folder at bottom-left with only blank document icons and abstract code glyphs, plus a small amber warning bubble labeled 「本体に触る？」. The flow then splits upward through a forked branch/worktree path in the center labeled 「作業場所を分ける」. It ends at top-right with a compact verification checklist containing two check chips labeled 「git status確認」 and 「小さく任せる」. The headline sits across the top-left/center with lots of negative space and should dominate the card. Use simple branch lines, check marks, small folder/repo icons, blank terminal-like rectangles with no text, and abstract symbols only. Style: modern Japanese business infographic, high readability, off-white background, deep charcoal headline, calm green verification accents, small amber caution accent. Professional but warm, bold typography, generous spacing. Maximum 5 text blocks total. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense UI, research paper layout, release notes layout, any fixed 3-column layout, three rectangular panels, purple-blue gradient dominance, beige/brown dominance, watermarks, logos, malformed Japanese, extra readable text, English letters such as TS or py, command prompts, code characters that look like readable words. Ensure Japanese text is correctly spelled with no garbling, especially 「任せる前に場所を見る」「本体に触る？」「作業場所を分ける」「git status確認」「小さく任せる」.
- 画像ファイル: storage/images/2026-07-15-702.png
- 文面:

AIに任せるほど、怖いのは「どこを編集したか」が曖昧になることです。

Claude Code v2.1.210では、worktree分離のサブエージェントが本体checkoutへgit変更できる不具合が修正されました。これは作業場所を分ける仕組みです。

私の実務判断は、性能より境界線を先に見ること。今日から1タスクだけ、依頼前に`pwd`と`git status`を確認してから渡すと安心です。

- ステータス: pending

---
