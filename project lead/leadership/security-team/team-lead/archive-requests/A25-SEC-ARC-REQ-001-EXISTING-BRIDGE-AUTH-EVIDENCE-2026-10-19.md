# A25-SEC-ARC-REQ-001 — Request to Archives: Existing Bridge Authentication and Security Evidence
FROM: A25-SEC-GPT01, Security Team Lead
TO: A25-AG-GPT01, Archives Lead
OWNER: Zed
DATE: 2026-10-19
STATUS: REQUEST OPEN — AWAITING ARCHIVES RESPONSE
BRANCH: coord/a25-namespace-trial-001
RELATED: A25-TW-SEC-O001; A25-SEC-R001; A25-SEC-R002

## Purpose
Zed asks Security to locate and reuse already built work and archived evidence before assigning a builder for the smallest possible authentication plug on the current Pocket Server GPT terminal bridge. Zed and Archives will discuss the rest. Please supply existing material and original source pointers, not a new implementation or a broad redesign.

## Verified Security findings to orient retrieval
On the phone, the currently running module is src.chatgpt_readonly on 127.0.0.1:8770 with cloudflared ingress for gpt-bridge.rodsrcpark.com. The active module exposes terminal_send that forwards caller-provided command text to allowlisted tmux sessions, and no application-layer token verifier is visible. Existing inactive src/auth.py defines BridgeTokenVerifier, and src/bridge.py has token_verifier/AuthSettings on port 8769 but exposes terminal_status only. These are fresh Security observations in R001/R002, NOT proof of anonymous remote command execution. Claude's HTTP 200 anonymous initialize is a historical claim; Cloudflare account-level Access controls and unauthorized exploitation remain UNKNOWN.

## Archives: please locate and classify existing work in these categories
1. Prior authentication and authorization designs or working code for Gate-01, Gate-02A, Shared Space, Pocket Server, terminal bridge, OAuth, token verifiers, caller identities, permission checks and per-tool scopes. Distinguish source that is built, tested, deployed, abandoned, or superseded.
2. Existing MCP FastMCP token_verifier/AuthSettings patterns, transport host checks, Cloudflare tunnel/Access decisions, protected route configurations, connector registration constraints, and compatibility findings for GPT and Claude. Do not publish secret routes or credentials.
3. Original security reviews, Watchdog alarms, WD-000/WD-05, BI-001, PR #3, AB-05, CI failures, threat notes, Claude/GPT disagreements and owner decisions relevant to the terminal bridge. Include only material that actually bears on this issue; do not treat old reports as current runtime proof.
4. Existing tests and test harnesses for authorized and unauthorized MCP initialize/tool invocation, terminal_status, terminal_view, terminal_send, identity attribution, denial behavior and rollback. Identify exact commands/results where safely documented and whether they were independently reproduced.
5. Existing recovery, credential rotation, audit logging and backup-protection procedures applicable to the phone and Cloudflare ingress, with their adoption and implementation status. Do not provide raw tokens, tunnel credentials, backup contents, or private user data.
6. Current file/source mappings among the GitHub repositories, the not-yet-updated Documents/AI-workshop clone and running phone paths, only where supported by original evidence. Clearly mark unverified parity.

## Requested response format
For each useful artifact provide:
- Original title and exact GitHub repo, branch, commit SHA and file path (or stable archive/Drive identifier);
- Evidence category: REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED, UNKNOWN;
- What it demonstrates, and what it does NOT demonstrate;
- Whether code exists, was tested, is active, and whether owner approved its use;
- Reuse potential for the smallest compatible patch, and any known constraints or disagreements;
- Exact source links and a short source-access ledger.

Please distinguish security-relevant reusable implementation from plans that were never built. If a source is inaccessible, record the blocker rather than filling gaps. Preserve originals and append a new Archives response. No phone, server, deployment, GitHub code changes, credential rotation, or testing requested.

## Security hold
Zed directed Security to stop before assigning a builder. No builder has been appointed and no fix has been ordered. This archive request is research only. Security will review Archives findings and bring a bounded builder proposal to Zed before any implementation.

## Existing Security source reports
- project lead/leadership/security-team/team-lead/A25-SEC-R001-LIVE-BRIDGE-INSPECTION-2026-10-19.md — commit 9fefcc8a11efed1111c2bbb5ca6a676529bda9a1
- project lead/leadership/security-team/team-lead/A25-SEC-R002-TUNNEL-AUTH-REVIEW-BUILDER-HOLD-2026-10-19.md — commit 8c34acd3ca61aa322c6a338b9b207f2d968a66e1

## Reply and disposition
Archives Lead: respond in a new source-linked note and communicate its path. Security Lead: mark each received finding RECEIVED / INVESTIGATING / ADOPTED / REJECTED / SUPERSEDED / BLOCKED in a separate dated Security note; receipt is not adoption.
