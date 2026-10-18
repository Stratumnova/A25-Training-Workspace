# A25-TW-R006 — Zone 1 Test and Termux Plan
FROM: A25-TW-BG-GPT01 (G1)
TO: A25-TW-GPT01
DATE: 2026-10-18
ORDER: A25-TW-O006 at c5a2655efa1975f7d97dd5f4b819668d5759bd68
STATUS: SOURCE REPAIRED; EXECUTION TESTS BLOCKED; PHONE UNTOUCHED

## Read-first and source evidence
Read owner-direction handoff, G1 R004 and G2 R005 (actual filename A25-TW-R005-BG-GPT02-ZONE1-GPT-CONNECTOR-IMPLEMENTATION.md). Inspected current pockettest build/shared-space-v0 source and tests via connected GitHub fetch_file. O006 baseline 4c2f30364075fdf1dced1a297c7458891053d7f3. Original retrieved blobs: shared/zone1_workspace.py f04b3f28b1755cff54956d4840f460bdd3554be9, shared/tests/test_zone1_workspace.py 1bafbee9fcdc18eac46d8d356460608dc5f77321, shared/server.py 0b31819af9d5f8fb155749dcc99674051599d88e.

## Verified source defects and repairs
1. In Workspace.__init__, Path(root).expanduser().resolve() ran before is_absolute(), so relative input was silently made absolute. Changed to check candidate_root.is_absolute() before resolving.
2. In Workspace.path, original check tested the literal two-character escape sequence `\\x00` rather than a real NUL. Changed to `chr(0) in relative`.
3. Added regression test test_reject_relative_root_and_nul_path.

Source commits:
- 7bcd24666fac5a1264f108aad08e40d47b9bfa45 — shared/zone1_workspace.py
- 57597e694ca98a33066ad8757b3454d629c3dbf8 — shared/tests/test_zone1_workspace.py
Latest full source commit SHA: **57597e694ca98a33066ad8757b3454d629c3dbf8**.
No server.py changes. Existing roundtable registrations remain present by static inspection; Gate-01 regression execution is UNKNOWN.

## Actual test evidence
Attempted direct fetch of `https://raw.githubusercontent.com/Stratumnova/pockettest/build/shared-space-v0/shared/zone1_workspace.py` using Python requests in local container.
Observed: `ConnectionError ... NameResolutionError ... Failed to resolve 'raw.githubusercontent.com' ([Errno -3] Temporary failure in name resolution)`.
GitHub connector could read source text and commit changes, but no bridge exists here to transfer fetched bytes into a runnable local checkout automatically. Thus pytest was NOT RUN. No stdout/stderr from tests exists; do not infer PASS. Local static inspection VERIFIED the two defects and exact changes; behavior is UNVERIFIED. MCP discovery, actual shared file lifecycle, Termux installation, tunnel and both-AI acceptance are UNKNOWN. No live tunnel/MCP error was observed in this order.

## Owner-run Termux procedure (NOT EXECUTED; owner/lead must authorize live phase)
These are commands for the owner to run in the *existing* Termux installation, not a request to create another server. Confirm working tree is clean and back up local changes before updating. Do not overwrite local modifications. Substitute the owner's actual existing checkout path; no live path is presumed.

```sh
# In the existing pockettest checkout (owner selects actual path):
pwd
git status --short
git branch --show-current
git fetch origin build/shared-space-v0
git switch build/shared-space-v0
git status --short
git pull --ff-only origin build/shared-space-v0
git rev-parse HEAD
# Expect 57597e694ca98a33066ad8757b3454d629c3dbf8 if no later commits.
```

Select a real Termux-accessible root using owner choice (example below uses HOME, NOT a claimed current path):
```sh
export A25_ZONE1_ROOT="$HOME/a25-zone1"
mkdir -p "$A25_ZONE1_ROOT"
test -d "$A25_ZONE1_ROOT" && printf 'Zone1 root available\\n'
```

Use the *existing* project Python environment and dependencies (activate its venv if one is in use; do not install packages into the running service blindly). If pytest is missing, owner may install it into that environment after reviewing local requirements. From existing checkout:
```sh
cd shared
python -m pytest -q tests/test_zone1_workspace.py
python -m pytest -q tests
```
Capture actual exit codes, stdout/stderr, Python version and pytest version; stop and report failures before restart. Check existing server process/service configuration and preserve existing A25_SHARED_DATA, POCKET_GPT_PATH, POCKET_CLAUDE_PATH, POCKET_ALLOWED_HOSTS and existing terminal bridge. A25_ZONE1_ROOT must be exported in the *environment of the existing server process* before its next authorized restart; setting it in an unrelated shell does not configure an already-running process. Do not restart or change tunnel until Workshop Lead/owner separately approves.

Disposable *local direct-class* check before live connector test:
```sh
cd shared
python - <<'PY'
import os
from zone1_workspace import Workspace
w = Workspace(os.environ["A25_ZONE1_ROOT"])
name = "Shared/o006-disposable.txt"
w.write(name, "zone1 o006 check")
assert w.read(name)["content"] == "zone1 o006 check"
print(w.inspect("Shared"))
print(w.command("pwd"))
w.delete(name)
print("disposable lifecycle complete")
PY
```
This check mutates only the named disposable file in the selected root; ensure it does not already exist. It is NOT an MCP test. After authorized existing-service update, G2 checks the separate actions connector for workspace_inspect/read/create/edit/delete/command, then runs the disposable lifecycle through GPT tools, then Claude edits same file, then GPT rereads. Preserve terminal_view and terminal_status unchanged.

## G2 coordination
Published builders-inbox/A25-TW-BG-GPT01-2026-10-18-O006-READINESS-AND-G2-HANDOFF.md at coordination commit ce778ff7e49f6c294c6f4775037fbe4b14c3b7b1. Six signatures unchanged. G2 must not infer source-test PASS or phone deployment from this report.

## Limitations and next justified action
Source only: no local executable checkout, no test PASS, no live phone changes. Workspace remains a local-trust prototype with non-atomic writes, no concurrent revision guard and allowlisted commands only. Recommend Workshop Lead obtain owner-run Termux test logs before G2 activation, and issue a separate authorized live update if green. If tests fail, return to G1 for scoped repair. This report does not authorize a restart.

Formal report path: project lead/coordination/reports/A25-TW-R006-BG-GPT01-ZONE1-TEST-AND-TERMUX-PLAN.md
Report publication commit SHA is returned after file creation; it is not self-referentially inserted here.
