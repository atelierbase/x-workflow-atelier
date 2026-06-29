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
## 2026-06-30-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-30（火）
- 軸: 主軸 / 海外翻訳
- ソース: https://arxiv.org/abs/2606.24429
- 画像プロンプト: Create a landscape PNG social media summary card, 1536x1024, clean modern Japanese business infographic style for X. This is NOT a research paper card and NOT an atmosphere image. It must be a practical one-second summary card for developers/business builders using Claude Code and Codex. Core message: AI coding agent changes are becoming invisible if you only check pull requests; teams should make AI-written changes traceable. Use short Japanese text only. Main headline large and strong: 「PRだけでは追えない」 Subtitle smaller: 「AI変更は“入口”で見える化」 Visual structure: left-to-right flow with a bottleneck and checklist, not a fixed 3-column layout. 1) Left: incoming AI work streams labeled 「PR」, 「commit」, 「設定ファイル」 flowing into repo. 2) Center: warning bottleneck labeled 「見落とし」 with small note 「単一シグナルは弱い」. 3) Right: practical action checklist with three short labels: 「署名を残す」 「設定を管理」 「レビュー線引き」 Small footer only, not prominent: 「参考: arXiv 2606.24429」. Design: high contrast, professional, calm. White/off-white background with deep navy text, teal accent, amber warning accent, subtle grid lines. Use simple icons: pull request branch icon, commit dot, file icon, checklist icon. Maximum 5 text blocks total. Japanese text must be clean and legible; avoid long sentences. Avoid generic AI atmosphere, random laptop, decorative-only scene, robot faces, code rain, sci-fi glow, research-label-first layout, and three equal columns.
- 画像ファイル: storage/images/2026-06-30-701.png
- 文面:

AIに書かせるほど、変更の追跡が詰まりやすくなります。

最近の海外調査では、Claude Code由来の変更でもPRだけでは拾い切れない例が出ています。PRは変更提案の入口ですが、AI経由のcommitや設定変更は別の道から入ることがあります。私の実務判断は、使う前に“署名”を決めること。今日、AI生成のcommit/PRに残す一文を1つ決めておくと安心です。

- ステータス: pending

---
