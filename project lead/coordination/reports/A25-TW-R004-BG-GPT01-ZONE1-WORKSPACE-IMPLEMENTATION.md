# A25-TW-R004 — G1 Zone 1 Workspace Implementation
Seat: A25-TW-BG-GPT01
Order: A25-TW-O004 at 015b1eda09e9bc48d745c4911c4d17c637e03ca4
Status: SOURCE IMPLEMENTED; LOCAL EXECUTION AND PHONE RUNTIME UNVERIFIED

## Sources and scope
Read owner-direction handoff at a3a5387222911959ecc96b2af61a3dd67d536a33 first, then O004. Source branch checked before changes: Stratumnova/pockettest build/shared-space-v0 at 9a419e925dff2de64ef948b7d6d8304eccf8387d. Preserved existing Gate-01 roundtable contracts and existing MCP transport. No new branch/repository, no phone/tunnel/server action.

## Source commits (verified GitHub write receipts)
1. b9c4b019997b49bdec2f81c7efc781cae014014c — added shared/zone1_workspace.py.
2. 33122659528015a1187661f9bbc108410f1b2c27 — updated shared/server.py to register workspace tools on both existing MCP endpoints and configure A25_ZONE1_ROOT during lifespan.
3. 0120591d037a0a9f24c1add8ad4b144c50c647c6 — added shared/tests/test_zone1_workspace.py.
Latest source commit: 0120591d037a0a9f24c1add8ad4b144c50c647c6.

## Implemented interface
workspace_inspect(path="."); workspace_read(path); workspace_create(path,content); workspace_edit(path,content); workspace_delete(path); workspace_command(action,path=".").
Both existing GPT and Claude MCP instances register the same tools. Commands: pwd, ls, python_version, pytest (Python -m pytest -q). Subprocess timeout 30 seconds, stdout/stderr bounded. Files UTF-8 and maximum 1 MB. Paths resolved under one configured root; relative traversal and outside-root symlink resolution rejected. Optional GPT/Claude/Shared directories are conventions, not access controls.

## Evidence and execution results
VERIFIED: GitHub acknowledged source file creation/update and test file creation at commits above.
VERIFIED: Attempted local source retrieval with curl from raw.githubusercontent.com; failed with `curl: (6) Could not resolve host: raw.githubusercontent.com`. Subsequent import-based test attempt failed `ModuleNotFoundError: No module named 'zone1_workspace'` because source could not be downloaded into local runtime. This is an environment access blocker, not a code test result.
UNKNOWN: pytest outcomes, actual sample lifecycle execution, MCP tool discovery, Android/Termux runtime, concurrent writes, Gate-01 regression status. Test code describes a sample create/read/edit/list/pwd/python/ls/delete lifecycle, but it was NOT executed. No fabricated PASS claim.
KNOWN LIMITS: local-trust prototype; command catalog restricted (no arbitrary shell, pip or git); no revision/locking for concurrent file edits; workspace symlinks resolving within root may be followed; existing shared endpoint gate-path access persists; text-only files; test dependency pytest needed. Runtime must be configured before lifespan starts.

## Repeatable setup (instructions only; NOT executed on phone)
In existing pockettest checkout on build/shared-space-v0, set `A25_ZONE1_ROOT` to the owner's chosen absolute Termux-accessible directory; preserve existing `A25_SHARED_DATA`, `POCKET_GPT_PATH`, `POCKET_CLAUDE_PATH`, allowed-host and other deployment configuration. Install existing MCP/Starlette/Uvicorn dependencies and pytest in the existing environment. Run `cd shared && python -m pytest -q tests/test_zone1_workspace.py` then existing suite; start the existing server with the already-approved host/port/tunnel process only after separate owner authorization. Both existing MCP routes then expose the six tools. No path on the phone has been presumed.

## Coordination
G2 handoff published at project lead/coordination/builders-inbox/A25-TW-BG-GPT01-2026-10-18-ZONE1-O004-G2-INTERFACE.md, coordination commit 0e6f082d9cf024c9cb987c847827a3a2fbdb20b1. G2 owns connector exposure and invocation, not source implementation.

## Next justified action
Workshop Lead should arrange source test execution in an environment able to fetch the branch, evaluate failures and regression results, then authorize any fixes. Only after source verification and G2 connector confirmation should owner separately approve phone deployment and real two-AI shared-file acceptance. This report is not proof of a working phone workspace.

## Report publication
Formal report path: project lead/coordination/reports/A25-TW-R004-BG-GPT01-ZONE1-WORKSPACE-IMPLEMENTATION.md
The full report commit SHA is returned by GitHub after this file is created; it cannot be embedded in its own content without a later addendum.
