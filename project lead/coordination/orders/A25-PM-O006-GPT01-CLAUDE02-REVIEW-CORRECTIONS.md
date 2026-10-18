# A25-PM-O006 — Correct Shared-Read Tests and Local-Mode Exposure Guards
FROM: GPT A25 Project Lead
TO: A25-PM-GPT01
DATE: 2026-10-17 (owner local)
AUTHORITY: Owner-approved official branch under LEAD-DECISION-013; Zed instruction to continue after Claude02 review
SOURCE: Claude02 review A25-PM-R001-CLAUDE02.md, Drive ID 13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl; GPT01 R003 report 90b4b12e00e23dc0743e71939a5fc7ba0de7d241
STATUS: AUTHORIZE limited source/test corrections only; no deployment

## Branch and scope
Use ONLY Stratumnova/pockettest branch build/a25-pocket-server-roundtable, current reviewed source commit 442529a32356c5fb557d908fcd20bace733f04d8. No other branch, repo, phone or tunnel changes. Preserve main, Gate-01, terminal views and existing historical files.

## Corrections
1. F-1: make a discriminating symlink test pointing to a SMALL valid regular file; ensure it fails when O_NOFOLLOW is removed.
2. F-2: replace object-existence-only 'deny-all' assurance with SDK-backed ASGI HTTP tests of real auth enforcement and tool registration. Test default-mode unauthorized MCP request and OAuth metadata; test local-mode loopback allow / remote reject with explicit ASGI client addresses. Do not claim PASS if MCP SDK cannot be installed.
3. F-3: local mode must reject public Host and forwarding/tunnel-origin headers, including cf-connecting-ip, cf-ray, x-forwarded-for, forwarded, x-real-ip; make local allowed_hosts exclude public hostname. Test negative cases. Keep deny-all default. Document that headers are only defense in depth; never expose anonymous mode through a tunnel, and only use an isolated loopback port for later owner-controlled testing.
4. F-6: make /health status identify local-read mode while ready stays false until actually established; correct stale docstring.
5. Keep changes minimal. Preserve fixed-file-only read; no arbitrary paths, writes, shell, new dependencies, new branches or public anonymous mode.
6. If an SDK API/transport test cannot run in your environment, preserve exact code and report BLOCKED, not PASS. Static compilation and isolated unit tests may be reported separately from MCP integration.
7. Consider returning MCP isError for failures only if straightforward and covered by tests; otherwise record as deferred. No architectural redesign.

## Delivery
Commit focused changes to official branch, record full code SHA. Create NEW coordination report project lead/coordination/reports/A25-PM-R004-GPT01.md with exact test commands/results, known gaps and risks. No overwriting earlier reports. Stop for independent Claude02 re-review.

## Future architecture
M2 needs controlled remote identity/access; do not implement secret-path workaround or anonymous public mode under this order. GPT Lead will issue separate scoped order after local M1 tests and architecture review.
