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
## 2026-07-03-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-03（金）
- 軸: 主軸 / 海外翻訳
- ソース: https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card for @AtelierBase_own Primary request: Create a landscape PNG summary card, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: Before letting Claude Code or any AI coding agent work on an unfamiliar external GitHub repository, start in read-only / no-execution mode, then explicitly approve execution only after checking what will run. Visible text: Use ONLY these exact 5 Japanese text blocks. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「外部repoは即実行しない」 2. Small subtitle: 「便利さの前に安全確認」 3. Label: 「読むだけ」 4. Label: 「許可して実行」 5. Label: 「ログを残す」 Visual structure: a branching decision flow, not a fixed 3-column academic layout. Left side: an unfamiliar repository folder icon and a stack of clean-looking files entering a caution gate. At the gate, the safe path goes first to a calm read-only review panel labeled 「読むだけ」, then after a clear approval switch it moves to 「許可して実行」, ending with a checklist/log card labeled 「ログを残す」. Show the unsafe direct path as a faded red shortcut blocked by a stop marker, without extra text. Use arrows, a clear stop/approve decision point, and a simple transformation from risky shortcut to controlled workflow. Style/medium: modern Japanese business infographic, polished editorial card, flat vector-like shapes rendered as a high-quality raster image. Composition/framing: large headline at top-left or top-center, decision flow across the middle, generous spacing, readable on mobile. Maximum 5 text blocks. Color palette: clean off-white background, deep charcoal headline, blue-gray repository cards, amber caution accent, green approval/logging accent, small red blocked-path accent. Constraints: Japanese text must be crisp and exactly spelled. Do not insert spaces inside Japanese labels. Do not add source names, dates, paper labels, paragraphs, tiny captions, screenshots, code snippets, laptops, robots, mascots, or decorative-only elements. Avoid: generic AI atmosphere, random laptop, decorative-only scene, research summary card, source/date labels, distorted or garbled Japanese text, misspellings in 「外部repoは即実行しない」「便利さの前に安全確認」「読むだけ」「許可して実行」「ログを残す」.
- 画像ファイル: storage/images/2026-07-03-701.png
- 文面:

AIに外部リポジトリを触らせる時は、先に「実行しない」設定から始めた方が安全です。便利さに任せるほど、知らないコマンドまで走ります。

Mozilla 0dinの検証では、きれいに見えるGitHub repo経由でClaude Codeが誘導される例が紹介されました。AIエージェントは、指示に沿ってツール実行まで進めるAIです。

私も初見repoは、まず読むだけ。今日の一回だけ、clone前に実行許可を切って確認してみてください。

- ステータス: pending

---
