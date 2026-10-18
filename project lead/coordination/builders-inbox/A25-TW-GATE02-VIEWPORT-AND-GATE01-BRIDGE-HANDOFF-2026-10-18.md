# A25-TW Gate-02 Viewport and Gate-01 Bridge Handoff
Date: 2026-10-18
Author seat: A25-TW-GPT01
Status: evidence handoff, not a Gate-01 implementation approval.

## Owner direction (ADOPTED)
Preserve the four-terminal viewport as a Gate-02 reference/backup and make the capability visible to workshop builders. Gate-01 may follow the view/control bridge architecture with specific view limitations. Do not infer that control permissions are already implemented.

## What was independently VERIFIED
- Existing GPT read-only MCP bridge served at local 127.0.0.1:8770 behind a Cloudflare tunnel. Tool terminal_view(session) captured a named tmux pane.
- Four allowlisted tmux sessions were individually queried successfully in the prior live verification: a25-gpt (Zone 1), a25-test (local testing), a25-bridge (GPT MCP bridge), a25-tunnel (Cloudflare). Unauthorized 'not-allowed' returned read_only=true, returncode=1, empty screen, 'Session not permitted'.
- Four-view candidate import under the Pocket Server virtualenv returned PASS for all four sessions and unauthorized rejection; first attempt using system Python failed because mcp was not installed in that interpreter.
- Backup of two-view source: ~/a25-workshop/gpt/backups/chatgpt_readonly-pre-fourview.py SHA256 a18a834c649aa8777a67794ba3dece222beb6f7d90962362485786d64075b359.
- Installed four-view source: ~/a25-workshop/gpt/src/chatgpt_readonly.py SHA256 e85f2e4065c1d0ba6827f0d10f3429f89041069f9820fede4590422f26876519; compiled successfully.
- Bridge restarted in tmux a25-bridge with PID 32091 and Uvicorn startup on port 8770. Tunnel restarted in tmux a25-tunnel with PID 30319 and registered Cloudflare QUIC connections.
- Zone 1 server startup observed on 127.0.0.1:8766, PID 21440 during capture. A prior raw GET produced 406 Not Acceptable; not a valid end-to-end MCP execution test.
- At this latest check, a25-bridge logs were returned and a25-test screen was returned; some subsequent terminal_view calls for a25-tunnel and a25-gpt failed internally. Thus reliability is not yet established.

## Architecture to preserve
ChatGPT MCP client -> Cloudflare ingress -> local read-only FastMCP bridge -> exact allowlist -> tmux capture-pane -p. No arbitrary tmux session input, no shell execution via this tool. Tool responses include session, read_only, returncode, screen, error.

## Gate-01 design recommendations (PROPOSED, NOT IMPLEMENTED)
1. Maintain distinct VIEW and CONTROL bridges/capabilities. Never treat access to a viewport as authorization to send keys or execute commands.
2. Use server-side principal-to-session allowlists, not merely a caller-supplied session string. Current four-name global allowlist is not per-builder authorization.
3. For CONTROL, require separate authenticated principals, explicit owner authorization, bounded command/action contracts, an append-only audit trail, and fail-closed handling. Do not expose arbitrary shell execution by default.
4. Give each builder only the sessions necessary for its assigned work; e.g. an assigned testing seat could see a25-test but not tunnel secrets/logs. These examples are policy proposals, not deployed permissions.
5. Keep Gate-01 and Gate-02 identities, data, and services distinct until separately tested. Current test-only Zone 1 path names must not be used as production credentials.
6. Treat tmux pane capture as visible text only, not complete device telemetry or retained evidence; redact sensitive output before sharing.

## Backup state and recovery
- VERIFIED on-device: source backup and installed source exist with hashes above; earlier original Gate-01 and pockettest tar backups were reported and hashed in prior checkpoints, but restore was not tested.
- THIS HANDOFF IS A DOCUMENTATION BACKUP ONLY. It does not contain an independently retrieved copy of the current on-phone source, cloudflared config, or runtime data. Do not label Gate-02 fully backed up until the owner creates and verifies a separate archive.
- Recommended owner-side backup: archive ~/a25-workshop/gpt/src/chatgpt_readonly.py, tests/chatgpt_fourview_candidate.py, backups/chatgpt_readonly-pre-fourview.py, and sanitized startup/recovery instructions; keep tunnel credentials/config and ledgers in a separate private encrypted backup, never a public repo.
- Recovery verification must include SHA checks, import/syntax, all four captures, denied session, service restarts, and optional reboot persistence test.

## Outstanding
UNKNOWN: cause of intermittent internal remote tool failures; continuity across network changes/reboot; Gate-01 control bridge; per-builder authorization; end-to-end Zone 1 MCP tool calls; backup restore success.
Existing Pydantic IncompleteFieldDefinitionWarning and Cloudflare stream-cancellation logs observed; no causal attribution established.

## Builder handoff
G1/G2 and Gate-01 builders may use the architecture and tests as REFERENCE. They must not assert Gate-01 control bridge exists or grant new permissions without a separate owner-approved order. Report any drift or conflicting evidence to the Project Lead. Preserve original evidence, record verification separately, and keep implementation claims distinct from adoption.

## Prior report
project lead/coordination/builders-inbox/A25-TW-FOUR-VIEWPORT-LIVE-VERIFICATION-2026-10-18.md (commit 091fbfd97bb550036460af1a9bb11e72144c0367).
