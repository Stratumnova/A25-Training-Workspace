# A25 Security Team — Onboarding and First Intake

DATE: 2026-10-19
OWNER: Zed
STATUS: PREPARED FOR RECEIVING SECURITY LEAD — NOT YET ACKNOWLEDGED

## Mission
Protect A25 Pocket Server's terminal access, identities, credentials, data and auditability while preserving evidence and honoring Zed's operational approvals. Investigate first, propose bounded remediation, verify before claiming completion.

## Primary original orders (do not relocate or rewrite)
- Workshop order: [A25-TW-SEC-O001 — Critical Bridge Authentication](https://github.com/Stratumnova/A25-Training-Workspace/blob/8e919b886abbafcef857a4ba87d88a6eb446e3e2/project%20lead/leadership/terminal-workshop/workshop%20clean%20up%20notes/A25-TW-SEC-O001-CRITICAL-BRIDGE-AUTH-2026-10-19.md).
- Leadership Pool notice: [POOL-2026-10-19-SECURITY-BRIDGE-EXPOSURE](https://github.com/Stratumnova/A25-Training-Workspace/blob/40e75d615dfff1841d40380273a27284cdd8ffb8/project%20lead/leadership-pool/POOL-2026-10-19-SECURITY-BRIDGE-EXPOSURE.md).
- Source phone artifact (not published here): `Documents/AI_Workshop/ClaudesResponse.md`, 5,667 bytes, SHA-256 `3880113d1e835a0770c2d2a4cae9b7bd36e5817ade70bafe94ae55d919f26b6b`; Workshop reports it read and hash-checked this file.

## Initial risk statement — carefully scoped
Claude **reported** an unauthenticated HTTP 200 MCP initialization at the public GPT bridge, no auth enforcement in the active `src.chatgpt_readonly.py`, shell-command capability in `terminal_send`, and shared GPT/Claude bridge attribution. Workshop **independently verified** that its authorized connector could execute shell commands, move/extract a ZIP and inspect files. It did **not** independently reproduce anonymous public tool invocation. A 200 initialization response alone is not proof that an unauthenticated caller successfully executed a shell command. Nevertheless the combination is a critical suspected exposure demanding urgent owner notification and bounded verification.

## First assignment
Accept or explicitly decline A25-TW-SEC-O001 in a **new** dated acknowledgment record. Do not silently treat this onboarding as receipt. The receiving lead should:
1. Inventory source evidence and running topology with read-only methods explicitly approved by Zed.
2. Separate observed public initialization from proven anonymous command execution.
3. Review active bridge code and dormant `src/bridge.py`, `src/auth.py` and token verifier as candidates, not preapproved fixes.
4. Model authenticated per-caller access, tool/session authorization, GPT/Claude attribution, audit logs, and fail-closed behavior.
5. Assess potentially exposed secrets and the unencrypted recovery backup without copying secrets into reports.
6. Produce containment options, staged cutover, rollback, test matrix and exact owner approval requests.
7. Obtain separate permission before probes, phone commands, changes, shutdowns, credential rotation or deployment.

## Verification and closure bar
Test unauthenticated rejection at the correct protocol layer; authorized GPT and Claude calls under distinguishable identities; unauthorized tool/session denial; audit attribution; regression and rollback. Preserve negative results. A repaired source file, passing local tests, owner approval, and successful live deployment are **different milestones**. Closure requires independent implementation verification and Zed's explicit acceptance.

## Evidence and escalation
Use REFERENCE / HISTORICAL CLAIM / VERIFIED / ADOPTED / SUPERSEDED / UNKNOWN. Preserve conflicting findings. If evidence indicates active compromise or increased urgency, escalate to Zed promptly with proposed impact and exact containment consequences; do not quietly change live services.
