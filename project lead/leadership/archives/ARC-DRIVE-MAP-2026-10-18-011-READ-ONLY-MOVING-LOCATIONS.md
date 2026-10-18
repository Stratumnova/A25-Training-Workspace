# ARC Drive Map 011 — Moving-location reference and read-only crawler boundary

FROM: A25-AG-GPT01 — Archives Lead
DATE: 2026-10-18
STATUS: REFERENCE MAP / OWNER-ADOPTED READ-ONLY ACCESS RULE; NOT A CANONICAL INVENTORY
TO: Archives Builder, Roundtable Lead, Claude Drive organizer, Gemini second crawler

## Owner direction (ADOPTED)
Zed authorizes read-only examination of the Google Drive A25 workspace and Gemini as a second read-only crawler. Claude is organizing the Drive based on the Archives/GitHub reference architecture. Folder/file locations may shift **within the same workspace area** as that organization proceeds. Crawlers must not move, rename, edit, delete, duplicate or otherwise organize Drive content. There is no expectation that source contents change merely because paths change.

## Observed Drive map (REFERENCE, owner screenshots; not live verified)
Drive > My Drive > `A25 AI workshop/workspace`:
- `A25_zeds-gpt/`
- `claude-originals/`
- `manifests/`
- `mirror/`
- `reports/`
- `training/`
- `zed-inputs/`
- `A25-CLAUDE-DRIVE-CONNECTION-TEST.txt`
- `README.md`

These names/locations are a screenshot snapshot, **not** a durable path contract. Google Drive's `Computers` tab screenshot says no folders syncing with Drive; this does not establish that My Drive or the workspace is empty or that syncing is impossible.

## Crawler protocol (PROPOSED operating details; subject to lead review)
1. Both Claude and Gemini may read/search/list original Drive items without modifying them; use original file IDs, title, MIME type, parent IDs, timestamps and exact retrieved content when available.
2. Record **observed-at time**, **crawler identity**, **stable Drive file ID**, **observed parent/path**, **content checksum if directly verified**, and **access outcome**. Treat paths as mutable; IDs and verified hashes are more useful for matching items after moves.
3. Separate **VERIFIED** (direct Drive retrieval) from **REFERENCE** (screenshots, Gemini copy/paste), **HISTORICAL CLAIM** (Claude prior progress), and **UNKNOWN** (moves not established). Gemini's descriptions do not become independent verification until original sources can be checked.
4. On a changed path, attempt read-only ID lookup and record both old and new observed paths; do not assume missing means deleted.
5. Preserve Claude's in-progress organization: no cleanup, repairs, automated folder creation, copy/move, permission edits or deletions by Archives/Gemini. A later owner/lead order is needed for any active restructuring.
6. Send a source ledger and unresolved location list to Archives; Roundtable tracks interrupted work and handoffs. No claim of Claude task completion without a final evidence-backed report.

## Open questions
- Which original file IDs currently map to the screenshot folders?
- Which folder moves were actually committed by Claude before its usage limit?
- Does Claude have a written organization plan or manifest with source/destination IDs?
- Which reports are canonical, mirrors or preserved originals?

## Sources
- Owner screenshots in Archives conversation (2026-10-18), not independently fetched from Drive.
- AB-03: https://github.com/Stratumnova/A25-Training-Workspace/blob/d40dfdebd165689c93984bd27b4341702721ae61/project%20lead/coordination/reports/A25-AB-R003-GPT01-CLAUDE-DRIVE-COMMUNICATION-EVIDENCE.md
- AB-06: https://github.com/Stratumnova/A25-Training-Workspace/blob/f0747c4643145125ca87f6b5ce2678197620d09f/project%20lead/coordination/reports/A25-AB-R006-GPT01-POCKET-SERVER-VERSIONS-REVIEWS.md
