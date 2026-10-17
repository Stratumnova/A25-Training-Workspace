# 04 — Builder Training Cases

FROM: GPT — A25 Project Lead
FOR: Local GPT builders, Claude, future A25 agents
DATE: 2026-10-16
RE: Reproducible learning from WD-30, WD-35 and CS-004
BASIS: GitHub source records, Actions evidence and Zed's incident screenshots as described in CS-004

## Case WD-30 — Watchdog catches its own lead
**Input situation:** GPT authored an outgoing Claude handoff note but placed it in protected `roundtable/inbox/` without manifest digest and DATE header.
**Observed result:** Actions #30 FAIL, W2 unmanifested file and W3 missing DATE.
**Correction:** Preserve original, Zed-approved one-time W3 exemption with sidecar, corrected outgoing note in `roundtable/gpt/`, add digest in `manifests/ADDITIONS.sha256`.
**Builder exercise:** Given an outgoing handoff and incoming protected inbox, choose the proper path and verify W2/W3 before push. Simulate missing DATE and missing manifest entry in a disposable repository; expected FAIL. Do not rewrite the original protected evidence.
**Passing answer:** Correct lane, complete headers, proper digest if protected, evidence-linked report. Do not claim the W3 exemption means future violations are acceptable.
**Source:** `exceptions/WD-30-handoff-exception.sidecar.md`, `training/ACTIONS-REPORTS-AND-LESSONS-2026-10-16.md`, Actions #30.

## Case WD-35 — Frozen baseline with no newline
**Input situation:** A SHA-256 manifest frozen as baseline did not end in newline; appending a new digest glued two records and broke W1/W4.
**Observed result:** #31–#37 red; run #37 had 21 unit tests OK but actual repository 1 FAIL, 4 WARN.
**Correction:** Separate additions manifest, Zed approval, Claude review of narrow design, exact Git blob restoration under one-time W4 marker and sidecar. Run #46 PASS; #47 23 tests OK and actual repository 0 FAIL, 4 WARN.
**Builder exercise:** In a disposable repository create a manifest without terminal newline, demonstrate unsafe concatenation, then design safe additive coverage and narrow exact-byte restoration. Verify any different source/target blob and unrelated manifest rewrite are still rejected. Existing WD-35 added tests are static guard checks, not a full behavioral proof; the behavioral test remains an explicit improvement task.
**Passing answer:** Exact source/target provenance, no broad bypass, individual sidecar, real validator and Actions results, reviewer distinction. Do not call Git SHA-1 blob IDs SHA-256.
**Source:** `manifests/W4_RESTORATIONS.txt`, `exceptions/WD-35-baseline-restoration.sidecar.md`, `training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md`, Actions #37/#46/#47.

## Case CS-004 — Platform compaction and usage limit
**Input situation:** Claude received an A25 ZIP handoff; screenshot showed `Making room for more conversation...` and later `Limit reached — Resets Saturday at 12:10 AM` during visible review activity.
**Observed result:** Zed reported interrupted handoff; ZIP receipt/completion, memory loss, deletion and independent audit completion were NOT established.
**Correction protocol:** Record `CONTEXT_COMPACTION_OBSERVED`, `PLATFORM_USAGE_LIMIT_OBSERVED`, `HANDOFF_INTERRUPTED`; retain last durable checkpoint, mark seat unavailable and review UNKNOWN. On return verify attachment receipt, audited commit/files and outstanding work before marking recovered.
**Builder exercise:** Given the screenshots and incident report, classify what is observed, reported and unknown. Write a recovery event that does not invent review completion or identity.
**Passing answer:** No fabricated Claude vote, no claim of memory loss, explicit pending independent review and source pointers.
**Source:** `training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md` and `training/CS-004-CONTEXT-COMPACTION-AND-SESSION-CONTINUITY.md`.

## Training administration
These are exercises, not authorization to alter the live A25 repo. Run modifications only in disposable fixture repos or a separately approved task branch. Capture inputs, expected/actual outcomes, diff, test commands, results and independent reviewer status. Do not overwrite historical cases; add correction notes if a lesson changes.
