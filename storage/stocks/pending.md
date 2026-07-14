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
