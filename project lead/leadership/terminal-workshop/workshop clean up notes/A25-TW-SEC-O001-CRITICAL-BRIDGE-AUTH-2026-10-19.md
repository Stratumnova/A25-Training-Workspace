# A25-TW-SEC-O001 — Critical Public Terminal Bridge Exposure

**Issued by:** A25-TW-GPT01, Workshop Lead
**To:** A25 Security Team / Security Lead (receiving assignment pending)
**Owner authorization:** Zed approved reading Claude's phone report and creation of a Security Team work order; owner explicitly requires keeping the Pocket Server live during this investigation.
**Date:** 2026-10-19
**Scope:** Pocket Server Ground Zero only
**Priority:** CRITICAL — remote shell-command exposure suspected
**Status:** OPEN / AWAITING SECURITY INTAKE — NOT FIXED
**Owner seal:** Ground Zero owner-sealed; no changes to sealed policy implied.
**Source artifact:** `/storage/emulated/0/Documents/AI_Workshop/ClaudesResponse.md`, 5,667 bytes, SHA-256 `3880113d1e835a0770c2d2a4cae9b7bd36e5817ade70bafe94ae55d919f26b6b` (hash independently checked by Workshop Lead via terminal).
**Source method:** Workshop Lead read the original via `a25-gpt` terminal on Oct 19. Claude's test claims are source-reported and require Security Team reproduction.

## Critical finding / risk

Claude reports that the active `src.chatgpt_readonly.py` bridge on local `127.0.0.1:8770`, exposed by the GPT Cloudflare tunnel, has no authentication references; `terminal_send` accepts arbitrary commands to the allowlisted tmux shell. Claude reports an anonymous remote MCP initialize request returned HTTP 200. The bridge's `terminal_status.mode: read-only` is descriptive only and **does not constrain command execution**. Claude and GPT also appear under one `gpt-workshop` identity, preventing trustworthy per-caller attribution.

**Independently observed by Workshop Lead:** this same bridge enabled real shell execution, including authorized file move/unzip. The original Claude report was read and hashed. **Not independently reproduced in this order:** anonymous remote access test, detailed active source review, token verifier efficacy, caller identity.

**Security implication:** potential internet-accessible command execution as Termux user and access to tunnel credentials, unused `bridge.token`, other stored credentials and unencrypted recovery backup in shared Documents storage. Treat as urgent potential compromise; do not publish secrets or assume observed IP addresses identify callers.

## Owner operational constraints

- **Keep existing bridge and tunnel live during the initial investigation**, per Zed's explicit direction.
- Do not stop/restart services, change Cloudflare, rotate credentials, edit deployed source, install packages, archive/delete files or change permissions without a separate authorized change plan.
- If an immediate containment action is necessary, report urgency and request Zed's approval with clear effect on live AI access.
- Conduct read-only inspection and prepare repair/test proposal first. Never issue arbitrary test commands via the public endpoint.
- No credentials, tokens, full tunnel IDs, or secret routes in public GitHub reports.

## Assigned investigation and remediation design

1. **Reproduce and bound exposure:** inspect running PID/module and actual MCP route, auth middleware, tmux tool allowlist, and tunnel ingress. Conduct a strictly harmless, rate-limited unauthenticated initialize probe only with explicit owner approval; log status, endpoint class and test method, no sensitive response data. A 200 initialize alone establishes absent initialization auth, not by itself every subsequent permission; verify the complete capability path safely.
2. **Evaluate existing dormant implementation:** `~/a25-workshop/gpt/src/bridge.py`, `src/auth.py`, `config/bridge.token` reportedly exist but are unused. Review actual code, token verification, bearer handling, endpoint compatibility, replay/rotation, per-tool authorization and denial behavior. Do not assume it is secure merely because token code exists.
3. **Design a fail-closed replacement:** unauthenticated requests must not reach MCP tool invocation; deny-by-default shell access; enforce caller authorization server-side, restrict commands and sessions, and separate GPT and Claude identities/audit attribution. Evaluate OAuth/per-caller identities or another owner-approved mechanism; avoid reintroducing unauthenticated shared-secret-route access.
4. **Prepare a staged migration:** preserve current connector functionality where possible; specify new endpoint/config requirements, backups, rollback, and cutover sequence. Any public tunnel switch or downtime requires Zed's explicit approval.
5. **Exposure response:** identify secrets potentially readable during the exposure window, recommend rotation/revocation of tunnel credentials and stored tokens (including GitHub if present), inspect logs for suspicious use with attribution caveats, and secure/encrypt or relocate the unencrypted 94.6 MB Documents recovery archive. Do not reveal or rotate secrets without authorization.
6. **Verification gate:** document unauthenticated request rejection (expected 401 or another appropriate explicit denial depending on transport), authorized GPT access, authorized Claude access with separate identity, denied unauthorized shell calls, log attribution, regression tests, and rollback test. Record exact tested versions and evidence.
7. **Historical components:** treat Gate-01, Gate-02A, Shared Space and C3 branch as not running in Claude's Oct 19 observation, not automatically disposable; inventory dependencies under Ground Zero.

## Security deliverables

- Read-only risk assessment with reproducible evidence and impact/likelihood.
- Remediation options and chosen recommendation, with authentication and authorization boundaries.
- Owner approval request before any disruptive or mutating action.
- Test matrix and staged cutover/rollback procedure.
- Post-fix verification report distinguishing VERIFIED, HISTORICAL CLAIM, ADOPTED, UNKNOWN.
- Separate note on any disagreement with Claude's report; preserve both until resolved.

## Acceptance criteria

The work order is not closed until Zed approves the implementation and the Security Team independently verifies that unauthenticated clients cannot execute commands, authenticated callers have correctly limited privileges, GPT and Claude attribution is reliable, and the exposure-response actions are dispositioned. A green test or owner approval alone does not prove a secure production deployment.

## Source classification

**REFERENCE:** original Claude report and pre-Ground-Zero Pocket Server code.
**HISTORICAL CLAIM / REPORTED TEST:** Claude's no-credential HTTP 200, no-auth source scan, caller-IP observations, and dormant token design.
**VERIFIED by Workshop Lead:** source file hash/availability; GPT command-shell write capability demonstrated during Ground Zero; bridge and tunnel reached by current GPT tools.
**ADOPTED:** owner-directed live investigation, Security Team work-order preparation, Ground Zero rules.
**UNKNOWN:** full unauthenticated tool execution from outside, evidence of exploitation, safe production auth implementation, exact exposure duration.
