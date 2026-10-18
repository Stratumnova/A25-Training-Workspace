# A25-TW-R001 — Pocket Server Source Route
FROM: A25-TW-BG-GPT01 (G1) TO: A25-TW-GPT01
DATE: 2026-10-18
STATUS: READ-ONLY RECONNAISSANCE COMPLETE; IMPLEMENTATION NOT AUTHORIZED
ORDER: A25-TW-O001 at c9ba07286b06e90034844cb7e046d8298b32197f

## Source access and version ledger
VERIFIED directly via GitHub repository API: Stratumnova/pockettest, public repository, default main f0a11d51968ad598691333d32971dfb483489073. Branches: build/a25-pocket-server-roundtable fabedb661bb5161055534589c7517f7e0738139d; build/gate02a-c1-auth-store 1b578ee32532f99093ab906af52e8b485c90a7e4; build/shared-space-v0 9a419e925dff2de64ef948b7d6d8304eccf8387d; proposal/shared-space-stage-2-identity 8ade3c00f4f5219182ec01b5154b4b89b71d3359; a25/training-workspace 77af2aa4d17fe7818ce8830cd56a0c4b41162f1d. These are observed branch heads, not deployment attestations.
Read exact source on build/shared-space-v0: gate01/server.py, gate02/server.py, gate02/listening_wall.py, shared/server.py, shared/secure_files.py, shared/storage.py. Did not independently inspect every file on all branches; auth-store and stage-2 implementation completeness remains UNKNOWN.

## Source-to-capability map
| Capability | Source / function | Evidence and limit |
|---|---|---|
| Separate MCP identities | gate01/server.py make_mcp, GPT/CLAUDE and secret route Mounts | VERIFIED distinct path-based identities; not credential-authenticated caller identity |
| Roundtable read/write | gate01/server.py read_logic, append_logic, _parse_ledger, _write_event | VERIFIED source provides read-first, cursor, duplicate response and append-only JSONL; dummy-data-only, no filesystem CRUD |
| Startup recovery | gate01/server.py recover_once | VERIFIED quarantines incomplete tail at startup, not runtime proof |
| Private Shared Space root | shared/storage.py resolve_data_root, prepare_data_root | VERIFIED external root, directory restrictions; does not create GPT/Claude/Shared access control |
| Guarded regular-file IO | shared/secure_files.py secure_read, secure_append, secure_rdwr | VERIFIED final-component O_NOFOLLOW, regular-file check; NOT a complete path confinement or generic create/update/delete API |
| Shared MCP service | shared/server.py configure_storage, make_mcp, lifespan | VERIFIED only server_status/read_roundtable/append_roundtable registered; no general file or command tools |
| Gate-02 | gate02/server.py DenyAllProvider, FastMCP auth settings | VERIFIED deny-all skeleton; not functional OAuth authorization |
| Request limits | gate02/listening_wall.py BodyLimitMiddleware | VERIFIED HTTP body limiter; not command sandbox |
| Terminal execution | no terminal command tool in examined server source | NOT VERIFIED as live service; historical viewport != command execution |

## Historical evidence and parity
A25-AV-R001 (053d2e7868bfdd85d1659d40e8e7002e14d58a47) independently inventories uploaded ZIP members and hashes, including gate01/gate02/shared code and 3-event backup; this verifies offline bytes, not current phone or GitHub parity. A25-AB-NOTE-2026-10-18-TERMUX-ZIP-SHA256-RECEIPTS at a202ae461a6cbd051894a1280bfafbc67998619b records six builder-observed phone terminal digest matches, not signed attestation or full parity. Archives disposition ARC-REVIEW-2026-10-17-007 distinguishes historical read-only viewport claims from current command access. Do not treat historic test counts, SDK success, live transport, or identity as verified here.

## Shortest justified Zone 1 route (PROPOSED, not adopted)
Use build/shared-space-v0 as source *candidate*, because it already joins the Gate-01 MCP transport and private data-root/file-descriptor helpers; keep Gate-02 deny-all separate until independent identity design is accepted. Before any implementation, G2/owner must settle principal-to-area access policy (GPT, Claude, Shared), shared-area write authority, command catalog and execution scope. Add explicit area-scoped list/read/create/update/delete MCP tools with relative-path confinement, symlink-safe traversal, bounded payloads, revision preconditions and structured errors. Add a distinct command_execute tool restricted to enumerated commands/arguments and explicit area policy; do not expose arbitrary shell execution by default. Log actor, target, operation and outcome. Preserve Gate-01 ledger contract and separate file data from ledger records. Test offline against traversal, symlink, cross-area, stale-revision, malformed input, and command denial before any phone deployment.

This is not a claim that secure_files.py already protects intermediate path components or that route secrecy authenticates a human or AI principal. Source branch suitability is architectural only; byte parity and integration tests are pending.

## Coordination
G2 handoff posted to project lead/coordination/builders-inbox/A25-TW-G1-TO-G2-SOURCE-INTERFACE-2026-10-18.md at commit 701bcd2847e7ab01a2e80543ffca56bea2234324. Tool signatures there are proposals, not implemented contracts.

## Next justified action / stop
Request separately scoped order approving target branch and exact file/command contracts after G2 review. No branch, source, phone, deployment, server, or permissions changed. Only authorized coordination documentation created. No runtime tests executed. STOP.

## Exact source links
- https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/server.py
- https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/secure_files.py
- https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/storage.py
- https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/gate01/server.py
- https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/gate02/server.py
