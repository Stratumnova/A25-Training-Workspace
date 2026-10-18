# A25 TW Terminal Viewport — 2026-10-18

## Owner request and adoption
Owner requested this setup be preserved in project notes: Terminal 1 and Terminal 4, with read-only viewport capability. Owner explicitly approved a bridge extension to permit Terminal 4 viewing while retaining Terminal 1.

## VERIFIED observations
- Existing GPT viewport tool `terminal_view()` reads tmux session `a25-gpt` via `tmux capture-pane -t a25-gpt -p`; it is read-only and has no session parameter in the inspected source.
- Live bridge source: `~/a25-workshop/gpt/src/chatgpt_readonly.py`; companion `~/a25-workshop/gpt/src/bridge.py`.
- Existing tmux session `a25-gpt:0.0` (pane PID 24733) was reported by Termux. Existing read-only bridge process PID 25557 was reported running.
- Terminal 1 is running a localhost-only Zone 1 Uvicorn test server on 127.0.0.1:8766, process PID 21440, with both StreamableHTTP session managers started.
- Terminal 4 executed curl against GPT MCP test endpoint and received HTTP 406 with expected Accept text/event-stream requirement; confirms HTTP endpoint response, not MCP tool execution.
- Terminals 2 and 3 serve the preexisting bridge and Cloudflare tunnel; preserve them.

## ADOPTED next step, NOT YET VERIFIED completed
- Owner approved extending existing bridge to expose two read-only tmux views, retaining default `a25-gpt` and permitting `a25-test` for Terminal 4, with allowlist and no command execution.
- Last proposed Terminal 4 command: `tmux new-session -s a25-test`. User's latest message says 'We have terminal 4 and 1 and a viewport', but no tmux output confirming `a25-test` creation or new plugin deployment was provided. Treat Terminal 4 as an active shell; second tmux viewport remains UNKNOWN until checked.
- Do not claim bridge extension deployed. Inspect, test separately, preserve original, then controlled cutover only after verification.

## Evidence rule
Distinguish owner-adopted plans from verified running implementation. Preserve existing working bridge and original server.
