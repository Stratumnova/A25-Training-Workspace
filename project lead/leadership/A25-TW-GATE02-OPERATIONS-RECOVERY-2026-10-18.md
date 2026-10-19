# A25 Gate-02 — Operations and Recovery Checkpoint
Date: 2026-10-18
Prepared by: A25-TW-GPT01
Evidence class: VERIFIED terminal viewport unless explicitly marked otherwise.

## Architecture and scope
Gate-02 is the existing GPT terminal view/write bridge on Android Termux. Gate-01 (Pocket Server / Zone 1 shared workspace) is separate and must not be restarted during Gate-02 recovery. Owner ADOPTED priority: continue Workshop build, refer security work to leadership pool.

## Verified backup
Archive: `~/a25-workshop/gpt/backups/20261018-gate02-write-pass.tar.gz`
SHA256 as printed in remotely observed Termux: `1dc800484db8afe8daba2e6583b28747dd63932cdc80ddc956c68ee9f9f5aa38`
Size: 1.7K (ls -lh).
Archive listing:
- `20261018-gate02-write-pass/chatgpt_readonly.py`
- `20261018-gate02-write-pass/chatgpt_readonly-pre-write-20261018.py`
- `20261018-gate02-write-pass/STARTUP.txt`
The archive's listing and sha256sum command completed in the terminal; a full extract-and-restart restore test was NOT performed. Archive does not contain the Python environment, tunnel config/credentials, or Gate-01 data. Original source backup equality was independently observed before changes: `e85f2e4065c1d0ba6827f0d10f3429f89041069f9820fede4590422f26876519` for source and pre-write backup.

## Working paths and components
Workspace: `~/a25-workshop/gpt`
Bridge module: `src/chatgpt_readonly.py` (historical filename retained despite new write tool).
Interpreter: `~/pockettest/gate02/.venv/bin/python`
Bridge bind: `127.0.0.1:8770`
Public MCP endpoint: `https://gpt-bridge.rodsrcpark.com/mcp`
Tunnel config path (NOT included in backup): `~/a25-workshop/gpt/config/cloudflared.yml`
tmux sessions: `a25-bridge` server, `a25-tunnel` tunnel, `a25-test` command tests, `a25-gpt` GPT workspace.
Gate-01 observed separately at `127.0.0.1:8766`; do not change for this procedure.

## Start / recover after phone reboot
1. Start Termux; verify existing tmux sessions: `tmux list-sessions`. If a session already exists, use it; do not create duplicates.
2. If missing, create server and tunnel sessions: `tmux new-session -d -s a25-bridge` and `tmux new-session -d -s a25-tunnel`; create `a25-test` separately for tests.
3. Check running bridge first: `ps -ef | grep '[c]hatgpt_readonly'`. Do NOT launch a second instance on 8770.
4. If no bridge is running, in `a25-bridge` run:
```bash
cd ~/a25-workshop/gpt
~/pockettest/gate02/.venv/bin/python -m src.chatgpt_readonly
```
To start detached from another Termux pane: `tmux send-keys -t a25-bridge 'cd ~/a25-workshop/gpt && ~/pockettest/gate02/.venv/bin/python -m src.chatgpt_readonly' Enter`. Check pane logs `tmux capture-pane -t a25-bridge -p | tail -n 25`.
5. Check tunnel process/pane before starting a second tunnel. If not running, in `a25-tunnel` run:
```bash
cloudflared tunnel --config ~/a25-workshop/gpt/config/cloudflared.yml run a25-gpt-bridge
```
6. Verify server startup lines `StreamableHTTP session manager started`, `Application startup complete`, and `Uvicorn running on http://127.0.0.1:8770`; verify connector terminal_status and terminal_view. In a fresh ChatGPT conversation, confirm `terminal_send` discovery; test only a harmless command in `a25-test` and read it back. Do not infer success solely from `terminal_send.ok`.
7. To make manual Termux commands visible through the connector, attach the physical Termux shell to `a25-test` with `tmux attach-session -t a25-test`. A plain Termux shell is NOT automatically the same tmux pane.

## Prior restart evidence
Old bridge PID 32091 was terminated and replaced by PID 30032, parent tmux pane PID 29675. Logs verified successful startup at 8770. These PIDs are historical and MUST NOT be reused after restart without checking.
A fresh ChatGPT session reportedly discovered `terminal_send` and returned `ok:true` for `echo A25_GATE02_WRITE_TEST_PASS` in `a25-test`. Workshop lead independently viewed the resulting command and exact marker output in the pane; cross-session command execution supported. The original lead conversation still exposed only the old two tools (stale tool discovery).
Warning about pydantic_settings forward reference appeared in logs but did not prevent server startup; cause/impact UNKNOWN.

## Restore notes
Verify archive SHA256 before use, inspect contents with `tar -tzf`, and extract to a temporary recovery directory before replacing live source. Do not overwrite a running server without explicit authorization. Full restore not tested.
