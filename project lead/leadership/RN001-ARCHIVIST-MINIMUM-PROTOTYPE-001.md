# RN-001 Archivist Minimum Prototype 001 — No New Tree
Date: 2026-10-17
Status: DESIGN READY; IMPLEMENTATION NOT STARTED

## Objective
Create the smallest deterministic, read-only evidence catalog from existing RN-001 sources and Local Source Evidence Checkpoint 001. Do not create a new project, repository or directory tree.

## Input
- Existing RN-001 original GPT/Claude reports and additive addendum.
- Existing pinned participant evidence index 002.
- Existing lead reviews and source-checkpoint 001.
- References to Android backup and Git worktree metadata, not copies of private device contents.

## Minimal record
record_id, project_id, component_id, source_system, source_locator, revision_or_sha, source_type, observer, event_time, observation_time, recorded_time, claim, verification_class, result_status, limitations, amends_record_id.

## Behavior
- Preserve original bytes and original locations.
- Derive a catalog from source references; do not overwrite originals.
- Treat inaccessible originals as unavailable, not fabricated.
- Distinguish report COMPLETE from test PASS, historical from current, branch from branch, file presence from content.
- Detect duplicate source records and conflicting project identities.
- Emit a stable record list and issue list from identical inputs.
- Provide an evidence link for every derived claim.
- No automatic file moves, branch creation, deployment, or server integration.

## Acceptance gates
A. Rebuild catalog twice from identical inputs and compare output.
B. Reconstruct distinct Gate-01/main/auth/Shared Space Stage1/Stage2/viewport records.
C. Keep event #3 time distinct from unknown recovery time.
D. Mark unverified Drive uploaded-byte hash as UNVERIFIED.
E. Preserve the 403 Node11 denial as a delivery/authz event, not a failed RN-001 runtime test.
F. Missing source yields a visible error and never an invented fact.
G. No new directories or original file changes.

## Execution gate
Before writing executable code, inspect existing candidate locations and obtain Zed's approval of exact destination and file plan. Use local tests first, then independent CI if applicable.
