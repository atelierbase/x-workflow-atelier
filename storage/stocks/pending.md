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
## 2026-07-03-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-03（金）
- 軸: サブ軸2 / 実業家視点
- ソース: https://developers.openai.com/blog/connect-private-mcp-servers-to-openai-products
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese X post summary card for @AtelierBase_own Primary request: Create a landscape PNG summary card, 1536x1024 aspect ratio. This must be a practical social post summary card, not a research card and not an atmosphere image. The viewer should understand in 1 second: conclusion, background, and practical action. Core message: When connecting AI coding agents / Codex to internal tools through MCP, do not expose private servers just to make them reachable. Keep the private tool inside the company boundary, let a small customer-controlled client initiate the outbound connection, and limit the reachable targets. This is about operational boundary design, not a product announcement. Visible text: Use ONLY these exact 5 Japanese text blocks. No other visible words, no English, no dates, no source names, no research labels, no watermark: 1. Main headline, very large: 「社内ツールは公開しない」 2. Small subtitle: 「つなぐほど境界を決める」 3. Label: 「外へ開けない」 4. Label: 「内側から接続」 5. Label: 「許可範囲だけ」 Visual structure: a boundary-and-flow card, not a fixed 3-column academic layout. Show a protected internal tool/server area on the left behind a clear boundary wall or shield. Show a narrow outbound path initiated from inside that boundary, passing through a controlled gate/checkpoint in the middle. Show an AI agent/workflow area on the right receiving only approved requests. Use a curved or stepped flow from left to right with gate icons, lock/check motifs, and a scoped access ring. Avoid equal three columns; use a strong left protected-zone vs right agent-zone contrast with a narrow controlled bridge. Style/medium: modern Japanese business infographic, polished editorial card, flat vector-like shapes rendered as a high-quality raster image. Composition/framing: large headline at top-left or top-center, the boundary flow across the middle, generous spacing, readable on mobile. Maximum 5 text blocks. Color palette: clean off-white background, deep charcoal headline, blue-gray internal tool shapes, amber boundary/gate accent, green approval/check accent, subtle muted red only around blocked public exposure. Constraints: Japanese text must be crisp and exactly spelled. Do not insert spaces inside Japanese labels. Do not add source names, dates, paper labels, paragraphs, tiny captions, screenshots, code snippets, laptops, robots, mascots, product logos, or decorative-only elements. Avoid generic AI atmosphere, random laptop, decorative-only scene, research summary card, source/date labels, distorted or garbled Japanese text, misspellings in 「社内ツールは公開しない」「つなぐほど境界を決める」「外へ開けない」「内側から接続」「許可範囲だけ」.
- 画像ファイル: storage/images/2026-07-03-703.png
- 文面:

社内ツールをAIにつなぐ時は、外へ公開する前に一度止まった方がいいです。便利さより、境界設計が先です。

MCPはAIに社内ツールを渡す接続規格ですが、OpenAIは内側から接続するSecure MCP Tunnelを紹介しています。少し地味ですが、ここが肝だと思っています。

私ならまず、Codexに触らせるツールを最小限に絞ります。今日できる小さな行動は、「AIに見せる範囲」を一行で書くことです。

- ステータス: pending

---
