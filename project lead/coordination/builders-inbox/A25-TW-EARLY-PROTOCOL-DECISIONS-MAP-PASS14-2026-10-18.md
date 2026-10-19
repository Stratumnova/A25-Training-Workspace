# A25 Workshop — Early Protocol and Decisions Map Pass 14
Date: 2026-10-18
STATUS: VERIFIED read-only historical document excerpts; implementation unverified
FROM: A25-TW-GPT01

## Files inspected on Android a25-test
- ~/pockettest/gpt/NOTES.md: heading GPT Workspace Notes; describes shared operational memory.
- ~/pockettest/claude/READ_ME_FIRST.md: Claude entry point; goal of GPT/Claude same owner-controlled Pocket Server without paid model API; V1 project files read-only, Roundtable append only.
- ~/pockettest/protocol/POCKET_SERVER_V1.md: remote MCP; phone authoritative; auth identity gpt/claude/owner server-derived; tools server_status, list_projects, list_files, read_file, read_roundtable, append_roundtable; durable ledger/cursors; project files read-only.
- ~/pockettest/shared_context/CURRENT_STATE.md: owner-write projects, GPT/Claude read-only, separate credentials, Roundtable read+append, no model API calls; Claude connector research reported OAuth/no-auth intersection; HTTPS reachability and tool-write capability unproven at that historical stage.
- ~/pockettest/shared_context/DECISIONS.md: D001 owner controls files; D002 GPT/Claude project read-only; D003 only Roundtable append writable; D004 separate credentials; D005 server-derived identity; D010 shared context both can read.
- ~/pockettest/shared_context/OPEN_ISSUES.md: historical open items include ChatGPT endpoint reachability, Claude endpoint reachability, Android tunnel/relay selection.

## Design evolution and discrepancy
Original V1 was read-only for project files and append-only for Roundtable. Later Zone 1 source contract proposes shared file create/edit/delete and bounded command actions including pytest. Treat this as distinct scope/evolution; do not silently substitute later behavior for V1 authorization. Whether later source is approved, installed or safely isolated remains separate.

## Evidence classifications
VERIFIED: bounded grep output from the six named historical Markdown files, with document paths and line numbers; a25-test prompt and end marker.
HISTORICAL CLAIM: connector research, staging status, proposed authentication and capability design.
ADOPTED: only the current read-only mapping instructions, not automatic adoption of historical implementations.
UNKNOWN: original platform-side plugin IDs/count, current remote registration, whether V1 or Zone 1 capabilities are active, current caller identity guarantees.

## Limits
Only heading/keyword-matched lines were viewed, not every line of the six files. No secret values, archive contents, personal storage or runtime operations were inspected. No phone modifications.
