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
## 2026-07-01-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-01（水）
- 軸: サブ軸1 / 自分の実例
- ソース: https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness
- 画像プロンプト: Create a landscape PNG information card for a Japanese X post, 1536x1024. This is a post summary card, not an atmosphere image. Make it minimal with exactly 5 text blocks total. Text blocks, use only these exact Japanese/English labels and no other visible text: 1. Main headline, very large: 「外部repoは実行前に止める」 2. Small subtitle: 「AIに任せるほど、初回実行の許可が重要」 3. Left step label: 「cloneまでOK」 4. Center checkpoint label: 「install / run は確認」 5. Right action label: 「通信先と差分を見る」 Visual structure: left-to-right flow with a strong stop gate/checkpoint icon between step 3 and step 4. Use abstract repository/code folder shapes, a shield/check icon, and a network/diff icon. No extra captions, no footer slogan, no numbered badges with text, no small explanatory sentences, no source name, no date, no research label. Design: clean modern Japanese business infographic, white/off-white background, deep charcoal text, green for OK, amber for caution, red for stop, blue for review/action. High legibility, generous spacing, professional. Avoid 3-column research-card look; make it feel like a practical safety flow. No generic AI atmosphere, no random laptop, no decorative-only scene, no robot mascot. Ensure all text is correctly spelled, no garbled characters, and no additional visible words beyond the five specified text blocks.
- 画像ファイル: storage/images/2026-07-01-702.png
- 文面:

AIに外部repoを任せる時は、最初に「実行しない線」を決めた方がいいです。

Mozilla 0dinの検証では、きれいに見えるGitHub repo（コード置き場）でも、初期化手順から悪性コマンドへ誘導できました。便利ですが、ここは慎重でいいですね。

私の実務では、初回はcloneまで。install/runは差分と通信先を見てから許可します。今日、AI用の実行NGリストを1つ作ってください。

- ステータス: pending

---
