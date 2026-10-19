# A25 Ground Zero — Archive Timestamp Observation and Terminal Viewing

**Date:** October 19, 2026
**Owner:** Zed
**Lead:** A25-TW-GPT01
**Location:** Workshop shutdown/startup notes
**Status:** OBSERVATION; timestamp cause not independently verified

## Archives file manager observation
After owner-authorized move and unzip of `A25-Training-Workspace-8f2e67ea53462616f13469cd434de53e370d1966.zip` from Downloads to `Documents/AI_Workshop`, Zed's Android file manager displayed **“10 hours ago”** on extracted directories, despite extraction just occurring. The ZIP in `AI_Workshop` displayed **“23 minutes ago”** in the owner's screenshot.

Previous live terminal output confirmed `ARCHIVE_MOVE_OK`, `ARCHIVE_UNZIP_OK`, `README_PRESENT`, and 428 extracted regular files. ZIP listing had 508 entries (including directories). Archive size was 958,956 bytes.

**Likely explanation (INFERENCE):** unzip preserves archive-stored file/directory modification timestamps, so the file manager's age labels need not equal extraction time. This has not been tested by comparing archive metadata to filesystem stat output. Do not treat display age alone as evidence of a failed extraction or stale destination.

## Terminal visibility request
Zed requested visibility into three running tmux sessions:
- `a25-gpt`: Workshop Lead's active shell commands and results.
- `a25-bridge`: running Python GPT MCP bridge logs and tool calls.
- `a25-tunnel`: running cloudflared tunnel logs.

These are separate tmux sessions, not separate servers. Viewing should use `tmux attach-session -t SESSION` from an ordinary Termux shell, and detach with Ctrl+B then D; **do not type shell commands into the bridge or tunnel panes**. Switching with `tmux switch-client -t SESSION` while attached is an alternative. This is a proposed user viewing workflow, not proof of simultaneous side-by-side phone display.

## Evidence / boundaries
VERIFIED: previous move and unzip command outputs; successful separate GPT shell test; three tmux sessions observed at Ground Zero.
REFERENCE: owner-provided Android screenshots showing age labels and older terminal captures.
UNKNOWN: exact Android timestamp rendering mechanism and whether file manager refresh affects label.
No deletions or edits of extracted files authorized.
