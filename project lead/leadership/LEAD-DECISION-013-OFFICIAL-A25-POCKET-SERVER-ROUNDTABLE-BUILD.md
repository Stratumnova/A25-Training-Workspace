# LEAD-DECISION-013 — Official A25 Pocket Server and Roundtable Communication Build
Decision date: 2026-10-17 20:02 MDT (owner-provided)
Authority: Zed, owner and Watchdog
Recorder: GPT A25 Project Lead
Status: ADOPTED; branch creation independently verified by GitHub tool response. Implementation NOT YET VERIFIED.

## Decision: when, why, where, for whom
WHEN: Owner approval at 8:02 PM MDT, October 17, 2026.
WHY: O003 could not edit protected main and was forbidden to create a branch. Existing branches were reviewed; a25/training-workspace is a documentation workspace, with gate02/server.py identical to main. Existing other branches have separate responsibilities. A single dedicated build branch resolves the blocker while preserving historical work.
WHERE: Repository Stratumnova/pockettest, official long-lived branch `build/a25-pocket-server-roundtable`.
BASE: `main` commit `f0a11d51968ad598691333d32971dfb483489073`.
FOR WHOM: Zed (owner); GPT A25 Project Lead (coordinator); A25-PM-GPT01 (primary builder); A25-CW-CLAUDE01 (Drive writer/relay operator); replacement Claude technical helper (independent code review, fresh identity assigned on launch); future Roundtable participants.

## Branch creation evidence
GPT Lead called GitHub create_branch with repository Stratumnova/pockettest, name build/a25-pocket-server-roundtable, exact base SHA f0a11d51968ad598691333d32971dfb483489073. Tool returned branch build/a25-pocket-server-roundtable. No server code modified in this action.

## Official branch rules (owner ADOPTED)
1. This is the ONE official implementation branch for A25 Pocket Server and Roundtable Communication, maintained start to finish through completion. Do not fork child branches or replace it without new Zed authorization.
2. Work in this existing repository and branch. Do not modify main or other development branches by default; preserve prior history and separate terminal viewpoint.
3. Every meaningful build change needs traceable authorization, author, location, rationale, test evidence, and known limitations. Keep reports and independent review records in existing A25-Training-Workspace coordination and Claude Drive channels.
4. Do not treat historical materials or builder reports as automatically verified. Keep REFERENCE / HISTORICAL CLAIM / VERIFIED / ADOPTED / SUPERSEDED / UNKNOWN separate. No assumed test PASS.
5. GPT Lead directs work; GPT builder implements; replacement Claude technical helper independently reviews; Claude Writer publishes and retrieves authorized Drive records; Zed retains approval for protected actions and operates Android phone as necessary.

## End-to-end project objective
Build a shared, durable Pocket Server hosted on Zed's Android phone, allowing distinct GPT and Claude accounts to independently read the same state, exchange Roundtable messages with append-only ledger/cursors and correct author attribution, resume after interrupted sessions/restarts, access common project files, and later write shared files and execute explicitly authorized terminal operations. Preserve free/no API-cost aspiration, distinct identities, read-first workflow, owner control, evidence integrity, and independent GPT/Claude verification. Do not confuse a Drive relay PASS with a live Pocket Server PASS.

## Progressive milestones (not completion claims)
M1: Minimal read-only shared-file view on existing Gate-02A source, deterministic tests; use nonsecret designated test file and no public anonymous deployment without explicit safe exposure review.
M2: Independent GPT and Claude client reading of identical content with size/hash receipts; stop/restart/retest and final stop under Zed's phone control.
M3: Shared write with integrity controls and durable ledger; define safe operation contracts.
M4: Distinct authenticated identities, bounded authorization, provenance and safe remote connectivity.
M5: Owner-directed controlled terminal/file operations, recovery, documentation and final acceptance.
Sequence can be refined by Lead based on evidence, but branch continuity is fixed unless owner changes it. Identity/security must be adequate before exposing write/terminal features remotely.

## Current evidence/status
R002 GPT builder is BLOCKED due to contradictory edit destination constraints, not a runtime failure. No Gate-02A shared-file code has been implemented, tests run, or Android deployment completed. Official branch creation resolves only the code-edit destination blocker. New corrective implementation order follows.
