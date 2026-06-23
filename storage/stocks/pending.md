# 受け渡しキュー（image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで X へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-23-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-23（火）
- 軸: 主軸 / AI自動化の監視・復旧設計
- ソース: Claude Status: Elevated errors for Claude Opus 4.8 (Jun 23, 2026) https://status.claude.com/
- 画像プロンプト: Create a polished social media summary card for X, landscape 1536x1024. This must summarize the post, not be an atmospheric image. Topic: Claude Opus 4.8 elevated errors on 6/23 and the practical lesson for AI operations. Main Japanese headline, exact and large: AI運用は止まる前提で作る. Use three large blocks connected by arrows: 1) 障害検知 2) 代替経路 3) 復旧確認. Include short supporting labels only. Small top label: Claude Opus 4.8 / elevated errors. Small badge: 6/23. Visuals: status monitor, alert line, fallback route, green recovery check. Palette: white, deep charcoal, teal, amber accents. Avoid generic AI atmosphere, random laptop, tiny text, long sentences, decorative-only scene. Reject if date, product name, headline, or major labels are wrong or garbled.
- 画像ファイル: storage/images/2026-06-23-703.png
- 文面:

Claudeのステータスで、6/23に Opus 4.8 の elevated errors が出ていました。

AI運用で怖いのは、賢さ不足より「止まった時に気づけない」ことです。

私なら、障害検知・代替モデル・復旧確認を最初からセットで設計します。

- ステータス: pending

---
