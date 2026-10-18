# Archive pool note — Gate-01 reopening and Zone 1 integration
FROM: A25-TW-GPT01 Workshop Lead
FOR: Archives / Archivist pool, A25 Project Lead, future recovery sessions
DATE: 2026-10-18 16:58 MDT (owner-supplied)
TYPE: REFERENCE + owner ADOPTED decision; not a completion report

## Why this exists
Owner Zed authorized reopening the previously frozen Gate-01 rather than discarding the old Roundtable implementation. Owner confirms Gate-01 was first, with security complexity frustrating progress; Gate-02 was pursued for a simpler working terminal viewport. This is owner-confirmed decision history; verify third-Gate chronology independently if material.

## What existed
Original Gate-01 at ~/pockettest/gate01/server.py, README, test_gate.py, ledger roundtable.jsonl and matching backup. Server code implements separate GPT/Claude FastMCP paths, three Roundtable tools, server-side author assignment, read-first append, unseen/context cursor and retry behavior. Gate-02 current bridge exposes terminal_view and terminal_status, and its running process/tunnel must not be interrupted.

## What was missing
Gate-01 did not expose shared file editing and test execution for both AI seats. Its historical three-event ledger is not a live cross-seat test of today's environment. Existing GPT terminal plugin is read-only. Shared Space MCP server and six workspace tools have not been deployed to phone or discovered by ChatGPT/Claude connectors. No live two-seat same-file workflow yet.

## What works now (VERIFIED)
- Gate-01 ledger copy parsed as event IDs 1,2,3; authors claude,gpt,claude; cursors 0,1,2. Original and backup hash: 61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9.
- Gate-01 archive tar integrity exit 0, hash ab7cdb174fb747121d6e0d08236689d9f12a6f16e4c0435d4fbf2799504c2e55, at ~/a25-workshop/gpt/backups/gate01-pre-reopen.tar.gz. No restore test.
- Newer pockettest Shared Space source b264897199b23d2692ccb1b399f4c7fd03390672 includes original three tools plus workspace_inspect/read/create/edit/delete/command on each seat's MCP route, using common A25_ZONE1_ROOT. 48 shared tests passed with one warning; local file lifecycle and offline Actions contract checker passed. These tests do not prove remote connections.
- 23 GB phone storage available at last check; user offers to free 4 GB if genuinely required.

## Archive interpretation rules
Do not collapse owner adoption into verification. Preserve Gate-01 original, local ledger, backup, current Gate-02 viewport, and newer Shared Space source lineage. Do not infer success from passing unit tests or source contracts. Do not silently supersede earlier records; add verification reports and decisions separately. The owner-approved plan is to reuse Gate-01 foundations with tested Zone 1 features, not to replace the working viewport.

## Outstanding sequence
1. Test newer recovery against disposable original ledger copy.
2. Determine compatible integration/startup and protect old ledger.
3. Start live Pocket Shared Space process under owner authorization without breaking Gate-02.
4. Connect GPT and confirm six tools; then connect Claude; run actual shared-file exchange.
5. Save exact source SHA, commands, output, connector discovery and failure evidence. Unknown whether third Gate build exists.

## Evidence pointers
Repository: Stratumnova/pockettest, original main f0a11d51968ad598691333d32971dfb483489073; Shared Space source b264897199b23d2692ccb1b399f4c7fd03390672. Prior workshop coordination records: A25-TW-LIVE-ZONE1-TEST-RESULTS-2026-10-18.md; A25-TW-LIVE-FULL-SUITE-RESULTS-2026-10-18.md; A25-TW-LIVE-ZONE1-FILE-LIFECYCLE-2026-10-18.md. Phone paths are evidence locators, not GitHub-backed copies.
