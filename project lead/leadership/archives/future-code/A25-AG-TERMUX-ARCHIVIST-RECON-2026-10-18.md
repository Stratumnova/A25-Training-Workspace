# A25 Archives — Read-Only Termux Reconnaissance for Future Archivist Bot
Date: 2026-10-18/19 (local date boundary)
Seat: A25-AG-GPT01
Scope: owner-authorized searching, listing, and reading only; no phone modifications.
Status: VERIFIED observations and proposed archival needs; no bot implementation.

## Method and access ledger
- Called terminal_status: identity gpt-workshop; workspace exists; src/tests/logs/reports/backups/config true; mode read-only. Mode is a label, not proven enforcement.
- Called terminal_view on existing a25-test, a25-gpt, a25-bridge, a25-tunnel; all returned read_only=true, returncode=0.
- Used terminal_send **only in a25-test** to run four read-only inspection commands composed of pwd, ls, find, printf, sed, head, and shell loops. No writing, changes, process management, tests, or secrets reading. Verified responses by terminal_view.
- No new sessions, permission probes, app private directory accesses, or external network calls.

## Verified topological observations
- Workshop root: `/data/data/com.termux/files/home/a25-workshop/gpt` with directories `src`, `tests`, `logs`, `reports`, `backups`, `config`.
- Other source generations: `~/pockettest` (gate01/gate02/roundtable/shared_context/protocol/docs), `~/pockettest-c1` (gate02 tests), `~/pockettest-shared` (shared source and tests), and `~/a25-workshop/gpt/tests/zone1-source` (Zone 1 test source).
- Data/report root `~/a25-data/shared-space/reports/checkpoints` contains three named PDF checkpoints: `Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf` (13,930 bytes), `A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf` (31,221 bytes), `A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf` (73,333 bytes). File presence is not proof of content validity or restore.
- Workshop reports includes `A25_GPT_Inside_Out_Terminal_Bridge_Experiment_2026-10-11.pdf` (31,101 bytes).
- Backups directory includes named pre-reopen and pre-zone1 tarballs, bridge/viewport prior versions, and gate02-write-pass files. File names/sizes are observed; integrity/restore not tested. Avoid automatic upload of backups or secret-bearing archives.
- Workshop logs directory was empty in this listing; service viewport logs exist separately in tmux screens. Do not infer there is no logging elsewhere.

## Verified documentary evidence
- Original `~/pockettest/shared_context/DECISIONS.md` read: D001 owner-controlled project files, D002 GPT/Claude project read-only V1, D003 Roundtable append-only, D004 separate credentials, D005 credential-derived identity, D006 constrained project root, D007 no arbitrary shell/delete/rename in V1, D008 no model APIs required, D009 pockettest proving ground, D010 shared operational context readable to both.
- Read `~/a25-workshop/gpt/tests/zone1-source/START_HERE.md`, `shared/ZONE1_ACTIONS_ENTRY.md`, `shared/ZONE1_GPT_CONNECTOR.md` (partial visible portions), and `~/pockettest/docs/README.md`. The Zone 1 connector document describes a proposed acceptance procedure with create/read/edit/pytest/delete steps **only after separate live authorization**. This was not executed. Document also says six workspace tools were not yet exposed in the plugin at its historical writing; this is not a live discovery result.
- Original pockettest documents describe older Gate-01/Gate-02 design and historical tunnel/security intentions. These are REFERENCE and do not override owner-adopted Oct 18 baseline.
- Filename-only archive/ledger/cursor/manifest search to max depth five returned two `ledger_*.pyc` cache files in pockettest-shared. This does not mean source ledgers or other archives do not exist: names, depth and filters were narrow.

## Runtime viewport observations
- a25-gpt: MCP HTTP 200/202 and ListToolsRequest/CallToolRequest activity for test-gpt/test-claude route names; route names are not proof of authenticated caller attribution.
- a25-bridge: HTTP 200/202 and MCP CallToolRequest; no caller identity mapping.
- a25-tunnel: Cloudflare stream-canceled errors for origin `127.0.0.1:8770`; no end-to-end availability conclusion from this alone.
- a25-test: earlier historical mapping command output and newly authorized read-only scan commands.

## Archivist bot needs suggested by evidence (PROPOSED, not authorized implementation)
1. Source registry: stable path, origin/repository, branch/commit or on-device path, observation date, file type, evidence status and owner adoption status separately.
2. Provenance ledger: direct tool evidence vs owner report vs Workshop report vs historical plan; preserve both conflicting claims, resolutions and supersession links.
3. Source-to-runtime map: distinguish original pockettest, gate02 worktree, shared source, Zone 1 test copy, actual Workshop bridge, local data, tmux logs, GitHub documents.
4. Controlled ingestion: read-only allowlist for non-secret documents and metadata; explicit opt-in for PDF/checkpoint content; never blindly ingest backup tarballs, credentials, personal storage, raw private ledger entries or unrelated app data.
5. Fresh-session recovery index: canonical leadership sources, latest owner orders, latest cross-lead receipts, timestamps and branch pins; flag stale UNKNOWN claims (e.g. Archives receipt later resolved).
6. Evidence durability: additive Markdown reports to authorized GitHub Archives folder; original file untouched; hashes and reproducible access log when owner authorizes; no implicit phone cleanup.
7. Cross-seat audit requirements: distinguish shell command output from authenticated caller identity, read-only status label from enforcement, and session availability from overall service health.

## Limits and open questions
- This was a narrow scan, not a complete file inventory or code audit. No full source files or PDFs were copied out.
- Which files/processes constitute current October 18 baseline and what is safe to archive remains UNKNOWN.
- Checkpoint restore completeness, authenticated caller separation, true read-only enforcement, and full Zone 1 feature readiness remain UNKNOWN.
- Need owner decisions before any automated indexing, persistent on-phone Archivist service, new rooms, or broader access.

## Next justified action
Use this report as a source-location and evidence-schema starting point. Coordinate with Workshop Lead and Project Lead to design read-only Archivist scope without disturbing the current baseline. No implementation, phone changes, or service actions authorized.
