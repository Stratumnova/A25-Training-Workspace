# A25-AB-R004 — Android Terminal, Viewport and Tunnel Communication Evidence

FROM: A25-AB-GPT01 — Archives Builder  
FOR: A25-AG-GPT01 — Archives Lead; Zed  
ORDER: A25-AB-O004 at `49fec56ae605595563c8a1b6804c772e19a6746a`  
DATE: 2026-10-17 (project record label; no current phone-time claim)  
STATUS: HISTORICAL SOURCE EXTRACTION COMPLETE; NO LIVE RUNTIME CHECK  
OWNER: Zed; Archives Lead supervises  
NEXT ACTION: Archives Lead independent review; AB-05 only if separately ordered

## 1. Source-access ledger

**Read method:** GitHub connector fetched Markdown source text; Drive connector fetched text from the specified original Drive IDs. `VERIFIED` below means this AB-04 session retrieved the named source text, **not** that historical phone actions, tool outputs, hashes, test results or identities were reproduced. No live phone, terminal, tunnel or server connector was called.

| Original | Revision / Drive ID | Access and limits |
|---|---|---|
| `project lead/coordination/reports/A25-AB-R003-GPT01-CLAUDE-DRIVE-COMMUNICATION-EVIDENCE.md` | d40dfdebd165689c93984bd27b4341702721ae61 | Full GitHub text; earlier builder synthesis, secondary for phone claims |
| `project lead/leadership/archives/ARC-REVIEW-2026-10-17-006-AB-R003-CLAUDE-DRIVE-DISPOSITION.md` | existing `coord/a25-namespace-trial-001` branch at fetch | Full GitHub text; exact individual authoring SHA not independently resolved; Archives accepted R003, not tests |
| `project lead/leadership/LEAD-TRAINING-NOTE-008-ROUNDTABLE-LIVE-WORKFLOW-OBSERVATIONS.md` | 627ae1198ae27bdde70086361da441f2bb6257be | Full; Lead's workflow observations and proposals |
| `project lead/leadership/roundtable/RT-TRAINING-2026-10-17-001-CONTEXT-AND-RECALL-INVENTORY.md` | d626ebde4ba83baa4de3406c4cbeb7619fc11e21 | Full; original lead-authored inventory, partly secondary for phone history |
| `project lead/leadership/roundtable/RT-HANDOFF-2026-10-17-002-EMERGENCY-SESSION-EXTRACTION.md` | f9a3fc912d15d1900b150b166cb56d2e371622df | Full; explicitly contaminated recall and separately checked source pointers |
| `project lead/leadership/LEAD-REVIEW-010-PM-GPT01-CLAUDE01-MAIN-VIEW.md` | existing coordination branch at fetch | Full; Lead comparison, not live test; authoring SHA UNKNOWN |
| `project lead/leadership/LEAD-STUDY-022-HANDOFF-EVIDENCE-LESSONS-2026-10-17.md` | existing coordination branch at fetch | Full; study, not test certification; authoring SHA UNKNOWN |
| `project lead/coordination/reports/A25-PM-R001-GPT01.md` | existing coordination branch at fetch; report receipt 9143345fc0a70e0cb4bd12c099be2f0f3b1a5731 cited by Lead | Full; source inspection only, no Android access |
| `project lead/coordination/reports/A25-PM-R002-GPT01.md` | existing coordination branch at fetch | Full; implementation BLOCKED, zero tests |
| `project lead/coordination/reports/A25-PM-R003-GPT01.md` | existing coordination branch at fetch; receipt 90b4b12e00e23dc0743e71939a5fc7ba0de7d241 reported | Full; source implementation, no runtime |
| `project lead/coordination/reports/A25-PM-R004-GPT01.md` | existing coordination branch at fetch; receipt bedb45073b700b9600c0f38924188f0d97e92ddd reported | Full; corrected source, SDK tests blocked |
| `project lead/leadership-pool/POOL-2026-10-17-ROUNDTABLE-SECURITY-AND-COMMUNICATION-DEPENDENCIES.md` | d98018a3fe53ed224c814237f5a61854b091e9a4 | Full; security dependency, no deployment authorization |
| `project lead/leadership-pool/POOL-2026-10-17-ARCHIVES-SECURITY-SAFETY-BLOCK-AND-COMMUNICATION-EVIDENCE.md` | b351aadb2b8e50bcf8e43bb7a5fea0bfb5834e2b | Full; communication provenance and deferred security question |
| `A25-PM-R001-CLAUDE01.md` | Drive `1OQd690BbRMMaGEIyKyoPNxmNmsOyudDb` | Full original text; contemporaneous reviewer account of `terminal_status` and `terminal_view`; **original tool envelopes/logs not independently retrieved** |
| `A25-PM-R002-CLAUDE02.md` | Drive `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va` | Full original text; SDK/Host boundary only; reviewer-reported isolated tests, no phone test |
| `A25clauderecall_id001-REPORT.md` | Drive `15fzkYQlfThEsemntyGnoUqA5hewAkF38` | Full original text; mixed historical observation, earlier source and Zed relay, explicitly not blind recall |
| `A25clauderecall_id001-ADDENDUM-01.md` | Drive `15XeF8U8oObFrw4ivMzsN_F0b7vYM65UA` | Full original text; later read-only viewport observations; partial screen listing only |

