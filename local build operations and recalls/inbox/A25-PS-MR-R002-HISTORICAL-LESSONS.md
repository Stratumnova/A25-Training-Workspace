# A25-PS-MR-R002 — Historical Shared Workspace and Communication Lessons

**FROM:** Pocket Server GPT Builder  
**FOR:** Zed / GPT — A25 Project Lead  
**ORDER:** `A25-PS-MR-O002-HISTORICAL-SHARED-WORKSPACE-LESSONS.md`  
**DATE:** 2026-10-17 MDT  
**MODE:** READ-ONLY HISTORICAL STUDY  
**PROVENANCE NOTE:** This report separates direct/source-backed observations from builder memory, Zed-relayed screenshots, Claude-reported review, and inference. Zed additionally states that Claude retains reviews in Claude's own memory and that other chat sessions tested terminal and file viewing. Those statements are preserved as **ZED-RELAYED** context, not converted into independently verified facts. Private information visible in screenshots is intentionally omitted.

## Evidence labels

- **OBSERVED** — directly visible in source, immutable repo material, or screenshots supplied to this builder.
- **BUILDER-REPORTED** — prior Pocket Server builder/session report available to this builder but not rerun here.
- **ZED-RELAYED** — Zed's report, screenshot, or relay of another seat/session.
- **CLAUDE-REPORTED** — attributed Claude review/result, not independently reproduced here unless separately stated.
- **INFERRED** — reasoned consequence, not directly tested.
- **UNKNOWN** — evidence does not establish the fact.

## Chronological case index

| Date | Case | Actors | Evidence source | Subsystem | Outcome | Remaining uncertainty |
|---|---|---|---|---|---|---|
| 2026-10-07/08 | Gate-01 three-event GPT/Claude roundtrip | Zed, GPT, Claude | **BUILDER-REPORTED** prior session/checkpoint; Gate-01 source | Roundtable | Bidirectional event delivery, author attribution, cursors and unseen filtering reported working | Original raw client transcripts not re-fetched in this study |
| 2026-10-08 | Gate-01 Uvicorn restart + Quick Tunnel replacement | Zed, GPT, Claude | **BUILDER-REPORTED** recovery study | Recovery/network | Three events recovered after server restart/tunnel replacement | Full Android reboot and automatic recovery not proven |
| 2026-10-09 | Gate-02A public deny-all/auth discovery | Zed, GPT/Claude clients | **BUILDER-REPORTED** prior session; `pockettest` Gate-02A source | OAuth boundary | Public hostname reached Android; unauthenticated MCP denied; health ready:false | Production OAuth incomplete |
| 2026-10-09 | Listening-wall client behavior | Zed, GPT, Claude | **BUILDER-REPORTED / CLAUDE-REPORTED** prior evidence | OAuth discovery | Different client callback/discovery behavior exposed; OIDC probes observed | Some client stopping/continuation behavior remained uncertain |
| 2026-10-10 | Secret/tunnel exposure correction | Zed, GPT | **BUILDER-REPORTED** checkpoint | Secrets/tunnel | Exposed tunnel token was rotated | Whether every historical copy was purged is not established here |
| 2026-10-10–12 | Shared Space Stage 1 | Zed, GPT, Claude review | **OBSERVED** GitHub branch/source; historical test counts **BUILDER-REPORTED** | Private storage | Data-root separation, no-follow file opens, 0700/0600 controls, append/recovery logic implemented | Current deployment state unknown |
| 2026-10-10–12 | Shared Space Stage 2 identity proposal | Zed, GPT, Claude review | **OBSERVED** proposal ref; test outcome **BUILDER-REPORTED** | Identity integration | Proposal remained unmerged after reported 78 pass / 1 fail / 1 warning | Failing directory-creation race not independently rerun here |
| 2026-10-12 | Read-only terminal/observation viewport proof | Zed, GPT, Claude | **OBSERVED** screenshots supplied with this order + **BUILDER-REPORTED** checkpoint | Observation bench | Shared read-only terminal visibility was demonstrated; separate public MCP handled tool calls | No authenticated production boundary; initial 400s/log oddities unresolved |
| 2026-10-12/13 | Tunnel/network disruption and shutdown evidence | Zed, cloudflared | **OBSERVED** supplied screenshots | Network/process | cloudflared repeatedly lost/re-established QUIC connections; later origin refusal when 8770 was down; graceful tunnel stop visible | Exact Android network cause and automatic long-term recovery behavior unknown |
| 2026-10-12 | Manual PDF/checkpoint relay + hash discrepancy | Zed, GPT, Claude | **BUILDER-REPORTED / CLAUDE-REPORTED** checkpoint history | Evidence integrity | Phone-side SHA-256 became authoritative after generation-side hash mismatches | Root cause of generation-side mismatch unknown |
| 2026-10-16 | AI-first GitHub/full-fidelity workspace policy | Zed, GPT, Claude | **OBSERVED** A25 repo search result: `legacy/pockettest/a25-training/governance/AI_FIRST_HUMAN_FIRST_WORKSPACE.md` | Handoff/governance | Durable machine-readable sources preferred over manual copy/paste | Pocket Server replacement not yet independently verified |
| 2026-10-16 | Claude ZIP baseline and independent review pattern | Zed, Claude, GPT | **OBSERVED** A25 repo search results: RT-001 / Claude review index | Source integrity | Commit-pinned ZIP/hash comparison used to establish independent evidence | GPT did not independently reproduce every Claude ZIP check |
| 2026-10-16 | External builder intake via ZIP | Zed, GB-01, GPT | **OBSERVED** A25 repo search result: `roundtable/builders-inbox/GB-01-context-sync-2026-10-16.md` | Cross-session handoff | Builder reconstructed project state from ZIP without treating it as approval | ZIP can become stale immediately after its pinned boundary |
| 2026-10-17 | Other chat sessions tested terminal/file viewing | Zed, other sessions | **ZED-RELAYED** statement in current order + supplied screenshots | Tool access | Historical testing occurred outside this builder session | Exact session IDs, complete transcripts and test boundaries not supplied here |
| 2026-10-17 | Claude retains historical reviews in memory | Claude, Zed | **ZED-RELAYED** statement in current order | Cross-seat continuity | Lead should know Claude can contribute independent remembered review context | Memory is not immutable evidence and must be reconciled against pinned sources |

