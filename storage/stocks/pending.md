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
## 2026-07-10-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-10（金）
- 軸: サブ軸1 / 自分の実例
- ソース: Anthropic Claude Code CHANGELOG.md: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- 画像プロンプト: Use case: infographic-diagram. Asset type: X Japanese post summary card, landscape PNG, target 1536x1024. Primary request: Create a timeline-stopping Japanese practical insight card about Claude Code / AI coding agent instructions. This must be a post summary card, not a research card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Core insight: AI coding agent instruction files do not get stronger just by adding more text. Claude Code's /doctor can now suggest trimming checked-in CLAUDE.md content that Claude can derive from the codebase. The practical move is to remove duplicated explanations in small increments. Visible text: use ONLY these exact Japanese text blocks, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「指示書は 足すより削る」 2. Small subheadline: 「AIへの説明が多すぎると判断が重くなる」 3. Small label: 「重複説明」 4. Small label: 「自動診断」 5. Small label: 「10行だけ削る」 Visual structure: a practical clog-to-clear workflow, not a fixed three-column academic card. Left side shows an overloaded instruction document with stacked note strips and tangled arrows, suggesting too much CLAUDE.md guidance. Center shows a simple diagnostic lens/checkup icon scanning the document. Right side shows a cleaner instruction file with fewer lines and a small green check, expressing the action: remove only duplicated explanations first. Use a left-to-right flow with visual rhythm: 「重複説明」 -> 「自動診断」 -> 「10行だけ削る」. The card must feel immediately useful to a founder/operator or developer using Claude Code or Codex. Design style: modern Japanese business infographic, high legibility, landscape composition, warm white background, deep charcoal headline, restrained teal for document elements, amber for clutter warning, green for the cleaned result. Large typography, generous spacing, maximum 5 text blocks, short labels only. Avoid generic AI atmosphere, random laptop, decorative-only scene, robot mascot, source/date/research-card layout, dense UI, tiny explanatory text, 3-column fixed academic card. Text accuracy: Japanese text must be correctly spelled with no garbling, especially 「指示書は 足すより削る」「AIへの説明が多すぎると判断が重くなる」「重複説明」「自動診断」「10行だけ削る」.
- 画像ファイル: storage/images/2026-07-10-702.png
- 文面:

AIへの指示書は、増やすほど強くなるとは限りません。

Claude Codeの最新CHANGELOGでは、/doctorが「コードから分かる内容までCLAUDE.mdに書いていないか」を見て、削る提案をするようになりました。CLAUDE.mdは、Claude Codeにプロジェクトのルールを渡す指示書です。

私も昼の見直しで、重複説明を10行だけ削ります。まず1ファイルからで十分です。

- ステータス: pending

---
