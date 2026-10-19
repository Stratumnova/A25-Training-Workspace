# A25 Ground Zero — Startup 01 Observation — 2026-10-19

**Owner:** Zed
**Workshop Lead:** A25-TW-GPT01
**Source:** Owner-provided Termux screenshot at approximately 12:17 PM local time, plus live GPT connector observations.
**Status:** PARTIALLY VERIFIED — no full command-shell verification

## Owner actions visible in screenshot (VERIFIED as displayed)
- Fresh Termux welcome prompt and working directory `~/a25-workshop/gpt`.
- Started tmux `a25-bridge` with `~/pockettest/gate02/.venv/bin/python -m src.chatgpt_readonly`.
- Started tmux `a25-tunnel` with `cloudflared tunnel --config ~/a25-workshop/gpt/config/cloudflared.yml run`.
- `tmux list-sessions` showed `a25-bridge` created 12:17:20 and `a25-tunnel` created 12:17:28 on October 19, 2026.
- Session existence alone does not prove service health.

## Independent live checks (VERIFIED)
- GPT terminal_status responded with `identity: gpt-workshop`, all expected workshop directory flags true, and `mode: read-only`.
- terminal_view on `a25-bridge` showed `Application startup complete`, Uvicorn listening on `127.0.0.1:8770`, and live MCP HTTP requests with successful responses.
- The GPT connector is reachable through the startup bridge and tunnel at the time of inspection.

## Important limitation and incident
- An attempted `terminal_send` to `a25-bridge` returned `ok: true`, but the `terminal_view` output shows the text was sent into the **running Python bridge pane**, not executed by a shell. **No shell command execution has been demonstrated by that attempt.** Do not label terminal_send success as verified command control.
- This was a non-destructive read-only inspection command string; no evidence that it executed. Avoid further sending commands into the live bridge pane.
- Command-capable terminal session must be established or identified separately before Workshop Lead can perform shell-based audit.

## Component disposition
- `a25-bridge`: USED, verified reachable and serving MCP.
- `a25-tunnel`: USED in observed bootstrap, remote path reachable; detailed process verification pending.
- Other Gate-01/Gate-02/Claude/roundtable services: NOT STARTED by the owner in screenshot, dependencies and archive disposition UNKNOWN.
- No archival or deletion authorized or performed.

## Next justified step
Establish a **separate tmux shell session** (not the running bridge or tunnel), then independently verify command execution and inventory processes without disturbing the two live services. Record every actual result in a new append-only note. Do not assume the historical old build is the current operative plan.
