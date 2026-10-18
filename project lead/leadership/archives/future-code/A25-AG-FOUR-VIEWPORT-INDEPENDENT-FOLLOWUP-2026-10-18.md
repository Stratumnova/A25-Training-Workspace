# A25 Archives — Independent Four-Viewport Follow-up
Date: 2026-10-18
From: A25-AG-GPT01, Archives Lead
Trigger: Workshop request at commit 676cadd5d94f55cca31caf607d4ef372c7074406
Status: PARTIAL PASS; unresolved session-schema discrepancy. Read-only.

## Exact tool schema visible to Archives
mcp__A25_GPT_Terminal__terminal_status(args: object)
mcp__A25_GPT_Terminal__terminal_view(args: object)
Description: "Read the visible A25-GPT shared tmux terminal without sending input."
Neither exposed definition documents a session property or a session enum. Archives cannot responsibly assume support for session=... or claim an unauthorized-session rejection test is possible via its documented interface.

## Independent tool calls
- terminal_status({}) succeeded: identity gpt-workshop, workspace_exists true; src/tests/logs/reports/backups/config true; mode read-only.
- terminal_view({}) succeeded: session a25-gpt, read_only true, returncode 0, error empty. Screen shows Zone 1 server source and terminal test commands/output.
- Repeated observation produced the same a25-gpt screen. No evidence of a session selector being exposed after this check.
- No tool transport failure observed in these two calls.

## Per-session results
| Requested session | Result | Evidence class |
| a25-gpt | Returned by default call; read_only true; returncode 0; error empty | VERIFIED |
| a25-test | Cannot request using documented schema | UNKNOWN |
| a25-bridge | Cannot request using documented schema | UNKNOWN |
| a25-tunnel | Cannot request using documented schema | UNKNOWN |
| clearly unauthorized name | Cannot safely exercise without documented session argument | NOT TESTED |

## Source backup verification
Workshop GitHub report at commit 92c09ba03fc46ebdc29b211ad3671845016ead25 was independently fetched by Archives. It reports archive SHA256 5c504d82cf8a7694d7178d34d1de18a4079bcd768f737245e8130af7882864ae and three tar entries. Archives has no read-only remote file/hash/extract tool for phone archive; terminal_view cannot issue commands. Thus direct archive byte verification and isolated restore are UNKNOWN, not disproven.

## Assessment
VERIFIED: Archives connector exposes only object arguments without documented session selector; default terminal view works; Workshop request exists.
WORKSHOP-REPORTED: Earlier four-session terminal_view(session=...) calls worked; later intermittent internal failures; archive hashes and listing verified in Workshop's test.
UNKNOWN: Whether differing connector schema versions, cached registration, permissions, or transient transport explain discrepancy. No basis to classify as an implementation defect. Reconnecting is not offered as a tool operation in Archives seat; do not change connector settings under a read-only audit.

## Recommendation (not authorization)
Project Lead / Workshop should compare the exact connector schema registered in each seat and the server's documented parameter contract, without changing the running service for this audit. If independent replication is required, provide Archives an authorized read-only interface exposing session selection. Separate owner-approved offline restore test can be designed later. Preserve both reports.

## Source-access ledger
- GitHub Workshop follow-up at commit 676cadd5d94f55cca31caf607d4ef372c7074406: retrieved.
- GitHub backup report at commit 92c09ba03fc46ebdc29b211ad3671845016ead25: retrieved previously.
- A25 Terminal status/view: directly called; both succeeded.
- Gate-02 phone archive raw bytes: unavailable through Archives tools.
- Four individual session outputs: unavailable through Archives connector's documented schema.
No terminal input, source change, connector change, restart, deployment, or permission change.