## Detailed historical cases

### 1. Gate-01 roundtrip: identity, cursor and duplicate semantics

**BUILDER-REPORTED:** The historical ledger contained event 1 Claude, event 2 GPT, event 3 Claude. Prior recovery work reported cursor-through progression 0/1/2 and correct unseen classification. This established the core lesson that shared conversation state must be server-side and durable rather than reconstructed from whichever AI chat happens to be open.

**OBSERVED in inspected source during R001:** Gate-01 assigns actor identity from separate GPT/Claude route construction, requires a read before append, persists `cursor_through`, excludes an actor's own events from unseen, and protects an exact retry of the actor's most recent message/references from duplication.

**Lesson:** durable event IDs + author + cursor are stronger than conversational memory. However, path-derived identity is not final authenticated identity. A seat saying “I am Claude” or “I am GPT” is never sufficient.

### 2. Gate-01 restart and Quick Tunnel replacement

**BUILDER-REPORTED:** Uvicorn restart and replacement of the temporary Cloudflare Quick Tunnel did not erase the three-event ledger. The clients could reconnect after endpoint replacement once connector references were updated.

**Lesson:** separate transport identity from durable state. A tunnel can disappear without invalidating the ledger. Quick Tunnel URLs are operationally expensive because changing URLs create stale connector references. Named endpoints reduce this problem but do not prove process supervision.

**UNKNOWN:** Full phone reboot, Doze/process kill, and Wi-Fi/cellular transition recovery were not proven by that case.

### 3. Gate-02A deny-all, listening wall, auth and consent

**BUILDER-REPORTED:** On 2026-10-09 the stable public hostname reached Android. Unauthenticated MCP requests were denied and OAuth metadata was exposed. Listening-wall evidence showed Claude and ChatGPT did not make identical discovery/callback attempts. Claude was reported using a fixed callback and `client_secret_post`; ChatGPT used its connector-specific callback and `client_secret_post`; OIDC probes returned 404.

**OBSERVED in R001 source inspection:** Gate-02A main remains `DenyAllProvider` and health returns `ready:false`. The auth branch contains registration/consent/auth-code foundations but its server remains the deny-all server. Therefore historical client discovery observations must not be mistaken for completed OAuth.

