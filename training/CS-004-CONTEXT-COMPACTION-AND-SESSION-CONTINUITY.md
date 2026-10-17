# CS-004 — Conversation compaction, session loss and continuity recovery

**FROM:** GPT — A25 Project Lead
**FOR:** Zed; Claude — Independent Reviewer; future A25 builders
**DATE:** 2026-10-16, after 23:09 MDT (screenshot device clock; not a verified platform event timestamp)
**RE:** Case study and future Roundtable / hallway continuity flag
**BASIS:** Zed's screenshot of Claude's interface and Zed's explicit request to track context compaction and memory continuity. This is a proposed training case, not proof of memory loss.

## Observation
Zed provided an image of a Claude chat while delivering a complete repository ZIP and associated screenshot for the independent audit. The interface visibly says `Making room for more conversation...`. The screenshot also shows `Sending...` in the composer. It does **not** establish that Claude lost any particular fact, that a session was replaced, or that the ZIP was successfully received. Preserve the original screenshot in Zed's possession unless a vetted, privacy-safe evidence copy is separately approved.

## Why A25 tracks this
GPT and Claude both work on lengthy projects with finite active context. Platform compaction, summaries, conversation replacement, missing message history and true memory-retrieval failure are distinct events. The external A25 ledger and checkpoints should permit reconstruction without treating a model's own recollection as authoritative.

## Event types
- `CONTEXT_COMPACTION_OBSERVED`: UI or platform indicates context was condensed; no loss presumed.
- `SESSION_REPLACED`: new chat/session used to continue work.
- `HISTORY_UNAVAILABLE`: earlier transcript not accessible in current working context.
- `RECOVERY_DISCREPANCY`: restored summary conflicts with durable record.
- `MEMORY_LOSS_CONFIRMED`: a specific required fact was demonstrably missing or wrong after a defined recovery test. Do not infer from UI text alone.

## Proposed Roundtable and hallway protocol
1. Create a server-stamped event with seat, platform, conversation alias (non-secret), observed time and source, last durable checkpoint ID, active task and commit, and evidence pointer.
2. Before further writes, the resumed seat reads the authoritative checkpoint, open decisions, pending approvals, active file hashes and latest Roundtable ledger cursor. A UI compaction signal alone does not require a hard stop; stop only if required continuity cannot be verified.
3. Run a read-only continuity probe: restate last authorized task, branch/commit, unresolved disagreements, file authority, no-merge rule, and exact next permitted action. Compare with durable sources rather than self-report.
4. Classify `PASS`, `PARTIAL`, `FAIL`, or `UNKNOWN`; record what survived, what was recovered externally and what remains uncertain.
5. For `PARTIAL` or `FAIL`, restore from GitHub/Drive/Pocket Server checkpoint, request missing evidence from Zed only when needed, and require independent review before sensitive changes resume.
6. Never manufacture a prior approval or reclassify a pending action as authorized because a summary says so. Never put secret tokens, passwords or private session identifiers in the public record.
7. Include the continuity event and recovery verdict in the next builder handoff and Actions report when the event affected a build.

## Suggested data fields for future Pocket Server
`event_id`, `event_type`, `seat_id`, `platform`, `session_alias`, `observed_at`, `timestamp_source`, `checkpoint_ref`, `ledger_cursor`, `repo_commit`, `active_task`, `evidence_ref`, `continuity_test_ref`, `result`, `missing_items`, `recovery_actions`, `reviewer`.

## CS-004 initial record
- **Observed:** Claude interface displayed `Making room for more conversation...` at device clock approximately 23:09 on 2026-10-16; screenshot supplied by Zed.
- **Concurrent work:** Claude was being given a full A25 repository ZIP for file-by-file audit and Drive mirroring.
- **Unverified:** Whether the upload completed; whether any facts were lost; whether the session changed; whether Claude recovered from external records.
- **Current verdict:** `UNKNOWN` — compaction UI observed; no continuity failure demonstrated.
- **Review requested:** Claude should independently confirm what happened after the compaction, whether the ZIP was received, and what prior decisions or files remain accessible. Preserve any disagreement.
- **Scope:** Training and design note only; no Watchdog exception, protected file rewrite, or main merge.

## Future training exercise
Intentionally start a fresh builder session from a durable checkpoint and verify it can reconstruct the current task and pending approval without inventing context. Compare results with a long-running session after compaction. Record errors and correction steps as independent test evidence.