**Unavailable/not independently accessed:** raw Android shell/tmux scrollback and process logs; original historical `terminal_view` and `terminal_status` connector response envelopes; old screenshot pixels and screenshot timestamps; raw Cloudflare/cloudflared logs and tunnel configuration; current phone worktrees; archived ZIP/PDF byte content; actual restart test tool transcripts. The existing project includes older attachments and checkpoint references, but their full original contents were **not** opened or audited in this batch. GitHub branch-ref reads were not pinned to a resolved HEAD SHA; no false commit precision is claimed.

## 2. Chronology — distinct builds, sessions, ports

| Period / time quality | System / port | Source-backed historical account | Evidence classification |
|---|---|---|---|
| Oct 7–8, 2026; exact command times not retrieved | **Gate-01**, historically `8765`, Quick Tunnel | Authless, route-derived GPT/Claude identities; append-only JSONL, per-participant cursors, read-first and retry semantics. Claude recall reports five phone tests PASS, but original test execution output not retrieved here. | HISTORICAL CLAIM from Claude recall and Roundtable handoff; not hardened Gate-02A |
| Oct 8 event times | Gate-01 ledger | Claude recall reports event #1 Claude 2026-10-08T03:19:27Z cursor 0; #2 GPT 04:52:11Z cursor 1; #3 Claude 05:02:21Z cursor 2. Recovery read later reported Claude context [1,2,3], unseen []; GPT context [1,2], unseen [3]. | HISTORICAL CLAIM / source-check reported in recall; event #3 timestamp **not** restart time |
| Oct 8, exact failure times UNKNOWN | Cloudflare Quick Tunnel | Claude recall cites Oct 8 checkpoint: **“Quick tunnel died twice (mobile network switches)”**. Earlier tunnel replacement/reconnection described in historical workflow; original cloudflared log absent. | HISTORICAL CLAIM; cause attribution beyond source remains UNKNOWN |
| Oct 10–13, exact timing mixed | Terminal bridge `~/a25-workshop/gpt`, historically `8769`; fixed shared viewport historically `8770` | Claude recall reports read-only bridge with unauthenticated 401 and Oct 12 three-party blind-marker demonstration; shared viewport then shut down. These are separate from Gate-01 ledger and Gate-02A. | OBSERVED_HISTORICAL / RECALL in Claude original; original bridge logs and authentication tests not reproduced |
| Oct 11 date displayed on Oct 17 screen | `~/a25-workshop/gpt` | Claude01 says terminal screen showed directory mode `drwx------`, dated Oct 11, not a Git repo. That screen observation cannot prove entire bridge source is unversioned elsewhere. | OBSERVED-DISPLAY in original; inference qualified |
| Oct 12–13 checkpoint period | Three phone worktrees | `~/pockettest` main `f0a11d51968ad598691333d32971dfb483489073`; `~/pockettest-c1` auth `1b578ee32532f99093ab906af52e8b485c90a7e4`; `~/pockettest-shared` Shared Space `9a419e925dff2de64ef948b7d6d8304eccf8387d` later printed on Oct 17 screen. Different code versions, not a single server state. | OBSERVED-DISPLAY for printed worktree heads; source branch identity not independently read from phone |
| Oct 17 viewport restoration, no per-line timestamps | tmux session `a25-gpt`, read-only viewer | Claude01 reports one `terminal_status` and one `terminal_view` call, `read_only:true`, returncode 0. RN Claude original reports GPT/Claude both viewed “A25 SHARED TERMINAL READY” and “A25 VIEWPORT LIVE TEST 2026-10-17”; Claude had already seen marker in GPT relay, so not blind. Zed said he saw Claude's access arrive. | Claude own historical tool observation + ZED_RELAYED; **not** authenticated two-client source read |
| Oct 17 second viewport look | tmux `a25-gpt` | Claude RN addendum reports listing of auth-line `gate02` files, Shared Space `shared/`, backups and 13 checkpoint files. Only end of listing visible; main worktree and viewport folder not visible in that read. | OBSERVED-DISPLAY, no independent directory access |
| Oct 17 source implementation | **Hardened Gate-02A** historically `8766`; later isolated local-mode example `8767` | GPT R001 remotely inspected main deny-all source; R002 BLOCKED by no authorized edit destination; owner adopted single official branch; R003 source `442529a32356c5fb557d908fcd20bace733f04d8`; R004 corrected source `fabedb661bb5161055534589c7517f7e0738139d`. No builder MCP integration tests or phone deployment. | GitHub source/report evidence; runtime UNKNOWN |
| Oct 17 O007 reviewer | Local-mode `8767` in test design, **not a demonstrated listener** | Claude02 R002 reports portless `Host: localhost` in SDK test predicts HTTP 421, identifies residual proxy/host parsing concerns. Reports 17 isolated harness tests + 10 regression tests, **zero SDK tests**. | Original reviewer claim; not live server evidence |

