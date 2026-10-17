# A25-NS-V001 — Lead Review of Builder Report R001
FROM: GPT — A25 Project Lead
FOR: LB-GPT01 / Zed
DATE: 2026-10-17
RE: Independent GitHub review of A25-NS-O001
BASIS: Four files independently fetched at commit 96175c13a2862566c15820db00fa884be91e3f3e
STATUS: DESIGN ACCEPTED FOR REFINEMENT; NO PRODUCTION RATIFICATION

## Verified
Read A25-NS-SPEC-DRAFT.md, A25-NS-MIGRATION-LEDGER-DRAFT.md, A25-NS-EXAMPLES.md, and A25-NS-R001-LB-GPT01.md from GitHub. All present, scope consistent with design-only order. Builder report names the three commit IDs and distinguishes synthetic examples from implementation. No executable tests were claimed. No claim of cryptographic AI-seat identity verification.

## Lead decisions
- Accept as draft grammar `A25:<SUBSYSTEM>:<KIND>:<LOCAL>@r<REV>`; logical ID excludes revision. Preserve exact historical aliases.
- Approve for next prototype design: proposed subsystem codes ARC, PS, WD, NS, TOOLS, HA, LORE, TRAIN, subject to collision checking and Zed's final ratification before production use.
- Keep artifact-kind vocabulary provisional; add `PROMPT`, `CONFIG`, `ASSET`, `BINARY`, `ARCHIVE` to candidate list and demonstrate why KIND cannot be inferred from title.
- Use centrally allocated sequential local IDs in first single-writer prototype; concurrent allocation and offline allocations remain unimplemented and must fail closed until tested. Do not claim global uniqueness beyond registry boundary.
- Immutable revision-qualified citations for audit evidence; logical ID permitted for navigational links only.
- Zed retains final authority for protected merges, public publication of restricted materials and legacy archival. Lead may approve synthetic prototypes and routine builder tasks within authorized scope. Builder may propose records but cannot self-ratify sensitive migrations.
- Keep UNKNOWN/REAL-PRIVATE denied in public projection. Public safe metadata requires explicit classification; avoid exposing private titles or paths.
- Digest rule: compute SHA-256 over exact bytes when available; do not treat Git SHA-1 as content SHA-256.
- Append-only ledger is a design requirement; choice of durable transactional backend remains OPEN.
- Scope and evidence are sufficient for next synthetic prototype order, not real migration.

## Findings to refine
- Kind-vocabulary collision: a conceptual protocol called 'Key5' must not automatically become CODE.
- Clarify when source file revisions versus artifact revisions change.
- Ensure source-verified owner claims are distinguished from actual implementation evidence.
- PDF exports remain derived artifacts with source and digest, not the canonical index.

## Next
Order A25-NS-O002 authorizes synthetic schema/validator only. No repo migration or main merge.
