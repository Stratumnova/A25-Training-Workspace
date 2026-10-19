# A25 Security Lead — Intake Receipt and Successor Onboarding Notes

DATE: 2026-10-19
OWNER: Zed
SEAT: A25-SEC-GPT01
SOURCE: Owner supplied the fresh Security Lead's intake response in the project chat.
EVIDENCE CLASS: HISTORICAL CLAIM for the new seat's actions; REFERENCE for its assessment. This document records the reported intake and does not independently certify GitHub reads or deployed security state.
STATUS: Intake reported complete; investigation and remediation pending. No new operational authority granted.

## Context and durable links
Repository: `Stratumnova/A25-Training-Workspace`
Branch: `coord/a25-namespace-trial-001`
Team home: `project lead/leadership/security-team/`
Standing charter: `project lead/leadership/security-team/team-lead/A25-SEC-GPT01-SECURITY-LEAD-CHARTER-2026-10-19.md`
Workshop order: `project lead/leadership/terminal-workshop/workshop clean up notes/A25-TW-SEC-O001-CRITICAL-BRIDGE-AUTH-2026-10-19.md`
Leadership Pool notice: `project lead/leadership-pool/POOL-2026-10-19-SECURITY-BRIDGE-EXPOSURE.md`

## Reported intake receipt
A25-SEC-GPT01 stated that it accepted the Security Team Lead role and received A25-TW-SEC-O001. It reported reading all six prescribed GitHub records: Security Team README, onboarding README, Team Lead README, Security Lead Charter, Workshop security order, and Leadership Pool notice. It expressly reported **not** accessing Claude's original phone artifact or deployed source, running **no** phone/terminal operations, and making **no** GitHub changes. No original per-read receipts or hashes were supplied with the intake text, so independently verified access remains unestablished here.

## Scoped findings as reported
- **SEC-F001 — Potential public command execution:** Claude historically reported an HTTP 200 unauthenticated MCP initialization, an unauthenticated active bridge, a shell-capable `terminal_send`, and shared GPT/Claude attribution. Workshop's authorized shell and file-operation tests were reported successful. **Anonymous remote shell command execution is UNKNOWN**: HTTP 200 initialization alone does not establish that tool invocation succeeds.
- **SEC-F002 — Caller identity:** Shared `gpt-workshop` identity is reported; actual caller-level audit attribution remains unresolved.
- **SEC-F003 — Credentials and backup:** Potentially accessible credentials and an unencrypted ~94.6 MB recovery archive were identified. Unauthorized access or exfiltration is **UNKNOWN**, not proven.

The seat recommended reviewing the existing active bridge and dormant token verifier first, confirming source/runtime correspondence only with owner-approved phone access, and then proposing the smallest compatible fix with rollback and verification. No repair was selected or deployed.

## Owner authority and anti-drift rules for successor leads
Zed retains final design, scope and operational approval. Security reviews must stay with the current A25 build and the assigned security issue; they may not invent requirements, replace the architecture, demand unrelated services, or reopen settled decisions without new concrete evidence. Warn clearly about serious risks and present bounded alternatives, but do not use risk statements to claim authority over Zed or other leads. A declined recommendation is recorded with residual risk; no quiet override or repeated pressure absent new evidence.

Preserve live bridge/tunnel during the initially authorized investigation **as a recorded owner constraint, not a security assurance**. No terminal commands, endpoint probes, source edits, credentials access/rotation, service interruption, GitHub writes, merges or deployment without the relevant separate approval. Escalate evidence of active compromise promptly with specific containment options and consequences.

## First work after owner authorization
1. Read original active bridge and dormant authentication implementation using specifically approved access; identify enforcement at the correct MCP/tool boundary.
2. Independently establish which module/process/tunnel is actually live before making runtime claims.
3. Design and seek approval for the smallest repair preserving GPT/Claude workflows and distinct attribution.
4. Plan negative unauthenticated tool tests, positive authorized caller tests, audit attribution, rollback, and secret exposure response.
5. Preserve all results as REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED, or UNKNOWN with source paths and timestamps.

## Handoff checkpoint
Case: OPEN. Work order: RECEIVED according to seat report. Anonymous command execution: UNKNOWN. Evidence of compromise: UNKNOWN. Remediation: NOT VERIFIED. Next action: **wait for Zed's scoped authorization**. Do not confuse a reported intake with independently verified findings, or a future owner-approved remediation with proof of deployment.

## Pattern for onboarding future team leads
Use this sequence: (1) named owner appointment; (2) exact existing repo/branch/namespace; (3) charter and original orders read; (4) authority and non-drift acknowledgment; (5) evidence classes and unresolved conflicts; (6) read-only intake with source ledger; (7) precise owner approval request; (8) additive durable receipt; (9) no self-certified closure. This is a repeatable process, not permission to impose this security charter on non-security teams.
