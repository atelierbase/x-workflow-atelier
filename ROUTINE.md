# 配信の起動

定期実行は停止中。明示された投稿依頼ごとに原稿と画像をcommit & pushし、GitHub Actionsの `scheduled-post.yml` を枠指定でdispatchする。
旧RoutineのAIニュース生成プロンプトは使用しない。手順はAGENTS.md。

2026-11-20のユーザー指定で、11/21〜11/23の朝8:10・昼12:15・夜20:30（日本時間）にX本体から9件を予約登録する。原稿と登録結果は `storage/scheduled/2026-11-21-to-23.json`。GitHub Actionsの定期実行は停止を維持し、同じ9件をAPIキューへ入れない。
