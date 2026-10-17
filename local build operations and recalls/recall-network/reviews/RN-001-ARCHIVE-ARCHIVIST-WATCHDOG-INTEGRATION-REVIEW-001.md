# RN-001 Archive / Archivist / Watchdog Integration Review 001
FROM: GPT — A25 Project Lead
FOR: Zed
DATE: 2026-10-17 16:09 MDT (owner-provided)
STATUS: ARCHITECTURE PROPOSAL / SCREENSHOT EVIDENCE REVIEW — NOT IMPLEMENTED

## Evidence
Owner supplied eight Termux screenshots on 2026-10-17 showing: a25-gpt tmux pane; file listings of ~/a25-workshop/gpt, ~/pockettest, ~/pockettest-c1, ~/pockettest-shared and Documents/AI_Workshop; read-only viewport process listening at 127.0.0.1:8770; HTTP MCP responses 200/202/400; named Cloudflare tunnel connection registrations and connectivity checks; later stream cancellation errors; and tmux clear-history. Independent GPT report A25gptrecall_id001 in GitHub inbox and Claude A25clauderecall_id001 ADDENDUM-01 Drive 15XeF8U8oObFrw4ivMzsN_F0b7vYM65UA were reviewed earlier. Screenshots are owner-supplied point-in-time evidence, not direct live access by lead.

## Findings
- Worktree families exist on the phone; filenames are not proof of content or commit.
- Cloudflare precheck shows one UDP region failed and HTTP/2 fallback; four registered connections. Later HTTP origin stream cancellations are errors requiring separate attribution, not automatic proof of full tunnel outage.
- Uvicorn port 8770 shows real MCP requests and mixed responses. The viewport remains a read-only observation surface, not command authorization.
- Screenshot of tmux clear-history shows display cleared; underlying files untouched; other logs not proven cleared.
- Captured listings expose sensitive config filenames; future public capture should use allowlists and redact secret paths.
- Phone document archive listing is partial; unknown checkpoints remain unresolved.

## Proposed architecture (NOT implemented)
1. Evidence Intake: user-approved source adapters for phone manifests, GitHub commit-pinned files, Drive original documents, and GPT/Claude reports. No public-pane secret ingestion. Record who submitted, how observed, source ref and raw hash if verified.
2. Immutable Archive: preserve original bytes, stable source IDs, version and branch identifiers; append-only receipts and manifests. Separate public index from private artifacts.
3. Archivist: parse candidate projects, aliases, components, timelines, test events and status claims; create evidence-linked derived indexes, never silently rewrite originals or conflate separate branches.
4. Watchdog: validate session-ID uniqueness and per-chat addendum convention, hashes, timestamps, source references, scope, status terminology and conflicting claims; quarantine invalid or ambiguous imports and fail aloud. Watchdog reports findings, not automatic repairs.
5. Lead reconciliation: adjudicate evidence conflicts by source revision, component, and observation time; mark unresolved items. Zed approves canonical state changes or sensitive operational actions.
6. Retrieval: project/branch/component/time indexed search returns source + provenance and explicit uncertainty, with GitHub/Drive/phone artifact refs.

## Required minimal event fields
record_id, session_id, report_id, addendum_seq, project_id, original_project_name, aliases, component_id, source_system, source_locator, source_commit_or_revision, author_claim, observer_seat, observed_at_utc, event_at_utc, recorded_at_utc, timezone_of_original, evidence_class, work_status, runtime_status, test_outcome, sha256, hash_verification, supersedes_or_amends, confidentiality, unresolved_questions.
Time types must remain separate; no fabricated timestamps. Dates in screenshots may be local; preserve offset and source clock, convert only when offset is known.

## Operational gates
G0 owner authorization / source classification
G1 identity + reservation and additive report IDs
G2 safe intake + content hash + provenance
G3 parse and source/branch/time normalization without destructive edits
G4 Watchdog rule checks and conflict quarantine
G5 Lead review and Zed approval where needed
G6 publish derived catalog and retrieval index
G7 restore / readback / cross-AI query tests

## Proposed acceptance tests
A. Import GPT report and Claude addendum; preserve both byte-exact and distinct evidence classes.
B. One session ID with multiple addenda succeeds; another chat reusing ID is rejected.
C. Gate-01 and hardened main, auth, Shared Space Stage 1 and Stage 2, and viewport remain separate components.
D. Event #3 posting timestamp cannot become Gate-01 restart recovery timestamp.
E. Filename presence cannot be promoted to source-verified code or tested status.
F. Mismatched hashes or absent post-upload hash produce UNVERIFIED, not PASS.
G. Offline phone or tunnel interruption does not corrupt archive; ingestion retries are idempotent.
H. Restricted files never appear in public viewport, reports, or derived public index.
I. Two AI sessions can retrieve same evidence and report different interpretations without overwriting either original.
J. Restore test from immutable originals reconstructs derived catalog.

## Proposed near-term order
(1) freeze current exchange as study evidence; (2) produce read-only phone manifest with worktree HEAD, file sizes and hashes on approved safe paths; (3) define schema and intake validators; (4) run dry-run Archivist and Watchdog on existing RN-001 records; (5) compare derived outputs with lead; (6) only then consider server integration. No phone commands, builds, merges or deployment authorized by this review.