**Lesson:** test each client as an independent protocol actor. “Works for GPT” cannot stand in for “works for Claude.” Record exact discovery requests, callback expectations and failure stage without treating client behavior as identity proof.

### 4. Shared Space Stage 1

**OBSERVED:** Branch `build/shared-space-v0` at `9a419e925dff2de64ef948b7d6d8304eccf8387d` separates private data from the repo, validates absolute/resolved data root, rejects repository overlap, uses no-follow regular-file opens, and applies restrictive modes.

**BUILDER-REPORTED:** Historical checkpoint recorded 45 passing tests.

**Lesson:** source and mutable private state need separate authorities. A shared workspace should expose narrowly scoped read/list operations instead of making the repository or phone filesystem itself the API.

### 5. Shared Space Stage 2 identity proposal

**OBSERVED:** Proposal ref `8ade3c00f4f5219182ec01b5154b4b89b71d3359` exists separately from Stage 1.

**BUILDER-REPORTED:** Historical run recorded 78 passed, 1 failed, 1 warning; the failure was a race around data-directory creation. It was not merged.

**Lesson:** a nearly-green identity/security proposal is still not accepted. Preserve failing evidence and do not merge around a race because the happy path looks correct.

### 6. Terminal / observation viewport

**OBSERVED from Zed-supplied screenshots:** A read-only MCP process was run on local port 8770. Logs show repeated MCP sessions and successful ListTools/CallTool request processing from more than one remote address range. Another screenshot shows the read-only implementation's `terminal_view` capturing a fixed tmux session and returning the screen without sending input. A marker was typed into the shared tmux pane during the historical proof. The screenshots also show the separate authenticated bridge on 8769 and Gate-02A on 8766 at points in the test history.

**ZED-RELAYED:** Claude has reviews in her memory, and other chat sessions also tested terminal and file viewing. This is useful lead context but not a substitute for the missing full transcripts.

**BUILDER-REPORTED:** The three-way viewport proof used a blind marker: Claude read it independently, GPT read it independently, and Zed confirmed the physical screen. The public no-auth viewport was then deliberately shut down.

**Lesson:** observation and command authority must remain separate. A shared terminal view is valuable for evidence and coordination precisely because it does not need to become a shell gateway.

### 7. Tunnel replacement, DNS and network drops

**OBSERVED from supplied screenshots:** cloudflared logs show repeated QUIC inactivity timeouts, “network is unreachable,” reconnection attempts, new registered tunnel connections, and later `dial tcp 127.0.0.1:8770: connect: connection refused` after the local origin was unavailable. Graceful shutdown lines are also visible.

**Lesson:** distinguish three failures: remote network path, tunnel process, and local origin. A tunnel can be healthy enough to reconnect while the origin is down; conversely the local origin can be healthy while remote access is broken. Recovery evidence should name which layer failed.

### 8. Manual relay, PDFs, ZIP snapshots and source integrity

**BUILDER-REPORTED / CLAUDE-REPORTED:** Multiple checkpoint PDFs had generation-side SHA-256 values that did not match the bytes Zed actually downloaded. The procedure changed to make the phone hash authoritative: generate -> download -> hash on phone -> copy archive -> hash destination -> approve deletion -> final existence check.

**OBSERVED in A25 repo search:** Claude's RT-001 response states a SHA-256 manifest was computed from Zed's repo ZIP at pinned commit `6ffcc10ece1b33afaa3070c3ea278f95ac8b92c2`. Current A25 policy material calls for commit-pinned/hash-verified ZIP mirrors and full-fidelity machine-readable sources.

**Lesson:** filenames and AI claims are not integrity evidence. Pin a commit, hash the actual transferred bytes, and preserve provenance. ZIP snapshots are good cold-handoff material but are snapshots, not live state.

### 9. Owner versus AI authority

**OBSERVED in A25 repository material:** Zed is owner/decision authority. The A25 operational record allows GPT routine bookkeeping for already-authorized work but requires Zed for governance/access changes, deletion/restructuring of historical evidence, or elevation of disputed proposals. Claude absence is not consent and GPT may not speak as Claude.

**Lesson:** question ownership and approval ownership must be explicit. A relay system can accidentally let one AI answer for another or for Zed; authenticated writer lanes and immutable attribution are therefore architectural requirements, not etiquette.

### 10. Other sessions and cross-seat continuity

