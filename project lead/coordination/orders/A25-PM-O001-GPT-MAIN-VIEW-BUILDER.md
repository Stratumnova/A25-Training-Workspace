# A25-PM-O001 — GPT Main-View Builder
FROM: GPT A25 Project Lead
TO: A25-PM-GPT01 — ONE FRESH GPT SESSION
DATE: 2026-10-17
PHASE: READ/PLAN FIRST; implementation only within existing approved paths and available tools

## Mission
Build the smallest working shared READ VIEW on existing Pocket Server hardened main, without changing the separate read-only terminal viewpoint. This is the first milestone of LEAD-DIRECTION-007. Do not start shared write or terminal execution yet.

## Starting evidence
Local ~/pockettest main HEAD f0a11d51968ad598691333d32971dfb483489073; tracked-clean at last owner-run check. ~/pockettest-c1 auth and ~/pockettest-shared are distinct branches/worktrees, not substitutes for main. Existing viewpoint ~/a25-workshop/gpt is separate. These are historical observations, not current verification.

## Rules
1. Read project lead/coordination/README.md, leadership Directive 006 and Direction 007; inspect current pockettest main source and existing tests. State exactly what you can access. Do not invent phone shell access.
2. Reuse existing repo, branch, directories, tests and server components. Do not create new repos/branches/folders or alter viewport.
3. First send lead a concise existing-file map and precise minimal code change plan, identifying any files that predate this order. Do not change prior code without explicit owner authorization.
4. Once authorized, implement ONLY read/view functionality on main. Require evidence that both GPT and Claude can access same designated source; coordinate independent verification through lead.
5. Test in sequence: initial viewing, stop, restart, both-view retest, stop. Zed controls phone operations until AI execution exists. Do not fake start/stop or tests.
6. If blocked, report to lead with command/tool, exact error, file/path and proposed next fix. Do not ask Zed to debug or create a new path. If reporting channel unavailable, output an exact report for relay, identifying delivery as BLOCKED.
7. No security redesign, Watchdog enhancement, Archivist work, new permission framework or future write/terminal stage.
8. Never merge to protected main or modify live phone server without Zed's explicit instruction.

## Reporting
Use existing project lead/coordination/reports/ and existing coordination branch if permitted. First report file: A25-PM-R001-GPT01.md. Include FROM, TO LEAD, scope, inspected files/SHAs, tests actually run, status PASS/FAIL/BLOCKED, outstanding work. Do not send troubleshooting tasks to Zed. Stop after first report and await lead order.
