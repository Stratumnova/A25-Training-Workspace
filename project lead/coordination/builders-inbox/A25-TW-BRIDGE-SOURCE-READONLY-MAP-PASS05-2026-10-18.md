# A25 Workshop — Bridge Source Read-only Mapping Pass 05
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Archives, Claude, builders, security pool
STATUS: VERIFIED source inspection; no blockers
BASIS: Direct terminal_send of read-only inspection commands to a25-test followed by terminal_view showing output and prompt.

## Owner directive
Continue ordinary bounded read-only mapping without repeated approval requests. On a blocked step, stop and report exact blocked item(s) to Zed for review before retrying. No alternate-route bypass. Existing phone modification and active-testing prohibitions unchanged.
See: project lead/coordination/builders-inbox/A25-TW-MAPPING-BLOCKER-ESCALATION-RULE-2026-10-18.md

## Verified active source
File: ~/a25-workshop/gpt/src/chatgpt_readonly.py
File mode: -rw------- (600); 2663 bytes observed.
Definitions: terminal_status line 20, terminal_view line 34, terminal_send line 63.
- terminal_status returns literal identity 'gpt-workshop', mode 'read-only', and directory existence flags.
- terminal_view permits tmux sessions a25-gpt, a25-test, a25-bridge, a25-tunnel; runs tmux capture-pane -t session -p, returns last 12000 stdout characters and up to 2000 stderr characters.
- terminal_send permits same four sessions, runs tmux send-keys -t session -l command, then separate Enter key; the observed code checks subprocess delivery return codes, not the shell command exit status.
- Source has allowed_origins setting for https://gpt-bridge.rodsrcpark.com; this is not authentication evidence.
- No command read-only filter appears in the inspected terminal_send body. Thus status label is not an enforced prohibition on shell commands.

## Boundary classifications
a25-test: designated read-only inspection shell; permitted for bounded metadata/source reads.
a25-gpt: server-log viewport, not a routine interactive shell; avoid command sends.
a25-bridge and a25-tunnel: service sessions; DO NOT SEND COMMANDS during mapping because input could disrupt services.
Shared Termux UID: no proven caller-specific command isolation.
Session allowlist: tmux target limitation, not filesystem sandbox.

## Workspace directory metadata
Observed subdirectories: reports, backups, backups/20261018-gate02-write-pass, src, src/__pycache__, tests, tests/zone1-source, tests/zone1-data, tests/gate01-recovery, tests/__pycache__, logs, config.
Names alone do not prove active use or contents. Sensitive config and logs were not opened.

## Unknown / next
Authentication, provenance, exit-code capture, filesystem restrictions, identity binding, and live enforcement remain UNKNOWN. Continue read-only metadata mapping only. Do not test modifications or disrupt sessions.