**Port rule:** `8765`, `8766`, `8767`, `8769`, `8770` describe **different historical roles/configurations**. They are not a current open-port scan. A tunnel hostname or localhost URL in a report is not proof a listener exists now.

## 3. Observation and custody chain

| Actor / surface | Operation or evidence | What it actually establishes | What it does NOT establish |
|---|---|---|---|
| **Zed**, owner/operator | Historically typed Android Termux commands, controlled tmux, process/tunnel restarts and relay between GPT and Claude | Owner-supplied operational provenance; where screenshot/tool records exist, command/output pairing can be investigated | GPT/Claude did not thereby execute Zed's shell commands; no full command transcript retrieved here |
| **GPT lead/builder**, GitHub connector | Read source commits and published reports | Remote repository source/report text, revision when pinned | Running phone worktree, current Uvicorn process or tunnel health |
| **Claude01**, `terminal_status` | Original reports identity `gpt-workshop`, `workspace_exists:true`, directories `src/tests/logs/reports/backups/config`, mode `read-only` | Client-side status response as reported in original | `gpt-workshop` is workspace label, **not authenticated caller identity** |
| **Claude01**, `terminal_view` | Original reports session `a25-gpt`, `read_only:true`, returncode 0; screen starts with `tmux clear-history`; lines lack timestamps | At that call, Claude obtained rendered session text | Does not prove independent `git` command execution, file bytes, server-side read-only enforcement or historical line timestamps |
| **Whoever controlled tmux input** | Printed `git status --porcelain=v1 -uno`, `git diff --quiet`, worktree hashes and `sha256sum` output to screen | Display-level observations: three tracked worktrees reportedly clean; printed ledger backup 441 bytes and digest `61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9` | `-uno` excludes untracked files; no independent hash computation; operator/timestamp of each printed command not established |
| **Claude RN addendum**, second viewport read | Listed auth/shared files, backup JSONL name and checkpoint inventory | File names visible on partial screen | Phone copy of JSONL **not byte-verified** against project attachment; no worktree HEADs in addendum screen |
| **Zed relay**, chat | Conveyed orders, reports, marker text and account observations | Communication provenance and owner direction | A marker seen in prior relay is not blind independent cross-AI proof; narrative GPT/Claude labels are not credential identities |
| **Gate-01 MCP path**, historical | Three ledger events, `cursor_through`, context/unseen and reported recovery | Reported route-derived ledger semantics in earlier Gate-01 implementation | Hardened OAuth authentication, Gate-02A shared-file reads, or current two-account access |

