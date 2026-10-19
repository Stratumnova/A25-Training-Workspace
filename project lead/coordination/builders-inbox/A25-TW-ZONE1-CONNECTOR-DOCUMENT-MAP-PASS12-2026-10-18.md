# A25 Workshop — Zone 1 Connector Document Map Pass 12
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security
STATUS: VERIFIED document read; deployment UNKNOWN

## Access
Owner explicitly authorized read-only inspection of public-safe ZONE1_GPT_CONNECTOR.md. Earlier combined and separate commands were blocked by tool safety; this simple cat command succeeded in a25-test. Full output verified through terminal_view. No phone state changed.

## Verified document contents
File: ~/a25-workshop/gpt/tests/zone1-source/shared/ZONE1_GPT_CONNECTOR.md
Heading: Zone 1 — GPT connector binding and verification.
Explicit status: SOURCE CONTRACT DOCUMENTATION ONLY, not a live connector installation or phone deployment.
References A25-TW-O005 and branch build/shared-space-v0.
Claims shared/server.py calls make_mcp('gpt') and make_mcp('claude'), both with six workspace operations: workspace_inspect, workspace_read, workspace_create, workspace_edit, workspace_delete, workspace_command.
Document says shared A25_ZONE1_ROOT; relative paths; UTF-8 content <=1,000,000 bytes; command timeout 30 sec; command actions pwd, ls, python_version, pytest.
Notes local-trust prototype, not hardened isolation; whole-file edit, no revision preconditions; pytest executes code.
Installation and acceptance procedure requires separate owner authorization, GPT/Claude endpoint registration, actual tool discovery and cross-seat test. Document states none of those deployment/acceptance activities occurred under O005.
Document warns separate GPT Terminal plugin tool surface is not equivalent to Zone 1 workspace tool surface. This is document-level claim and may refer to earlier plugin versions.

## Security significance
Distinguish planned Zone 1 shared write-capable tools from current terminal plugin and earlier Gate-01 route-derived identity. Same-root two-route access is a proposed trust boundary; no verified live exposure. Do not treat document's acceptance procedure as authorization to run tests.

## Status
VERIFIED: exact document text retrieved.
HISTORICAL CLAIM: O005 source inspection, nondeployment and proposed interface.
OWNER-REPORTED: multiple historical Claude and GPT plugins.
UNKNOWN: actual installed plugin tool sets, active Zone 1 deployment, endpoint registrations, current route auth.
ADOPTED: map only.

## Blocked/untested
Viewport archive member listing remains unattempted in this pass after previous tool block. No archive extraction, credential reads, live tests, or phone modifications.