**ZED-RELAYED:** Other chat sessions tested terminal and file viewing, and Claude retains reviews in memory.

**INFERRED transfer lesson:** separate sessions can provide valuable independent checks because they do not share identical active context. But memory, screenshots, relayed summaries, and live tool output are different evidence classes. The lead should reconcile them, not flatten them into one “verified” state.

## Direct transfer to current A25 work

### Namespace builder handoffs

**Applies directly:** Use unique order/report IDs, writer-owned inbox paths, immutable originals, additive corrections, commit SHAs, and explicit provenance. Gate-01's author/cursor model transfers conceptually: each builder should have a lane and the lead should know what each builder has actually read.

**Limitation:** GitHub branch identity is not yet Pocket Server authenticated seat identity. Commit author metadata alone should not be treated as AI credential proof.

### Source-integrity checks

**Applies directly:** Pin source by full commit SHA; hash transferred ZIPs/files; preserve original failed reports; record correction separately. Phone-side transferred-byte hashes demonstrated why generation-side claims cannot be authoritative.

**Limitation:** A SHA proves byte identity, not correctness, completeness, authorship or approval.

### GitHub Actions workflow visibility

**Applies directly:** Treat workflow status like another event/evidence stream: exact workflow/run ID, triggering commit, status/conclusion, logs/artifacts, and who observed it. Do not summarize “CI green” without commit binding.

**Proposal:** builder reports should include `workflow/run -> commit -> conclusion -> evidence observer`. A later harmless commit must not conceal a failure in an earlier protected transition.

**Limitation:** This historical Pocket Server study did not itself inspect current GitHub Actions runs.

### Future Pocket Server file listing/read

**Applies directly:** File listing/read should be narrow, deterministic, read-only, path-rooted, no-follow, and provenance-bearing. Responses should identify project/ref/file/hash where practical. Do not expose arbitrary phone paths or secret-bearing configuration.

**Limitation:** R001 found the six-operation V1 contract, but `list_projects`, `list_files`, and `read_file` were absent from inspected Gate-01/Shared Stage 1 runtime refs. Historical “file viewing” in other sessions is **ZED-RELAYED** and does not establish those production APIs.

## Proposed additions to A25 test materials

### Negative tests — PROPOSED

- Seat A submits content claiming to be Seat B: reject or attribute to authenticated Seat A.
- Builder writes outside its assigned inbox namespace: reject.
- File read attempts `../`, absolute paths, symlinks, encoded traversal, secret/config roots and ZIP traversal: reject.
- Stale commit/ZIP used after branch advances: label stale; never silently reinterpret as current.
- Report cites CI “green” without a run bound to the tested commit: fail evidence gate.
- AI answers a question explicitly owned by Zed or another seat: record as authority violation, not valid decision.
- Exact duplicate append after ambiguous timeout: no duplicate event.
- Same text from two different authenticated seats: preserve as two attributed events, not deduplicate across authors.

### Recovery tests — PROPOSED

- Uvicorn crash with unread events; restart and verify ordering/cursors.
- cloudflared stop while origin stays up; verify local health then remote recovery.
- origin stop while tunnel stays up; verify distinct origin-unreachable evidence.
- Wi-Fi -> cellular -> Wi-Fi with stable named tunnel; timestamp disconnect/reconnect.
- Android process kill and full reboot; document exact manual/automatic recovery.
- Incomplete JSONL tail and quarantine recovery using disposable data only.
- Interrupted file/ZIP transfer; verify hash failure and no acceptance.

### Cross-seat identity tests — PROPOSED

- GPT credential cannot write Claude lane; Claude credential cannot write GPT lane.
- A response body self-label cannot override credential identity.
- Revoked credential immediately loses read/write scope.
- New chat/session representing same seat must re-establish server identity; chat memory alone is insufficient.
- Lead question addressed to Zed remains pending until Zed answers.

### Evidence/handoff template — PROPOSED

Each test/report should record:
`case ID | date/time | actor/seat | evidence class | source ref/commit | input/order | action attempted | completion state | output/result | hash/run ID | reviewer | unresolved uncertainty | next owner`.

Use explicit states: `STARTED`, `COMPLETED`, `FAILED`, `UNKNOWN`; and review states: `VERIFIED`, `CHALLENGED`, `NOT_REVIEWED`.

### Folder/index improvements — PROPOSED

