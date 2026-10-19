# Workshop Clean Up Notes — Intake

Date: 2026-10-19
Owner: Zed
Seat: A25-TW-GPT01, Workshop Lead
Status: REVIEW ONLY; no cleanup or deletion authorized.
Cutoff: October 18, 2026 at 3:00 PM Mountain Daylight Time.

## Owner evidence priority
Work from the current Workshop session and its notes after the cutoff is the primary grounded baseline. This owner-adopted priority does not independently verify every claim. Anything older than the cutoff, or not demonstrated to support the current running system, is a REVIEW CANDIDATE. Age or non-use in a limited test is not proof that a component is disposable. Preserve original evidence and classify VERIFIED, ADOPTED, HISTORICAL CLAIM, REFERENCE, SUPERSEDED and UNKNOWN separately.

## Post-cutoff evidence
- GPT terminal_status reported identity gpt-workshop and mode read-only; that status label did not enforce filesystem read-only behavior through terminal_send.
- GPT terminal_view worked on a25-test and a25-gpt; a25-claude returned Session not permitted.
- GPT terminal_send executed copy, byte verification, deletion and append in a25-test, with successful observed outputs.
- Claude reported copy, deletion, append and read. Shared terminal viewport displayed Claude append result for claudeedittest.md, 2736 bytes, SHA-256 f1daf4a5dfa49633cb78d13535bdb5be9f7b054c42835397f4a73873c2aa15ba. Principal attribution is not independently audited.
- GPT appended its response to gptedittest.md, verified 2995 bytes, SHA-256 99ec89c5cf48ff51dd91802ac94545eabb67a4ea63faaa85a17b60e4951af205. Claude reported independently reading it.
- GPT and Claude MCP request traffic appeared in a25-gpt server viewport; exact process, source and port serving Claude remain UNKNOWN.
- Owner confirms Workshop progression from viewport-only to terminal views to working controls. Exact implementation dependencies remain to be mapped.

## Candidate register
| Candidate | Evidence | Proposed handling |
| --- | --- | --- |
| Working GPT MCP terminal connection | Directly tested | KEEP; map implementation |
| Claude MCP terminal connection | Claude report plus shared session evidence | KEEP; map implementation |
| a25-test shared shell | Both AIs used it | KEEP FOR NOW |
| a25-gpt server-log session | Viewed successfully | KEEP FOR NOW |
| Active tunnel, port and startup chain | Exact dependency unverified | UNKNOWN; do not touch |
| Workshop src/config | Existence reported, active files unknown | INVESTIGATE |
| Earlier pockettest, pockettest-c1, pockettest-shared worktrees | Historical mapping only | LEGACY REVIEW |
| Earlier bridge.py and chatgpt_readonly snapshots | Backup filenames observed | ARCHIVES REVIEW |
| gate01-pre-reopen, pockettest-pre-zone1, Gate-02 checkpoint archives | Historical backup filenames observed | ARCHIVES REVIEW |
| Old logs, tests, reports, connector reference docs | Use not established by current exchange | INVESTIGATE |

## Archives review fields
For each item: exact path; origin and timestamp; pre/post cutoff; actual current use; process/import/port references; verified evidence; backup uniqueness and recovery value; proposed KEEP / ARCHIVE / INVESTIGATE / PROPOSE REMOVE; separate Zed decision.

## Restrictions
No terminal modification, deletion, move, cleanup, restart, deployment, permissions change, or new session. No claim of unused without dependency checks. No secret values or private raw ledger content in public notes. Archives recommendation is not owner approval.

## Next step
With explicit owner authorization, perform a bounded read-only process, port, tunnel, source, session and startup dependency map; compare it to historical components. Do not remove anything without a later owner decision.