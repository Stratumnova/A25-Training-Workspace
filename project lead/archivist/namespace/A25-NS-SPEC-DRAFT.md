# A25 Universal Namespace Registry — DRAFT v0.1
FROM: LB-GPT01
FOR: GPT — A25 Project Lead
DATE: 2026-10-17
ORDER: A25-NS-O001
STATUS: PROPOSAL ONLY — not ratified or implemented

## Authority and separation
A25 is the approved permanent root. Proposed subsystem codes ARC, PS, WD, NS, TOOLS, HA, LORE, TRAIN remain pending lead/owner ratification. Registry identifiers are independent of GitHub repository paths, branch names, filenames, and display titles. No legacy name is rewritten. A registry ID conveys *which record*, not whether a service is trusted or code is executable.

## Proposed grammar
Canonical logical artifact ID: `A25:<SUBSYSTEM>:<KIND>:<LOCAL>`
Revision-qualified record ID: `A25:<SUBSYSTEM>:<KIND>:<LOCAL>@r<REV>`
- `SUBSYSTEM`: uppercase ASCII [A-Z][A-Z0-9]{1,15}, from approved namespace registry; reserve `CORE` and `NS` pending decision; proposed ARC, PS, WD, TOOLS, HA, LORE, TRAIN.
- `KIND`: registered uppercase ASCII [A-Z][A-Z0-9]{1,15}; initial proposal `DOC`, `SPEC`, `CODE`, `TEST`, `EVENT`, `CONCEPT`, `PERSONA`, `DATA`, `REPORT`, `ORDER`, `LEDGER`.
- `LOCAL`: uppercase ASCII letter followed by 3–12 uppercase alphanumeric characters, minted centrally from an atomic sequence or sufficiently collision-resistant random allocation; examples `N000001`, `K000001`. Do not derive uniqueness from human titles.
- `REV`: positive decimal integer without leading zeros, monotonic per logical artifact; immutable snapshots.
- Parser must reject unknown prefix/kind, mixed case, whitespace, path separators, Unicode confusables and malformed revisions. Alias/display names retain original Unicode and punctuation separately.
- Registry stores the immutable logical ID and distinct immutable revision IDs. The latest revision is a *pointer* subject to audit, not a mutable historical record.

## Uniqueness, ownership and allocation
Uniqueness key: full logical artifact ID globally within A25; unique revision key: logical ID plus revision. No reuse after retirement, cancellation, or rejection. Central transactional allocator with unique constraints and idempotency key; do not assign IDs offline without reserved allocation ranges. Registry must reject concurrent duplicate claims and preserve conflict events. Allocation and state changes record actor principal (if authenticated), assigned seat (if documented), approval evidence, UTC timestamp, source and rationale. A narrative name never grants write authority.

## Identity model — four independent fields
- `narrative_identity`: named persona or fictional node from a source.
- `assigned_ai_seat`: role assigned by authorized A25 governance.
- `authenticated_principal`: credential-validated actor, or null when unverified.
- `source_author`: credited author claim, with evidence and confidence.
Never infer one field from another. Credential presence does not prove an AI provider identity unless the authentication system establishes it.

## Source and relationship rules
Source pointer: `repository_url`, `source_ref`, `resolved_commit_sha`, `source_path`, optional `blob_sha`, and `source_sha256` only if actual bytes were hashed. A Git SHA-1 is not a SHA-256. Distinguish `original_source`, `derived_compression`, and `index_entry`. Relationship edges have `subject_id`, `predicate`, `object_id_or_source`, `evidence_pointer`, `confidence`, `verification_status`; proposed predicates: `derived_from`, `supersedes`, `references`, `inspired_by`, `implements_concept`, `possibly_related`. No auto-merge on matching labels.

## Aliases and collisions
Alias records contain exact `original_term`, `source_context`, `repo`, `revision`, `path`, `artifact_kind`, `technical_interpretation`, `evidence_pointer`, `confidence`, `verification_status`, `relationships`, `notes`. Aliases are many-to-many, non-unique, searchable, never authentication keys. A search returns disambiguated matches with provenance. Collisions require explicit resolution records; never silently select a winner. Preserve literal Gate-01, Phase P0, Batch 7, Key5, and Key 5 as aliases scoped by system.

## Privacy and publication
Classification: PUBLIC, TEST-SENSITIVE, TEAM-RESTRICTED, REAL-PRIVATE, UNKNOWN. UNKNOWN and REAL-PRIVATE denied by default. Classification is independent of access policy and authorized synthetic leak-test scope. Public registry projections expose only approved safe metadata; never publish private titles, raw secrets or unverified ZIP contents. Source archives remain authoritative.

## Status and lifecycle
Registry record states proposed: `PROPOSED -> REVIEWED -> APPROVED -> ACTIVE -> DEPRECATED -> RETIRED`, with `REJECTED` and `QUARANTINED` as explicit alternatives. A change creates a new revision and audit event, not historical rewriting. Migration progression is separately tracked in the migration ledger; `LEGACY-ARCHIVED` requires owner acceptance and verified source preservation. Failure must produce an explicit error and retained evidence.

## Open lead decisions
1. Ratify subsystem codes, reserved codes and kind vocabulary.
2. Choose allocator (central sequence vs random), expected offline mode and canonical delimiter grammar.
3. Define role authorized to approve namespace records and migrations.
4. Confirm whether revision suffix belongs in every human-readable citation or only immutable snapshot references.
5. Approve privacy-safe public projection fields and audit retention.
No code, migration, or ID assignment is authorized by this draft.
