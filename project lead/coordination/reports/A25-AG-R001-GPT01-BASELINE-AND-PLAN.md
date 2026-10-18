# A25-AG-R001-GPT01 — Baseline and Plan
FROM: A25-AG-GPT01 (GPT Archives, Watchdog Support and GitHub Agent Lead; conversational seat claim)
FOR: Zed; GPT A25 Project Lead
DATE: 2026-10-17 MDT (owner-supplied session date)
RE: LEAD-HANDOFF-016 independent reconnaissance and initial plan
BASIS: GitHub connector read-only inspection of pinned handoff and repository files/trees; no local execution

## Authority and status
ADOPTED (owner instruction): delegated leadership of Archives, Watchdog support tooling and GitHub Agent/Bot; Pocket Server and Roundtable Communication remain under GPT A25 Project Lead. This report is discovery and planning only. No new branch, deployment, credentials, permission change, or phone access authorized. No changes to Claude02 O007.

## Verified source-access ledger (GitHub connector)
- Handoff pinned at `fe67faffad23c6f413938cb375c2003ef15bc2d6`: `project lead/leadership/LEAD-HANDOFF-016-A25-AG-GPT01-ARCHIVES-WATCHDOG-GITHUB-AGENT.md` (content retrieved).
- A25-Training-Workspace `coord/a25-namespace-trial-001` tree fetched; returned tree SHA `fe67faffad23c6f413938cb375c2003ef15bc2d6`, `truncated=false`. File contents inspected via GitHub fetch_file, not executed.
- pockettest `build/a25-pocket-server-roundtable` tree fetched at `fabedb661bb5161055534589c7517f7e0738139d`, `truncated=false`; observed `roundtable/README.md` and `shared_context/{CURRENT_STATE,DECISIONS,OPEN_ISSUES}.md` paths. Runtime not checked.
- Stratumnova-vault `main` tree fetched at `ddaf9f47ab745d1c96af295419600ce5d189b90d`; Tools_Templates- `main` tree fetched at `b2c774b6571311fe9f02c586009451e56cfe2d95`. Partial discovery only, not a comprehensive repository inventory.
- `project lead/coordination/README.md` inspected: orders and reports live in existing folders on coordination branch, report additions are append-only, no main merge without owner.
- `project lead/archivist/README.md` and `REPOSITORY-DIRECTORY.md` inspected: master index and eight public-repo owner-intent map exist; per-repo deep mapping not established by these files. Public index excludes private originals.
- `local build orders/LBO-001-GITHUB-AI-AGENT-SETUP.md` inspected: agent configuration is ordered/proposed, not demonstrated as deployed. `LBO-002-P1-ARCHIVIST-ONBOARDING-ADDENDUM.md` inspected: incremental per-repo map requirement and approval boundaries.
- `project lead/leadership/RN001-ARCHIVIST-MINIMUM-PROTOTYPE-001.md` inspected: explicitly DESIGN READY, IMPLEMENTATION NOT STARTED.
- `project lead/coordination/orders/A25-AR-O001-ARCHIVIST-OFFLINE-DESIGN.md` inspected: design-only order, no new implementation path.
- `local build operations and recalls/recall-network/reviews/RN-001-ARCHIVE-ARCHIVIST-WATCHDOG-INTEGRATION-REVIEW-001.md` inspected: architecture proposal, NOT IMPLEMENTED; screenshot observations are point-in-time.
- `watchdog/check.py` inspected (blob `3d9746af8a62eb808aa40f3a04b900c751c40efa`): Python read-only repository validator with hash, path and protected-record checks. `watchdog/test_check.py`, `test_fixtures.py`, `test_wd35_guard.py` exist; not run in this session.
- `.github/workflows/watchdog-draft-tests.yml` inspected (blob `d2309fc0f408f93520fa9d4b057082820b3f2b1f`): read-only contents permission, checkout, unittest, repository validator on `build/wd-02-watchdog-v0`; no changes made.
- GitHub Actions REST read: latest returned run #65, ID `39054994799`, commit `0ecb6079f66a46648ff9777bf1e88f1a2616a045`, branch `build/wd-02-watchdog-v0`, conclusion `success` (API metadata verified). Does NOT establish current coordination branch, other branches or full rules pass; job logs not inspected.
- `project lead/coordination/reports/A25-NS-R004-LB-GPT01.md` inspected: builder reports manual workflow dispatch unavailable and code execution unverified; this is a historical report, not independently reproduced test.
- `project lead/master archive/03-WATCHDOG-ACTIONS-HISTORY.md` inspected: historical run outcomes and incident narratives; individual causes not independently reproduced here.

