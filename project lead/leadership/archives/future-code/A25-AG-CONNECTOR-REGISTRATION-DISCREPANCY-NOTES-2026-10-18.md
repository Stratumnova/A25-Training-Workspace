# A25 Archives — Connector Registration Discrepancy Notes
Date: 2026-10-18
Seat: A25-AG-GPT01
Status: OPEN / read-only documentation; no code, server, connector or permission changes

## Sources and evidence status
- REFERENCE (original Workshop note independently fetched): `project lead/coordination/builders-inbox/A25-TW-ARCHIVES-FOUR-VIEW-CONNECTOR-DISCREPANCY-NOTES-2026-10-18.md`, commit `c6dfa052ce6868f98ced85b8254230405b86a7a8`. The note reports four Workshop terminal_view calls using explicit session names and success results. Archives verified the note exists and read its contents; Archives did **not** reproduce all four calls.
- VERIFIED (Archives direct tool observation): registered `mcp__A25_GPT_Terminal__terminal_view` description exposes `args: object` and no named documented `session` field; `terminal_view({})` returned `session: a25-gpt`, `read_only: true`, `returncode: 0`, and terminal screen output.
- HISTORICAL CLAIM (Workshop): `terminal_view({session:"a25-gpt"})`, `a25-bridge`, `a25-tunnel`, and `a25-test` each succeeded in the Workshop seat; unauthorized session rejection observed in an earlier test.
- UNKNOWN: whether Archives' generic `args: object` interface accepts an explicit `session` property at runtime. Lack of a documented named parameter **does not prove** runtime rejection. Archives has not made an explicit session call for sessions 2–4 in this seat.
- UNKNOWN: exact registered connector/app ID, endpoint, registration version, schema JSON `inputSchema`, refresh state and route parity across Workshop and Archives. No access to those details established.

## Component boundary
Gate-01 is the original shared-message ledger system. Gate-02 is the newer workspace/server development environment. The read-only GPT terminal viewport bridge and GPT-side connector registration are distinct from both application layers. Neither same ChatGPT account nor same tool display name proves identical connector registration or endpoint. No evidence establishes that Archives is routed to Gate-01 instead of Gate-02.

## Candidate explanations — HYPOTHESES ONLY
- Stale/different GPT connector registration or cached tool definition.
- Different endpoint or older viewport bridge build.
- Generic advertised tool schema that accepts `session` even without explicitly listing it.
- Session-specific tool definition refresh discrepancy.

## Corrected interpretation of earlier PASS/FAIL
- Terminal 1: direct Archives PASS for the default `a25-gpt` view.
- Terminals 2–4: **NOT VERIFIED by Archives**, rather than demonstrated server FAIL. Earlier Archives responses calling them FAIL referred to lack of demonstrated independent selection, not a failed explicit runtime invocation.
- Workshop four-session PASS is preserved as a separate reported finding pending cross-seat evidence comparison.

## Next justified action
Project Lead/connector builder should compare exact registered input schemas, endpoint identities (redacting secrets), and registration versions across seats. With owner authorization, attempt a read-only explicit-session invocation in Archives before diagnosing rejection. Do not change Termux, Gate-01, Gate-02, bridge code, connector registration, or permissions on this note alone.

## Preservation
Keep both Workshop and Archives findings intact. No adopted root cause and no implementation change is claimed.
