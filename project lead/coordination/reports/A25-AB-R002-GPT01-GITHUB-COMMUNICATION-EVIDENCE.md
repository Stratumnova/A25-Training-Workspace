# A25-AB-R002 — GPT–GitHub Communication Evidence

FROM: A25-AB-GPT01 — Archives Builder  
FOR: A25-AG-GPT01 — Archives Lead; Zed  
DATE: 2026-10-17 (project label; exact publication time not asserted)  
ORDER: A25-AB-O002 at c4e8ddfcdc9cbf6b6ae1c222763d8059b732a658  
SCOPE: AB-02, read-only historical GitHub communication audit  
EVIDENCE STATUS: VERIFIED fetched source text and this report's publication receipt only; historical operations separately classified  
DECISION: No adoption or technical certification; submit for Archives Lead review  
OWNER: Zed; Archives Lead supervises  
NEXT ACTION: Archives Lead independent review, then separately authorize AB-03  
BLOCKERS: Original provider tool logs, independent Drive bytes, full historical CI logs and MCP runtime not reproduced.

## 1. Source-access ledger

All below are in `Stratumnova/A25-Training-Workspace`. "Full" means the GitHub connector returned complete Markdown text in this AB-02 session; it does not independently verify assertions inside. For first group, explicit pinned authoring/receipt SHA was used; second group was fetched from existing `coord/a25-namespace-trial-001` branch HEAD, so the exact individual historical authoring SHA is UNKNOWN unless noted. Attribution follows document headers, not independently authenticated identity.

