# 受け渡しキュー（直投稿モード / 在庫は溜めない）

このファイルは **クラウドRoutine → GitHub Actions の受け渡し場所**。
Routine（x-post-now スキル）が発火時に**1本だけ**生成して追記し、push をトリガーに
GitHub Actions（送信専用）が X へ投稿して posted.md に移すと、ここは再び空になる。

- 在庫(ストック)は溜めない。ここに長く残る投稿があれば「送信ワークフローが動いていない」サイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `.claude/skills/x-post-now/SKILL.md` / `skill/agents/writer.md` 準拠。

---
