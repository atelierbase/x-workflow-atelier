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
## 2026-07-01-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-01（水）
- 軸: サブ軸2 / 実業家視点
- ソース: https://arxiv.org/abs/2606.30317
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card, landscape PNG, intended final size 1536x1024. Primary request: Create a clean modern Japanese business infographic card that summarizes this practical conclusion: when using AI agents with MCP tools, adding too many tools makes the agent choose worse, so narrow the tool set before delegating work. This is a post summary card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Visible text: use ONLY these exact 5 text blocks, no other visible words, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「道具を増やす前に絞る」 2. Small subtitle: 「MCPは多いほど迷う」 3. Left label: 「全部つなぐ」 4. Center label: 「選択で詰まる」 5. Right label: 「今週使う分だけ」 Visual structure: a left-to-right problem-to-action flow, not a fixed 3-column research card. Left side shows many small abstract tool/app blocks flowing into an AI agent decision point. Center shows a bottleneck/filter gate with a warning signal and a tangled path, visually expressing confusion. Right side shows a narrowed, calm checklist of three clean tool blocks and a clear green path. Make the center bottleneck the visual anchor. Style: high-legibility Japanese infographic, white/off-white background, deep charcoal text, restrained amber warning in the center, green for the narrowed action path, blue accents for tool blocks. Professional, practical, and reader-first. Generous spacing, large typography, no tiny explanatory text. Avoid: generic AI atmosphere, random laptop, robot mascot, decorative-only scene, research paper card, source/date footer, 3-column academic summary layout, extra captions, garbled Japanese text, misspelled MCP, extra labels beyond the five specified text blocks.
- 画像ファイル: storage/images/2026-07-01-703.png
- 文面:

AIに道具を増やすほど、逆に迷わせます。

6/29公開のMCPサーバー分析では、ツール数が増えると選択精度が落ち、10〜15個を超えると90%未満になるケースがありました。MCPはAIに外部ツールを渡す仕組みです。

これは便利さより運用設計の話です。私の実務では、全部つなぐ前に「今週使う道具」だけに絞ります。今日、MCPツールを3つ棚卸ししてみてください。

- ステータス: pending

---
