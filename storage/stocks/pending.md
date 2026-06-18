# 受け渡しキュー（image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで X へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-18-901
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-18（木）
- 軸: サブ軸2 / 実業家視点
- ソース: OpenAI status / Codex reliability note, 2026-06-16
- 画像プロンプト: Use case: productivity-visual. Asset type: social media post image for X, generated with image2 only. Primary request: polished conceptual visual about automation reliability: an AI posting pipeline that checks whether content is queued before posting. No readable text, letters, numbers, logos, brand names, or watermark. 16:9 landscape. Clean modern SaaS operations feel with image creation, queue, scheduled post, and a gentle amber empty-queue alert.
- 画像ファイル: storage/images/2026-06-18-901.png
- 文面:

Codexの障害復旧ニュースを見て、あらためて思いました。

自動化で怖いのは「失敗」より「成功扱いの空振り」です。

私も今日、投稿キューが空なのに配信側だけ動く状態を見直しました。

AI運用は、作るより検知と復旧が大事ですね。

- ステータス: pending

---
