# A25-NS-O002 — Synthetic Namespace Registry Prototype
FROM: GPT — A25 Project Lead
FOR: LB-GPT01
DATE: 2026-10-17
RE: Build and test an isolated A25 namespace validator and migration ledger prototype
BASIS: A25-NS-V001 lead review; A25-NS-O001 design drafts
STATUS: AUTHORIZED — SYNTHETIC PROTOTYPE ONLY

## Read first
`project lead/coordination/reviews/A25-NS-V001-LEAD-REVIEW.md`, the three A25-NS draft documents, and `project lead/archivist/TEST-DATA-AND-PRIVACY-POLICY.md`.

## Deliverables
1. Create a dedicated builder implementation branch based on this coordination branch. Do not develop executable code directly on the coordination branch. Report the branch and full base SHA.
2. Build a minimal offline schema/validator with no external services or secret credentials. Validate grammar, registered subsystems and kinds, unique IDs, revisions, aliases, classifications, and explicit provenance. Use a small fixture dataset with only synthetic data.
3. Include a single-writer deterministic ID allocator for prototype tests; reject duplicate and unreserved claims. Do not pretend it supports concurrent writers or distributed offline allocation.
4. Implement a simple append-only migration event log for synthetic fixtures; validate legal state transitions, hash conflicts, missing evidence, source-versus-destination revisions, and denied-by-default unknown classifications. Document durability limitations.
5. Add tests for Gate-01 collisions, Key5 PROMPT versus CODE, wrong AI seat impersonation, revision conflicts, fake-token leakage, invalid grammar, missing source, duplicate ID, and attempted rewrite of prior ledger events. Never use actual secrets.
6. Provide README with exact test command, known limitations and example queries. Include a small machine-readable index demonstrating retrieval/disambiguation without publishing restricted content.
7. Write report `project lead/coordination/reports/A25-NS-R002-LB-GPT01.md` on **coord/a25-namespace-trial-001**, pointing to implementation branch and pinned full commits, test evidence, failed tests and open decisions. If you cannot write report to coordination branch, fail loudly to Zed.

## Constraints
- No changes to main, Watchdog, Pocket Server, original Stratumnova repositories or protected A25 history.
- No migration of real files, real namespace assignments, private ZIP uploads, or external service integration.
- Do not claim a working maintenance bot, Watchdog integration or authenticated AI identity.
- Stop after tests and report. No merging without Zed's approval.

## Goal
Prove a basic namespace can distinguish identical names in different systems and refuse unsafe retrieval/migration. Report actual observed behavior, not just test-file presence.
