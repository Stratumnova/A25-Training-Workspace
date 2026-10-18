# A25-TW-O007 — G2 Separate Actions Entry
FROM: A25-TW-GPT01 TO: A25-TW-BG-GPT02
DATE: 2026-10-18
STATUS: QUEUED; ACTIVATE ONLY AFTER WORKSHOP LEAD REVIEWS G1 R006
Read owner handoff, R004/R005, G1 R006 and current G1 interface before starting.

## Objective
Keep the existing A25 GPT Terminal terminal_view/terminal_status untouched. Provide a SECOND GPT-facing Actions entry with BOTH view/inspection AND commands and file CRUD, backed by the same Zone 1 workspace. No replacement of the read-only viewport. Reuse existing Pocket Server Zone 1 MCP tools; do not create another server.

## Work
Inspect actual existing connector/tool registration and current branch head. Build/adjust source configuration or registration and documentation for a separate Actions entry: inspection/view of workspace files and directory, create/read/edit/delete, workspace command/test execution. Distinguish read-only terminal viewport from action-side view. Preserve compatible tool names from G1 unless coordination requires a documented change. Give exact owner-side connector installation/discovery steps, without publishing secrets. Execute source/contract tests when possible; report any environment blocker honestly. No new repo/branch, no phone changes, no tunnel/service restart or permissions edits in this order. No security redesign or Watchdog.

## Deliverables
Coordination note to G1 in builders-inbox and report project lead/coordination/reports/A25-TW-R007-BG-GPT02-ZONE1-SEPARATE-ACTIONS-ENTRY.md with exact source SHA, tests, errors, and owner setup instructions. Stop. If G1 R006 is failed/blocked, do not start until Workshop Lead resolves dependency.
