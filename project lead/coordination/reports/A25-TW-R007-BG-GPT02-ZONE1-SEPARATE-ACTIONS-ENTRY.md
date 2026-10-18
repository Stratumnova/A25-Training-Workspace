# A25-TW-R007 — Separate GPT Actions Entry

FROM: A25-TW-BG-GPT02 (G2)
TO: A25-TW-GPT01 — Workshop Lead
DATE: 2026-10-18
ORDER: A25-TW-O007 at 5fa9d98433d41092d8bbad79b8d7a62698a2b345
STATUS: SOURCE-ONLY CONFIGURATION AND CONTRACT CHECK COMMITTED; CONNECTOR INSTALLATION AND LIVE TESTS PENDING

## Authorization and prerequisite
Read lead clearance at f95a199aa8f648aff3c1dfa7ea989c8c41bd6c2d, expressly releasing O007 for source-only work. Read G1 R006 from `project lead/coordination/reports/A25-TW-R006-BG-GPT01-ZONE1-TEST-AND-TERMUX-PLAN.md`; G1's latest reported source fix SHA was `57597e694ca98a33066ad8757b3454d629c3dbf8`; its pytest was NOT RUN. Also consulted owner direction, R005 and O007 from prior reads. Directly fetched current `shared/server.py`, `shared/zone1_workspace.py`, new source artifacts on existing `build/shared-space-v0` branch.

## Implementation and exact changed paths
Repository: `Stratumnova/pockettest`
Existing branch: `build/shared-space-v0`
1. NEW `shared/zone1_actions_entry.json`: machine-readable separate ChatGPT MCP connection manifest naming six existing Zone 1 workspace tools, GPT endpoint reuse, allowed command actions, and distinction from terminal viewport. This JSON is source metadata, **not** an automatically installed ChatGPT connector.
2. NEW `shared/ZONE1_ACTIONS_ENTRY.md`: practical owner-side setup and discovery instructions, action-side viewing versus terminal viewport, disposable CRUD/command tests, Claude follow-up, limits.
3. NEW `shared/check_zone1_actions_contract.py`: offline Python source-contract assertion script for six registrations and existing GPT MCP mount.

Source commits: `fe8635e592acdf38a5d5170c38e0f62f27b2aa0d`, `076e4123e29f9cd82d309ff936600744fed4b406`, `b264897199b23d2692ccb1b399f4c7fd03390672`.
**LATEST FULL SOURCE COMMIT SHA: `b264897199b23d2692ccb1b399f4c7fd03390672`.**

The existing `shared/server.py` already registers `workspace_inspect`, `workspace_read`, `workspace_create`, `workspace_edit`, `workspace_delete`, `workspace_command` on the GPT MCP endpoint. G2 did NOT change `shared/server.py`, the original read-only A25 GPT Terminal plugin, phone service, routes, tunnel, credentials or permissions. The second entry is a separately configured ChatGPT MCP connector to the existing GPT route; it does not add a new server. The source artifacts alone cannot create or install a ChatGPT connector.

## Source contract test evidence
Using direct GitHub fetches and JavaScript assertions on retrieved source bytes:
- PASS: six unique manifest workspace tool names.
- PASS: six matching `shared/server.py` registrations.
- PASS: `GPT=make_mcp("gpt")` and `Mount(GPT_PATH,app=GPT.streamable_http_app())` present.
- PASS: manifest declares no new server or route.
- PASS: command catalog `pwd`, `ls`, `python_version`, `pytest` present in implementation.

These are STATIC SOURCE checks, not execution of `check_zone1_actions_contract.py` or pytest. Python checker NOT RUN; pytest NOT RUN; no source/runtime PASS inferred from G1's R006. Live MCP discovery, ChatGPT connector setup, Android file operations, commands and Claude cross-seat operations NOT RUN.

## G1 coordination
NEW `project lead/coordination/builders-inbox/A25-TW-BG-GPT02-2026-10-18-O007-ACTIONS-HANDOFF.md`
Coordination commit: `bf22970bf8a9682bd6bfe3a4c18da24df1f76698`.
G1 requested to run offline checker and pytest when environment permits, preserve six tool signatures and viewport.

## Owner-side activation instructions (NOT EXECUTED)
1. G1/owner, under separate live approval, validate source tests in existing Termux checkout and update **existing** Pocket Server process with `A25_ZONE1_ROOT` configured in its service environment; preserve current terminal viewport service and routes.
2. Keep A25 GPT Terminal read-only plugin unchanged. In ChatGPT Plugins/Connectors management, create a **second MCP connector entry** named `A25 Zone 1 Actions`, using the existing GPT Pocket Server Streamable HTTP HTTPS endpoint (owner's tunnel + existing private GPT route). Never post endpoint secret route publicly.
3. Refresh/discover six `workspace_*` tools. `workspace_inspect` and `workspace_read` provide action-side viewing; the original `terminal_view` remains a separate pane. If the UI cannot create a second connection to the same endpoint, report exact blocker; do not invent a new service or endpoint.
4. Execute disposable file create/read/edit/delete and `workspace_command("pwd",".")`, then a disposable pytest project, recording outputs. Claude edit/GPT reread only after separate Claude activation.

## Limitations / next justified action
Separate Actions entry is configured **by owner through ChatGPT UI**, not programmatically created by the manifest. This order delivered source metadata, documentation and static checker; actual installation and live tool exposure remain UNKNOWN. Existing command tool is allowlisted, not arbitrary shell; `workspace_edit` replaces entire content. Local trust applies; no Watchdog or auth redesign attempted.

Workshop Lead should coordinate G1 test results and separate owner-approved phone deployment/ChatGPT connector installation before live acceptance. No new repo, branch, phone action, restart, permission change, or live credential publication.

## Report publication
Full report commit SHA returned by GitHub create-file result and reported in completion message, rather than self-referentially guessed here.
