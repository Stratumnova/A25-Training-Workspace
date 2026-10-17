# A25 Infrastructure and Study Materials Audit 001
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / future Claude reviewer
DATE: 2026-10-17, Zed request 13:28 MDT
RE: Cross-repository, tools, Pocket Server, HalfAwake and folder audit
BASIS: Direct GitHub repo/branch/tree/source reads; live connector status calls; prior Case Study 001
STATUS: READ-ONLY INSPECTION + THIS REPORT; NO DEPLOYMENT OR MERGE

## Observed live tool capability
- GitHub connector: repository listing, public repository fetch, branch trees, file reads and historical Actions runs work. Prior trial established file creation on development branch.
- Pocket Gate `server_status` and `read_roundtable`: both returned `UNAVAILABLE: Connection failed` during audit. This is not proof the phone server is stopped; no live state or identity can be attested.
- A25 GPT Terminal `terminal_status` and `terminal_view`: both failed internally. No live terminal content was obtained.
- GitHub workflow dispatch: no dispatch operation in builder's available connector; O004 workflow committed but no run evidenced. Do not treat unrelated Watchdog green as prototype green.

## GitHub repository availability
Connected account listing returned five repositories: public `pockettest`, `Tools_Templates-`, `A25-Training-Workspace`; private `GuildCraft-Android`, `Stratumnova_coins`. Separate public repository API reads succeeded for `HalfAwake`, `halfwake-pocket`, `HalfAwake.Pocket.v1`, `Stratumnova-vault`, `Stratumnova_lite`. Accessible public metadata is not equivalent to connector write permission.

## Pocket Server source audit
- `Stratumnova/pockettest` five branch heads observed: main `f0a11d51968ad598691333d32971dfb483489073`, auth `1b578ee32532f99093ab906af52e8b485c90a7e4`, Shared Space `9a419e925dff2de64ef948b7d6d8304eccf8387d`, Stage2 proposal `8ade3c00f4f5219182ec01b5154b4b89b71d3359`, historical A25 training `77af2aa4d17fe7818ce8830cd56a0c4b41162f1d`.
- Main `gate02/server.py` instantiates `DenyAllProvider` and reports `ready:false`. Auth branch has additional registration/consent/store modules but same inspected `DenyAllProvider` in server.py.
- Shared Space Stage 1 `shared/server.py` offers `server_status`, `read_roundtable`, `append_roundtable` for GPT/Claude, dummy-data only. It does NOT expose V1 `list_projects`, `list_files`, `read_file` despite these appearing in `protocol/POCKET_SERVER_V1.md`.
- Stage 1 uses secret-path actor separation, not provider-authenticated identities. It has file-backed JSONL Roundtable, fsync, startup recovery of incomplete tail, secure append/read helpers, and storage outside repository. It uses in-memory `pending_read` and should be tested for restart behavior against V1 cursor requirements.
- Stage 2 proposal explicitly says bearer secret paths are not OAuth, deployment is not approved, and integration requires review. No arbitrary shell or remote owner endpoint authorized.
- No live connection confirmed in this audit.

## HalfAwake source audit
- Public `HalfAwake` main `64d1b968161df6d2abcf588635d208269bd7ed0c`; `halfwake-pocket` main `92ae414f7c8be79fe8f761cf0c98dc50d7052a97`; `HalfAwake.Pocket.v1` main `b89103d190b7c9b81c23c87b4667588316016590`.
- All inspected READMEs state not compiled at documentation time. No claim of tested APK.
- Expanded source includes `LogStore.kt` core truth versus personality/tech layer separation, addon bridge, local diary, widget and UI. Android manifest deliberately omits INTERNET permission. It is not a demonstrated networked Pocket Server client.
- Reuse patterns: local log projections, separate factual and personality layers, manual copy/export and modular addons. Do not silently enable network permissions or conflate lore with evidence.

## A25 branch/file inventory
- `main` at `34b0d235a2bc78c975c57c1d16ecd74028832f5d`: 78 tracked files.
- `build/wd-02-watchdog-v0` at `0ecb6079f66a46648ff9777bf1e88f1a2616a045`: 118 files.
- `build/a25-ns-o002-synthetic-prototype` at `e5c9754eeebd4d7474fc6adfe259f75385bf38a6`: 131 files.
- `coord/a25-namespace-trial-001` before this report at `f895f04f14263ea5a81e2cca88a52664aacdee46`: 137 files, 16 under `project lead/coordination`.
- File counts overlap inherited histories and must not be summed. The default branch START_HERE is a baseline snapshot, not a cross-branch current index.
- Existing historical `case-studies/ID_REGISTRY.md` documents a prior ID collision and explicitly warns against treating its registry as exhaustive. New A25 namespace draft must preserve historical aliases and reserve IDs before assignment.
- Overlapping folders `case-studies/`, `project lead/coordination/case-studies/`, `roundtable/`, `archives/claude/`, `legacy/`, `project lead/archivist/` need a derived navigation index, not premature moves.

## Proposed target organization (NOT YET AUTHORIZED TO MIGRATE)
- `governance/`: approved decisions, permissions, policies.
- `coordination/orders/`, `coordination/reports/`, `coordination/reviews/`: cross-seat work.
- `evidence/case-studies/`, `evidence/tests/`, `evidence/manifests/`: verifiable outcomes, source refs and failures.
- `catalog/namespace/`, `catalog/repositories/`, `catalog/lineage/`: derived index, registry and migration map.
- `projects/pocket-server/`, `projects/halfwake/`, `projects/watchdog/`: pointer records to authoritative code repositories, not duplicate code copies.
- `legacy/`: original source-preserving imports, unchanged.
All proposed folders are logical categories, not a command to rename existing files. Current source remains authoritative until Zed approves migration.

## Recommendation
Keep GitHub as authoritative source/ledger. Consider bringing Pocket Server online ONLY for bounded, read-only, synthetic connectivity tests after Zed explicitly starts it and confirms no unreviewed service or credentials are exposed. Check `server_status`, actor attribution, read_roundtable cursor behavior, restart recovery and limited dummy-data file listing if actually implemented. Current Stage 1 does not provide shared ZIP browsing via MCP. Owner may locally unzip controlled files into separate workspace; do not claim AI remote access until list/read tools are built and tested. Do not use Stage 2 identity proposal for production.
Keep HalfAwake independent/offline and use its UI/logging patterns as a reference; do not make it a Pocket Server client in this phase.
Prioritize (1) read-only capability inventory; (2) cross-branch source index; (3) Pocket Server synthetic connectivity; (4) authenticated read-only project listing with path/privacy controls; (5) source-hash transfer and CI evidence; (6) maintenance bot after governance and access tests.

## Study/test improvements
Use separate C1 communication, C2 source integrity, C3 execution, C4 integration and C5 production gates with PASS/FAIL/BLOCKED/NOT_TESTED. Track exact branch/commit and whether a test belongs to it. New case-study addendum should record Pocket Gate and Terminal connection failures, no automatic sync, and observed distinction between spec and implemented MCP tools.

## Owner input needed
Before live testing: which code checkout and service (Gate-01, Stage 1 Shared Space, or other) is actually running on Android; whether Zed wants to start it for dummy-data-only read-only connection test; which local directories are explicitly authorized for eventual file-list/read tools. Never ask for raw credentials in chat.
