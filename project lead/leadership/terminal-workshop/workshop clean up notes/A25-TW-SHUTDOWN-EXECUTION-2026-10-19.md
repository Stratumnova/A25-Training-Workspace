# A25 Workshop — Shutdown Execution Result — 2026-10-19

Owner authorized shutdown and GitHub logging. This report is written after observed actions, independently of the phone.

## Backup prerequisite (VERIFIED)
Private and Documents archives both exist and SHA-256 match:
ca5710a0c428a63122b98d06f6cfc4f0e3cd476965288b5bfe8999c416d6fb4e
Archive listing: 8854 entries. Documents path: /storage/emulated/0/Documents/AI_Workshop/a25-recovery-20261019.tar.gz.
Documents recovery instructions: AI_Workshop/A25-COLD-START-SHUTDOWN-20261019.md.
Warning: Documents archive is unencrypted and may contain credentials. No restore test performed.

## Actions and direct observations (VERIFIED)
1. tmux process map observed:
   - a25-gpt shell PID 24733 -> secondary Uvicorn Python PID 21440.
   - a25-bridge shell PID 29675 -> GPT terminal Python PID 30032.
   - a25-tunnel shell PID 29677 -> cloudflared PID 30319.
   - a25-test shell PID 23226, current terminal control pane.
   - Separate cloudflared PID 22097, parent shell PID 25838, not in listed tmux pane.
2. Sent SIGTERM to PID 21440. After 2 seconds, ps -p 21440 returned no process. GPT terminal_status still responded with identity gpt-workshop.
3. Sent SIGTERM to PID 22097. After 2 seconds, ps -p 22097 returned no process. ps still showed PID 30032 and 30319, and GPT terminal_status still responded with identity gpt-workshop.
4. No backup, configuration, source files, or phone package changes made during shutdown actions.
5. GPT bridge and GPT tunnel intentionally LEFT RUNNING for owner handoff. Shutdown is NOT COMPLETE at this checkpoint.

## Final owner handoff — after reading this report
On phone in Termux, when ready to sever GPT's connection and stop the remaining tmux-managed processes, run:
    tmux kill-server
Then exit remaining ordinary Termux shells (use exit) and close Termux.
This stops the tmux server and its sessions, including a25-bridge, a25-tunnel, a25-gpt and a25-test. It will sever GPT control. Do not run it until ready.
NOTE: Other non-tmux Termux shell processes can remain until exited; do not equate tmux shutdown with full phone/app shutdown. Secondary server and separate cloudflared were already terminated and checked.
If tmux kill-server errors, do not assume success; inspect tmux list-sessions and ps.

## Cold start (PROPOSED, NOT TESTED)
Use the saved phone document to start terminal bridge module and Cloudflare tunnel. The user previously received the four-step owner workflow (open Termux, start bridge, start tunnel, ask GPT to check).
Do not start duplicate sessions if any remain.
No external reachability or cold-start success has been verified.

## Evidence labels
VERIFIED: commands executed and process checks, GPT terminal response, archive checksum/listing.
ADOPTED: owner-authorized shutdown, GitHub log and backup procedure.
UNKNOWN: whether other non-tmux services remain; remote reachability after final handoff; whether cold start succeeds; complete restore.
