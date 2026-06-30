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
## 2026-06-30-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-30（火）
- 軸: サブ軸2 / 実業家視点
- ソース: https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness
- 画像プロンプト: Create one complete landscape PNG social media summary card for X, 1536x1024. Use Codex image2 style generation only. This is a Japanese practical business infographic card, not HTML, not SVG, not a mockup, not a decorative atmosphere image. Purpose: a one-second self-relevant summary card for Japanese developers and business builders using Claude Code / Codex / AI coding agents. The card must communicate conclusion, background, and practical action by itself. Core claim: When you let an AI coding agent touch an external repository, decide the allowed execution boundary before optimizing for speed. Main headline must be large, short, and strong: 「AIに任せる前に線を引く」 Strict text rule: Render ONLY these exact 5 Japanese text blocks. Do not add any other letters, words, dates, source labels, UI text, captions, logos, watermarks, code snippets, numbers, or extra punctuation anywhere in the image. Icons and shapes must contain no internal text. 1. AIに任せる前に線を引く 2. 見た目は安全 3. 自動実行 4. 外部から操作 5. コマンド確認 Visual structure: use a left-to-right risk-to-guardrail flow, not three equal columns. Left side: a clean-looking repository folder/card with a calm green check icon, labeled 「見た目は安全」. Center: an automatic setup gear/terminal arrow, labeled 「自動実行」, leading to a warning boundary line. Right side: a blocked remote-control hand or network plug icon outside a shield boundary, labeled 「外部から操作」. Bottom or right-side action chip: a checklist/terminal icon, labeled 「コマンド確認」. The main headline sits top-left or top-center and dominates the card. Style: professional Japanese SaaS/productivity information card, warm white background, dark charcoal text, teal primary accent, muted amber warning accent, small green check accent, strong red only for the blocked external control. High contrast, generous margins, readable on mobile, polished editorial spacing, modern flat/vector-like raster infographic. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot faces, humanoids, code rain, sci-fi glow, dark blurry background, research paper layout, source/date/research labels as main focus, fixed three-column layout, tiny paragraphs, misspelled Japanese, distorted text, wrong labels, extra text, purple gradient.
- 画像ファイル: storage/images/2026-06-30-703.png
- 文面:

AIエージェントに外部リポジトリを触らせる時は、速さより先に「実行していい範囲」を決めた方がいいです。

Mozilla 0dinの検証では、きれいに見えるGitHubリポジトリ経由でClaude Codeが遠隔シェルまで誘導されました。遠隔シェルは外部から端末を操作される状態です。私の実務判断は、初回セットアップだけ人間が見ること。今日、clone後に走るコマンドを1つずつ読む時間を入れてください。

- ステータス: pending

---
