# CASE-001 — Addendum 003: Branch Audit and Test-Gate Findings
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / future Claude reviewer
DATE: 2026-10-17 13:23 MDT (Zed relay)
RE: Overall findings from namespace prototype workflow visibility and branch audit
BASIS: Owner screenshots; GitHub branch listing and Actions runs listing; O001–O004 reports and prior case-study checkpoints
STATUS: EVIDENCE-BASED CASE STUDY; CI EXECUTION UNVERIFIED

## Findings
1. GitHub proved useful as a durable human-mediated cross-session communication channel. Zed relayed short prompts, not complete build orders or full reports. No autonomous inter-chat notification was demonstrated.
2. The builder delivered synthetic design and prototype code without receiving Zed's local ZIP uploads. This does not prove it knows their contents.
3. Branch listing confirmed six branch heads: `build/a25-ns-o002-synthetic-prototype` at `e5c9754eeebd4d7474fc6adfe259f75385bf38a6`; `coord/a25-namespace-trial-001` at `040120438b2e126d8e9ce2184fa984550673cc3f` (at time of audit); `build/wd-02-watchdog-v0` at `0ecb6079f66a46648ff9777bf1e88f1a2616a045`; `main` at `34b0d235a2bc78c975c57c1d16ecd74028832f5d`; plus `builder/inbox-gpt-builder-2026-10-16` and `test/gpt-connector-capabilities-20261016`. Branch isolation was observed; branch-protection policy was not established by these records.
4. GitHub Actions returned 65 recorded runs of `A25 Watchdog draft tests`, all associated with Watchdog workflow; screenshots show green and older red runs. No namespace workflow run was evidenced. Watchdog green results do not verify namespace code.
5. O003 blocked on exact-source execution due DNS; O004 added manual-only workflow on implementation branch but no dispatch action was available. No completed namespace CI run exists in observed evidence.
6. GitHub workflow not visible in owner screenshot is consistent with default-branch registration constraints, but precise root cause has not been proven.
7. Builder's reported 14 passing tests concern locally constructed code, not proven identical committed bytes. Do not promote to green.

## Proposed standard acceptance gates (not yet globally ratified)
- C1 COMMUNICATION: Order/report independently retrievable with exact commits.
- C2 SOURCE INTEGRITY: Branch/commit/blob identified and hashes checked; source provenance present. Git blob SHA-1 is not SHA-256.
- C3 EXECUTION: Exact committed source executed; environment, commands, exit status, logs, run ID and test counts recorded.
- C4 INTEGRATION: Connected-system behavior verified in an authorized environment.
- C5 PRODUCTION: Security, durability, governance and owner acceptance proven.
Each gate has independent `PASS | FAIL | BLOCKED | NOT_TESTED` outcome. A delivery PASS must not override an execution BLOCKED.

## Trial checkpoint
C1 PASS; C2 source identified and inspected (byte-exact execution handoff still blocked); C3 BLOCKED; C4 NOT_TESTED; C5 NOT_TESTED. Keep status separate by gate, artifact and branch.

## Next test
Establish an authorized byte-exact execution route, such as a registered GitHub Actions workflow or verified source materialization. No protected/main changes merely to trigger tests. If GitHub workflow registration requires main, request explicit owner approval for the smallest safe alternative, rather than silently merging.

## Leadership/case-study duty
After each builder report, lead independently reviews, appends a checkpoint, records decision and next experiment, and resumes scoped project leadership. Claude later audits independently; narrative seat labels are not authenticated identities.