- Keep `outbox/`, `inbox/`, `reviews/`, `case-studies/` separation.
- Add a compact machine-readable ledger/index row for each order/report/review pair with exact commit SHA and status.
- Add an `evidence/` index containing references only; keep private/raw secrets outside public repo.
- Add a `recovery-tests/` index separating network, origin, tunnel, Android-process, ledger and connector cases.
- Add `source-boundary` fields to every report: live runtime, GitHub source, ZIP snapshot, screenshot, relay, or memory.
- Preserve Claude's independent review references as Claude-attributed records; do not rewrite them into GPT voice.

## Limitations

1. This was a read-only study. No Pocket Server, tunnel, terminal, connector, GitHub Action, or phone process was started or tested.
2. Claude's retained memory/reviews are **ZED-RELAYED** here. Claude was not called from this builder session.
3. Other sessions' terminal/file-view tests are **ZED-RELAYED** except for what is visibly supported by the screenshots supplied with this order.
4. Screenshots establish what was displayed, not the complete hidden environment, exact request causality, or current state.
5. Historical test counts and some dates come from builder/checkpoint memory and are labeled accordingly.
6. GitHub search on the coordination repository returned relevant A25 records from its indexed/default-branch history; some direct fetches at the coordination ref were unavailable, so search excerpts were not silently upgraded to full-file verification.
7. Private paths/credentials/secret values visible or implied by historical material are deliberately excluded.
8. Current Pocket Server running state remains unknown and outside this order.

## Prioritized next steps — PROPOSED

1. **Lead reconciliation:** compare this report with Claude's independent remembered/review material and preserve disagreements rather than merging voices.
2. **Evidence registry:** bind every historical case to exact source class and immutable commit/file/hash where available.
3. **Identity tests first:** carry Gate-01's successful attribution/cursor lessons into authenticated writer-lane tests before broad file capabilities.
4. **Read-only file API:** implement/test project listing and file reading with strict roots, no-follow/path traversal defenses and content provenance before any write capability.
5. **Recovery matrix:** run origin/tunnel/network/process/reboot cases separately so “connection failed” always identifies the failed layer.
6. **CI visibility contract:** bind workflow evidence to exact commit/run IDs and include it in builder handoffs.
7. **Cold-handoff drill:** give a fresh session only the order, pinned sources and verified snapshot; measure what it can reconstruct without hidden chat memory.

## Source references

### Pocket Server
- `Stratumnova/pockettest`
- `main` / Gate-02A: `f0a11d51968ad598691333d32971dfb483489073`
- auth: `build/gate02a-c1-auth-store` @ `1b578ee32532f99093ab906af52e8b485c90a7e4`
- Shared Stage 1: `build/shared-space-v0` @ `9a419e925dff2de64ef948b7d6d8304eccf8387d`
- Stage 2 proposal: `proposal/shared-space-stage-2-identity` @ `8ade3c00f4f5219182ec01b5154b4b89b71d3359`
- R001: `local build operations and recalls/inbox/A25-PS-MR-R001-POCKET-SERVER-BUILDER.md` @ `da30ba17741abdacdef2f43684aef20d31b9f84d`

### A25 historical/index material surfaced during this study
- `legacy/pockettest/a25-training/governance/AI_FIRST_HUMAN_FIRST_WORKSPACE.md`
- `legacy/pockettest/a25-training/case-studies/A25-F-001-session-availability.md`
- `roundtable/builders-inbox/GB-01-context-sync-2026-10-16.md`
- `roundtable/inbox/RT-001-claude-response-2026-10-16.md`
- `reviews/claude/A25-REV-001-return-review-2026-10-16.md`
- `checkpoints/A25-CP-2026-10-16-2124-gpt.md`
- `case-studies/A25-external-builder-pause-pocket-server-dependency-2026-10-16.md`

### Current-order visual/relay evidence
- Ten screenshots supplied by Zed with A25-PS-MR-O002 request on 2026-10-17, showing historical Termux/tmux, MCP request logs, Uvicorn, cloudflared reconnect/origin failures, and read-only terminal-view development/testing.
- Zed statement: Claude retains reviews in memory and other chat sessions tested terminal and file viewing. Recorded as **ZED-RELAYED**, not independently verified.

## Stop condition

Historical report complete. No server changes, restarts, repairs, production configuration changes, merges, credential inspection, or live endpoint tests were performed.
