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
## 2026-07-12-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-12（日）
- 軸: サブ軸2 / 実業家視点
- ソース: arXiv: Harnessing Code Agents for Automatic Software Verification (2026-07-07) https://arxiv.org/abs/2607.06341
- 画像プロンプト: Use case: infographic-diagram Asset type: X Japanese post summary card, landscape PNG, target 1536x1024 / 3:2. Primary request: Create a clean, high-legibility Japanese practical insight card for founders and developers using Claude Code / Codex. This must be a post summary card, not a research card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Core insight: When delegating serious work to AI coding agents, do not rely on confidence or a final human skim. Build an acceptance gate first. Recent code-agent verification work shows the practical pattern: let the agent work freely, but only accept outputs that pass a deterministic checker or command. Translate this into everyday development/operations: before handing a task to Codex or Claude Code, define one concrete pass/fail check. CRITICAL TEXT RULE: use ONLY these five visible text blocks. Do not add any other readable words, letters, numbers, dates, source names, research labels, filenames, code text, UI labels, captions, footer, watermark, or brand logos anywhere in the image. Decorative cards must use plain lines and shapes only, no words. Exact visible text blocks: 1. Main headline, very large: 「合格条件を先に作る」 2. Small subheadline: 「AIを信じる前に通す」 3. Small label: 「任せる」 4. Small label: 「機械で判定」 5. Small label: 「通ったら採用」 Visual structure: a pass/fail gate flow, not a fixed 3-column academic card. Left side: a neutral task bundle moving forward, labeled only 「任せる」. Center: a prominent verification gate/checkpoint labeled only 「機械で判定」 with a shield/check icon, branching subtly with one muted rejected path and one clear accepted path, but no text on the branches. Right side: a clean approved output card labeled only 「通ったら採用」 with a check mark and three plain blank lines, no text. Use a curved or stepped path so the flow reads: delegate -> deterministic check -> accept only if passed. Design style: modern Japanese business infographic, warm white background, deep charcoal headline, muted gray for uncertain AI output, teal for verification, restrained green for accepted output, one small amber caution accent. Large typography, generous spacing, maximum 5 text blocks, short labels only. The main headline should feel like a reader pain/practical decision, not a paper title. It should feel immediately useful to a founder/operator or developer using Claude Code or Codex. Avoid: any extra readable text besides the five specified blocks, generic AI atmosphere, random laptop, decorative-only scene, robot mascot, source/date/research-card layout, dense UI, tiny explanatory text, 3-column fixed academic card, code screenshots, brand logos. Text accuracy: Japanese text must be correctly spelled with no garbling, especially 「合格条件を先に作る」「AIを信じる前に通す」「任せる」「機械で判定」「通ったら採用」.
- 画像ファイル: storage/images/2026-07-12-703.png
- 文面:

AIに任せた仕事ほど、「最後に人が見る」だけでは不安が残ります。

7月7日の検証研究では、Claude Codeに証明を書かせ、Coqで通ったものだけ採用する形で4,257件を自動化。Coqは、正しさを機械で確認する道具です。

私の実務判断は、信じる前に合格条件を作ること。今日、Codexに任せる1作業へ「通ったらOK」の確認コマンドを1つ付けてみてください。

- ステータス: pending

---
