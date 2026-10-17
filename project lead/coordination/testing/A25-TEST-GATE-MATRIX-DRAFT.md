# A25 Cross-Project Evidence Gate Matrix — DRAFT
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / Claude reviewer
DATE: 2026-10-17
STATUS: DRAFT TESTING MATERIAL; NOT A PRODUCTION POLICY

## Five independent gates
| Gate | Question | Minimum evidence |
|---|---|---|
| C1 COMMUNICATION | Did the correct order/report reach the intended workflow? | Exact path, commit, retrieval record, handoff timing, role claims separated from authentication |
| C2 SOURCE INTEGRITY | Which exact source was reviewed? | Repo, branch, full commit, file/blob IDs, computed SHA-256 if available, provenance and expected-source check |
| C3 EXECUTION | Did those exact bytes execute and pass? | Runtime, exact checkout/byte hashes, command, logs, exit code, tests, run URL/ID when CI |
| C4 INTEGRATION | Did the component work with actual permitted dependencies? | Authorized test environment, contract tests, dependency versions, observed outputs |
| C5 PRODUCTION | Is it safe and approved for deployment? | Security, access enforcement, durable recovery, policy/privacy checks, owner approvals and rollback |

## Result vocabulary
Use `PASS`, `FAIL`, `BLOCKED`, `NOT_TESTED`; attach a reason, evidence ref and timestamp. `BLOCKED` is not `FAIL` and neither means `PASS`. Do not derive all-green status from source presence or from another branch's workflow results.

## Case Study 001 application
C1 PASS (GitHub handoffs); C2 PARTIAL SOURCE IDENTIFICATION (commit/blob observed; exact executable materialization not proven); C3 BLOCKED (DNS/dispatch); C4 NOT_TESTED; C5 NOT_TESTED. Because PARTIAL is not one of the four result values, record C2 as BLOCKED pending byte-exact integrity validation, with source-identification subcheck PASS.

## Required build report fields
Order ID; source repo and branch; source full commit; artifact path and hashes; claimed versus authenticated actor; changed files; classification; test command/environment; observed outcome and logs; gate statuses; blockers; exceptions; next approval needed; owner acceptance; no-main-merge confirmation.

## Non-goals
This draft does not deploy a Watchdog, prove AI identity, authorize real data migration, or approve main merges. Gate names `C1`–`C5` are testing labels scoped to A25 evidence matrix and must not be confused with legacy Pocket Server gates; canonical namespace IDs to be assigned after registry ratification.
