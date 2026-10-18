# A25-AB-R001 — Roundtable Original-Source Intake

FROM: A25-AB-GPT01 (Archives Builder)  
FOR: A25-AG-GPT01 (Archives Lead), Zed  
DATE: 2026-10-17 (owner-local project date; exact report publication time not asserted)  
SCOPE: AB-01 read-only source intake; no runtime testing  
EVIDENCE STATUS: VERIFIED source text retrieval only; underlying historical actions separately classified  
DECISION: Findings submitted for Archives Lead review; no new adoption  
NEXT ACTION: Archives Lead independently review, authorize AB-02 if appropriate  
OWNER: Zed; Archives Lead supervises this report  
BLOCKERS: Independent runtime/CI and Drive byte parity not established

## 1. Source-access ledger

GitHub connector fetched the following exact paths at pinned commit URLs. All 13 returned document text (not merely a tree listing); the connector's returned text was available for analysis. Attribution follows document FROM/recorder fields and is not cryptographic proof of authorship.

| # | Exact path | Pinned commit | Access / attribution limit |
|---|---|---|---|
| 1 | `project lead/leadership/roundtable/RT-TRAINING-2026-10-17-001-CONTEXT-AND-RECALL-INVENTORY.md` | `d626ebde4ba83baa4de3406c4cbeb7619fc11e21` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 2 | `project lead/leadership/roundtable/RT-HANDOFF-2026-10-17-002-EMERGENCY-SESSION-EXTRACTION.md` | `f9a3fc912d15d1900b150b166cb56d2e371622df` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 3 | `project lead/leadership/archives/ARC-REVIEW-2026-10-17-003-ROUNDTABLE-FULL-EXTRACTION-COVERAGE-AND-GAPS.md` | `b8f8c1068a63aecaae1c6ef1ceac492320af4170` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 4 | `project lead/leadership/LEAD-TRAINING-NOTE-008-ROUNDTABLE-LIVE-WORKFLOW-OBSERVATIONS.md` | `627ae1198ae27bdde70086361da441f2bb6257be` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 5 | `project lead/leadership/LEAD-TRAINING-NOTE-011-DUAL-PROJECT-REFERENCE-EVIDENCE.md` | `cb6b29ac80579e9c060972fa6e18588fb575d3fd` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 6 | `project lead/leadership/LEAD-TRAINING-NOTE-012-CLAUDE-WRITER-FIRST-PUBLISH-VERIFICATION.md` | `587ad3bfbf6fdf28f568e6f848328975ec36079e` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 7 | `project lead/leadership/LEAD-STUDY-022-HANDOFF-EVIDENCE-LESSONS-2026-10-17.md` | `087dc1d3105bb716546788d90dd18dbd343b8436` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 8 | `project lead/leadership/LEAD-HANDOFF-021-ROUNDTABLE-ARCHIVES-SESSION-2026-10-17.md` | `a719151678137d77334636a702ff075c45c16a1c` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 9 | `project lead/leadership/LEAD-DECISION-013-OFFICIAL-A25-POCKET-SERVER-ROUNDTABLE-BUILD.md` | `62961a8c4d681015de8dc0269fa4a34167c632c2` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 10 | `project lead/leadership/LEAD-PROJECT-MAP-019-ACTIVE-CHAT-SESSIONS-AND-OWNER-CONTROL.md` | `a358374eb49278522766159ba6e5d4968787a8da` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 11 | `project lead/leadership/LEAD-ACK-024-ROUNDTABLE-DIRECTIVE-023-ADOPTION.md` | `ee86f3320fd75eb325b31522f5f201196373c10a` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 12 | `project lead/leadership/LEAD-DIRECTIVE-023-LEADER-OWNED-TRAINING-AND-SHARED-POOL.md` | `4d6b63e2351a3d89c8750e3487f7e732ec02e6ba` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 13 | `project lead/leadership/LEAD-DIRECTIVE-025-LEADERSHIP-FOLDER-OWNERSHIP-AND-HANDOFF-RULES.md` | `1ee9e2b4e825228c188ef08cdfa861a34a30e51e` | Full text returned by GitHub connector; author/authority from document header, not independently authenticated |
| 14 | `case-studies/A25-roundtable-rooms-design-and-training-2026-10-16.md` | `d9e90c6f12f2eb740a33b269055424f9f0cbc27a` | Full text returned; GPT Project Lead authored case study; Zed quotations relayed, not independently byte-matched |

