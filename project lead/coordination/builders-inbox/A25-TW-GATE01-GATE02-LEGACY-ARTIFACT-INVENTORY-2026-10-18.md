# A25 Workshop — Gate-01 / Gate-02 Legacy Artifact Inventory
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Claude, Archives
STATUS: PARTIAL VERIFIED; blocked TCP listener inventory escalated to owner

## Purpose and authority
Owner requested mapping of leftovers from drifted/frozen Gate-01 and Gate-02 Pocket Server builds: old tunnels, connectors, plugins and terminal integrations. READ-ONLY commands only; no files/processes/config modified or moved. Under adopted blocker rule, stop blocked item and ask owner before further action.

## Verified from phone (three read-only inspection passes)
Top-level project trees:
- ~/pockettest with gate01, gate02, claude, gpt, protocol, roundtable, shared_context.
- ~/pockettest-c1 with gate01 and gate02 plus similar project components.
- ~/pockettest-shared with gate01, gate02, shared server and tests, plus project components.
- ~/a25-workshop/gpt with src, config, backups, tests, logs, reports.
- ~/a25-data.
- ~/.cloudflared.
Git worktree metadata from pockettest:
- ~/pockettest main at f0a11d5.
- ~/pockettest-c1 build/gate02a-c1-auth-store at 1b578ee.
- ~/pockettest-shared build/shared-space-v0 at 9a419e9.
- ~/a25-workshop/gpt/tests/zone1-source detached worktree (SHA not retrieved).
Gate-02 source inspection: each of pockettest, pockettest-c1, pockettest-shared gate02/server.py has DenyAllProvider declaration; this is source presence, not verified live deployment. pockettest-shared/shared/server.py has FastMCP server declaration.
Active process metadata: two cloudflared processes using same workshop tunnel config and named tunnel; Python src.chatgpt_readonly process; Pocket Gate-02 uvicorn on loopback 8766. Four tmux sessions a25-bridge, a25-gpt, a25-test, a25-tunnel.
Tunnel-related file names ONLY: ~/.cloudflared/pocket-gate02.toke (249 bytes), pocket-gate02.token (249 bytes), cert.pem (282 bytes), UUID-named JSON (175 bytes); workshop config/bridge.token (65 bytes), cloudflared.yml (264 bytes). Contents NOT opened; filename similarity does not prove duplication or obsolescence.
A project file-name scan found cloudflared.yml under workshop config and MCP executable files in virtualenvs.

## Interpretation
VERIFIED: parallel code worktrees and distinct server implementations exist; multiple tunnel processes exist; token-like files exist.
UNKNOWN: obsolete vs intentional, which tunnel processes are serving which connector, app/plugin registration state, caller authentication, credentials validity, exact listener set, current deployment of all source trees.
No artifacts are approved for cleanup. Do not publish credential contents.

## Blocked item for Zed
Attempted passive TCP listening socket inventory via ss -ltn or netstat -ltn. 'ss' not installed; netstat reports no AF INET TCP support. No installation, alternate approach, or privileged probing attempted. Await owner's review before trying another method. This does not block interpretation of previously observed processes.

## Next possible authorized read-only investigation
After owner review: trace active processes to their working directories and configuration references without reading secrets; inventory historical connector/plugin metadata from available records; compare worktree code paths and deployments. No modifications or active access tests.
