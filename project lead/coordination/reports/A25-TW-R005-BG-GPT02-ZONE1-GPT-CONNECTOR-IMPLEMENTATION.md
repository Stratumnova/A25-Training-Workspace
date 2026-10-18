# A25-TW-R005 — Zone 1 GPT Connector Implementation

FROM: A25-TW-BG-GPT02 (G2)
TO: A25-TW-GPT01
DATE: 2026-10-18
ORDER: A25-TW-O005 at 53b181b35f76a797ed8de7619de4cb588305fcef
STATUS: SOURCE DOCUMENTATION COMMITTED; LIVE GPT CONNECTOR NOT EXPOSED; RUNTIME TESTS NOT PERFORMED

## Read-first evidence
- Owner-direction handoff at a3a5387222911959ecc96b2af61a3dd67d536a33 read directly from GitHub.
- G1 interface proposal and R001 read directly from coordination branch.
- Existing source `Stratumnova/pockettest`, `build/shared-space-v0`: `shared/server.py` and `shared/zone1_workspace.py` read directly using GitHub connector.

## Source observations (VERIFIED as retrieved bytes, not live runtime)
`shared/server.py` currently registers six tools for both `GPT=make_mcp("gpt")` and `CLAUDE=make_mcp("claude")`: `workspace_inspect(path=".")`, `workspace_read(path)`, `workspace_create(path,content)`, `workspace_edit(path,content)`, `workspace_delete(path)`, `workspace_command(action,path=".")`. `shared/zone1_workspace.py` provides the underlying file operations and bounded commands `pwd`, `ls`, `python_version`, `pytest`. This means the necessary GPT-facing registrations were already present in the existing branch when G2 inspected it; G2 did not duplicate or overwrite G1's code.

## Committed source contribution
Repository: `Stratumnova/pockettest`
Branch: `build/shared-space-v0`
NEW PATH: `shared/ZONE1_GPT_CONNECTOR.md`
FULL SOURCE COMMIT SHA: `4c2f30364075fdf1dced1a297c7458891053d7f3`
Contents: exact tool signatures/returns; owner-side connector setup path without publishing secret routes; same-root assumption; verification procedure for GPT create/read/test, Claude edit, GPT read/test, and disposable file delete; known limits and failure handling.
No source implementation code changed by G2 because six GPT registrations already exist in G1's current source. The required work remaining is deployment and actual plugin exposure, which O005 explicitly forbids G2 from doing.

## G1 coordination
NEW inbox path: `project lead/coordination/builders-inbox/A25-TW-BG-GPT02-2026-10-18-G1-CONNECTOR-CONTRACT.md`
Commit: `59c0ea3a89031c3ad1bff6f4896ac37dee031639`
Records exact observed names/signatures and asks G1 to preserve/confirm contracts and report tests. No G1 response observed in this execution.

## Testing evidence
- PASS: GitHub connector fetched pinned order, handoff, interface note, R001 and two source files.
- PASS: GitHub connector created new G1 inbox note and new source documentation file, returning full commit SHAs.
- NOT RUN: source/local unit tests. GitHub connector does not provide execution of the Android source, and no tested local checkout of the current changing branch was established.
- NOT RUN: live Android commands, phone file CRUD, plugin tool discovery after deployment, Claude edit, cross-seat acceptance. These are explicitly outside O005.
- NOT CLAIMED: installation or exposure of workspace tools in the currently connected A25 GPT Terminal plugin. It still advertises `terminal_status` and `terminal_view` only.

## Next justified action / owner involvement
G1 provides source test results and confirms current head after parallel work. Workshop Lead then obtains separate owner permission for on-phone update of existing Pocket MCP process, sets an agreed `A25_ZONE1_ROOT`, and arranges GPT connector registration/discovery of the updated existing GPT MCP route. Only then can GPT exercise the six workspace tools. Claude is activated later for the shared-workspace test. Do not publish route secrets or mistake GitHub commits for live deployment.

## Source observations / limits
Local-trust implementation; `workspace_edit` replaces complete files without revision guard; `pytest` runs local project code; source path resolution and mutations have potential race windows. These are observations for G1/security owners, not an authorization to redesign security. No phone changes, branches, deployments, credentials or permissions touched.

## Report commit
The full GitHub commit SHA for this report is supplied by the GitHub create_file result in the completion response, not guessed within the report.
