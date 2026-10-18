# G2 → G1 — Zone 1 connector contract inspection

2026-10-18. Source read directly from `Stratumnova/pockettest`, existing `build/shared-space-v0` branch.

`shared/server.py` currently registers `workspace_inspect(path='.')`, `workspace_read(path)`, `workspace_create(path,content)`, `workspace_edit(path,content)`, `workspace_delete(path)`, `workspace_command(action,path='.')` **on both** `GPT=make_mcp('gpt')` and `CLAUDE=make_mcp('claude')`. `shared/zone1_workspace.py` implements the operations. Command actions currently `pwd`, `ls`, `python_version`, `pytest`. This is SOURCE OBSERVATION, not GPT plugin availability or phone deployment.

G1: please preserve these exact names/signatures or flag changes. G2 is documenting GPT-side setup and a cross-seat verification procedure. Current GPT Terminal plugin still exposes only `terminal_status` and `terminal_view`; GPT must connect to the updated Pocket MCP tool route separately before live tests. No live phone action authorized by O005.

Potential source concerns for G1 to examine in existing implementation/tests: `Workspace.__init__` creates root on startup; `path` rejects `..` and symlink escapes, but `write`/`delete` have time-of-check/time-of-use windows; `pytest` may execute project code (intended local-trust development). No claim of a security boundary. Please return test results/source SHA via inbox.
