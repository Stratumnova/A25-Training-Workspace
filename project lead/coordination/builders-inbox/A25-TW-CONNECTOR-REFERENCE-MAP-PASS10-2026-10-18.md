# A25 Workshop — Connector Reference Map Pass 10
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives
STATUS: VERIFIED bounded read-only mapping; external registrations UNKNOWN

## Inspected scope
Read-only grep over ~/pockettest/docs, Gate-01 README, Roundtable README, and Workshop reports Markdown; existence checks for mcp, uvicorn, cloudflared executable names in Gate-01 and Gate-02 virtual environments. No credentials or ledger data read.

## Verified
- Gate-01 README describes two separate GPT/Claude MCP connector URLs at tunnel-host plus caller-specific path plus /mcp.
- ~/pockettest/gate01/.venv/bin has mcp and uvicorn executables.
- ~/pockettest/gate02/.venv/bin has mcp and uvicorn executables.
- No cloudflared executable in those two virtualenv bin directories; earlier scan verified system Termux bin/cloudflared.
- Previously verified two running cloudflared processes reference the a25-gpt-bridge named tunnel.

## Historical claims
- Oct 8 recovery index references named tunnel pocket-server-gate02 and roundtable.rodsrcpark.com route to loopback 8765.
- Index is a historical reference, not proof of current DNS, tunnel, or plugin registration.

## Unknown and bounded negatives
- Whether ChatGPT or Claude currently have the original Gate-01 or Gate-02 connector registrations.
- Whether historic named tunnel remains registered remotely.
- Whether other config files or plugins exist outside the inspected Markdown/filename scope.
- Installed executable does not establish active process or external registration.

## Classification
VERIFIED: direct local source/document/executable evidence.
HISTORICAL CLAIM: old tunnel/route checkpoint.
UNKNOWN: external platform connector state and remote Cloudflare registration.
ADOPTED: mapping only, no installs, changes, tests, cleanup, or credential inspection.

## Next mapping-only scope
Compare authorized platform connector metadata (if available) to locally documented endpoints without opening secrets or modifying integrations.