## Capability and permissions inventory
VERIFIED connector interface availability in this GPT seat: GitHub `fetch`, `fetch_file`, `create_file`, plus numerous issue/PR/Git data operations exposed by tool metadata. `create_file` accepts an existing branch and returns a commit SHA; actual write scope is demonstrated only by this authorized report commit if successful. Read operations above succeeded. GitHub Actions run metadata is readable. No workflow-dispatch action identified in the inspected tools; exhaustive absence across all possible interfaces NOT VERIFIED. GitHub App installation privileges, branch protections, OAuth principal, Claude-side connector parity, paid agent/Copilot entitlement, autonomous agent runtime, and private archive access are UNKNOWN. Do not equate connector action availability with effective permissions. Google Drive and Plugin Creator are mentioned in handoff as installed; their live permissions were not exercised here.

## Existing candidate location
Use `project lead/archivist/` as the existing governance/index entrypoint and `project lead/coordination/reports/` for this report. For offline prototype code, request approval of a precise existing file destination after checking current source/test candidates; do not create `/a25/`, a parallel archive, new branch or new folder by assumption. Watchdog code already resides at `watchdog/`, and CI draft at `.github/workflows/`; preserve independence and existing checks.

## Risks and discrepancies
1. Historical archive summaries and screenshots are not current phone verification; unknown local worktrees/ZIP hashes cannot be inferred from GitHub.
2. A source-authored `author` field is not authenticated AI identity. Preserve authenticated principal, seat claim, original author claim, and publisher separately.
3. Append-only reports need source hashes, exact revisions, privacy classifications, read-back and immutable correction records; Git history alone is not a permission boundary.
4. A green Actions conclusion is limited to its exact branch/commit/workflow; missing logs and skipped execution remain explicit.
5. Public catalog must not leak private repo names, chat exports, secrets or sensitive device paths.
6. Automated bot write access, unattended execution and approval impersonation are high risk; do not enable by default.
7. Cross-AI relay via GitHub/Drive is not proven real-time, bilateral, byte-exact or identity-safe without independent tests.

## Minimal staged plan — proposed, not authorized implementation
P0: Complete read-only branch/repository/source map and identify existing Archivist implementation candidate; record original source pointers and unresolved access gaps.
P1: Draft deterministic offline evidence schema and validator; separate source observation, claim, test, adoption, supersession and unavailable. Include timestamp/branch/hash/provenance/privacy fields.
P2: Run local fixtures on existing RN-001 originals: missing source, duplicate record, branch conflation, unknown timestamp, 403 delivery, unverified upload hash, forbidden public metadata, deterministic repeat build.
P3: Add read-only Watchdog support reports for provenance gaps, report/test mismatches, permission drift and exception escalation; no automatic approvals or source rewriting.
P4: Evaluate installed GitHub connector against least-privilege GitHub App or native agent. Test human-invoked report-only task and pinned commit read-back before requesting any write-capable bot.
P5: With separate approval, demonstrate cross-AI handoff (source receipt, distinct author/publisher, idempotent retry, exact byte/hash readback, fresh-session recovery); do not assert Claude parity until independently observed.
P6: Lead/Claude independent review; Zed decides any integration, deployment, new credentials, privileged writes or branch merge.

## Questions for GPT A25 Project Lead (no blocking questions to owner for report)
1. What exact existing path and branch are reserved for Archivist prototype implementation, and is A25-AR-O001 still awaiting builder design report?
2. Which Watchdog WD-02 rules, exceptions and baselines are frozen, and what interface should support tooling consume without modifying validator code?
3. What source privacy/custody classifications may be indexed publicly versus privately, and which relay tests are currently authorized?
4. Is LBO-001 assigned to another builder, and are there active bot or Claude review assignments that must not be duplicated?

## Owner approval required before
Creating branches/repos/folders, choosing protected code destination, writing implementation code outside a scoped order, modifying Watchdog/Pocket Server, importing private originals, creating credentials or GitHub Apps, enabling agent automation, changing permissions, deploying, or merging. This R001 report commit alone is explicitly requested.

## Conclusion
Baseline is PARTIALLY VERIFIED (repository trees, specific source files, connector reads, one Actions conclusion); execution/runtime/permissions and cross-AI parity remain UNKNOWN. Recommend a scoped offline Archivist/Watchdog evidence prototype using existing paths after lead coordination and owner approval. No implementation or live server actions performed.
