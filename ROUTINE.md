# ROUTINE.md - legacy notice

このrepoの生成担当は旧Routineではなく **Codex Automation**。

正本:

- `AGENTS.md`
- 親ディレクトリの `CODEX-AUTOMATION-SETUP.md`

現行フロー:

```text
Codex Automation
  research -> write -> image2 PNG -> scripts/queue_image2_post.py -> commit & push

GitHub Actions
  scheduled-post.yml -> scripts/scheduled_poster.py -> X投稿
```

Codex AutomationはXへ直接投稿しない。`scripts/scheduled_poster.py` はGitHub Actionsだけが実行する。