| Source (path relative to repository) | Ref | Access | Attribution / limit |
|---|---|---|---|
| `project lead/coordination/reports/A25-AB-R001-GPT01-ROUNDTABLE-SOURCE-INTAKE.md` | cb4ccc54cfe6db7c18a2de4072bb89df97273c22 | Full | Builder's prior report; Archives found 14 listed sources but prose incorrectly said 13 |
| `project lead/leadership/archives/ARC-REVIEW-2026-10-17-004-AB-R001-INTAKE-DISPOSITION.md` | 9347b2b3374bef0ce1546ddc4cedb02adf83f7ab | Full | Archives Lead accepts with discrepancy; no independent replay of all fetches |
| `project lead/leadership/archives/ARC-REVIEW-2026-10-17-003-ROUNDTABLE-FULL-EXTRACTION-COVERAGE-AND-GAPS.md` | b8f8c1068a63aecaae1c6ef1ceac492320af4170 | Full | Archives secondary gap map |
| `project lead/leadership/LEAD-TRAINING-NOTE-008-ROUNDTABLE-LIVE-WORKFLOW-OBSERVATIONS.md` | 627ae1198ae27bdde70086361da441f2bb6257be | Full | Roundtable Lead training; described workflow |
| `project lead/leadership/LEAD-STUDY-022-HANDOFF-EVIDENCE-LESSONS-2026-10-17.md` | 087dc1d3105bb716546788d90dd18dbd343b8436 | Full | Lead study, secondary synthesis |
| `project lead/leadership/roundtable/RT-TRAINING-2026-10-17-001-CONTEXT-AND-RECALL-INVENTORY.md` | d626ebde4ba83baa4de3406c4cbeb7619fc11e21 | Full | Roundtable Lead source inventory, not independent runtime |
| `project lead/leadership/roundtable/RT-HANDOFF-2026-10-17-002-EMERGENCY-SESSION-EXTRACTION.md` | f9a3fc912d15d1900b150b166cb56d2e371622df | Full | Roundtable Lead emergency handoff |
| `project lead/leadership/LEAD-DECISION-013-OFFICIAL-A25-POCKET-SERVER-ROUNDTABLE-BUILD.md` | 62961a8c4d681015de8dc0269fa4a34167c632c2 | Full | GPT Lead recording Zed ADOPTED branch authorization |
| `project lead/leadership/LEAD-REVIEW-014-CLAUDE-WRITER-R003-AND-REVIEWER-LAUNCH.md` | 779894152030ce3e8e7b43f55a708034fdc96354 | Full | Lead records Drive readback; hash reviewer-reported |
| `project lead/leadership/LEAD-REVIEW-015-CLAUDE02-R001-O006-DISPOSITION.md` | 699575f58c7c8bb776f516c7d731ae0a0935ea9e | Full | Lead adopts specific review findings, not runtime PASS |
| `project lead/leadership/archives/ARC-NOTE-2026-10-17-002-GITHUB-BLOCKED-WRITE-OWNER-REVIEW.md` | d584710cf01349cd3d93dd542500c78276b8d953 | Full | Archives Lead reports own observed safety stop and approved retry |
| `project lead/leadership/archives/ARC-REVIEW-2026-10-17-001-ROUNDTABLE-P0-PRESERVATION-RECEIPT.md` | b0e476e5f4927268738f19b0249769c75e8b1046 | Full | Successful preservation receipt; recovery not tested |
| `project lead/leadership-pool/POOL-2026-10-17-ARCHIVES-GITHUB-BLOCKED-WRITE-REVIEW-RULE.md` | 09ad9c54aae54f9998472a0844f5d7094d341867 | Full | Cross-lead policy notice, no automatic adoption |
| `project lead/leadership-pool/POOL-2026-10-17-ARCHIVES-SECURITY-SAFETY-BLOCK-AND-COMMUNICATION-EVIDENCE.md` | b351aadb2b8e50bcf8e43bb7a5fea0bfb5834e2b | Full | Security question, root cause UNKNOWN |
| `project lead/leadership/LEAD-DIRECTIVE-005-EXISTING-PATHS-FIRST.md` | coordination branch HEAD | Full | Zed organizational rule, no automatic Watchdog enforcement |
| `project lead/leadership/LEAD-DIRECTION-007-POCKET-MAIN-VIEW-RESTART-GATE.md` | coordination branch HEAD; pinned link 557f34065ada28876690acdac479e26248c281a6 in Review 009 | Full | Original main-first direction, later code destination changed by owner |
| `project lead/leadership/LEAD-REVIEW-009-CLAUDE-PM-R001-AND-GPT-LAUNCH.md` | coordination branch HEAD | Full | Lead notes Claude tree-navigation failure and pinned-link response |
| `project lead/leadership/LEAD-REVIEW-010-PM-GPT01-CLAUDE01-MAIN-VIEW.md` | coordination branch HEAD | Full | Lead comparison of GPT source inspection and Claude viewport |
| `project lead/coordination/orders/A25-PM-O003-GPT01-MAIN-READ-IMPLEMENTATION.md` | coordination branch HEAD; historical 979b99db5f3e27c646c719f822f5bb27ef2b5d9a | Full | Original contradictory implementation constraints |
| `project lead/coordination/orders/A25-PM-O004-GPT01-OFFICIAL-BRANCH-IMPLEMENT-SHARED-READ.md` | coordination branch HEAD | Full | Owner-authorized branch scope |
| `project lead/coordination/orders/A25-PM-O006-GPT01-CLAUDE02-REVIEW-CORRECTIONS.md` | coordination branch HEAD; order commit 4cf75a4b464973e15d11b3fd72e7f590478131bb | Full | Limited correction scope |
| `project lead/coordination/orders/A25-PM-O007-CLAUDE02-R004-INDEPENDENT-REVIEW.md` | coordination branch HEAD | Full | Review request only, not result |
| `project lead/coordination/reports/A25-PM-R002-GPT01.md` | coordination branch HEAD | Full | GPT builder BLOCKED report |
| `project lead/coordination/reports/A25-PM-R003-GPT01.md` | coordination branch HEAD; report commit 90b4b12e00e23dc0743e71939a5fc7ba0de7d241 | Full | GPT builder source commits and ZERO tests |
| `project lead/coordination/reports/A25-PM-R004-GPT01.md` | coordination branch HEAD; report commit bedb45073b700b9600c0f38924188f0d97e92ddd | Full | GPT builder corrected source and dependency/test blocker |
| `case-studies/A25-F-005-wd03-safety-stop-authorized-retry-2026-10-16.md` | coordination branch HEAD | Full | GPT-authored incident; exact quoted platform error |
| `case-studies/WD-05-github-actions-failures-and-recovery-2026-10-16.md` | coordination branch HEAD | Full | GPT-authored CI case, references original logs; logs not independently fetched here |
| `project lead/master archive/03-WATCHDOG-ACTIONS-HISTORY.md` | coordination branch HEAD | Full | GPT-authored historical Actions ledger; original run logs not independently fetched here |

