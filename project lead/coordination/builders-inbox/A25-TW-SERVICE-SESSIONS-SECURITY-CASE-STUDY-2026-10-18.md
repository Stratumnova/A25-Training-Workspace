# A25 Workshop — Service Sessions Security Case Study
Date: 2026-10-18 (observed tunnel logs cross UTC midnight to 2026-10-19)
FROM: A25-TW-GPT01
FOR: Zed, A25 Project Lead, Security, Claude, Archives
STATUS: VERIFIED bounded read-only investigation; NO phone changes

## Owner authorization (ADOPTED)
Owner explicitly authorized deeper study of previously designated do-not-send-command sessions with view-only operations and commands to view, absolutely no changes/moves. Following a safety block, owner authorized continuing this study. This does not authorize sending commands into service panes or modifying the phone.

## Evidence collection
- terminal_view(a25-bridge): returncode 0; visible MCP request activity with HTTP 200 and 202, CallToolRequest processing and created transport session IDs. Raw IP addresses and session IDs omitted from this public report.
- terminal_view(a25-tunnel): returncode 0; multiple Cloudflare 'stream canceled by remote with error code 0' events, originService http://127.0.0.1:8770, destination GPT bridge HTTPS /mcp. Exact public endpoint and remote IPs intentionally omitted here. These log errors alone do not establish outage or compromise.
- terminal_view(a25-gpt): one attempt returned an unusable result; no new finding from that attempt. Earlier inspection showed server logs.
- A bounded read-only terminal_send to a25-test (NOT to service sessions) obtained tmux metadata, process metadata, and remainder of bridge source. Initial view result unusable, next ordinary view showed full output and shell prompt.
- No secrets/config file contents opened; no session input sent to a25-bridge, a25-tunnel or a25-gpt; no files changed.

## Verified tmux state
tmux list-sessions: a25-bridge (1 window, detached), a25-gpt (1 window, attached), a25-test (1 window, attached), a25-tunnel (1 window, detached).
tmux list-panes -a pane_current_command: a25-bridge python, a25-gpt python, a25-test tmux, a25-tunnel cloudflared.
Process list showed:
- Pocket Gate-02 uvicorn server on localhost port 8766.
- Two cloudflared tunnel processes using the same workshop cloudflared.yml and same named tunnel.
- Active Python -m src.chatgpt_readonly process.
Do not infer duplicate tunnel failure from process count alone.

## Verified bridge send semantics
~/a25-workshop/gpt/src/chatgpt_readonly.py: terminal_send calls tmux send-keys with command, then tmux send-keys Enter. Returns ok based on Enter subprocess returncode; it does not inspect shell exit code or enforce read-only command grammar. Its allowlist includes a25-bridge, a25-tunnel, a25-gpt, a25-test. Therefore service panes are technically targetable by connector, despite operational do-not-send designation. This is a security review concern, NOT an authorization to test disruption.

## Assessment
VERIFIED: MCP request processing visible; Cloudflare tunnel errors visible; live tmux/process layout; send tool's session allowlist and lack of command completion proof.
HISTORICAL CLAIM: prior reports of caller identity separation or security mechanisms remain unverified unless independently checked.
UNKNOWN: caller authentication and authorization, command provenance, impact of duplicate cloudflared processes, exact ingress policy, log exposure risk, audit completeness, whether remote stream cancellations affect reliability.
ADOPTED: owner view-only case-study limits, escalation-on-block rules, no phone changes.

## Security questions for leadership
1. Should command sending to service sessions be disabled in future approved code changes?
2. How should distinct GPT/Claude caller identity and audit be enforced?
3. Does a read-only mode label create a misleading security expectation?
4. Are two cloudflared processes intentional, and what do their runtime connections serve?
5. How can transport errors be correlated with actual user-visible failures without exposing credentials?

## Next justified action
Read-only source and metadata review; preserve unresolved findings. No hardening implementation, restarts, config changes, network probes or active access tests without separate owner approval.
