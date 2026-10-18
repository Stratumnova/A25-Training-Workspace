# A25 TW live Termux baseline and backup receipt
Date 2026-10-18, owner local time MDT. Recorded from actual A25 GPT Terminal terminal_view output; read-only observation.

VERIFIED observed:
- Termux pockettest checkout: /data/data/com.termux/files/home/pockettest
- git branch main; HEAD f0a11d51968ad598691333d32971dfb483489073; git status --short empty.
- PID 25557 Python process from pockettest/gate02/.venv; PID 26121 cloudflared a25-gpt-bridge; ps command line truncated, full service status unknown.
- Owner ran tar -czf ~/a25-workshop/gpt/backups/pockettest-pre-zone1-20261018.tar.gz -C ~ pockettest
- sha256sum output: b6cebc1f6473a80c6a239eda4b56f34f39d78aa618d24ca5cc76a4a42a99814c
- ls -lh: -rw-------, 37M, Oct 18 16:28, under ~/a25-workshop/gpt/backups/.
UNKNOWN: archive integrity via tar -tzf, independent restore, backup contents, live Zone 1 deployment. Preserve the existing main checkout and bridge until tests and staged plan.
NEXT: verify archive integrity, fetch new source branch without switching main or restarting service, inspect tests and execute in isolated checkout if possible.
Owner requires backups/logs and shutdown around 22:00 MDT Oct 18.