Total: **28 source documents** fetched as full text. Historical SHA values given in report bodies are not automatically verified Git object IDs. GitHub branch HEAD is a moving reference; future verification should pin the actual revision. Original author/seat/principal are not interchangeable.

## 2. Chronological incident ledger

| Event / date precision | Operation and evidence | Failure, response, outcome | Classification |
|---|---|---|---|
| 2026-10-16, time UNKNOWN (WD-03) | GPT attempts `watchdog/test_fixtures.py` on `build/wd-02-watchdog-v0`; A25-F-005 | Exact reported error: `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` STOP, Zed reviews complete 1:1 payload, approves at recorded 18:07 (written year 2025 preserved as a discrepancy); same write retried once; commit `3952dfe3eeac32d0398ac55ea62af9c9f8672172`; source readback reports 11 functions, 5,491 chars, blob `308cc78cd03983eb744d15ee6ff07c4e173425af`. Tool logs not replayed here. | HISTORICAL CLAIM; ADOPTED approval; reported write/readback, not test PASS |
| 2026-10-16, after 18:33 MDT (WD-05) | GitHub Actions tests and actual-repo validator; WD-05 and master archive | Commits `44190693` import SyntaxError (0 tests), `f1547f2` 16/16 isolated PASS, `2c3172e`, `f108284`, `01c6a20` 15/16 regression, `8e8fd10a688ab1c74f531022339fab3cd6bf9167` 16/16 and actual repo 0 FAIL/3 WARN per archived run `105660203481`. This is reported historical CI, not independently replayed here. | HISTORICAL CLAIM; later correction does not erase red runs |
| 2026-10-17, time UNKNOWN (Claude01 navigation) | Claude attempts sibling GitHub tree discovery; Review 009 | Claude could open exact order URL but could not find Directive 006/Direction 007 through tree, nor read pockettest source; lead supplied direct pinned blob links. Viewport output is not independent source read. | HISTORICAL CLAIM; reported workaround |
| 2026-10-17, time UNKNOWN (GPT source inspection) | R001 as cited by Review 010, and R002 | GPT inspected hardened main `f0a11d51968ad598691333d32971dfb483489073` and `gate02/server.py` blob `b8bb1a524375ecafa2cb29ce802316e27b0c8743`; deny-all, no shared tool. | HISTORICAL CLAIM in original builder/lead records |
| 2026-10-17, time UNKNOWN (O003) | Lead orders code change without new branch and without editing protected main; O003/R002 | GPT builder reports no permissible edit destination, STOP with patch plan, no code committed or tests run. Not a GitHub API denial or provider safety block. | VERIFIED text of R002; historical blocker claim |
| 2026-10-17 20:02 MDT owner-supplied | Zed resolves branch destination; Decision 013, O004 | Owner ADOPTED official `Stratumnova/pockettest` branch `build/a25-pocket-server-roundtable`, from main `f0a11d5...`. Lead records successful GitHub create_branch response. New branch was owner-authorized exception, not unilateral workaround. | ADOPTED decision; historical tool receipt |
| 2026-10-17, time UNKNOWN (O004/R003) | GPT writes `gate02/server.py` and `gate02/test_shared_read.py` on official branch | Commits `040e89612e9878ff0a337a496cf57a50d13a6108`, `442529a32356c5fb557d908fcd20bace733f04d8`. `import mcp` raised `ModuleNotFoundError: No module named 'mcp'`; curl exit 6 `Could not resolve host: raw.githubusercontent.com`; unittest discovery ran 0 tests and exit 5. ZERO PASS. | HISTORICAL CLAIM from original builder report |
| 2026-10-17 20:36 MDT relay (Claude02 review) | Lead reads reviewer Drive report and issues O006; Review 015 | Claude02 reports 21 isolated tests (not SDK integration); lead ADOPTS F-1 weak symlink test, F-2 nonfunctional auth coverage, F-3 anonymous proxy exposure risk, F-4 remote identity gap. Code correctness and runtime remain UNKNOWN. | ADOPTED correction tasks; HISTORICAL CLAIM test count |
| 2026-10-17, time UNKNOWN (O006/R004) | GPT source/test correction on official branch | Commits `fbf3b519bc7322be9c09266c2973eb2420fb4228`, `fabedb661bb5161055534589c7517f7e0738139d`. `import mcp` still fails; pip attempt returns name-resolution failures, then `Could not find a version that satisfies the requirement mcp==1.26.0`. Network/index failure does not prove nonexistent package. SDK/ASGI tests UNEXECUTED. | HISTORICAL CLAIM source updates and blockers; UNKNOWN runtime |
| 2026-10-17, time UNKNOWN (O007) | Claude02 independent re-review requested at corrected commit | O007 original is an order, not reviewer disposition. Result not obtained in this batch. | UNKNOWN |
| 2026-10-17, time UNKNOWN (Archives blocked write) | Archives attempts preservation receipt `ARC-REVIEW-001`; ARC-NOTE-002 and POOL security note | Generic OpenAI safety-check block; no commit; exact body shown 1:1; Zed explicitly approves same Markdown retry, with .txt fallback if blocked; unchanged retry yields `b0e476e5f4927268738f19b0249769c75e8b1046`. .txt NOT attempted. Cause UNKNOWN; this is one observed case according to Archives Lead. | HISTORICAL CLAIM of observed incident; ADOPTED owner procedure |
| 2026-10-17, AB-01 (time UNKNOWN) | GPT builder fetched pinned sources via GitHub connector; R001 and ARC-REVIEW-004 | Initial raw URLs with unescaped spaces produced `INVALID_ARGUMENT: Error code: INVALID_ARGUMENT; Error: HTTPError: 400: GitHub Fetch URL must use HTTPS and a valid GitHub host.` Correct escaped GitHub blob URL succeeded. R001 table lists 14 sources but prose says 13; Archives accepted with count discrepancy. | VERIFIED R001 text, Archives disposition; historical fetch-log claim |
| 2026-10-17, AB-02 (this session) | GitHub connector fetches pinned and branch-ref Markdown source files | Source text retrieval succeeded for 28 documents; no source changes or execution. | VERIFIED in this session, bounded to document text |

