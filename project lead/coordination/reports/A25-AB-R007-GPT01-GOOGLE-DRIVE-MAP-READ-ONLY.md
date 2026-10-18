# A25-AB-R007 — Google Drive Workspace Read-Only Moving-Location Map

FROM: A25-AB-GPT01, Archives Builder  
TO: A25-AG-GPT01, Archives Lead; Zed  
DATE: 2026-10-18 (live read snapshot during this session; exact request timestamp not logged)  
ORDER: A25-AB-O007 @ `bbc06e022cb94ef9771e26565be9f3d9b32fa4f7`  
BRANCH: `coord/a25-namespace-trial-001`  
STATUS: READ-ONLY INVENTORY; NOT A COMPLETION OR CONTENT-INTEGRITY CERTIFICATION  
NEXT: Archives Lead review; STOP.

## 1. Evidence basis and access ledger

**ADOPTED:** Zed authorized GPT and Gemini read-only crawls while Claude may organize files; no GPT/Gemini Drive writes. [Order](https://github.com/Stratumnova/A25-Training-Workspace/blob/bbc06e022cb94ef9771e26565be9f3d9b32fa4f7/project%20lead/coordination/orders/A25-AB-O007-GPT01-GOOGLE-DRIVE-MAP-READ-ONLY.md) and [ARC-DRIVE-MAP-011](https://github.com/Stratumnova/A25-Training-Workspace/blob/452ce8d284a639dd120d63a6fce96663e82694ef/project%20lead/leadership/archives/ARC-DRIVE-MAP-2026-10-18-011-READ-ONLY-MOVING-LOCATIONS.md) retrieved in full. Screenshot layout in ARC map is **REFERENCE**, not independently authoritative.

**VERIFIED:** connected Google Drive search returned root folder ID `18vX9GOSIVZ5NMwpjAWmxAh5b6C56cZS1`, exact title `A25 AI workshop/workspace ` (trailing space in returned title), parent `0ABdqcytRzikJUk9PVA`; created `2026-10-17T01:29:03.309Z`, modified `2026-10-17T04:02:00.048Z`. [Open root](https://drive.google.com/drive/folders/18vX9GOSIVZ5NMwpjAWmxAh5b6C56cZS1).

**VERIFIED direct content fetches:** root `README.md` ID `1rfhW06PDxgsfoTDAwOmfJ_jAhDrs8muB`; training `DRIVE-WORKFLOW-RULES-2026-10-16.md` ID `1CQUKlYRBbccekiQmElxKB2OeaDWZnYJi`; Claude Lead indexes v001 `1KqWQwc0nuIu1ZrLDhC6LrFcxiHnLeF7_`, v002 `1P5B7bgNxzRprCXonTBxaYm6DnHXFgDW0`; crawl note `1loDyEetLGoDG3MOsWczzgxpQiLAyptTf`; correction note `1NS5IegH3ouNg83qPFo87BNwOefRK_mbL`; connection test `14FsXI2Cll-yFkZUn8YfWf23mWtCdGWCY`. All seven readable as text. Search/list operations returned stable IDs, MIME, size, parent IDs and creation/modified timestamps for many additional files; their **content was not necessarily fetched**.

**VERIFIED direct metadata:** `A25-PM-R001-CLAUDE01.md` `1OQd690BbRMMaGEIyKyoPNxmNmsOyudDb`; Claude02 R001 `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl`; Claude02 R002 `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va`; Writer handoff `1cro418zgfdk6o8YMhDfFZaZ6fyREE67o`; root README. Metadata for all four named review/handoff items reports `created_time == modified_time` but **this does not prove unchanged bytes across a move**. Requested `md5Checksum,sha256Checksum` fields were not surfaced by connector response. **No content SHA-256 was independently computed in AB-07.**

**Access outcomes:** All explicitly fetched items opened. No actual permission-denied response in this batch. Empty folder listings are **VERIFIED no visible direct children in that query snapshot**, not proof of permanent emptiness, deletion or full access to every historical item. Each explicit folder-child search used `'<folder-id>' in parents and trashed = false`, `topn:100`; no `next_page_token` was returned in these responses. Counts are scoped to the returned visible results. The Drive may change after each read.

## 2. Current root snapshot — stable IDs

All following root items have parent `18vX9GOSIVZ5NMwpjAWmxAh5b6C56cZS1` **VERIFIED** via direct-child search; folders have MIME `application/vnd.google-apps.folder`.

| Item | Stable Drive ID | Direct children visible at snapshot | Type / interpretation |
|---|---|---:|---|
| `A25_zeds-gpt/` | `1ZGnliml_E45aZn_sfOTy5zCtCgv-gl-x` | 0 | GPT-reserved space by README; no visible files |
| `claude-originals/` | `10wmqATFDd4t6_QWoEudEwa_r0wtLBRmm` | 12 | 8 subfolders + 4 CT files currently direct |
| `manifests/` | `1OeqwSIQQ0pPkL1iwfr7SBIQKLs-OSsPn` | 0 | Planned hash manifests; none visible |
| `mirror/` | `1mom49KXevkbxAQOw9k3-WUsY2JNCkHWi` | 0 | Planned pinned GitHub copies; none visible |
| `reports/` | `1KrGiR7W2gbZFJf_zT96zz0O9kD9tIecB` | 0 | Planned comparison reports; none visible |
| `training/` | `1HfqxtUxdXJCTwaNhTYpifzXB3Ot0DI66` | 2 | Original training records |
| `zed-inputs/` | `1Pqb0Iz05p6sbM8js8Op-e-PkrNhFAAtr` | 1 | GPT-authored/Claude-carried source, labeled |
| `README.md` | `1rfhW06PDxgsfoTDAwOmfJ_jAhDrs8muB` | — | `text/markdown`, 1,922 bytes; root instructions |
| `A25-CLAUDE-DRIVE-CONNECTION-TEST.txt` | `14FsXI2Cll-yFkZUn8YfWf23mWtCdGWCY` | — | `text/plain`, 356 bytes; test, expressly non-authoritative |

**Root snapshot totals:** 7 folders + 2 files. **VERIFIED** matches ARC screenshot **names**, now with IDs; screenshot time and exact path comparison not independently timestamp-aligned.

## 3. Current claude-originals nested map — stable IDs and visible contents

All eight subfolders below have direct parent `10wmqATFDd4t6_QWoEudEwa_r0wtLBRmm`, folder MIME, and current location **VERIFIED** by child search. The current direct root also holds CT-001 `1g7RUPwpY5KSE6W3-yeIH6PKK_Ctz4jam` (2,390 bytes), CT-004 .txt `1c6fRjSHyjjEb2x01YbtkcX6ygmCYPQJW` (114), CT-004 .md `1ZXyd4yABS2E9Q8-dZirY_7Mk1ENzqAHc` (1,047), CT-006 `1rOoPvQBr-8U4J-P96fCKcQ6B0iBTGxa9` (1,622). Their content not independently opened in AB-07.

| Subfolder | ID | Visible files | Stable IDs / names |
|---|---|---:|---|
| `writer-records/` | `1gbFlRPolQNSQbgtfjRItFNssyU2R_ocQ` | 2 | `1cro418zgfdk6o8YMhDfFZaZ6fyREE67o` O005 Claude technical handoff (2,446 B); `1YFD9IXNgwaN53cYiis3NHkFu-bgNZb-0` CW initialization (5,377 B) |
| `checkpoints-and-specs/` | `14Feadlwhmg84h2MUSWPyJWG_Q1sk97RD` | 2 | `1f-k2TTuBm3hPGI0JFwZsiO50Ov02e1N-` Claude checkpoint (3,677 B); `1c3VHjisLlTg6czDrPqwKQIImhkJvNrlA` PS requirements (3,706 B) |
| `channel-tests/` | `1gtZsomt83vKhOklvxBGhacREU7ewLgoc` | 0 | Empty in this snapshot; CT files still directly under `claude-originals` |
| `recall-network/` | `1161jpWzCiHhzhmOVcUE6Bj0JEF2gNETk` | 5 | `1R0yqCbeB46zKi0XF3Ky5vIvS7xuKzyw0` PS-CR R001 (20,460 B); `15fzkYQlfThEsemntyGnoUqA5hewAkF38` recall REPORT (14,674 B); `15XeF8U8oObFrw4ivMzsN_F0b7vYM65UA` ADDENDUM (3,179 B); `1ZdhmukNEcsDFgT7V0YVGQTmHObwoVTpl` RN001 fresh 001 (18,160 B); `1HmkKQyRLnFE3ji2cuwpAN-CLh5_81Pvd` RN001 fresh 002 (19,609 B) |
| `watchdog-reviews/` | `1eeO1CN1E6FA8RbH8IMJ3HdoFIT5guxQl` | 6 | WD-26 `1gwfRcIvDetmxws0Idhjln81AUJgmtyeR`; WD-27 `1kLKo2v_wXOoW2jUOeVsvg930GgMiraWv`; WD-28 `17UDtBiZ6-9rf1mAi-fhtllsPOkkIEIQK`; WD-29 `1aJd5YXVpwIIU5nCj4KACqmU5fbAzNMVk`; WD-30 `1j66ZGPRPSLosJ1xTKysGyjW0ZoXmRGOD`; WD-35 `1xuiznve5b4x1FOk5X-EpUzqxSoVwjNYx` |
| `roundtable-reviews/` | `1sPxV8BmL5tA1OSAhOHuVUhUaxYzLzSrf` | 3 | `1OQd690BbRMMaGEIyKyoPNxmNmsOyudDb` Claude01 R001 (8,917 B); `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl` Claude02 R001 (26,577 B); `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va` Claude02 R002 (23,663 B) |
| `claude-pool/` | `1tRhloX0OEgvRKucPhShZK_jMtaH-MfaI` | 0 | Claude leadership pool, no visible files |
| `claude-lead/` | `1rqlZjlD-thxNDkVGuZ5kRo6OfRKnHwNz` | 6 | `1YY9kHporEkU0jSlVQjV82oUZhxpCmh3y` note 001; `1NS5IegH3ouNg83qPFo87BNwOefRK_mbL` correction 002; `190ZOaDIWtRFCUB8SrQA7AXeCIgkxHzlc` note 003; `1loDyEetLGoDG3MOsWczzgxpQiLAyptTf` note 004; `1KqWQwc0nuIu1ZrLDhC6LrFcxiHnLeF7_` index v001; `1P5B7bgNxzRprCXonTBxaYm6DnHXFgDW0` index v002 |

**Other direct-child evidence:** `training/` contains `1CQUKlYRBbccekiQmElxKB2OeaDWZnYJi` DRIVE-WORKFLOW-RULES (4,510 B) and `1mXAQVOWUwNmvkT_b9aanl39_OWfkZkth` CLAUDE-REVIEW-LOG (3,917 B). `zed-inputs/` contains `1EuSYWi5I2v3od70h4TWgaA0T2KTmk91g` `GPT-AUTHORED_carried-by-Claude_A25-CP-2026-10-16-2124-gpt.md` (7,239 B). Filename explicitly distinguishes original author from courier; exact byte equivalence to any GitHub copy **UNKNOWN**.

## 4. README, plans, precedent and contradictions

**VERIFIED content, not proof of execution:** Root README dated 2026-10-16 19:57 MDT identifies Claude as Drive custodian and quotes Zed's 19:53 approval. It defines `mirror/<github-commit>/` as byte-exact GitHub copies, `manifests/` as SHA-256 records, `claude-originals/` as source reviews, `reports/` as comparison records, and `A25_zeds-gpt/` as GPT's space. It says Claude writes everywhere else, GPT only in its own folder, both may read all, no automatic overwrites, and original bytes/hash readback are required. **Crucial:** README explicitly states these are **conventions, not enforced Google account identity separation**.

**VERIFIED content:** Training `DRIVE-WORKFLOW-RULES-2026-10-16.md` (ID `1CQUKlYRBbccekiQmElxKB2OeaDWZnYJi`) adds `zed-inputs` and `training`, says Drive is evidence/backup not authoritative code, mandates append-only and **never edit, move or delete**, raw bytes, digest readback, and separates GPT authorship from Claude courier. Its earlier no-move convention conflicts with the later **owner-adopted O007 allowance that Claude may organize within the workspace**. Preserve both; **ADOPTED current O007 governs this builder's read-only task**, but whether Claude was separately authorized to move every historical item is **UNKNOWN**. No retroactive rewrite of original rules.

**VERIFIED Claude Lead notes:** `README-CL-INDEX-v002` explicitly **SUPERSEDES v001 as an index**, while retaining both files; it is navigation, not source proof. `CL-NOTE-002` corrects note 001's false “R002 missing” conclusion: initial listing stopped at a page token. **AB-07 directly verified R002 by stable ID `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va`**, parent `roundtable-reviews`, 23,663 bytes, created/modified `2026-10-18T02:52:08.559Z`. Claude Lead note 002 had reported R002 in `claude-originals` root at its earlier observation; both can be true at different times. Do not conflate missing from page one with deletion.

**VERIFIED note content / HISTORICAL CLAIM of earlier work:** `CL-NOTE-004` says Claude Lead crawled a 257-file ZIP, found Drive rules, created `claude-lead` and `claude-pool` without moving prior files, and changed index/note descriptions without content edits. That is Claude's own historical report, **not** AB-07 independently verified ZIP traversal or description-change audit. It reports `mirror`, `manifests`, `reports`, `A25_zeds-gpt` empty, consistent with current child searches.

## 5. Observed versus planned moves — location pairs and content boundary

| Item / stable ID | Earlier location evidence | Current location verified by ID | Classification |
|---|---|---|---|
| Claude02 R002 `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va` | Claude Lead `CL-NOTE-002` reports direct parent `claude-originals` ID `10wmqATFDd4t6_QWoEudEwa_r0wtLBRmm` at earlier read; AB-03 earlier connector also reported parent there | `claude-originals/roundtable-reviews` ID `1sPxV8BmL5tA1OSAhOHuVUhUaxYzLzSrf` | **VERIFIED current**, earlier original reported/AB-03 read; **strong location-change evidence**, exact mover/time and raw content equality UNKNOWN |
| Claude02 R001 `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl` | AB-03 connector reported `claude-originals` root | `roundtable-reviews` same ID above | **VERIFIED current**, earlier archived retrieval; exact move event and content parity UNKNOWN |
| Claude01 R001 `1OQd690BbRMMaGEIyKyoPNxmNmsOyudDb` | AB-03 connector reported `claude-originals` root | `roundtable-reviews` | **VERIFIED current**, no direct move log |
| Writer O005 `1cro418zgfdk6o8YMhDfFZaZ6fyREE67o` | AB-03 connector reported `claude-originals` root | `writer-records` ID `1gbFlRPolQNSQbgtfjRItFNssyU2R_ocQ` | **VERIFIED current**, content parity UNKNOWN |
| Recall REPORT `15fzkYQlfThEsemntyGnoUqA5hewAkF38` and ADDENDUM `15XeF8U8oObFrw4ivMzsN_F0b7vYM65UA` | AB-03 connector reported `claude-originals` root | `recall-network` ID `1161jpWzCiHhzhmOVcUE6Bj0JEF2gNETk` | **VERIFIED current**, raw content equality UNKNOWN |
| `README-CL-INDEX-v001` `1KqWQwc0nuIu1ZrLDhC6LrFcxiHnLeF7_` | Earlier index v001 content remains | Same `claude-lead` folder as v002 | **SUPERSEDED index only**, not a move or deletion |
| `channel-tests/` | Intended classification suggested by name | 0 direct children; CT files remain in `claude-originals` root | **UNKNOWN** whether move planned/pending; no evidence of completion |
| `mirror/`, `manifests/`, `reports/` | README describes intended copies/manifests/reports | 0 visible direct children each | **PROPOSED layout / VERIFIED current empty listing**, not proof earlier items deleted |

**No original Drive move-event log, mover identity, or before/after byte hash was retrieved.** Therefore current parent changes are not content changes, and unchanged `modifiedTime` alone is not byte-exact proof. Avoid claiming Claude completed all reorganization or that any item was deleted.

## 6. Canonical originals, mirrors, reports and training

**VERIFIED by explicit text:** README says `claude-originals` stores Claude-authored original reviews and reports; original Claude02 R001/R002 and Claude01 R001 stable IDs are now nested within it. `mirror` is intended for copies pinned to GitHub commits, but **no mirror object was observed**. `manifests` and `reports` are intended integrity/comparison outputs, currently no visible direct children. `training` contains named Drive rules and Claude review log. `zed-inputs` contains a file whose name explicitly marks GPT authorship and Claude courier. CT-004/006 files are channel tests by filename, not certified canonical sources. Claude Lead notes/indexes are leadership navigation/claims; their own text cautions against treating them as original technical proof.

**UNKNOWN:** byte-exact equivalence of any Drive file to a GitHub file; author authentication by Google account (README says same connector account); comprehensive archive completeness; future location after Claude moves; presence of inaccessible or unindexed items outside the root subtree.

## 7. Gemini second crawler — comparison protocol, no fabricated findings

**ADOPTED:** Zed authorized Gemini as a second **read-only** crawler. **UNKNOWN:** no Gemini-specific crawl output, stable-ID inventory, error log or timestamp was supplied in this AB-07 turn. **Do not claim Gemini has inspected anything.**

For Zed courier: send Gemini's exact observation timestamp/timezone, folder/file IDs, parent IDs, name, MIME, size, modified time, page tokens/page counts, any directly fetched original text and independently computed digest with method. Label owner-relayed Gemini results **REFERENCE** until AB-GPT01 independently checks the same IDs through Drive. Compare by stable ID, not pathname; a different parent observed at different times may be a move, not contradiction. If name/size/modifiedTime differ, record both observations, then check revision history and bytes before asserting content alteration. If either crawler sees a permission error or partial page, mark **UNKNOWN** and preserve exact error. Escalate unresolved GPT/Claude/Gemini discrepancies to Archives Lead, not silent resolution.

## 8. Blockers and next read-only verification

- No direct permission-denied errors in selected searches/fetches; permissions of all workspace descendants **not exhaustively audited**.
- No original move logs or digest comparisons. Do not equate unchanged modified timestamps with unchanged contents.
- Folder queries showed no next-page token; unlike Claude Lead's earlier partial listing, these specific queries appear complete **for their response snapshot**, not for future or hidden items.
- Some file content not read (WD review bodies, CT records, other Claude notes, large recall records); listed metadata only. Source text for the seven explicit documents is available; no claim of comprehensive content inspection.
- The root README's append-only/no-move convention and O007's later authorized Claude organization differ; document as evolving authority, not evidence of misconduct.
- Recommended next check: after Claude declares an organization checkpoint, **read-only** re-list root and all nested folders with pagination, query key stable IDs directly, record timestamps/parents/size/modifiedTime and compare against this ledger; only then, with authorized raw downloads/revision reads, calculate and compare SHA-256 for selected moved originals. Obtain Claude's explicit source/destination move log if it exists, and separately compare any Gemini report by ID.

**STOP:** No Drive modifications, moves, renames, deletes, permission changes, branches, CI, phone, server, tunnel or deployment. Only this one GitHub coordination report may be created.
