# A25 Workshop — Legacy Plugin and Viewport Artifact Map Pass 11
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives
STATUS: VERIFIED bounded read-only filename inspection

## Owner-reported
Zed confirms having created several plugins for both Claude and GPT in early Pocket Server/viewport stages. Exact count and registrations remain unknown. See leadership security note A25-SECURITY-MCP-PLUGIN-LEGACY-DIVERGENCE-NOTE-2026-10-18.md.

## Verified local filenames
- ~/a25-workshop/gpt/backups/a25-gate02-viewport-20261018.tar.gz
- ~/a25-workshop/gpt/tests/zone1-source/shared/ZONE1_GPT_CONNECTOR.md

Bounded scan across pockettest, pockettest-c1, pockettest-shared and Workshop to maxdepth 4 for filenames containing plugin, connector, viewport, manifest; excluded .venv and .git paths. No other matching files returned. Separate grep of selected Pocket Server README/docs found Gate-01 connector URL description. No contents of archive or connector document opened in this pass.

## Classification
VERIFIED: file existence, search scope.
OWNER-REPORTED: multiple historical Claude and GPT plugins.
UNKNOWN: archive content, connector document details, remote registration state, active/inactive plugin status, link between artifacts and historical viewport.
ADOPTED: mapping only, no modifications, cleanup, installations or active testing.

## Next read-only map
Inspect ZONE1_GPT_CONNECTOR.md text if nonsecret; list archive member names only (do not extract); compare with documented architecture. Do not open credential files.