## 3. Fetch/read modes and limits

- **Tree discovery** enumerates paths/blobs, not their content, runnable bytes, permissions or current state. Claude01's tree-navigation failure is not evidence that the underlying files did not exist.
- **File fetch** returns text for a specific path. A **commit-pinned blob URL** fixes a source revision and is preferable to moving branch HEAD; a branch-relative fetch is a current snapshot, not an original authoring timestamp.
- **Executable bytes:** GitHub source fetch is not equivalent to having local dependencies or a runnable SDK environment. R003's curl DNS failure and R004's pip DNS failure are independent from successful connector-based text fetch. No byte-exact execution test performed here.
- **Escaped paths:** AB-01 unescaped URL validation failure was corrected by percent-encoding spaces (`%20`) in GitHub blob URLs. It was a request/URL-shape error, not proof of GitHub outage or inaccessible source. This AB-02 session used valid escaped URLs.

## 4. Write/publish, permissions and receipts

Orders and reports use the existing coordination branch and existing folders. Code belongs to its authorized pockettest branch. O003 simultaneously barred protected-main changes and new branch creation; R002 properly marked BLOCKED rather than silently modifying code. Zed's 20:02 MDT decision created one official branch and O004 separately authorized implementation. The R003/R004 commit SHAs are evidence pointers to source changes, **not** test or deployment PASS. The GitHub publisher identity, GPT seat, source author and authenticated principal require separate verification; repository write access does not prove the later remote Pocket Server client identities.

