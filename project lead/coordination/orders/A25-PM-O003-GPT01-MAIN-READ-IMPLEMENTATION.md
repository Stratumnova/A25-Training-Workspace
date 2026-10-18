# A25-PM-O003 — GPT01 Main Shared Read Implementation
FROM: GPT A25 Project Lead
TO: A25-PM-GPT01
DATE: 2026-10-17
STATUS: IMPLEMENTATION ORDER — existing paths only, no deployment
PREVIOUS: A25-PM-O001 / R001; LEAD-REVIEW-010; Directive 006; Direction 007

## Mission
Implement the smallest reversible shared-file read capability in the existing Stratumnova/pockettest hardened main Gate-02A server, using existing source/test paths. The existing separate read-only terminal viewport is untouched. Work in place; do not create a new repo, branch or folder.

## Authorized scope
1. Inspect existing gate02/server.py, its middleware/dependencies and current existing tests. Identify precise files to change; preserve existing unrelated behavior.
2. Add ONE read-only tool that returns the exact bytes/text (or lossless encoding), SHA-256 and byte length of a single designated existing file; do not invent a new storage location. Use a fixed configurable path (not arbitrary client-supplied path). Do not expose secrets or unrelated directories.
3. Resolve the current deny-all client reachability blocker with the smallest reversible read-only access route for both GPT and Claude, without launching broader security/identity work. State exactly what access route and configuration are needed and whether it can be verified remotely. Do not misrepresent anonymous access as authenticated identity.
4. Add minimal deterministic tests within existing test locations, including byte/hash correctness, missing file, absence of write/exec tools, and basic regression behavior. Keep tests narrow and relevant to this milestone.
5. Do not implement write/shell/delete/rename, expand Watchdog/Archivist, move or version the viewport, or create new directories.
6. Do not change protected main, deploy, alter phone configuration, start/stop servers or tunnel, or claim live runtime PASS. Prepare a reviewable patch and test evidence in the existing repository workflow only if the available connector supports a non-destructive edit route without creating a branch; otherwise report BLOCKED with exact patch proposal. Zed has not yet authorized live phone changes or main merge.
7. Do not silently modify historical code outside this scoped implementation. If implementation cannot be done without violating existing-path/no-branch rule, stop and report blocker; do not work around by creating another tree.
8. Report blockers and design choices to GPT Project Lead, not Zed. Provide exact filenames, before/after diff, tests run and their outputs. Clearly label unexecuted tests.

## Deliverable
Write ONE NEW report at project lead/coordination/reports/A25-PM-R002-GPT01.md on coord/a25-namespace-trial-001. If code changes cannot be committed under these constraints, include a precise patch plan and mark implementation BLOCKED. Return report path and full commit SHA, then stop.

## Later gate
After lead reviews implementation evidence, lead will coordinate independent Claude review and Zed's initial view/stop/restart/retest/final-stop phone sequence. Do not run those in this order.
