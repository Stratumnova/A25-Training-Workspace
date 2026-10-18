# A25-TW-BG-GPT01 — O006 readiness / G2 interface
Date: 2026-10-18
Source: Stratumnova/pockettest build/shared-space-v0
Latest source SHA: 57597e694ca98a33066ad8757b3454d629c3dbf8

VERIFIED: six Zone 1 tools remain registered in shared/server.py on both existing GPT and Claude MCP routes: workspace_inspect(path="."), workspace_read(path), workspace_create(path,content), workspace_edit(path,content), workspace_delete(path), workspace_command(action,path="."). Existing roundtable tools are still present in source. No A25 GPT Terminal viewport/status tool was modified.

O006 source fixes: shared/zone1_workspace.py now validates absolute configured root *before* resolve and rejects actual NUL in paths; shared/tests/test_zone1_workspace.py adds regression coverage. Local source fetch from raw.githubusercontent.com fails with DNS name resolution, so tests remain NOT RUN; phone runtime NOT VERIFIED. Do not activate G2 on the premise of passing tests.

Configuration: A25_ZONE1_ROOT must be an owner-selected absolute Termux-accessible folder; existing A25_SHARED_DATA, POCKET_GPT_PATH, POCKET_CLAUDE_PATH unchanged. Actions: pwd, ls, python_version, pytest. Response contracts unchanged from O004.

Next: obtain actual local pytest and regression output, then Workshop Lead coordinates authorized existing-service update and connector exposure. Separate actions connector must support file operations and commands; preserve A25 GPT Terminal terminal_status and terminal_view.