The **Oct 17 Claude01 screen** displayed main/auth/shared worktree hashes, `git status --porcelain=v1 -uno`, `git diff --quiet` and a ledger-copy digest. Claude explicitly classified O3–O6 as **OBSERVED-DISPLAY**, not independent source-file reads. The **later RN addendum** explicitly limits its screen to the end of a listing; its inability to see `~/a25-workshop/gpt` cannot supersede the earlier screen claim about that path. These are distinct viewports, not mutually exclusive statements.

## 4. Transport and reliability incident ledger

| Incident / boundary | Recorded evidence and error | Resolution/status |
|---|---|---|
| Gate-01 read-first and cursor | Claude recall identifies ledger #1–#3 with cursors 0/1/2; historical recovery reports GPT unseen [3], Claude unseen [] | HISTORICAL CLAIM of a past Gate-01 recovery. No independently retrieved original `read_roundtable` response here; not a Gate-02A PASS |
| Recovery-time attribution drift | Claude RN original corrects earlier claim that `2026-10-08T05:02:21Z` was recovery time | **SUPERSEDED:** that is event #3's timestamp. Actual restart recovery time **UNKNOWN**; original mistaken reports remain preserved |
| Quick Tunnel on mobile network switches | Original Claude recall quotes “Quick tunnel died twice (mobile network switches)” | Historical failure reported; no original cloudflared logs or precise timestamps retrieved; successful later reconnection cannot be assumed permanent |
| Network/origin failures | Claude recall mentions `cloudflared` timeouts, IPv6 unreachable and origin refusal on `8770`; Zed attributes drops to phone leaving Starlink coverage | HISTORICAL CLAIM / ZED_RELAYED cause; exact underlying error lines, exit codes and recovery times **UNKNOWN** in AB-04 |
| Oct 12 blind-marker proof vs Oct 17 marker | Claude recall reports Oct 12 blind-marker three-party demonstration; Oct 17 Claude saw marker in GPT relay before own `terminal_view` | Preserve separate episodes; Oct 17 is **not blind**; neither proves authenticated MCP shared read |
| Read-only viewport freshness | `terminal_view` shows `tmux clear-history` and no line timestamps; whoever types chooses screen content | Display may be stale or selectively cleared. **No demonstrated stale-screen incident** with an independently measured delay; freshness UNKNOWN |
| Terminal read-only | Tool schema reportedly has no command input and returns `read_only:true` | Client interface observed by Claude; server-side enforcement, auth and audit log UNKNOWN |
| Separate GitHub source and Android runtime | GPT R001/R002/R003/R004 explicitly deny live phone/server/tunnel access and report zero SDK integration tests | Do not convert static source inspection into phone/runtime PASS |
| Cloudflare/public anonymous risk | GPT R003/R004 and Claude02 R002 warn loopback peer can be spoofed by trusted proxy path; `cf-ray`/forwarded headers defense in depth | No public tunnel exposure approved for anonymous local mode; exact deployed proxy path UNKNOWN |
| Owner-controlled lifecycle gate | Claude01 proposed T1–T8: two independent reads, stop, restart, re-read, final stop | **PROPOSED, NOT EXECUTED** for official shared-file read. No end-to-end two-client restart PASS |

## 5. Security, identity and transport boundaries

**Gate-01 (earlier):** historical authless route-derived identity, JSONL ledger and cursors; a path-specific GPT or Claude route is not cryptographically authenticated per-user OAuth. Historical restart recovery does not certify present identity separation or service availability.

**Gate-02A hardened `main`:** GPT R001 inspected source at `f0a11d51968ad598691333d32971dfb483489073`, reporting `DenyAllProvider` and `ready:false`. This was a source-level observation, not a live phone check. It should not be conflated with Gate-01's working authless ledger.

**Official build branch:** Zed ADOPTED `build/a25-pocket-server-roundtable` for development; source-level opt-in `A25_LOCAL_READ_MODE=1` is anonymous loopback-only with host/header guards. Claude02 R002 reports residual parsing weaknesses and predicts an SDK local-mode test defect. **Not an approved public tunnel deployment; no demonstrated authenticated independent remote GPT and Claude reads.** OAuth work on `build/gate02a-c1-auth-store` is a distinct historical branch; presence of registration/consent source is not proof token issuance or production wiring.

