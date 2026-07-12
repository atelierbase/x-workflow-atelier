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
## 2026-07-12-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-12（日）
- 軸: サブ軸1 / 自分の実例
- ソース: Anthropic Claude Code CHANGELOG.md: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- 画像プロンプト: Use case: infographic-diagram. Asset type: X Japanese post summary card, landscape PNG, target 1536x1024. Primary request: Create a clean Japanese practical insight card for founders and developers using Claude Code / Codex. This must be a post summary card, not a research card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Core insight: When AI coding agents feel unstable, do not add more instructions first. Trim the checked-in project instruction file. Claude Code's /doctor can propose trimming checked-in CLAUDE.md content that Claude can derive from the codebase. Practical habit: before adding rules, remove duplicated or obvious instructions and keep only decisions the agent cannot infer. CRITICAL TEXT RULE: use ONLY these five visible text blocks. Do not add any other readable words, letters, file names, bullet text, code text, UI labels, captions, footer, watermark, dates, or source names anywhere in the image. Decorative cards must use plain lines and shapes only, no words. Exact visible text blocks: 1. Main headline, very large: 「指示を増やす前に削る」 2. Small subheadline: 「CLAUDE.mdを軽くする」 3. Small label: 「重複」 4. Small label: 「自動で分かる」 5. Small label: 「残す指示」 Visual structure: a clutter-to-clean workflow, not a fixed 3-column academic card. Left side: a messy stack of instruction notes labeled only 「重複」, with crossed-out plain horizontal lines and duplicate-looking blank marks, but absolutely no other text. Middle: a clean diagnostic lens/checkpoint labeled only 「自動で分かる」, showing abstract folder/check shapes and plain lines, no filenames or code. Right side: one short neat instruction card labeled only 「残す指示」 with a star/check icon and three plain blank lines, no text. Use a curved or stepped path so the flow reads: too many instructions -> diagnosis -> smaller useful rule set. The main headline is the dominant reader judgment. Design style: modern Japanese business infographic, high legibility, landscape composition, warm white background, deep charcoal headline, muted gray for clutter, teal for diagnostic clarity, restrained green for the final kept instruction. Large typography, generous spacing, maximum 5 text blocks, short labels only. It should feel immediately useful to a founder/operator or developer using Claude Code or Codex. Avoid: any extra readable text besides the five specified blocks, generic AI atmosphere, random laptop, decorative-only scene, robot mascot, source/date/research-card layout, dense UI, tiny explanatory text, 3-column fixed academic card, code screenshots, brand logos. Text accuracy: Japanese text must be correctly spelled with no garbling, especially 「指示を増やす前に削る」「CLAUDE.mdを軽くする」「重複」「自動で分かる」「残す指示」.
- 画像ファイル: storage/images/2026-07-12-702.png
- 文面:

AIに指示を足すほど、逆に迷子になることがあります。

Claude Codeの最新CHANGELOGでは、/doctorがchecked-in CLAUDE.mdの削りどころを提案するようになりました。CLAUDE.mdは、プロジェクトごとのAIへの指示書です。

私の実務判断は、追加より先に棚卸し。今日、自分のCLAUDE.mdから「コードを見れば分かる指示」を1つ消してみてください。

- ステータス: pending

---
