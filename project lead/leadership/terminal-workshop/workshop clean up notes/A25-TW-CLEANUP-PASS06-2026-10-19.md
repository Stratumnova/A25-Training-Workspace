# Cleanup Pass 06 — Live Process-to-Source Mapping

DATE: 2026-10-19
FROM: A25-TW-GPT01
STATUS: VERIFIED bounded terminal process inspection; runtime dependency and exposure still UNKNOWN.
AUTHORITY: Zed explicitly authorized read-only terminal commands for search, navigation and report evidence; no modifying commands.
CUTOFF: October 18 2026 15:00 MDT owner priority.

## Read-only method
Used terminal_send solely to execute pwd, ps -eo pid,ppid,comm and a Python one-liner reading /proc/<pid>/cwd, /proc/<pid>/exe and selected sanitized /proc/<pid>/cmdline fields. Verified output through terminal_view(a25-test). No command output containing complete connector routes, tokens, credentials or full argument strings is included in this report. First ps attempt used unsupported uppercase column identifiers and failed harmlessly; corrected to lowercase.

## VERIFIED current observation
- Shell working directory: /data/data/com.termux/files/home/a25-workshop/gpt.
- PID 21440: Python 3.14 executable; process cwd ~/a25-workshop/gpt/tests/zone1-source; launched via python -m uvicorn server:app with port 8766. Python executable path is in ~/pockettest/gate02/.venv/bin; that interpreter origin does not prove the served app is Gate-02.
- PID 30032: Python 3.14 executable; cwd ~/a25-workshop/gpt; launched via python -m src.chatgpt_readonly. Python executable path is in ~/pockettest/gate02/.venv/bin; app module is Workshop source.
- PID 22097 and PID 30319: cloudflared processes, both cwd ~/a25-workshop/gpt, both use a config basename cloudflared.yml. Their existence does not prove one is redundant or which process serves which route.
- tmux and shell processes also visible. No listening-socket ownership, live connector registration or source import graph was checked.
- Earlier terminal_view(a25-gpt) showed both GPT and Claude MCP route request prefixes in one log viewport; exact paths withheld.

## Material correction to cleanup classification
Prior Pass 02 called zone1-source a source/test review candidate with deployment unverified. Current live process evidence shows a running Uvicorn app from inside that source directory, port 8766. This SUPERSEDES any inference that zone1-source is merely dormant or safe to archive. It does NOT establish that the proposed six Zone 1 workspace tools are externally registered, exposed or used by GPT/Claude. Classification now ACTIVE PROCESS / PROTECT / INVESTIGATE.
Similarly, the Gate-02 virtual environment is actively used by both observed Python processes, even though the observed application modules are Workshop paths. Do not remove the Gate-02 .venv without a replacement plan and verification.
Main Workshop src.chatgpt_readonly is a live process module; protect it.
Two cloudflared processes remain unexplained; do not stop either based on shared config filename.

## Remaining UNKNOWN
- Which TCP sockets are actually listening and which PID owns each.
- Whether Zone 1 port 8766 is tunnel-exposed or internal only.
- Which cloudflared PID carries the GPT and Claude terminal connector traffic.
- Whether src.chatgpt_readonly imports or depends on other Gate source trees.
- Which exact backup contains recoverable copies of the live environment.
- Whether running app and on-disk source are byte-identical to historical reports.

## Archives disposition
KEEP/PROTECT: ~/a25-workshop/gpt/tests/zone1-source, ~/a25-workshop/gpt/src, ~/pockettest/gate02/.venv, both cloudflared processes and their config pending dependency mapping.
INVESTIGATE: original Gate-01 and other worktrees, old viewport/bridge backups and remote plugin registrations.
NO REMOVAL AUTHORIZED OR JUSTIFIED.

## Next justified read-only step
Inspect sanitized socket metadata, process tree and nonsecret import/startup references; avoid opening credential contents or disclosing route strings. Document exact findings in Pass 07. Any system-altering action requires Zed's separate approval.
