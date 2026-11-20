# やりくり公式 X 運用

更新: 2026-11-19。既存Xアカウント（user ID 1736331586814271488）を、たまるんとのこらんによる家計管理の発信へ切り替える。
同じGitHub repo `atelierbase/x-workflow-atelier` を引き継ぐ。正本の作業場所はこの `yarikuri/x/`。
旧 `sns-auto-post/x/` と `hiro-inaka-ai/x/` は今後の投稿準備に使わない。

## 必ず読む

- `skill/references/00-context.md`
- `skill/references/characters.md`
- `skill/references/product.md`
- `skill/templates/voice-guide.md`
- `skill/templates/single-post-templates.md`
- `skill/agents/writer.md`
- `storage/analytics/learnings.md`
- `CONTENT-PLAYBOOK.md`（参考投稿の選び方と今回の検証方針）

## 内容

給料日前の金欠、カード代、年払い、予算と残高の違いを、短い会話と図解で伝える。
アプリがなくても試せる確認方法を先に示し、製品紹介は短く添える。
たまるんは「ぼく」、のこらんは「私」。優しく明るい会話。困っている読者を笑わない。
旧AIニュース・実業家の一人称・売上実績は新投稿へ持ち込まない。
全機能無料。「広告なし」は訴求しない。未公開機能・架空の体験談・金融機関連携・自動通知を案内しない。

## 画像と投稿

- 毎回 `種類: 画像付き`。組み込みimage_gen/image2のみで制作する。
- 採用済みnote画像の再利用可。加工が必要ならimage_genを使う。
- 新規画像は `brand/character-reference.png` を参照。クリーム・茶・ミルクグレー基調。
- 挨拶・自己紹介では、名前と性格・二人の関係が伝わる短い場面を主役にしてよい。
- 投稿の結論と具体的な確認方法を図解。日付・数字・日本語を目視検査する。
- PNG、5MB以下。`storage/images/<ID>.png` に保存。
- X加重文字数280以内。日本語は多くが2、URLは23。絵文字連結は検査が保守的に数えるため短くする。
- IDは `YYYY-MM-DD-NNN`。朝701、昼702、夜703。既存IDは再利用しない。
- `scripts/queue_image2_post.py` で検査。同じ枠の積み増しは禁止。

## 配信

生成側はXへ直接投稿しない。画像と原稿をcommit & pushし、GitHub Actionsで配信する。
現在は定期実行停止を引き継ぐ。明示された投稿依頼ごとに手動dispatchで1本を送る。
pushだけでは送信されない。自動投稿スケジュールは別途設定するまで追加しない。
同日に同じ枠へ追加投稿する依頼では、新しいIDを付けて `post_id` 入力でその1本を明示する。
投稿状態ファイルや過去の投稿履歴を消して枠ガードを回避しない。同じIDは再配信されない。

```bash
python3 scripts/scheduled_poster.py --dry-run
git add <今回変更したファイル>
git commit -m "queue: yarikuri X image post"
git push origin main
gh workflow run scheduled-post.yml -R atelierbase/x-workflow-atelier -f slot=夜
# 明示された同枠の追加投稿の場合
gh workflow run scheduled-post.yml -R atelierbase/x-workflow-atelier -f slot=夜 -f post_id=<新しいID>
```

dry-runは認証・ネットワーク不要。実配信はアカウントIDを照合してから画像をアップロードする。
Actionsの完了と `posted.md` の実際の投稿URLを確認する。キュー投入を投稿完了と扱わない。
旧原稿・運用指示は `archive/2026-11-19-ai-account/` に保管。現在のプロフィールは `profile.md`、移行結果は `MIGRATION.md`。

## 2026-11-20 キャラクター刷新

食べ物は縦じまの細長いひまわりの種。たまるんは片方に残した大きな頬、のこらんは空の頬と口で顔幅を小さめにする。空袋や食べ終わった殻を使う。旧どんぐり・膨らんだのこらんは新規生成に使わない。詳細は `skill/references/characters.md`、正本は `brand/character-reference.png`。

## X本体の予約投稿（2026-11-20 ユーザー指定）

今回の11/21〜11/23の9件は、ユーザーがX標準の予約投稿・朝昼夜各1本を指定したため、ブラウザのX予約機能で登録する。GitHub Actionsのpendingには重複投入しない。原稿・PNG・予約日時・確認状態の正本は `storage/scheduled/2026-11-21-to-23.json`。将来の予約済みを投稿済みと扱わず、実際の公開後にURL・反応を確認する。一般の即時投稿は従来の配信経路を使い、送信前にこの予約台帳との重複を確認する。


## 予約時刻の選び方（2026-11-20 最新指定）

ユーザー指定は固定時刻ではなく、朝・昼・夜の枠内で毎日違う時刻をランダムに選ぶ運用。目安は朝7:15〜9:35、昼11:40〜13:35、夜19:10〜22:10 JST。1日3本を維持し、極端に近い時刻を避ける。既存予約を調整するときは日時だけを編集し、X上の保存完了を待ってから一覧の本文・日時・画像添付・件数を照合する。今回の変更履歴は `storage/scheduled/2026-11-21-to-23-time-randomization.json`。
