# A25 Archives — Four-Viewport Read-Only Retest
Date: 2026-10-18 (owner local)
Seat: A25-AG-GPT01
Status: VERIFIED for read-only viewport selection; root cause of earlier schema discrepancy UNKNOWN

## Authorization and scope
Owner expressly authorized Archives to test terminal access and view information for future reporting, but prohibited changing, moving, deleting, or altering anything. This retest used terminal_status and terminal_view only. No terminal_send commands, file edits, process controls, or configuration changes.

## Independently verified connector interface
Tool discovery in this Archives session exposed:
- terminal_status(args: object)
- terminal_view(args: {session?: string}), default a25-gpt
- terminal_send(args: {session: string, command: string}), **not invoked**

This differs from the earlier Archives observation of a generic terminal_view(args: object) with no documented named session field. The cause of that earlier discrepancy remains UNKNOWN.

## Live read-only calls and results
1. terminal_status({}): identity gpt-workshop; workspace_exists true; src, tests, logs, reports, backups, config present; mode read-only.
2. terminal_view({session:"a25-gpt"}): response session a25-gpt, read_only true, returncode 0; visible MCP HTTP 200/202 and CallToolRequest/ListToolsRequest activity. PASS.
3. terminal_view({session:"a25-test"}): response session a25-test, read_only true, returncode 0; visible Gate-01 server.py source inspection output from workshop test copy. PASS.
4. terminal_view({session:"a25-bridge"}): response session a25-bridge, read_only true, returncode 0; visible /mcp HTTP 200/202 and CallToolRequest log entries. PASS.
5. terminal_view({session:"a25-tunnel"}): response session a25-tunnel, read_only true, returncode 0; visible Cloudflare stream cancellation/error log lines and local origin 127.0.0.1:8770. PASS for viewport visibility, NOT a tunnel health PASS.

## Findings and evidence classification
- VERIFIED: Archives can directly select and read all four named tmux viewports through its currently advertised connector schema.
- VERIFIED: all four direct calls returned success and a matching session identifier.
- VERIFIED: terminal_send is advertised in this seat, but its behavior and safety controls were NOT tested.
- HISTORICAL CLAIM: Workshop earlier reported successful four-viewport selection; this retest independently corroborates the narrow access result.
- UNKNOWN: why the Archives tool schema changed; whether a connector registration refresh caused it; whether all access walls are enforced; whether Cloudflare stream cancellation lines indicate an active operational fault.
- SUPERSEDED for current access only: earlier Archives inability to select sessions 2–4. The original report remains preserved, not rewritten.

## Decision
PASS — read-only four-viewport access in Archives. No approval or evidence for write access, terminal_send execution, restarts, deployment, or any filesystem changes. No server changes performed.
