# CASE STUDY — Moving a Roundtable decision from discussion to implementation

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and builders
**DATE:** 16 October 2026; record creation clock time not independently verified
**RE:** W5 multi-state decision, provenance, and implementation handoff
**BASIS:** Zed's direct 16:01 MDT confirmation in GPT chat; Claude's 16:02 MDT message relayed by Zed; Claude's 15:42 and 15:52 reviews; earlier committed case-study correction

**Status:** DECISION APPROVED / IMPLEMENTATION NOT YET VERIFIED.
**Identifier:** Descriptive process case study, not a numbered A25-F record. Assigning another F number awaits an ID registry to avoid further collisions.

## Sequence: discussion to implementation

1. **Observed defect.** The RT-005 safety-stop incident was mistakenly recorded as F-002 even though legacy fork-sandbox evidence already owned that ID. Claude caught the collision; GPT verified the legacy record and added an immutable correction at F-004, preserving the erroneous original.
2. **Design question.** Strict W5 would repeatedly fail against this immutable historical collision. Zed asked whether W5 could flag multiple states. GPT proposed PASS / WARN / FAIL / SKIPPED, with verified corrections yielding WARN rather than FAIL.
3. **Independent review.** Claude agreed, adding mechanical requirements for correction records: duplicate ID, exact paths of both records, canonical record, and original error commit. Any missing field remains FAIL. Any FAIL fails CI; WARN-only passes; SKIPPED cannot count as complete.
4. **Human authority.** Zed's original words in Claude's chat, as Claude quoted them at 16:02 MDT: `recommends multi state but when is left to gpt and Claude as Zed has no input for this and that's ok`. Zed then confirmed directly in GPT chat at 16:01 MDT: `I did give Claude that approval so it can be markert as level 2 cleared.` The direct GPT-chat confirmation is observed here; the earlier Claude-chat quotation is human-relayed and independently attested by Zed. **Decision provenance: Level 2 cleared, Zed-approved.**
5. **Delegated sequencing.** GPT and Claude agree on WD-01A ID registry, WD-01B additive F-004 time correction, WD-01C two-sided baseline manifest, WD-02 W1–W6 including multi-state W5, WD-03 tests including the live collision expected WARN, WD-04 Claude review, WD-05 Actions integration.
6. **Execution handoff.** Claude notes that for WD-01C GPT must name the baseline commit; Zed then downloads that commit ZIP and supplies it to Claude for independent SHA-256 comparison. Do not declare the baseline accepted before the two sides match.

## Reusable discussion-to-implementation procedure

- Capture the actual observed problem and immutable evidence before proposing fixes.
- Separate proposals, independent technical review, human authorization, and delegated implementation choices.
- Preserve exact human decision words and their source; do not promote relayed approvals to direct observation without confirmation.
- Translate the approved design into bounded batches with objective completion checks, explicit dependencies, and an assigned independent reviewer.
- Maintain an append-only audit trail for mistakes and corrections. Verify GitHub writes by read-back.
- Only mark a batch implemented or verified after concrete code, tests, and evidence; agreement is not implementation.

## Current boundary

The W5 policy and batch order are approved. The registry, time correction, baseline comparison, Watchdog implementation, tests, independent final review, and CI evidence remain pending. This record does not claim those steps were completed.

## Relevant references

- `case-studies/A25-F-004-correction-rt005-safety-stop-id-2026-10-16.md`
- `case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md` (misnumbered original, preserved)
- `legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md` (prior ID owner)
