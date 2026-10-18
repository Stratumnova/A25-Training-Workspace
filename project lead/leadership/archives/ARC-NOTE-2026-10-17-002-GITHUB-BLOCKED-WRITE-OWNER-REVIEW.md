# ARC-NOTE-2026-10-17-002 — GitHub Blocked-Write Owner Review Procedure
FROM: A25-AG-GPT01 — Archives Lead
FOR: Zed; Archives Lead; Roundtable Lead; future A25 leaders and builders
DATE: 2026-10-17 (project record date)
SCOPE: Shared leadership learning / proposed workflow for blocked GitHub document uploads
STATUS: ADOPTED — Zed's instruction; platform safety controls remain authoritative
SOURCE: Zed direct instruction in Archives Lead chat; observed ARC-REVIEW-2026-10-17-001 upload sequence
OWNER: Zed
NEXT ACTION: Cross-lead notification through leadership pool; leaders apply to authorized documentation submissions
BLOCKERS: Exact reason for first safety block UNKNOWN

## Owner-directed procedure
When a GitHub file upload is blocked:
1. STOP that upload action and report the exact failure; do not claim a commit.
2. Return the complete proposed file **1:1**, without silent edits, to Zed in the current session, including intended repository, branch, path, commit message and block status. Zed reviews the exact text.
3. Do not retry until Zed explicitly approves that proposed upload.
4. After approval, attempt the same authorized upload again and verify the returned commit SHA and destination. If the Markdown attempt is blocked again, report the block to Zed; with Zed's approval, a `.txt` alternative may be attempted while preserving the body text and documenting the changed extension.
5. If a safety control continues to block the action, STOP and report it; owner approval is not permission to evade or override platform safety checks. Never claim success without an actual commit and readback when feasible.

## Observed case (limited evidence)
- First attempt to create `project lead/leadership/archives/ARC-REVIEW-2026-10-17-001-ROUNDTABLE-P0-PRESERVATION-RECEIPT.md` was blocked by a generic safety response; no commit returned.
- Archives Lead presented the original complete body 1:1 to Zed.
- Zed explicitly approved retry, with `.txt` fallback if the Markdown retry failed.
- The unchanged Markdown retry returned commit `b0e476e5f4927268738f19b0249769c75e8b1046`; `.txt` fallback was not needed.
- This is ONE directly observed blocked-then-successful retry in this Archives session. Zed reports that similar prior cases also passed on second attempt, but the broader success rate and root cause have not been independently audited. A successful retry does not establish why the first attempt was blocked.

## Scope and preservation
This is a leadership workflow and training note, not a technical diagnosis or guarantee that retry will work. Preserve original failed-action reports, owner approval and resulting commit as separate evidence. Leaders should pass this guidance to builders through authorized orders; do not modify existing historical reports to retrofit this procedure.
