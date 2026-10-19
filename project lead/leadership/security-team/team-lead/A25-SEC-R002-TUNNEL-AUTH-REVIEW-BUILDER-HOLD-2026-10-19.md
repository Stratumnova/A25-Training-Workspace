# A25-SEC-R002 — Tunnel and Auth Review / Builder Assignment Hold
DATE: 2026-10-19
SEAT: A25-SEC-GPT01
OWNER: Zed
STATUS: INVESTIGATION CHECKPOINT — HOLD BEFORE BUILDER ASSIGNMENT
BRANCH: coord/a25-namespace-trial-001

## Authority
Owner authorized terminal investigation of flagged A25-TW-SEC-O001, and instructed Security Lead to STOP when time to assign a builder to write fixes. No source changes, deployment, restart, shutdown, credential exposure, public probe, or builder assignment performed.

## Fresh verified evidence (terminal read-only)
- Active process previously confirmed: python -m src.chatgpt_readonly on port 8770; cloudflared running.
- config/cloudflared.yml contains ingress for gpt-bridge.rodsrcpark.com to http://127.0.0.1:8770 and fallback http_status:404. Credentials path was redacted in displayed output. No Cloudflare Access policy appears in this local YAML. This does NOT exclude separately configured account-level Access policy.
- Active src/chatgpt_readonly.py exposes terminal_send(session, command), which sends caller-supplied text to allowlisted tmux sessions followed by Enter, without visible authentication/token verifier or command filtering. TransportSecuritySettings allowed_hosts is a host check, not user authentication.
- Dormant src/auth.py defines BridgeTokenVerifier using a token file and hmac.compare_digest. No token value read or published.
- Dormant src/bridge.py configures token_verifier and AuthSettings on port 8769, but exposes terminal_status only. It is not a drop-in replacement for live port 8770 command-capable service.
- terminal_status mode read-only is a status string, not enforcement.

## Claims and limits
VERIFIED: active source lacks application-layer caller auth; local tunnel config forwards to active bridge; live terminal_send performs arbitrary caller-provided shell command via tmux if invoked.
HISTORICAL CLAIM: Claude observed anonymous public HTTP 200 MCP initialize. An HTTP 200 initialize does not alone prove anonymous tool invocation.
UNKNOWN: Cloudflare account-level Access enforcement, external unauthenticated terminal_send execution, compromise, exposure duration, caller attribution, suitability of dormant verifier for current GPT/Claude connections.

## Minimal builder brief (NOT an order or assignment)
Goal: add fail-closed caller authentication/authorization to existing command-capable active bridge while preserving its three tools, allowlisted sessions, current operational workflow and tunnel topology. Reuse existing auth primitives only after compatibility and identity review. Ensure unauthorized callers cannot invoke terminal_send; do not rely on mode label, Host header, or obscurity. Provide test receipts for denied no-credential/wrong-credential requests and permitted authorized status/view/send with a harmless test command; ensure no secrets printed. Coordinate with Workshop Lead for staged compatibility, rollback and owner-approved deployment. Do not redesign Gate-01, add new architecture, rotate secrets or modify Cloudflare independently. Identity separation is a follow-on decision with Zed; don't silently change caller identities.

## Owner decision point
STOP HERE per Zed: request appointment/authorization of Security Builder to prepare minimal code patch, plus explicit scope and whether independent reviewer will be appointed. Security Lead may review the resulting patch and evidence; only Zed approves deployment. No builder appointed in this session.

## Recovery
Previous A25-SEC-R001 live inspection commit 9fefcc8a11efed1111c2bbb5ca6a676529bda9a1. Original A25-TW-SEC-O001 and Security Lead charter remain controlling. Treat this note as fresh inspection evidence, not a fix or closure. No runtime changes.