## 5. Safety stops and attribution

WD-03 and Archives receipt are distinct historical cases. In both, project records describe STOP, exact human review, owner approval, one ordinary retry and subsequent commit. WD-03 preserves the inconsistent written approval year 2025 vs conversation date 2026. The Archives receipt was successful on the Markdown retry; fallback `.txt` was not used. Generic OpenAI safety-check response is **not** a GitHub API rejection. The source of enforcement and content-related cause remain UNKNOWN; future Security Lead may inspect authorized diagnostics. Zed's permission does not bypass a platform denial. If blocked again, STOP; do not mutate content or extension to evade controls.

## 6. Identity, authority and verification boundaries

Zed is owner and courier; GPT Roundtable Lead issues scoped orders; GPT builders author their reports and code; Claude01/Claude02 reviewers and Claude Writer are distinct roles. The Drive publisher may not be the reviewer or original author. GitHub account used for a commit is not necessarily the narrative seat or a Pocket Server authenticated principal. Screenshot chat labels, Drive readback, successful GitHub writes and isolated tests do not establish authenticated remote GPT/Claude access.

## 7. Verified, claimed and unresolved

**VERIFIED in AB-02:** complete textual retrieval of the 28 listed GitHub documents; AB-01 discrepancy documented in Archives review; text of O003/O004/O006/O007, builder reports and historical case studies. **ADOPTED historically:** Zed's official branch decision, scoped correction tasks, and blocked-write human-review procedure. **HISTORICAL CLAIM:** earlier provider block/approval/retry events, reported CI logs, source/test outcomes and Drive receipts. **SUPERSEDED:** O003's blocked code-edit destination by later owner-approved O004 branch authorization; earlier R003 source state by R004 corrections (historical reports unchanged). **UNKNOWN:** exact platform block cause; O007 result; SDK/ASGI execution, current CI enforcement, Android runtime, remote identity, original log completeness, independent Drive SHA verification.

Original Watchdog master archive lists workflow runs #20–54 with reported API conclusions and selective job-log checks; WD-05 lists separate earlier failures and a successful historical run. They are not a universal green status. This batch did not invoke GitHub Actions or independently download job logs.

## 8. AB-03 handoff queue — not executed

1. Claude01 original read-only report: Drive ID `1OQd690BbRMMaGEIyKyoPNxmNmsOyudDb`. Verify source navigation failure, viewport-vs-independent-read distinction, publication metadata and hash where feasible.
2. Claude Writer R003 handoff: Drive ID `1cro418zgfdk6o8YMhDfFZaZ6fyREE67o`, folder `10wmqATFDd4t6_QWoEudEwa_r0wtLBRmm`. Check original author/publisher, reported 2,446 bytes and SHA `003313ff9e3cc4bca4d89a188a8645b8d73e3cf5d57d3dfdc9d24d1deb22543c` independently.
3. Claude02 R001 independent review: Drive ID `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl`. Check 21 isolated tests vs SDK tests and exact F-1/F-2/F-3/F-4 findings; do not assume source hash independently verified.
4. Claude02 O007 result `A25-PM-R002-CLAUDE02.md`: locate original Drive ID, publisher, test evidence and disposition, if available. UNKNOWN until retrieved.
5. Claude Writer first publish: Drive ID `1YFD9IXNgwaN53cYiis3NHkFu-bgNZb-0`; independently compare bytes/hash and distinguish transport from live Pocket Server. RN-001 Claude report `15fzkYQlfThEsemntyGnoUqA5hewAkF38` and addendum `15XeF8U8oObFrw4ivMzsN_F0b7vYM65UA` are separate recall-network originals, not assumed Roundtable results.

No AB-03 Drive operations performed. Preserve originals and discrepancies. No code, branch, CI, terminal, phone or server operations performed for AB-02.
