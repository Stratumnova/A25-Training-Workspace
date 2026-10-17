# A25 Migration Ledger — DRAFT v0.1
FROM: LB-GPT01
FOR: GPT — A25 Project Lead
DATE: 2026-10-17
ORDER: A25-NS-O001
STATUS: PROPOSAL ONLY — no migrations executed

## Purpose
Append-only, evidence-linked account of each legacy source considered for A25. Registry names do not depend on GitHub paths; legacy originals remain intact. An entry is not proof of code functionality, ownership, consent or migration success.

## Proposed entry fields
- `entry_id`, `event_sequence`, `event_type`, `recorded_at_utc`, `previous_event_digest` (optional tamper-evident chaining, subject to lead decision).
- `source_repository_url`, `source_ref`, `resolved_commit_sha`, `source_path`, `source_kind` (`original_source`/`derived_compression`/`index_entry`), `source_blob_sha`, `source_sha256` (null unless actual byte hash calculated).
- `original_term` (exact spelling), `source_context`, `artifact_kind`, `technical_interpretation`, `evidence_pointer`, `confidence`, `verification_status`, `notes`.
- `proposed_canonical_id` (null until allocated), `allocated_canonical_id`, `proposed_revision`, `relationships` (typed, independently evidenced).
- `data_class`, `classification_evidence`, `access_policy_ref`, `synthetic_fixture_id`, `synthetic_verified`, `test_authorization_ref`, `allowed_surface`; do not publish sensitive source titles or contents in public projections.
- `narrative_identity`, `assigned_ai_seat`, `authenticated_principal`, `source_author` as separate nullable/attributed fields.
- `migration_state`, `state_change_evidence`, `verification_method`, `test_result_ref`, `operator`, `reviewer`, `owner_acceptance_ref`, `rollback_plan_ref`, `exception_code`.

## Migration states and gates
`DISCOVERED -> CLASSIFIED -> MAPPED -> PORTED -> VERIFIED -> ACCEPTED -> LEGACY-ARCHIVED`.
Each transition appends an event with evidence and authorized decision. `BLOCKED`, `EXCLUDED`, `FAILED`, and `QUARANTINED` are explicit outcomes, not silent skips. UNKNOWN classification blocks public mapping/publication; REAL-PRIVATE never enters public records. TEST-SENSITIVE requires verified synthetic provenance and scoped authorization for intentional exposure. TEAM-RESTRICTED requires explicit publication approval.

`PORTED` means a controlled copy/translation exists, not that the original was moved or deleted. `VERIFIED` requires recorded checks (hashes where possible, interface behavior where relevant). `ACCEPTED` requires explicit owner acceptance. `LEGACY-ARCHIVED` is archival status after acceptance, never deletion by implication.

## Rollback and reconciliation
Maintain immutable original source URL/ref/path and expected hash; record destination commit and generated artifact digest separately. On mismatch, stop, mark `FAILED` or `QUARANTINED`, record both revisions, and require human review. Rollback is a new compensating event and/or reverting destination commit; never rewrite earlier ledger entries or silently alter source archives. Reconciliation reports unresolved aliases, ID collisions, duplicate content, missing sources and divergent revisions.

## Validation plan (SYNTHETIC; not executed)
1. Same `Gate-01` alias in distinct systems resolves to separate IDs.
2. Key5 concept versus alleged Key5 executable implementation cannot be merged without evidence.
3. Source revision drift produces a blocked reconciliation event.
4. Missing classification defaults to UNKNOWN/quarantine.
5. TEST-SENSITIVE fixture denied to normal unauthorized retrieval; controlled leak-test exposure requires fixture authorization.
6. Duplicate allocation and cross-seat impersonation attempts fail closed.
7. An accepted migration retains a resolvable original and documented rollback path.

## Lead decisions required
Choose ledger storage and concurrency semantics, acceptable digest algorithms, approval authorities, migration-state exception vocabulary, and minimum verification/acceptance evidence. No real records were ingested or migrated under this order.
