# やりくりXへの切り替え結果

2026-11-19完了。ユーザーの依頼により、既存アカウントをやりくり版へ変更。ユーザー名変更と旧公開投稿の全削除も実施した。

## 現在の運用先

- X: [@yarikuri_app](https://x.com/yarikuri_app)
- 表示名: たまるんとのこらん｜やりくり公式
- アカウントID: `1736331586814271488`（既存アカウントを引き継ぎ）
- ローカル正本: `/Users/hirotomo.ishii/atlier-base-v1/projects/sns-auto-post/yarikuri/x/`
- GitHub: `atelierbase/x-workflow-atelier`（同じ配信repoを引き継ぎ）

## 完了したこと

- 表示名・自己紹介・製品サイト・note共通アイコン・X用の新ヘッダーを反映。
- ユーザーがIDを `AtelierBase_own` から `yarikuri_app` へ変更。画面とAPIで確認。
- フォロワー27人・フォロー12人は引き継いだ。
- 通常一覧の115件に加え、数値ユーザーIDによる全期間検索で古い投稿6件を発見。合計121件（リポスト1件を含む）を削除。
- 削除後、投稿数0件・通常タイムライン0件・全期間検索の3ページすべて0件を確認してから新規投稿した。
- 削除対象の取得控え・詳細実行結果・検証JSONは `archive/2026-11-19-ai-account/` にローカルのみで保存。GitHubへ新たに公開しない。
- 旧AI用の指示・テンプレート・分析はarchiveへ保管し、現行の発信指示を家計管理と二人の会話へ切り替えた。
- 旧 `sns-auto-post/x/` のREADME・AGENTSを新しい運用先への移管案内に更新。

## 初回投稿

- 日時: **2026-11-19 22:00 JST**
- ID: `2026-11-19-703`
- URL: https://x.com/yarikuri_app/status/2123401016527749283
- 内容: リニューアルの挨拶と、公開済みnote第1記事への案内。
- 画像: 採用済みnote表紙を再利用し、`storage/images/2026-11-19-703.png` に保存。
- 配信: GitHub Actionsの手動dispatch。実行44529147479成功、posted.mdへの記録とpending消化を確認。
- [Actionsの実行結果](https://github.com/atelierbase/x-workflow-atelier/actions/runs/44529147479)

## 配信と検証

生成側はPNGと原稿をcommit & pushし、GitHub Actionsで配信する。手動実行専用ワークフローを有効化した。
定期スケジュールは停止状態を引き継ぎ、新たな定期実行は設定していない。
配信時には数値アカウントIDを照合してから画像をアップロードし、実際のユーザー名で投稿URLを記録する。
日本語・URLを含む文字数の検査、認証不要のdry-run、誤ったアカウントで画像アップロード・投稿が行われないことを確認した。

新ヘッダーは組み込みimage_genで制作。画像は `brand/profile-header-x-v1.png`、生成プロンプトは `brand/header-prompt.txt`、制作情報は `brand/assets.json`。
