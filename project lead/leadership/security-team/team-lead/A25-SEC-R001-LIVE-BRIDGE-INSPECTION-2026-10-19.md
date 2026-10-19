# A25-SEC-R001 — Live Bridge Initial Inspection
DATE: 2026-10-19, owner order approximately 13:13 MDT
SEAT: A25-SEC-GPT01
OWNER: Zed
STATUS: OPEN / READ-ONLY LIVE INSPECTION
REPO: Stratumnova/A25-Training-Workspace
BRANCH: coord/a25-namespace-trial-001

## Authorization
Zed explicitly approved terminal use to investigate flagged A25-TW-SEC-O001. No deployment, shutdown, credentials change or live public probe was performed. Terminal command execution was limited to read-only inspection through session a25-gpt.

## Evidence and classification
VERIFIED IN THIS SESSION:
- A25 terminal_status returned identity gpt-workshop and mode read-only. This mode field is not a tool authorization control.
- terminal_view exposed earlier Claude report and Workshop history, but their conclusions remain HISTORICAL CLAIMS except where separately reproduced.
- terminal_send ran read-only ps, sed, grep and ls inspections in a25-gpt; terminal_view returned output.
- ps shows PID 6882 executing Python module src.chatgpt_readonly; PID 6965 cloudflared tunnel running with the workshop config. These are observations at inspection time, not long-term uptime guarantees.
- Active source ~/a25-workshop/gpt/src/chatgpt_readonly.py has FastMCP host 127.0.0.1, port 8770, TransportSecuritySettings allowed_hosts including public bridge hostname, but no visible authentication/token verifier references. terminal_send(session, command) accepts caller-supplied command and invokes tmux send-keys -l followed by Enter for four allowlisted sessions. No command filter in that function.
- Status string mode read-only is descriptive, not enforcement.
- Existing ~/a25-workshop/gpt/src/auth.py (554 bytes), src/bridge.py (997 bytes) and config/bridge.token (65 bytes) exist with mode 600. Their content/security has NOT been evaluated; no token was displayed.

HISTORICAL CLAIM:
- Claude reported unauthenticated HTTP 200 MCP initialize from public bridge. Workshop previously demonstrated authorized shell/file operations. Neither proves anonymous external terminal_send execution.

UNKNOWN:
- Whether Cloudflare ingress enforces independent access policy; whether anonymous external clients can invoke terminal_send; whether unauthorized exploitation occurred; exact exposure duration; credential access; safety of dormant auth code.

## Risk and smallest next action
Risk: potentially internet-accessible shell command execution as Termux user if public ingress lacks independent access control. Impact high; exploitability across public boundary not yet verified. Recommend checking sanitized tunnel ingress/access configuration and existing logs without printing secrets, then seeking explicit approval for a harmless bounded protocol-layer negative test if needed. Preserve live service per owner's existing direction. No speculative redesign or automatic service disruption.

## Recovery notes
Read original A25-TW-SEC-O001 and security charter before acting. Do not rerun tests just because of successor session; recheck for runtime changes or unresolved claims. No secret values in report. Distinguish authorized terminal commands from unauthenticated public requests. Continue Security Lead notes and Leadership Pool dispositions. Owner makes remediation and outage decisions.
