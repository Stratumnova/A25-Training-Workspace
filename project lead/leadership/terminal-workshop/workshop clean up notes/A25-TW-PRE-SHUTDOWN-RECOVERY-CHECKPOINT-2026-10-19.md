# A25 Workshop — Pre-Shutdown Recovery Checkpoint (2026-10-19)

STATUS: BACKUP CREATED / SHUTDOWN NOT STARTED
OWNER: Zed
WORKSHOP LEAD: A25-TW-GPT01

## Current authority
Owner approved a controlled shutdown followed by a cold start, but required inspection and backup first. No shutdown actions have yet been executed. Owner finishes shutdown after GPT stops safe components. On cold start, owner restores minimum terminal access, GPT then resumes. System-altering operations outside this planned scope still require explicit approval.

## Verified Termux preflight
- Working project: ~/a25-workshop/gpt
- tmux sessions present: a25-bridge, a25-gpt, a25-test, a25-tunnel.
- PID 21440: Python interpreter from ~/pockettest/gate02/.venv, running uvicorn server:app with port argument 8766 and cwd ~/a25-workshop/gpt/tests/zone1-source. Resolved server module UNKNOWN.
- PID 30032: same Python environment running src.chatgpt_readonly from ~/a25-workshop/gpt; inspected module configures localhost port 8770 and implements terminal_status, terminal_view, terminal_send through tmux.
- PID 22097 and PID 30319: cloudflared using config basename cloudflared.yml. Tunnel-to-port association UNKNOWN.
- Android denies /proc/net/tcp and /proc/net/tcp6; netstat lacks AF INET TCP support. This does not establish no listeners.
- Approximate free storage at inspection: 23 GB.

## Backup
- Private path: ~/a25-recovery-20261019.tar.gz
- Size: 91 MB (ls -lh)
- Archive entries: 8854 (tar -tzf ... | wc -l)
- SHA-256: ca5710a0c428a63122b98d06f6cfc4f0e3cd476965288b5bfe8999c416d6fb4e
- Scope: a25-workshop, pockettest, pockettest-c1, pockettest-shared, .cloudflared.
- VERIFIED: archive creation command completed, SHA-256 calculated, tar listing read successfully.
- NOT VERIFIED: extraction/restore test, all service dependencies, all Termux packages/environment settings, completeness of ChatGPT chat history.
- SENSITIVE: archive includes private configuration and may contain credentials. Keep private; do not publish to GitHub or unencrypted shared phone storage.
- Single-device limitation: this backup is on the same phone, not an independent off-device copy.

## Startup/recovery strategy
1. Before shutdown, verify terminal bridge and tunnel startup command references; prepare manual minimum bootstrap procedure.
2. Arrange independent protected copy of private archive, ideally encrypted/off-device, before any shutdown. Do not expose secrets in public GitHub.
3. Preserve this GitHub checkpoint as independent documentation, not a full export of the chat transcript.
4. Only then stop secondary processes one by one, observing failures and preserving control bridge until final owner handoff.
5. Owner completes shutdown and opens fresh Termux. Reestablish bridge/tunnel using verified instructions; GPT checks terminal_status and resumes.
6. Do not delete old files or modify production configurations during the recovery exercise.

## Evidence classes
VERIFIED: specific terminal process observations and archive SHA/listing.
HISTORICAL CLAIM: previous working GPT/Claude bidirectional exchanges and recovery notes; current restoration not tested.
ADOPTED: owner-directed shutdown/restart test with backup prerequisite.
UNKNOWN: exact live tunnel-to-port dependency, independent off-device archive, complete restoration capability.

## STOP GATE
No shutdown until owner accepts backup storage location and minimum bootstrap procedure is checked. Do not claim GitHub documentation replaces full chat export or Termux backup.