Fetch issue: initial unescaped raw URLs containing spaces returned `INVALID_ARGUMENT: HTTPError: 400: GitHub Fetch URL must use HTTPS and a valid GitHub host`; retried with properly escaped GitHub blob URLs and successfully retrieved all 13. This was URL-format failure, not source absence. No source files modified.

## 2. Roundtable leadership chronology (source-grounded)

- **2026-10-16 — REFERENCE / HISTORICAL CLAIM:** Case study records Zed's intention to preserve Roundtable rooms, separate GPT/Claude records, engineering rationale and Watchdog lessons. This is design and training, not a live shared-room server (case study at pinned tree).
- **2026-10-17, time UNKNOWN — HISTORICAL CLAIM:** Training Note 008 records manual courier workflow and read-first/event provenance requirements. Note 011 records evidence classification and separation of independent reviewer/author/publisher. Note 012 reports Claude Writer's first Drive publication and lead readback; reported SHA is not independently recalculated (see RT-TRAINING inventory and originals).
- **2026-10-17 20:02 MDT (owner-supplied) — ADOPTED:** Zed authorizes one official `Stratumnova/pockettest` implementation branch `build/a25-pocket-server-roundtable` based on hardened main `f0a11d51968ad598691333d32971dfb483489073`. Decision 013 records a GitHub create_branch tool receipt. This does not certify implementation or live phone deployment.
- **2026-10-17, exact time UNKNOWN — HISTORICAL CLAIM:** Corrected shared-read implementation is recorded at `fabedb661bb5161055534589c7517f7e0738139d`; O007 Claude02 independent re-review remained pending at the inventory/handoff checkpoint. No MCP SDK runtime integration verified (RT-TRAINING, HANDOFF-021, MAP-019).
- **2026-10-17, exact time UNKNOWN — ADOPTED (owner map):** Project Map 019 records separate GPT Roundtable Lead, Archives Lead, GPT server builder, original LB-GPT01 and Claude Writer/Claude02 reviewer sessions. Screenshot chat labels are not authenticated principals.
- **2026-10-17 21:48 MDT (owner-supplied) — ADOPTED:** Directive 023 puts training under leader custody and cross-project notes in shared pool; raw builder evidence remains downstairs. ACK 024 separately records Roundtable Lead adoption. Acknowledgment is not implementation evidence.
- **2026-10-17 21:59 MDT (owner-supplied) — ADOPTED:** Directive 025 establishes new leader-specific areas while historical root records remain unchanged. Archives and Roundtable ownership are separate; Security is reserved.
- **2026-10-17, exact time UNKNOWN — REFERENCE:** RT-TRAINING-001 inventory, RT-HANDOFF-002 emergency extraction and ARC-REVIEW-003 gap map are later reference and handoff layers, not replacements for the originals they index. Their document dates do not establish minute-level order.

## 3. Decision and adoption register

| Decision / item | Authority and classification | Implementation / runtime |
|---|---|---|
| Preserve separate Roundtable records and owner-controlled courier | Zed wording relayed in case study; REFERENCE, with owner intent historically recorded | Folder/document practices described; shared live messaging UNKNOWN |
| Official Pocket Server build branch | Zed ADOPTED in Decision 013; lead records branch creation receipt | Branch creation historically tool-confirmed; MCP SDK integration UNKNOWN |
| Source evidence classification | Owner direction in Note 011 and Directive 023; ADOPTED policy | Individual report assertions still HISTORICAL CLAIM until checked |
| Leader-owned training / cross-lead pool | Zed Directive 023 ADOPTED; Roundtable ACK 024 ADOPTED | Documentation interface, not automatic cross-lead approval |
| Leadership folder ownership | Archives recorder under Zed delegation, Directive 025 ADOPTED | Existing originals canonical; no migration authorized |
| Corrected shared-file read | Builder/lead historical reports; HISTORICAL CLAIM | Source commit identified, no verified live GPT+Claude read or deployment |

