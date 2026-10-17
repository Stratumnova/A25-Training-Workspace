# A25 Root Namespace and Legacy Migration Decision

FROM: GPT — A25 Project Lead
FOR: Zed, LB-GPT01, Claude
DATE: 2026-10-17 23:39 MDT
RE: A25 root namespace and controlled Stratumnova migration
BASIS: Zed's explicit decision, 2026-10-17 23:39 MDT

## Approved
- `A25` is the permanent root namespace for the new working system.
- Stratumnova is the legacy source system; its repositories are inputs to controlled A25 migration.
- New working artifacts receive consistent A25 names across projects; original names are retained as searchable historical aliases.
- The destination is an organized A25 working folder/repository structure with code, documentation, tests and a future maintenance bot supporting Roundtable builds.
- Legacy Stratumnova material is archived for later reference after verified migration, not destroyed or overwritten.

## Proposed subsystem prefixes (not yet individually ratified)
`A25-ARC` Archivist; `A25-PS` Pocket Server; `A25-WD` Watchdog; `A25-NS` namespace registry; `A25-TOOLS` tools/Build by Coin; `A25-HA` HalfAwake; `A25-LORE` lore/concepts; `A25-TRAIN` training/governance.

## Namespace design requirements
- Globally unique canonical IDs within A25; no reused full identifier.
- Include system/subsystem, artifact kind, local ID and revision in registry records; human-readable canonical forms should be stable.
- Keep historical aliases with source context and provenance; aliases must never be assumed globally unique.
- Disambiguate Gate-01, Phase P0, Batch 7, Key5 and similarly overloaded terms by owning system and artifact kind.
- Registry records carry owner/authority, status, source revision/path, relationships, and verification evidence.
- Canonical identifier assignment and changes are auditable; do not retroactively rewrite historical records.
- A narrative or prompt concept is not executable code without separate implementation evidence.
- Public metadata and restricted test content must follow `TEST-DATA-AND-PRIVACY-POLICY.md`.
- Maintenance bot is a planned component, not an already deployed service; Watchdog integration is not yet demonstrated.

## Migration state progression (proposal)
`DISCOVERED -> CLASSIFIED -> MAPPED -> PORTED -> VERIFIED -> ACCEPTED -> LEGACY-ARCHIVED`.
Failures or exclusions remain explicit; archive originals only when owner-approved completion criteria are met. Avoid moving/copying protected or private contents into public A25 without authorization.

## Immediate work
Before assigning new build IDs or migrating code, create an A25 namespace registry specification and migration ledger design. Then use a small representative cross-repository pilot (e.g., the two distinct Key5 artifacts) to test namespace collisions, aliases and code-versus-prompt evidence. Deep mapping proceeds incrementally with source-linked README, file maps and later PDF snapshots. Do not merge to main without Zed's approval.

## Status
Owner root decision APPROVED. Subsystem prefix proposals and implementation details PENDING REVIEW. No original repository changed by this document.
