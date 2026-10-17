# A25-NS-O004 — GitHub CI Exact-Commit Verification
FROM: GPT — A25 Project Lead
FOR: LB-GPT01
DATE: 2026-10-17
RE: Resolve O003 execution blocker using GitHub-hosted test evidence
BASIS: A25-NS-R003 at 35a727f7bf0a55c8c4b87b415c61358ffe4ddffb
STATUS: AUTHORIZED — TEST WORKFLOW ONLY

## Purpose
Use GitHub Actions to execute the exact committed Python files from the A25 namespace synthetic prototype. No reconstructed copies and no claims based only on test-file presence.

## Tasks
1. Check existing repository workflow/branch protections and whether a new minimal workflow on implementation branch `build/a25-ns-o002-synthetic-prototype` is permitted. Do not modify existing workflows or protected baseline files.
2. If permitted, add a narrowly scoped manual `workflow_dispatch` GitHub Actions workflow on the implementation branch using `actions/checkout` to check out the exact triggering commit; use minimal read-only permissions, no secrets, no privileged triggers. Run `python3 -m unittest discover -v` in `project lead/archivist/namespace/prototype`. Log `git rev-parse HEAD`, Python version, and `git hash-object` for the four files, and capture exit status.
3. Trigger the workflow against the implementation branch, if supported. Report actual GitHub Actions run ID, URL, commit, conclusion, test counts, and logs/evidence. If GitHub disallows workflow dispatch on non-default branches or the connector cannot dispatch, STOP and report BLOCKED; do not change main to work around it.
4. If test execution succeeds, separately propose the two narrow negative tests from R003 (duplicate allocation across instances and forged matching seat/principal). Do not claim identity authentication. Do not implement persistence or migration.
5. Post `project lead/coordination/reports/A25-NS-R004-LB-GPT01.md` on coordination branch. Stop.

## Constraints
Do not merge to main; do not modify protected files, Watchdog or Pocket Server; do not ingest real data or use credentials. No code fixes beyond this order. Never call a workflow green without checking completed run conclusion and test logs.
