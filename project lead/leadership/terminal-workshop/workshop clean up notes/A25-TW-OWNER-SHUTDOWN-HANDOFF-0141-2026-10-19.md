# A25 Workshop — Owner Shutdown and Cold-Start Handoff Note

**Recorded owner time:** 2026-10-19, 1:41 AM (Zed-supplied; timezone not independently verified)
**Owner:** Zed
**Workshop Lead:** A25-TW-GPT01, GPT Terminal Workshop Lead
**Leadership reference:** project lead/leadership/terminal-workshop/README.md
**Classification:** ADOPTED owner plan; execution details below separately classified

## Owner's direction

At 1:41 AM on October 19, Zed and the Workshop Lead coordinated shutdown of the A25 phone server. Zed intends to leave the system down for a few hours and then return with a fresh terminal workspace. During the next startup, record the actual startup sequence and distinguish components **used** from components **not used**. The objective is an evidence-based clean startup, not automatic deletion of old files.

## Execution evidence before owner handoff (VERIFIED in live terminal)

- Secondary Uvicorn Python PID 21440 was sent SIGTERM; later `ps -p` showed it absent.
- Secondary cloudflared PID 22097 was sent SIGTERM; later `ps -p` showed it absent.
- GPT bridge Python PID 30032 and its cloudflared PID 30319 were deliberately left running so the owner could perform the final shutdown.
- GPT terminal_status continued responding after secondary stops.
- Owner was instructed to run `tmux kill-server`, exit Termux shells, and force-stop Termux via Android app settings.
- **UNKNOWN:** This session has not independently observed the owner's final tmux/Termux shutdown; do not label the entire phone server VERIFIED stopped until the owner confirms or cold-start evidence establishes it.

## Backup and handoff

- Private backup: `~/a25-recovery-20261019.tar.gz`.
- Phone Documents backup: `/storage/emulated/0/Documents/AI_Workshop/a25-recovery-20261019.tar.gz`.
- Both copies SHA-256: `ca5710a0c428a63122b98d06f6cfc4f0e3cd476965288b5bfe8999c416d6fb4e`.
- Archive listing: 8854 entries. Extraction/restore not tested.
- Phone instructions: `Documents/AI_Workshop/A25-COLD-START-SHUTDOWN-20261019.md`.
- Documents archive is unencrypted and may contain credentials. Do not publish it.

## Next-session cold-start evidence plan

1. Owner opens Termux fresh after the planned downtime; no assumption that app force-stop removed files or services.
2. Owner restores minimum GPT terminal bridge and Cloudflare tunnel using saved proposed commands.
3. Workshop Lead verifies `terminal_status`, live processes, tmux sessions, and tool command execution.
4. Start each additional service individually; record exact command, dependency, purpose, active connection, verification result and whether actually needed.
5. Mark historical components as review candidates if unused; never delete or archive solely because they did not start.
6. Publish a fresh GitHub startup ledger with VERIFIED, ADOPTED and UNKNOWN separated.

## Related GitHub reports

- `A25-TW-PRE-SHUTDOWN-RECOVERY-CHECKPOINT-2026-10-19.md`
- `A25-TW-SHUTDOWN-LOG-2026-10-19.md`
- `A25-TW-SHUTDOWN-EXECUTION-2026-10-19.md`

**Status at writing:** GPT phase verified completed; owner final shutdown and future restart not independently observed.
