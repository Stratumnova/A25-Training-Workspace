# A25 Workshop Lead — Gate-01 Reopening Decision
FROM: A25-TW-GPT01 Workshop Lead
FOR: Zed, A25 Project Lead, future workshop builders and Archivist
DATE: 2026-10-18 16:58 MDT (owner-supplied)
STATUS: ADOPTED owner authorization; implementation NOT YET DONE

## Owner decision
Zed explicitly authorizes reopening Gate-01 for development and building on top of its existing foundation. Zed confirms the historical rationale: Gate-01 was the initial Roundtable implementation, security complexity created a loop/obstacle, and Gate-02 was subsequently used to obtain a simpler working GPT terminal viewport. If a third Gate build exists, chronology needs correction; this is owner-confirmed recollection, not independently established exhaustive history.

## Scope and constraints
Extend existing Stratumnova/pockettest, prefer reuse to replacement. Preserve Gate-01 original ledger, behavior, and backup; keep Gate-02 terminal bridge and cloudflared tunnel running. Avoid unnecessary new repos or branches. Do not assume permission to delete historical code, deploy an unverified connector, publish private data, or merge protected branches. Phone live testing authorized separately 2026-10-18. No requirement to re-open the security debate for the local prototype.

## Verified via live read-only Termux viewport and tests
- Gate-01 original ~/pockettest/gate01/server.py implements FastMCP, two GPT/Claude secret-path mounts, status/read/append, server-side author assignment, cursor/unseen logic and append-only JSONL.
- Original ledger and backup both 441 bytes and identical SHA256 61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9. A disposable copied ledger parses to three events, IDs [1,2,3], authors [claude,gpt,claude], cursor_through [0,1,2]. This proves file structure, not live recovery.
- Gate-01 pre-reopen archive at ~/a25-workshop/gpt/backups/gate01-pre-reopen.tar.gz; SHA256 ab7cdb174fb747121d6e0d08236689d9f12a6f16e4c0435d4fbf2799504c2e55; tar listing exit 0; restore not tested.
- Original main checkout f0a11d51968ad598691333d32971dfb483489073; isolated Shared Space source worktree at b264897199b23d2692ccb1b399f4c7fd03390672 on existing pockettest development line.
- Shared Space source preserves three Roundtable MCP tool names and adds six workspace tools: inspect/read/create/edit/delete/command. Local test suite: 48 passed, one warning; standalone local file lifecycle PASS; source checker PASS. These are not live connector tests.
- Existing gate02 Python venv versions: mcp 1.26.0, starlette 1.7.0, uvicorn 0.54.0, pytest 8.4.2. Active viewport bridge and tunnel previously observed, no Pocket Shared Space uvicorn process.
- Phone storage at check: 23 GB available; no additional 4 GB requested.

## Missing / unknown
Live GPT/Claude workspace connectors are not installed or verified; Shared Space server not deployed; original Gate-01 copied-ledger recovery through newer implementation not yet tested; no cross-seat same-file read/edit verification; existence of any third Gate implementation unresolved. New storage implementation differs from Gate-01 and must be tested against disposable ledger copy before touching original data.

## Next justified action
Run newer Shared Space recovery logic against the disposable copy of the Gate-01 ledger; inspect resulting events and error handling. Then plan controlled integration/startup that leaves Gate-02 intact. Verify live GPT tool discovery and file lifecycle, then Claude independently, before claiming shared workspace success.

## Evidence classes
ADOPTED: owner decision to reopen and extend Gate-01. VERIFIED: live terminal outputs and local tests above. HISTORICAL CLAIM: prior Gate-01 green/frozen and previous cross-seat successes as reported in archived docs; owner recollection of why Gate-02 was built. UNKNOWN: live production behavior and third Gate existence. No source deployment or merge is implied by this record.
