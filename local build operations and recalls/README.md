# Build Operations and Recalls — A25
STATUS: ACTIVE handoff workspace; coordination branch only
OWNER: Zed; GPT lead maintains indexes and reviews; assigned builders submit their own reports.
PURPOSE: memory recall, operational recovery, startup reconstruction, network drop studies, source verification and safe cross-session handoffs.

This folder is a sibling of `local build orders/`, not a replacement for that folder or for `project lead/coordination/`. No merge to main is authorized by its creation.

## Navigation
- `outbox/`: lead-issued read-only recall/recovery orders for builders to fetch.
- `inbox/`: builder responses, with report IDs and explicit provenance.
- `reviews/`: lead or independent reviewer findings and follow-up decisions.
- `case-studies/`: immutable experiment plans, results and corrections.
- `INDEX.md`: status, exact paths, response IDs, branches and commits.

## Operating procedure
1. Lead publishes a uniquely identified order to outbox, then updates INDEX.
2. Zed relays only the order path, repo and branch to a separate builder session.
3. Builder reads the pinned order, performs only authorized operations and creates a NEW report in inbox on this same coordination branch. Builder must not overwrite orders or existing reports.
4. Builder returns report path and full commit SHA to Zed. Zed relays that reference to lead.
5. Lead independently fetches report, checks evidence and writes review and case-study result; does not convert claims into verified facts.
6. Preserve original recall before source checks, append corrections separately, mark unknowns and blockers.
7. For branch conflicts, STOP and report. No forced pushes, history rewrites, protected-branch changes or main merge.

## Security
Read-only diagnostic unless separate approval. No passwords, bearer paths, access tokens, private user files or secret values in this public repository. Never treat an AI seat label as authenticated identity. No service restart, tunnel reconfiguration or self-repair under a recall order. Keep real-private evidence out of this repository; store only sanitized metadata and approved references.
