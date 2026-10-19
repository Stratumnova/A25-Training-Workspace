# Cleanup Pass 01 — Historical Dependency Leads

DATE: 2026-10-19
FROM: A25-TW-GPT01
SCOPE: GitHub source review only; terminal send not used; no phone changes.
CUTOFF: 2026-10-18 15:00 MDT (owner evidence-priority rule).
STATUS: Historical findings recovered, current runtime dependencies NOT yet verified.

## Original GitHub notes read
- project lead/coordination/builders-inbox/A25-TW-ARCHITECTURE-DRIFT-MAP-PASS08-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-TUNNEL-METADATA-MAP-PASS09-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-CONNECTOR-REFERENCE-MAP-PASS10-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-LEGACY-PLUGIN-VIEWPORT-MAP-PASS11-2026-10-18.md
All are dated October 18 but have no exact creation time in their text. Do not assume before or after the 3 PM cutoff without commit timestamps.

## Candidate 01 — Gate-01 original
PASS08 reports source in pockettest/gate01/server.py using separate FastMCP GPT/Claude route mounts. PASS10 confirms README described two caller-specific MCP connector URLs and Gate-01 virtualenv included mcp/uvicorn executables. Historical Gate-01 GREEN/FROZEN claim is not current runtime proof. CLASS: LEGACY REVIEW / DEPENDENCY UNKNOWN. Archives should preserve source and original checkpoint before considering removal.

## Candidate 02 — Gate-02 worktree
PASS08 reports pockettest/gate02/server.py with FastMCP, health endpoint and request body limit middleware. PASS10 reports installed mcp/uvicorn executables in Gate-02 venv. Earlier mapping saw a Gate-02 uvicorn process, but the current process and relationship to working terminal connector have not been reverified. CLASS: INVESTIGATE, NOT UNUSED.

## Candidate 03 — Shared Space worktree
PASS08 reports pockettest-shared/shared/server.py with separate caller route mounts. No current dependency demonstrated by the October 19 file exchange. CLASS: LEGACY REVIEW / DEPENDENCY UNKNOWN.

## Candidate 04 — Workshop bridge
PASS08 reports a25-workshop/gpt/src/bridge.py with its own FastMCP streamable HTTP app, distinct from Gate-01, Gate-02 and Shared Space. October 19 terminal tool success supports a working bridge capability, but deployed process-to-file binding still needs verification. CLASS: PROTECT CURRENT BASELINE; trace process/source before any cleanup.

## Candidate 05 — Tunnel process/config
PASS09 observed two cloudflared processes, PIDs 22097 and 30319 at the time, both referencing ~/a25-workshop/gpt/config/cloudflared.yml and named tunnel a25-gpt-bridge. This does not establish duplicate unnecessary processes or current state. File metadata: cloudflared.yml size 264 bytes, mode 600, mtime 2026-10-11 18:41 -0600. CLASS: PROTECT/INVESTIGATE; do not restart or expose config contents.

## Candidate 06 — Historical tunnel credential files
PASS09 observed ~/.cloudflared/pocket-gate02.token and pocket-gate02.toke, both 249 bytes, and cert.pem 282 bytes. Similar names/sizes do not establish duplication, use, or redundancy. CLASS: SENSITIVE UNKNOWN; metadata-only review, no credential contents in reports.

## Candidate 07 — Viewport backup
PASS11 verified filename ~/a25-workshop/gpt/backups/a25-gate02-viewport-20261018.tar.gz. Content was not inspected in that pass. CLASS: ARCHIVES CANDIDATE; verify integrity and uniqueness before owner disposition.

## Candidate 08 — Connector documentation
PASS11 found ~/a25-workshop/gpt/tests/zone1-source/shared/ZONE1_GPT_CONNECTOR.md. This is documentation/source-contract evidence, not proof of deployed connector. CLASS: REVIEW/KEEP AS REFERENCE until linked to runtime.

## Candidate 09 — Legacy plugin registrations
Zed reported several older GPT/Claude plugins. PASS10/11 could not verify current external platform registrations. CLASS: UNKNOWN; remote metadata comparison required before identifying inactive entries.

## Practical priority
1. Preserve the working terminal connection and its bridge/tunnel/startup dependencies.
2. Compare active process command lines and sockets against Gate-01, Gate-02, Shared Space and Workshop bridge.
3. Determine which old worktrees and backups are runtime-independent and whether Archives already has durable copies.
4. Separate Archive recommendation from owner authorization to remove.

No files or services on Android were modified. No deletion is proposed on present evidence.
