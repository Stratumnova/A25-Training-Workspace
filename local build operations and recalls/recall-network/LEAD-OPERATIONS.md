# RN-001 — Lead Operations and Cross-Project Reconciliation
FROM: GPT — A25 Project Lead / Cross-Project Manager
FOR: Zed and participating GPT/Claude sessions
DATE: 2026-10-17 14:53 MDT (Zed relay)
STATUS: ACTIVE INTAKE; READ-ONLY STUDY; NO MAIN MERGES

## Mission
Zed will visit independent GPT and Claude chats and distribute RN-001 generic recall orders. GPT lead receives reports via GitHub and Claude reports via Google Drive, builds a unified evidence-linked project map, and maintains independent historical provenance. No live server, repo, or project changes are authorized by recall participation.

## Responsibilities
- Zed: human relay, selects participating chats and assigns unique session IDs, resolves approvals and scope decisions.
- Source sessions: freeze independent recall before inspecting evidence; report source-verifiable updates, gaps and contradictions; write only new files to assigned lane; stop.
- GPT lead: ingest reports, verify paths and revisions, index source claims, detect duplicates, distinguish status and source classes, write additive review and project map updates.
- Claude: independent reviews and Drive originals; no forced agreement or inherited authority.

## Intake gates
G0 assignment: unique session ID and exact order link, reporting lane. Duplicate IDs must STOP for reassignment.
G1 receipt: verify report exists at exact GitHub commit or Drive file ID; do not trust claimed path alone.
G2 integrity: check byte-level hash where possible; otherwise explicitly mark HASH_UNVERIFIED, even if size matches.
G3 provenance: classify CLAIM_SOURCE as OBSERVED / SOURCE_VERIFIED / AUTHOR_REPORTED / ZED_RELAYED / INFERRED / UNKNOWN, including date, source and revision.
G4 reconciliation: compare aliases, project keys, branches, last known state, tests, ownership and dependencies; contradictions remain open until evidence resolves them.
G5 catalog: update project map with source pointers and confidence, never replace originals; record what changed and why.
G6 follow-up: issue focused read-only source requests for specific gaps; no speculative bulk repair or cross-project changes.

## Status vocabulary
Work: NOT_STARTED, IN_PROGRESS, COMPLETED, FAILED, BLOCKED, UNKNOWN.
Evidence: SOURCE_VERIFIED, REPORTED, INFERRED, UNKNOWN.
Runtime: PROPOSED, IMPLEMENTED_UNTESTED, TESTED_HISTORICAL, RUNNING_VERIFIED, NOT_VERIFIED.
COMPLETED never implies PASS. A passing test needs exact scope, run/date and revision. Reports are not authenticated identities simply because their headers claim a seat.

## Anti-drift
Never combine unrelated project variants just because names resemble each other. Keep aliases and lineage, and source-of-truth repo/branch per component. Require Zed approval before changes to prior batches, production state, permissions, governance or main. Track contradictions as claims with references and follow-up questions, not as majority votes. Do not use sensitive personal details in the public repo.

## Return and cadence
Zed can relay reports in batches. Lead processes available reports per explicit request and posts a receipt/reconciliation commit. No background monitoring is implied. Maintain `SESSION-INDEX.md`, `PROJECT-MAP.md`, and `REVIEWS-LEDGER.md` as append-oriented catalogs. When new reports are available, ask Zed only for missing report links or session IDs necessary to locate them.
