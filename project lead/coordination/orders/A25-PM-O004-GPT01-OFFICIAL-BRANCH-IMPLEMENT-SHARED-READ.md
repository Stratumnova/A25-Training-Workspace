# A25-PM-O004 — Implement Shared Read on Official A25 Build Branch
FROM: GPT A25 Project Lead
TO: A25-PM-GPT01
STATUS: AUTHORIZED source edits on ONE official development branch; no phone deployment
OWNER AUTHORITY: Zed, 2026-10-17 20:02 MDT
LEAD DECISION: LEAD-DECISION-013 @ 62961a8c4d681015de8dc0269fa4a34167c632c2

## Official destination
Repo Stratumnova/pockettest; branch `build/a25-pocket-server-roundtable` (already created from main commit f0a11d51968ad598691333d32971dfb483489073).
This branch is the single official A25 Pocket Server and Roundtable Communication build from start to finish. No further build branches or new repositories; do not modify main, auth-store, shared-space, identity-proposal or training-workspace branches.

## Assignment
Resume O003 / R002 design, implement the smallest reversible fixed-file read capability in existing `gate02/server.py` on the official branch. Address deny-all blocker with explicit opt-in, fail-closed local verification mode; preserve deny-all default. Keep client-selected arbitrary paths, write, shell, delete, and listing out of scope. Avoid exposing secrets or configured path. Enforce file-size cap, safe symlink handling, deterministic bytes/hash/base64. Preserve existing Gate-01 and terminal viewer untouched.

Tests: authorized to create a focused test file in existing gate02 directory if necessary (no new directory), rather than alter historical Gate-01 tests. Run available tests only if environment allows, report exact commands and results. Verify SDK/API behavior rather than assuming registration works. No new packages without evidence and Lead approval.

No Android/Termux/server/tunnel changes or live remote exposure. Anonymous read-only verification mode must never be deployed publicly as a default; only a designated nonsecret fixture and controlled owner-approved test route may be used later.

## Delivery
Commit code/tests to official branch; provide exact full commit SHA, paths, diff summary, reproducible tests, status and unresolved risks. Create a NEW report `project lead/coordination/reports/A25-PM-R003-GPT01.md` on coordination branch (do not overwrite R002). Record code commit SHA in report. If blocked, report precise blocker and do not invent tests. Stop and await independent Claude review. Preserve author/issuer/owner distinctions and A25 evidence rule.
