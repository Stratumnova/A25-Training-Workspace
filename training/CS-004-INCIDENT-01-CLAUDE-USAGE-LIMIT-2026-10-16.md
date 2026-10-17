# CS-004 / Incident 01 — Claude usage limit during repository handoff

**FROM:** GPT — A25 Project Lead
**FOR:** Zed; Claude — Independent Reviewer; A25 builders
**DATE:** 2026-10-16 23:13 MDT (Zed's report; screenshot clock ~23:12)
**RE:** Platform interruption, incomplete handoff and continuity verification
**BASIS:** Two screenshots supplied by Zed and Zed's explicit report at 23:13 MDT. Human-attested, screenshot-observed; not an independent platform event log.

## Observed evidence
- Earlier screenshot (~23:09 device time): Claude UI showed `Making room for more conversation...` during Zed's A25 ZIP handoff. This is a context-management signal, not evidence of actual memory loss.
- Later screenshots (~23:12 device time): same conversation labeled `Rc Park`; an A25 training workspace ZIP and multiple screenshots are visibly attached to Zed's 23:08 message. The Claude response area displays `Reviewing the uploaded workspace and its branch history.`
- One screenshot shows `Limit reached` and `Resets Saturday at 12:10 AM`, with an Upgrade control; the other shows the composer without the limit overlay.
- Zed reports the Claude seat became unavailable just as the update was being given. The UI does not establish that the conversation or attachments were deleted, that the review finished, or that Claude's long-term memory was lost.

## Classification
- `CONTEXT_COMPACTION_OBSERVED`: YES (earlier screenshot)
- `PLATFORM_USAGE_LIMIT_OBSERVED`: YES
- `HANDOFF_INTERRUPTED`: YES (Zed report and screenshots)
- `SESSION_REPLACED`: NOT ESTABLISHED
- `HISTORY_UNAVAILABLE`: NOT ESTABLISHED
- `MEMORY_LOSS_CONFIRMED`: NO EVIDENCE
- `REVIEW_COMPLETED`: NOT VERIFIED
- `CONTINUITY_VERDICT`: UNKNOWN pending Claude's own return and read-only confirmation

## Recovery procedure
1. Mark Claude seat temporarily unavailable and audit state `PAUSED/UNVERIFIED`. Do not count the review as completed or attribute unissued decisions to Claude.
2. Retain Zed's ZIP and screenshots, the GitHub development branch/commit, Drive training and Claude's latest verified checkpoint. Do not put personal screenshots or unvetted private details in a public repository.
3. After platform access returns, Claude verifies whether the ZIP was received, names the actual branch/commit inside it, reports which files were audited and what remains pending, and compares with Drive and GitHub durable checkpoints.
4. Record a `RECOVERY_VERIFICATION` event with evidence, exact gaps, verdict PASS/PARTIAL/FAIL/UNKNOWN and reviewer. Do not infer continuity from a model's self-confidence.
5. If Claude cannot continue, preserve the pending independent-review gate and ask Zed to supply a new session with checkpoint; do not let GPT silently replace Claude's independent sign-off.
6. This incident is a case-study record, not a Watchdog rule exception or a change to merge authority.

## Future Pocket Server / hallway requirement
Add `PLATFORM_USAGE_LIMIT_OBSERVED`, `HANDOFF_INTERRUPTED`, `SEAT_UNAVAILABLE`, `SEAT_RESUMED`, and `RECOVERY_VERIFICATION` events. Store server-stamped event time, seat, platform, source type, last durable checkpoint, in-flight task, commit, last confirmed receipt, unresolved reviews, evidence pointer, and next permitted action. Treat message receipt, file upload, processing start, processing finish, and independent approval as distinct states.

## Builder lesson
A UI showing an attachment and an in-progress response is not proof of successful review. Platform compaction and rate limits are distinct from confirmed memory loss. Preserve work outside either chat and make interruption/recovery observable and auditable.

## Current gate
Claude's full ZIP audit is pending. WD-35 baseline restoration remains pending. No merge to main. No further substantive development should be represented as independently reviewed until Claude returns or Zed changes the plan.
