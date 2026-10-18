# A25-AB-O006 — Pocket Server versions and technical review evidence

**FROM:** A25-AG-GPT01, Archives Lead
**TO:** A25-AB-GPT01, Archives Builder
**DATE:** 2026-10-18
**BRANCH:** `coord/a25-namespace-trial-001`
**STATUS:** AUTHORIZED — READ-ONLY RESEARCH + ONE NEW REPORT
**REPORT PATH:** `project lead/coordination/reports/A25-AB-R006-GPT01-POCKET-SERVER-VERSIONS-REVIEWS.md`

## Objective
Reconstruct the distinct historical Pocket Server / Gate-01 / Gate-02A code lines, branches, checkpoints and GPT/Claude reviews, with a pinned original-source ledger. This is **not** a Watchdog/PR #3 investigation.

## Required source coverage
1. Inspect the official Pocket Server repo `Stratumnova/pockettest`, especially `main`, `build/a25-pocket-server-roundtable`, and pinned official implementation commits `442529a32356c5fb557d908fcd20bace733f04d8` and `fabedb661bb5161055534589c7517f7e0738139d`.
2. Trace separately the historical main deny-all baseline `f0a11d51968ad598691333d32971dfb483489073`, auth work `1b578ee32532f99093ab906af52e8b485c90a7e4`, Shared Space Stage 1 `9a419e925dff2de64ef948b7d6d8304eccf8387d`, and Stage 2 proposal `8ade3c00f4f5219182ec01b5154b4b89b71d3359`. Verify each commit's repo and branch before relying on it; if a hash cannot be located, mark UNKNOWN.
3. Retrieve original coordination orders/reports for Pocket Server work, especially `A25-PM-O007-CLAUDE02-R004-INDEPENDENT-REVIEW.md`, `A25-PM-R004-GPT01.md`, and source evidence indexed by `A25-AB-R003-GPT01-CLAUDE-DRIVE-COMMUNICATION-EVIDENCE.md`. Seek original Claude02 O007 review `A25-PM-R002-CLAUDE02.md` if connector access allows; otherwise identify it as inaccessible, not as verified.
4. Record original test outputs, review observations, unverified claims and unresolved defects separately. Include F-1/F-2/F-3/F-6 and R2-1 portless Host header issue when original sources support them; do not infer that review/test success means deployed integration or live MCP success.
5. Compare Claude and GPT reviews without resolving disagreements by preference. Distinguish local harness tests, regression tests, MCP SDK integration, phone/Termux operations, CI and production deployment.

## Evidence rules
- Mark each substantive statement **REFERENCE**, **HISTORICAL CLAIM**, **VERIFIED**, **ADOPTED**, **SUPERSEDED** or **UNKNOWN**.
- Pinned links, exact file paths, commit SHAs, dates, source-access outcomes and test scope required.
- Uploaded reports/ZIPs and prior AI summaries are references, not self-proving facts. Verify original code and tests where accessible.
- Preserve earlier versions and corrections; do not silently rewrite or overwrite source records.
- If a source cannot be accessed, document exact blocker and move on. Do not invent missing contents.

## Output and stop conditions
Create **only one new report** at the exact report path above on the existing coordination branch. Include a compact version matrix, review/test evidence ledger, unresolved questions and next justified verification action.
No other GitHub files, branches, PRs, merges, CI reruns, permission changes, phone/server/tunnel operations, or deployment.
Return report path and **full commit SHA**, then stop.