**Read-only terminal viewport:** `terminal_status` identity `gpt-workshop` names workspace; `terminal_view` session `a25-gpt` and `read_only:true` describe displayed tool response. Neither verifies server-side enforcement, caller authentication, role principal or the exact file bytes shown on screen. The Oct 17 marker had prior relay contamination; separate chat/account UI labels and courier messages are not authenticated server principals.

**Owner execution vs AI observation:** Zed historically typed phone commands. Claude/GPT may observe screen output and compare records; they do not gain command authority from observing. Future terminal execution is a separate owner-approved milestone. The Roundtable training note's event types are proposed schema candidates, not a deployed logging system.

## 6. Reconciliation, gaps and status ledger

| Issue | Current AB-04 classification |
|---|---|
| Claude01 says viewport folder not a Git repo; later RN addendum says viewport folder not visible | **Compatible different screens**; earlier observation is reported display, later visibility gap does not negate it. Independently versioned source UNKNOWN. |
| Claude RN original says Gate-01 restart recovery “recorded 05:02Z”; same original Phase B corrects it | **SUPERSEDED** time attribution. Event #3 time retained; restart time UNKNOWN. |
| Oct 12 three-party blind marker vs Oct 17 two-seat marker | Distinct reported tests. Oct 17 marker explicitly non-blind; do not promote either to authenticated MCP PASS. |
| `git status -uno` / `git diff --quiet` reports clean | Screen-displayed tracked state only; untracked files excluded, local worktree not independently queried. |
| Phone JSONL copy digest shown as matching archive digest | OBSERVED-DISPLAY; AB-04 did not independently hash phone or archive. Later RN addendum filename-only observation explicitly says byte identity unverified. |
| Oct 17 viewport read marked RUNNING_VERIFIED in Claude original | Verified **by that author at that historical instant**; present runtime UNKNOWN, original tool envelopes not replayed. |
| Port assignments across projects | Historical port roles only; no present listening sockets checked. |
| Cloudflare disconnect attribution to mobile/Starlink | ZED_RELAYED / historical checkpoint; no independent network trace. |
| Uvicorn start/stop, tunnel replacement and persistent cursor after restart | Historical Gate-01 claims; original process log and timestamped command/output chain unavailable. No official Gate-02A lifecycle verification. |
| Claude02 O007 R002 | **Original Drive report VERIFIED accessible** in AB-03/AB-04; reviewer findings remain HISTORICAL CLAIM until reproduced; 0 SDK tests, no deployment approval. |
| OAuth / authenticated dual-client MCP / terminal write | **UNKNOWN or deferred**, not demonstrated by viewport. |
| Archives acceptance | **ADOPTED for archival intake** of R003 by ARC-REVIEW-006; not adoption of phone/test claims. |
| Current phone, tunnel, server, sessions | **UNKNOWN**; deliberately not queried under O004. |

**No unsupported PASS:** The strongest direct AB-04 evidence is retrieval of original GitHub/Drive text. The reported terminal tool calls are **original first-person Claude accounts**, not live calls or raw tool transcripts independently reproduced by this builder. Screen text is evidence of display, not independently executed shell commands. No raw phone logs, source-file bytes or live endpoint responses were obtained.

## 7. AB-05 handoff queue — NOT EXECUTED

Candidate originals for the next separately authorized batch: Watchdog W1–W6 design and implementation records; WD-03 `case-studies/A25-F-005-wd03-safety-stop-authorized-retry-2026-10-16.md`; WD-05 `case-studies/WD-05-github-actions-failures-and-recovery-2026-10-16.md`; `project lead/master archive/03-WATCHDOG-ACTIONS-HISTORY.md`; original Watchdog branch source blobs/commit hashes, independent Claude reviews, exact GitHub Actions run IDs and logs. Preserve WD-03 platform safety stop and Zed-approved retry as separate events, with exact error; do not infer platform cause. Preserve WD-05 early red runs, later reported 16/16 isolated PASS and actual-repo 0 FAIL/3 WARN as **historical reported** until independently retrieved from original logs. W4 multi-commit enforcement, W6 permissions, fixture validity and later corrections require separate evidence. Ask which findings were adopted and which were only proposed; never silently merge Watchdog design with deployed enforcement. No CI, phone, branch, source modification or AB-05 execution in this batch.

**Publication boundary:** This report is the sole authorized new file. No historical sources, code, branches, Drive documents, phone, terminal, tunnel, server or CI were altered or queried live.
