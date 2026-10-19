# A25 Workshop — Architecture and Historical Drift Map Pass 08
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives, Claude
STATUS: VERIFIED source and README inspection; historical claims not independently adopted
Owner scope: mapping only; no phone modifications, no active tests.

## Verified source route declarations
- pockettest/gate01/server.py: FastMCP instances per who; Starlette mounts GPT_PATH and CLAUDE_PATH to separate streamable_http_app() endpoints.
- pockettest/gate02/server.py: FastMCP, custom GET /health route, BodyLimitMiddleware around streamable_http_app.
- pockettest-shared/shared/server.py: FastMCP per who, Starlette GPT_PATH and CLAUDE_PATH mounts.
- a25-workshop/gpt/src/bridge.py: separate FastMCP application and streamable-http entry point.

## Reference documentation — historical claims, not runtime verification
Gate-01 README: dummy-data-only proof; one process, one append lock, JSONL ledger, two secret routes as identity; startup recovery; read/append/cursor/retry expectations; tunnel guidance. README is a design/implementation claim.
Roundtable README: owner authority, GPT/Claude read+append, project files separately protected.
Pocket Server recovery index dated 2026-10-08: states Gate-01 GREEN/FROZEN with 3-event exchange and two phone ledger files; Gate-02 not implemented at checkpoint; named Cloudflare tunnel and public route previously configured; checkpoint PDFs were not committed with index; old Gate-01 secret paths should not be reused. These statements are historical claims, not proof of current deployment.

## Architectural separation
Gate-01: route-based identity and ledger.
Gate-02: OAuth-related baseline and request middleware.
Shared Space: route-based identity plus storage and secure-file helpers.
Workshop bridge: separate terminal-facing FastMCP source.
Do not infer all share caller authentication or current runtime behavior.

## Current evidence status
VERIFIED: direct source lines and existing README text; earlier process evidence for active src.chatgpt_readonly, Gate-02 uvicorn, cloudflared.
HISTORICAL CLAIM: archived checkpoint's GREEN/FROZEN and tunnel setup statements.
UNKNOWN: current Gate-01 ledger event count, credential status, live routes for each component, which historical tunnels remain registered, external connector/plugin registration.
ADOPTED: read-only mapping and owner escalation on blockers.

## Next mapping target
Inventory nonsecret historical config references, deployment file metadata and registered plugin metadata when accessible; never open tokens, credentials, secret paths or private ledger contents. No builds, restarts, installs, cleanup or network probes.
