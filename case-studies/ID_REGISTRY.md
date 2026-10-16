# A25 Case Study ID Registry — WD-01A

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and builders
**DATE:** 16 October 2026, after Zed's 16:10 MDT message; exact write time unknown
**RE:** Append-only case-study identifier registry, initial known entries
**BASIS:** GitHub read-back of named legacy/current files; Claude-attested F-003 reservation

**Status:** WD-01A initial registry, pending independent Claude review and full repository inventory. This list is not yet certified exhaustive. Append new entries; do not silently rewrite historical assignments.

| ID | Status | Canonical file / reservation | Evidence |
| --- | --- | --- | --- |
| A25-F-001 | Assigned (legacy) | `legacy/pockettest/a25-training/case-studies/A25-F-001-session-availability.md` | GitHub read-back; front matter `id: A25-F-001` |
| A25-F-001-CORR-001 | Assigned correction | `case-studies/A25-F-001-correction-001-completed-work-lost-report.md` | GitHub read-back; front matter |
| A25-F-002 | Assigned (legacy; original owner) | `legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md` | GitHub read-back; front matter `id: A25-F-002` |
| A25-F-002 (collision) | Historical erroneous use; superseded as an ID by F-004 correction | `case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md` | GitHub read-back; original remains immutable |
| A25-F-003 | **Reserved, not yet verified as archived** | Claude's Block 1 rollback case study, path pending | Claude-attested at 15:40 MDT |
| A25-F-004 | Assigned correction and canonical identifier for RT-005 safety-stop incident | `case-studies/A25-F-004-correction-rt005-safety-stop-id-2026-10-16.md` | GitHub read-back; corrects misnumbered F-002 |

## Unnumbered process records

- `case-studies/PROCESS-2026-10-16-w5-discussion-to-implementation.md` — W5 approval-to-implementation process
- `case-studies/PROCESS-2026-10-16-w5-quote-attribution-correction.md` — additive correction of quotation and attribution

## Allocation and W5 rules

- Before assigning an ID, inspect this registry **and** legacy/active file identifiers; registry absence does not prove an ID is free.
- Reserve an ID explicitly before creating a new numbered case study.
- Preserve the original files, including mistakes. Use additive corrections and exact paths/commits for conflict resolution.
- W5 should mechanically validate correction references before treating a collision as WARN. A mere statement of correction is insufficient.
- A registry or manifest coverage check cannot be declared PASS until the full repository inventory is checked.

## Follow-up

Claude independently checks this registry against the baseline ZIP and identifies missing assigned IDs before WD-01A is considered complete. WD-01B then adds the F-004 time correction; WD-01C establishes the two-sided baseline.
