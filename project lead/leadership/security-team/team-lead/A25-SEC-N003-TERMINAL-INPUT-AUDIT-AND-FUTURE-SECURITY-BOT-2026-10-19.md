# A25-SEC-N003 — Terminal Input Audit and Future Security Bot Requirements

DATE: 2026-10-19
OWNER: Zed
AUTHOR/SEAT: A25-SEC-GPT01, Security Team Lead
STATUS: INVESTIGATION NOTES + FUTURE REQUIREMENTS (NOT IMPLEMENTED)
BRANCH: coord/a25-namespace-trial-001
RELATED: A25-TW-SEC-O001; A25-SEC-R001; A25-SEC-R002; A25-SEC-ARC-REQ-001

## Owner's question and decision
Zed asked whether actions other than searching/reading occurred on the Pocket Server during the previous approximately 2.5 hours, with emphasis on file edits, deletions, moves and other changes, **not** merely whether MCP requests occurred or who made them. Zed then directed Security to preserve findings for successor recovery and for a future security bot capable of answering these questions. This note records requirements; it is NOT an authorization to build, deploy or change runtime logging.

## Directly observed evidence (VERIFIED within inspection scope)
- On 2026-10-19 at 19:38:48 MDT, terminal `date` returned local time; target retrospective window was approximately 17:08–19:38 MDT.
- `tmux list-sessions` showed `a25-bridge` (created 12:17:20), `a25-gpt` (created 12:19:25), and `a25-tunnel` (created 12:17:28) on October 19.
- `~/.bash_history` was present but last modified October 18 at 18:56. It did not provide a reliable saved record of October 19 commands.
- Live `a25-gpt` tmux scrollback displayed command prompt lines for Security inspection, recovery checks, directory listings, bridge log inspection, modification-time search and input-audit queries. These visible recent commands were read-only.
- Earlier scrollback also showed Archives ZIP handling/extraction and construction/writing of `/storage/emulated/0/Documents/AI_Workshop/ClaudesResponse.md`, consistent with earlier owner-authorized historical work. Their exact execution time could not be established from command lines because pane history lacked per-command timestamps.
- A separate `find ~/a25-workshop/gpt -type f -mmin -90 -print` at 19:36:24 MDT returned no matching files. This covers only regular files with recent modification timestamps in that tree; it does not establish no deletions, moves, directory changes, timestamp-preserving edits or changes elsewhere.
- `a25-bridge` tmux pane showed repeated MCP requests and `CallToolRequest` entries. HTTP log lines lacked timestamps and authenticated caller identity; request presence is not proof of filesystem mutation. A later capture had additional requests, but timing and actions were not attributable.
- Inspection used terminal_send with read-only shell commands and terminal_view; no Security-initiated file edits, moves, deletes, service restarts or credential changes were performed.

## Conclusion with limits
VERIFIED: No write, move or delete command was identified in the visible **recent** prompt entries inspected; no recently modified regular file was found within the scanned workshop tree during the 90-minute metadata check.
HISTORICAL CLAIM / corroborated scrollback: Earlier authorized ZIP extraction and Claude report creation occurred on October 19, but cannot be placed inside or outside the 2.5-hour target window solely by the prompt lines.
UNKNOWN: Whether any unlogged command, non-tmux process, file deletion, rename, preserved-timestamp write or activity outside the scanned tree occurred within that window. No claim of comprehensive filesystem integrity or absence of compromise is warranted.
UNKNOWN: Who invoked individual MCP tool calls; the owner explicitly did not require attribution for this question.

## Future security bot — required questions
The eventual bot should answer, with an explicit time window and confidence:
1. Did any file get created, written, overwritten, renamed, moved, deleted, permissions-changed, or content-changed?
2. Which exact path(s), action type(s), and timestamps? Were they inside the defined monitored scope?
3. Was an operation a read/search only, a process/service change, or a filesystem mutation?
4. What evidence supports each answer (event ID, hash/baseline diff, timestamped command/audit record), and what coverage gaps prevent certainty?
5. If no changes are found, can the bot say `NO CHANGES VERIFIED` only when monitoring coverage is complete; otherwise `NO CHANGES OBSERVED IN COVERED SOURCES`?
6. Did anything alter the running bridge, tunnel, source, credentials, GitHub clone or Documents/AI_Workshop backup?
7. Can it compare current state with a known approved baseline without modifying the target?

## Minimal functional requirements (PROPOSED, not adopted implementation)
- Timestamped append-only action/event records with local timezone and UTC, operation type, affected path(s), result, and correlation ID; separate incoming MCP requests from executed shell actions and filesystem changes.
- File change detection that covers creations, modifications, renames and deletions using a trustworthy initial manifest/hash snapshot plus periodic comparisons or platform-supported event monitoring. Clearly state coverage for unmonitored paths, preserved timestamps, offline gaps, and tampering risk.
- Read-only audit queries for time windows (e.g. `last 2.5 hours`) with concise action summaries, exact evidence pointers, explicit UNKNOWN cases and no false clean bills.
- Monitor at minimum `~/a25-workshop/gpt`, relevant live Pocket Server directories and `Documents/AI_Workshop`, but finalize paths and exclusions with Zed/Workshop Lead; avoid scanning unrelated personal files by default.
- Do not expose token values, credentials, private contents or raw shell input that might contain secrets in reports. Prefer redacted command classification and secure audit custody.
- Preserve existing Workshop tools and operation; bot must not silently block, kill, restart, modify, delete or move files. Any enforcement or remediation requires separate owner authorization.
- Separate READ/SEARCH, WRITE/CREATE, MOVE/RENAME, DELETE, PERMISSION, PROCESS/SERVICE and UNKNOWN events; do not infer mutation from `CallToolRequest` alone.
- Provide test receipts for a harmless controlled create/edit/rename/delete sequence in a designated test directory, plus read-only/no-change cases, coverage failure, baseline restoration and safe rollback. No such test is authorized by this note.
- Evaluate reuse of existing Watchdog/Archives/audit tooling first; Archives request A25-SEC-ARC-REQ-001 is OPEN.

## Follow-up and authority boundary
Zed previously instructed Security to stop before assigning a builder for the bridge auth fix. This bot concept is a distinct future work item, not an assigned builder task. Obtain owner scope/priority and Archives response before any design/build order. Coordinate with Workshop Lead to avoid runtime disruption. Security Lead owns evaluation; Zed owns final decisions.

## Recovery rule
Do not turn `no visible recent mutations` into `nothing changed`. Preserve the original historical records, this evidence ledger and subsequent decisions separately. Repeat a test only to resolve changed runtime, missing coverage, or contradiction.