## 4. Communication channel inventory

- **GPT–GitHub:** Orders/reports and branch changes are described and pinned; connector source retrieval for this report is VERIFIED. Earlier code-test/write claims remain historical unless exact commits and logs are independently checked. No direct autonomous inter-AI chat is inferred.
- **Claude–Google Drive:** Writer/technical reviewer roles are separate. Note 012 records lead readback of Writer's document (Drive ID `1YFD9IXNgwaN53cYiis3NHkFu-bgNZb-0`); the writer-reported 5,377 bytes and SHA256 `6f2b3a8b25eda67a185966b609b961f1f3d2f2bc0ac775d9d61564d89843812c` are HISTORICAL CLAIM, not independently rehashed here.
- **Zed courier:** Owner controls relay and approvals, including cross-account transfer. This is a described operational workflow, not authenticated automated transport.
- **Android Termux/tmux/read-only viewport:** Historical owner-operated phone, terminal and read-only surfaces must be separated from command execution permissions. No live viewport, tunnel, phone, server or SDK action in AB-01. Runtime status UNKNOWN.

## 5. Conflict and gap ledger

1. **O003 permission contradiction:** earlier destination constraints blocked builder edits; owner Decision 013 established a distinct authorized implementation branch. Preserve R002 BLOCKED and corrective orders, not rewrite earlier history.
2. **O004/O006/O007:** correction and independent re-review are distinct events. O007 disposition not in these sources; UNKNOWN, not PASS.
3. **Tests:** 21 isolated tests reported by Claude02 on earlier code, and other builder-reported tests, do not establish MCP SDK integration or a two-account live read. Exact CI and logs require independent inspection.
4. **Drive:** Writer publication/readback is not independent content hashing or server verification. Drive bytes and original Claude reports were not retrieved in this batch.
5. **Identity:** Chat labels, narrative seats, GitHub publishers, authors, authenticated principals and owner are separate. Screenshot-based role map is not identity authentication.
6. **Chronology:** owner-supplied times exist for 013/023/025; most notes provide date only. UNKNOWN minute order must not be invented.
7. **Coverage:** RT-TRAINING inventory and ARC gap map are secondary mappings. AB-01 is not exhaustive history; RN-001 and Watchdog remain separate tracks.

## 6. AB-02 original-source queue — not executed

Priority 1: `project lead/leadership/LEAD-DIRECTIVE-005-EXISTING-PATHS-FIRST.md`, `LEAD-DIRECTION-007-POCKET-MAIN-VIEW-RESTART-GATE.md`, `LEAD-REVIEW-009-CLAUDE-PM-R001-AND-GPT-LAUNCH.md`, `LEAD-REVIEW-010-PM-GPT01-CLAUDE01-MAIN-VIEW.md` (paths under historical leadership root; exact authoring SHAs require source index/tree verification). Retrieve original O003/R002/O004/O006/O007 and GitHub tool/CI logs before deciding failure cause.

Priority 2: `project lead/leadership/LEAD-REVIEW-014-CLAUDE-WRITER-R003-AND-REVIEWER-LAUNCH.md` at `779894152030ce3e8e7b43f55a708034fdc96354`, `LEAD-REVIEW-015-CLAUDE02-R001-O006-DISPOSITION.md` at `699575f58c7c8bb776f516c7d731ae0a0935ea9e`, Claude02 Drive original ID `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl`; compare first-person reports to original GitHub commits and test logs.

Priority 3: Review GPT–GitHub transport/safety-stop records and workaround cases `case-studies/A25-F-005-wd03-safety-stop-authorized-retry-2026-10-16.md`, `case-studies/WD-05-github-actions-failures-and-recovery-2026-10-16.md` (commit SHAs UNKNOWN until individually fetched). Do not treat safety approval as bypass permission.

## 7. Boundaries and next gate

No files other than this report created or changed; no code/branch/phone/server/CI/deployment action. Original documents preserved. Archives Lead should verify R001 independently, request correction if needed, and only then issue AB-02. Neither this report nor an adopted decision establishes successful technical implementation.
