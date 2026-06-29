# 受け渡しキュー（image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで X へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---## 2026-06-27-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-27（土）
- 軸: 主軸 / 海外翻訳
- ソース: https://arxiv.org/abs/2606.26959
- 画像プロンプト: Use case: infographic-diagram Asset type: X post information-card, LANDSCAPE 1536x1024 PNG. Create one clean Japanese infographic card. This must be a horizontal 3-column business information card, not a square image and not a poster. IMPORTANT TEXT RULES: Use ONLY these 6 Japanese text blocks. Do not add any other words, numbers, English, date, labels, captions, source labels, or punctuation beyond these exact blocks: 1. AIは並列運用へ 2. Codex利用研究 3. 5倍超 4. 3体以上 5. レビュー設計 6. 小さく分けて任せる Meaning to communicate visually: - Conclusion: AI agent work is moving toward parallel operation. - Background: Codex usage grew more than 5x, and users run 3+ agents. - Practical action: split work into small tasks and strengthen review design. Layout: - Top: big headline "AIは並列運用へ". - Top-right small pill: "Codex利用研究". - Middle: exactly three columns, each with one large short label: "5倍超", "3体以上", "レビュー設計". - Bottom footer: "小さく分けて任せる". - Use simple abstract icons only: trend arrow, three task cards, checklist shield. Style: modern Japanese SaaS/productivity information card, warm off-white background, deep navy text, teal and amber accents, crisp flat vector-like illustration, high contrast, generous margins, no people, no robots, no laptop. Avoid: random AI atmosphere, glowing brain, stock photo, decorative-only scene, extra text, misspelled Japanese, distorted characters, square crop.
- 画像ファイル: storage/images/2026-06-27-701.png
- 文面:

6月25日に公開された Codex の利用研究、かなり面白いです。

2026年前半でアクティブユーザーは5倍超。10%超の利用者が、週に3つ以上のCodexエージェントを並列で動かしているそうです。

エージェントAIは「作業を受け取って動くAI」。私も小さく分けて任せ、最後のレビューだけ厚くしています。

- ステータス: pending

---## 2026-06-28-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-28（日）
- 軸: 主軸 / 海外翻訳
- ソース: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- 画像プロンプト: Use case: infographic-diagram Asset type: X post information-card, LANDSCAPE 1536x1024 PNG. Primary request: Create one polished Japanese business infographic card summarizing a post about the latest Claude Code changelog. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Meaning to communicate visually: Conclusion: AI development agents are moving from flashy new features toward operational reliability. Background: recent Claude Code changelog emphasizes hook matching precision, background job recovery, and MCP reconnection/auth reliability. Practical action: before increasing agents, design them so they do not get lost, stop silently, or fail to reconnect. STRICT TEXT RULE: Render ONLY the exact text blocks below. Do not add any other letters, numbers, words, UI text, captions, labels, punctuation, dates, watermark, or logo anywhere in the image. Exact text to render: 1. AIエージェントは運用品質へ 2. Claude Code更新 3. フック厳密化 4. BG復旧 5. MCP再接続 6. 増やす前に、止まらない設計 Layout: Wide 1536x1024 horizontal card with generous margins. Top: large strong headline "AIエージェントは運用品質へ". Top-right small pill: "Claude Code更新". Middle: three clean columns, each with one concise label: "フック厳密化", "BG復旧", "MCP再接続". Use simple abstract icons only: precise hook/link icon, background task stack with restart arrow, plug/network reconnect arrow. Bottom footer action strip: "増やす前に、止まらない設計". Style: modern Japanese SaaS/productivity information card, warm off-white background, deep charcoal/navy text, teal and muted amber accents, small green reliability accent, crisp flat vector-like illustration, high contrast, readable on mobile, professional spacing. Avoid: generic AI atmosphere, glowing brain, robot, humanoid face, laptop photo, code rain, stock-photo scene, decorative-only scene, extra text, tiny paragraphs, misspelled Japanese, distorted letters, distorted English, wrong or extra numbers, square crop.
- 画像ファイル: storage/images/2026-06-28-701.png
- 文面:

直近のClaude Code changelog、派手な新機能より「運用品質」の改善が多くて面白いです。

hook matcherの厳密化、background jobsの復旧、MCP auth再接続など。hookは操作時に処理を走らせる設定、MCPはAIに外部ツールをつなぐ仕組みです。

私もエージェントを増やすほど、まず「落ちない・迷子にならない」を見ています。

- ステータス: pending

---## 2026-06-29-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-29（月）
- 軸: 主軸 / 海外翻訳
- ソース: https://arxiv.org/abs/2606.26959
- 画像プロンプト: Use case: infographic-diagram Asset type: X post information-card, LANDSCAPE 1536x1024 PNG. Primary request: Create one polished Japanese business infographic card summarizing a post about recent Codex usage research. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Meaning to communicate visually: Conclusion: AI agent work is shifting from one-off prompts to reusable skills and workflow assets. Background: recent Codex usage research found 26.6% of users use skills, and requests for tasks estimated over 8 hours for an experienced human increased nearly tenfold. Practical action: convert repeated prompts into small reusable procedures with inputs, steps, and review checks. STRICT TEXT RULE: Render ONLY the exact text blocks below. Do not add any other letters, numbers, words, UI text, captions, labels, punctuation, dates, watermark, or logo anywhere in the image. Icons and diagram shapes must contain no internal text. Exact text to render: 1. AI作業はスキル化へ 2. Codex利用研究 3. 26.6% 4. 8時間級 5. 手順を資産化 6. 毎回頼むより、型にする Layout: Wide 1536x1024 horizontal card with generous margins. Top: large strong headline "AI作業はスキル化へ". Top-right small pill: "Codex利用研究". Middle: three clean columns, each with one concise label: "26.6%", "8時間級", "手順を資産化". Use simple abstract icons only: reusable instruction card/library, long task timer, checklist template. Bottom footer action strip: "毎回頼むより、型にする". Style: modern Japanese SaaS/productivity information card, warm off-white background, deep charcoal/navy text, restrained accents in teal, muted amber, and small green reliability marks, crisp flat vector-like illustration, high contrast, readable on mobile, professional spacing. Avoid: generic AI atmosphere, glowing brain, robot, humanoid face, random laptop, code rain, fake UI screenshots, stock-photo scene, decorative-only scene, extra text, tiny paragraphs, misspelled Japanese, distorted letters, distorted English, wrong or extra numbers, purple/blue gradient, square crop.
- 画像ファイル: storage/images/2026-06-29-701.png
- 文面:

6月25日のCodex利用研究で、気になった数字がもう1つあります。

利用者の26.6%が「skills」を使っているそうです。skillsは、複雑な作業手順をAIに共有できる指示セットのこと。

私も毎回プロンプトを書く作業ほど、手順を短い型にしています。これは楽になります。

- ステータス: pending

---