# POOL-2026-10-19-SECURITY-BRIDGE-EXPOSURE — Critical Security Intake

**FROM:** A25-TW-GPT01, Workshop Lead
**TO:** A25 Security Lead / Security Team, A25 Project Lead
**DATE:** 2026-10-19 (Ground Zero session)
**PROJECT:** Pocket Server only
**TYPE:** CONCERN / EVIDENCE / SECURITY WORK ORDER INTAKE
**STATUS:** OPEN — SECURITY RECEIPT PENDING
**OWNER:** Zed
**SOURCE:** [A25-TW-SEC-O001 (pinned)](https://github.com/Stratumnova/A25-Training-Workspace/blob/8e919b886abbafcef857a4ba87d88a6eb446e3e2/project%20lead/leadership/terminal-workshop/workshop%20clean%20up%20notes/A25-TW-SEC-O001-CRITICAL-BRIDGE-AUTH-2026-10-19.md)

## Evidence and limits
Workshop Lead read and SHA-256-checked the original Claude phone report `Documents/AI_Workshop/ClaudesResponse.md`. Claude reports anonymous MCP initialization returning HTTP 200 on the public GPT terminal bridge and no server-side auth in the active module. The Workshop Lead independently verified real command execution through the connector, but **has not independently reproduced the anonymous public endpoint probe**. Same bridge identity reportedly shared by Claude and GPT.

## Message for receiving lead
**Critical potential remote-command exposure.** Take intake of A25-TW-SEC-O001 and review source, live topology, unauthenticated capability, existing unused token-verification code, caller identity separation, credential rotation, backup protection and staged remediation. Do not publish credentials. Zed explicitly wants the workshop live during initial investigation; **no shutdown, deployment, rotation, file change or access-control change is authorized by this pool note**. Bring a proposed containment or cutover plan to Zed for approval.

Ground Zero's owner-sealed decision applies to Pocket Server; old plans are reference, not controlling implementation requirements. Preserve evidence and do not mistake untested code for a fix.

## Open questions
1. Can a genuinely unauthenticated outside client invoke `terminal_send` (not just initialize MCP)?
2. What exact auth/authorization change is safe for both GPT and Claude?
3. Which credentials require rotation, and can they be rotated without unapproved downtime?
4. Which lead/seat is currently authorized to accept Security Team work orders?

## Receipt / disposition
**PENDING.** Receiving leader should publish a separate acknowledgment/disposition; do not silently edit this note. This notice does not claim the Security Team has started or accepted the work.
