# A25 Workshop — Controlled Shutdown Log — 2026-10-19

Owner authorization: "You may begin shut down and logging it. Put your logs on GitHub since we are shutting down the system."

## Pre-shutdown verified checkpoint
- Private backup: ~/a25-recovery-20261019.tar.gz
- Documents backup: /storage/emulated/0/Documents/AI_Workshop/a25-recovery-20261019.tar.gz
- Both SHA-256: ca5710a0c428a63122b98d06f6cfc4f0e3cd476965288b5bfe8999c416d6fb4e
- Both archive listings: 8854 entries. No restoration test.
- Documents procedure: AI_Workshop/A25-COLD-START-SHUTDOWN-20261019.md
- WARNING: Documents backup contains potentially sensitive configuration and is unencrypted. Never publish backup.
- This GitHub log is independent of the phone.

## Live mapping before shutdown
tmux panes:
- a25-bridge pane shell PID 29675 -> Python PID 30032, GPT terminal bridge module src.chatgpt_readonly; KEEP UNTIL OWNER HANDOFF.
- a25-gpt pane shell PID 24733 -> Python PID 21440, uvicorn server:app (port argument 8766); SECONDARY.
- a25-test pane shell PID 23226; active terminal command surface; KEEP UNTIL HANDOFF.
- a25-tunnel pane shell PID 29677 -> cloudflared PID 30319; likely GPT bridge tunnel from parentage and config, KEEP UNTIL HANDOFF.
- separate cloudflared PID 22097, parent shell PID 25838; not in listed tmux pane; SECONDARY CANDIDATE, mapping of remote route not independently verified.

## Execution state
Log initialized BEFORE service shutdown. Subsequent events must be appended in a separate GitHub file or commit, verified against terminal observations. Do not confuse planned stops with completed stops.

## Planned controlled stop
1. Send TERM to secondary Uvicorn PID 21440. Verify disappearance and terminal bridge still responds.
2. Send TERM to secondary cloudflared PID 22097. Verify disappearance and terminal bridge still responds.
3. Preserve PID 30032 and 30319, a25-bridge and a25-tunnel until owner handoff.
4. Owner finishes stopping GPT bridge/tunnel and remaining tmux sessions using explicit final handoff instructions. Do not issue blanket killall.
5. Owner opens fresh Termux and starts bridge and tunnel per saved proposed bootstrap procedure. Cold start not yet verified.

## Evidence rule
VERIFIED: terminal process mapping, backup hashes and archive listings.
UNKNOWN: actual remote connection ownership for each tunnel; full cold-start success; all off-tmux services.
ADOPTED: owner-approved controlled shutdown and GitHub logging.
