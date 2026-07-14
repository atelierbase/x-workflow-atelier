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
## 2026-07-14-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-14（火）
- 軸: サブ軸2 / 実業家視点
- ソース: RuBench: Evaluating AI Coding Agents in Real-World Software Engineering Tasks (arXiv:2607.06411) https://arxiv.org/abs/2607.06411
- 画像プロンプト: Use case: infographic-diagram. Asset type: X post summary card, landscape PNG, 1536x1024 composition. Primary request: Create a clean Japanese social post summary card about choosing AI coding agents by execution evidence, not by model name alone. This is NOT a research-card or paper summary. It should feel immediately personal to a builder deciding whether to trust Claude Code / Codex-like coding agents in real work. Core message: The model name is not enough. Check what actually ran, where it routed, and whether tests passed. Visible text: use ONLY these exact Japanese text blocks, no other readable text, no English, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「モデル名だけで選ばない」 2. Supporting label: 「指定モデル」 3. Supporting label: 「自動迂回」 4. Supporting label: 「ログ確認」 5. Supporting label: 「テスト結果」 Visual structure: a decision-flow card, not a fixed three-column card. Left side shows a simple model badge labeled 「指定モデル」. A subtle split path bends through a hidden reroute gate labeled 「自動迂回」 toward the center. Right side shows a verification panel with two stacked checks labeled 「ログ確認」 and 「テスト結果」. The main headline spans the upper area and feels like a practical warning/judgment for the reader. Use arrows, check marks, route lines, and small terminal/test icons only. Style: modern Japanese business infographic, high readability, off-white background, deep charcoal headline, calm teal verification accents, small amber caution accent. Professional but warm, with generous spacing and bold typography. Maximum 5 text blocks total. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense UI, research paper layout, 3-column fixed card, purple-blue gradient dominance, beige/brown dominance, watermarks, logos, malformed Japanese, extra readable text.
- 画像ファイル: storage/images/2026-07-14-703.png
- 文面:

AI開発エージェントは、モデル名だけで選ぶと判断を間違えます。

7月7日のRuBenchでは、Claude CodeやCodex CLIを「製品設定」ごとに評価し、ある設定で20%のタスクが別モデルへ自動迂回していました。ここ、びっくりしました。

私の実務判断は、性能表より実行ログを見ること。今日から1タスクだけ、使ったモデル名・コマンド・テスト結果を残すと安心です。

- ステータス: pending

---
## 2026-07-14-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-14（火）
- 軸: サブ軸1 / 自分の実例
- ソース: ITPro: Flaws in some of the most popular AI coding tools left developers wide open to attack (Wiz GhostApproval report) https://www.itpro.com/security/flaws-in-some-of-the-most-popular-ai-coding-tools-left-developers-wide-open-to-attack
- 画像プロンプト: Use case: infographic-diagram. Asset type: X post summary card, landscape PNG, 1536x1024. Create a clean Japanese social post summary card about AI coding agent approval safety. This is NOT a research card, NOT a UI screenshot, NOT a news card. It should feel like a practical one-second warning for a builder using coding agents. CRITICAL TEXT RULE: Use ONLY these five Japanese text blocks as visible text. No other letters, no file names, no folder names, no button text, no English, no numbers, no dates, no source labels, no footer, no watermark: 1. 「承認前に実パスを見る」 2. 「見えている場所」 3. 「本当の保存先」 4. 「作業外に注意」 5. 「声に出して確認」 Visual structure: abstract path-resolution flow. Top: the main headline 「承認前に実パスを見る」 in very large bold type. Left: a simple outlined project box with generic folder/file icons only, labeled 「見えている場所」. Middle: a chain-link/symlink icon and a curved dashed arrow leaving the project boundary. Right: a destination box with a generic target icon only, labeled 「本当の保存先」. Near the boundary crossing: small caution triangle plus label 「作業外に注意」. Bottom right: checkmark badge plus label 「声に出して確認」. Do not draw any realistic app permission dialog, terminal screen, file tree, file path, filenames, folder names, approve/reject buttons, or code snippets. Style: modern Japanese business infographic, high readability, off-white background, deep charcoal headline, calm teal path/check accents, restrained red-orange caution accent, generous spacing, strong hierarchy. Maximum five text blocks total. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense UI, research paper layout, source/date labels, 3-column fixed card, purple-blue gradient dominance, beige/brown dominance, malformed Japanese, extra readable text.
- 画像ファイル: storage/images/2026-07-14-702.png
- 文面:

AI開発エージェントに任せるほど、「承認したつもり」の範囲が怖くなります。

ITProが紹介したWizのGhostApproval調査では、symlinkで作業フォルダ外へ書き込めるケースが複数ツールで確認されました。symlinkは別ファイルへの近道です。

私の実務判断は、許可前に実パスを見ること。今日から1回だけ、差分の保存先を声に出して確認すると安心です。

- ステータス: pending

---
