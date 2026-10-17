# Terminology Crosswalk and Evidence Rules

FROM: GPT — A25 Project Lead
FOR: LB-GPT01 and reviewers
DATE: 2026-10-17
RE: Preserve Zed's terms without confusing conceptual artifacts and executable software

## Key rule
Keep `original_term` exactly as written in its source, including case, punctuation and project-specific spelling. Record `source_context`, `artifact_kind`, `technical_interpretation`, `evidence_pointer`, `confidence` and `verification_status` separately. A term can represent different things in different repositories.

## Example: Key 5 (owner's clarification, not source-code verification)
| Context | Original term | Owner-stated kind | Evidence still needed |
| --- | --- | --- | --- |
| Stratumnova original lore | Key 5 | Prompt/concept, **not code** | Exact source file and text |
| Pocket Server | Key 5 | Code according to owner | Exact implementation path, code inspection and execution/test evidence |

Never automatically unify records because they share a term. Create a relationship such as `inspired_by`, `implements_concept` or `possibly_related` only when grounded, with a source and certainty. Do not turn a concept into a tested feature through interpretation.

## Additional distinctions
- `narrative_identity`: persona or lore entity from a document.
- `assigned_ai_seat`: project role from authorized A25 assignment.
- `authenticated_principal`: credential-validated service identity; do not infer from labels.
- `source_author`: credited source author; provenance claim may be unverified.
- `original_source` versus `derived_compression` versus `index_entry`: maintain lineage and original bytes.
- `source_sha256`: byte digest only when actually computed; Git commit SHA is **not** a content SHA-256.
- `Watchdog`: integrity validator for specified protected surfaces, not a universal live auditor until separately integrated.

## Required crosswalk fields
`term_id, original_term, repo, revision, path, artifact_kind, technical_interpretation, evidence_pointer, verification_status, relationships, notes`.

Never store private file contents or private titles in this public crosswalk. Unsupported interpretation remains UNKNOWN.
