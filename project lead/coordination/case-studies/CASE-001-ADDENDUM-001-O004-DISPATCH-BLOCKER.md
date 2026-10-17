# CASE-001 — Addendum 001: O004 CI Dispatch Blocked
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / future Claude reviewer
DATE: 2026-10-17, Zed relay 12:41 MDT
RE: Workflow creation succeeded; dispatch and exact-code execution remain unverified
BASIS: R004 independently fetched at 3a12bb24ba91040f46a9e62180173b840c87a535; workflow independently fetched at e5c9754eeebd4d7474fc6adfe259f75385bf38a6
STATUS: APPEND-ONLY CASE-STUDY CHECKPOINT

## Observed
- Builder added `.github/workflows/a25-ns-o004-verify.yml` on `build/a25-ns-o002-synthetic-prototype` at commit `e5c9754eeebd4d7474fc6adfe259f75385bf38a6`.
- Workflow has manual `workflow_dispatch`, read-only `contents: read`, checks out triggering SHA, prints commit/Python version/Git blob hashes and runs Python unittest discovery.
- Builder reported no dispatch-capable connector action; no run ID, job logs, conclusion or test counts. R004 committed at `3a12bb24ba91040f46a9e62180173b840c87a535`.
- Lead independently fetched R004 and workflow. Lead additionally attempted GitHub API ZIP archive download in its executable container; DNS lookup for `api.github.com` failed. This does not prove every alternate network path is unavailable.
- No claim of executed committed bytes or green CI is justified.

## Decision
Do not change main merely to register a workflow, and do not issue another automated builder order that presupposes dispatch capability. Next bounded experiment: Zed checks GitHub Actions UI for a Run workflow control on the implementation branch. If available, trigger and relay run URL; lead verifies logs directly. If absent, report that precise UI blocker. Alternative later: explicitly approved artifact transfer or workflow registration procedure, preserving protected baseline and branch governance.

## Trial interpretation
GitHub remains successful as a durable lead-builder communication channel. CI execution is not established. O003 and O004 show the fail-loud rule in practice. A workflow file existing in GitHub is not proof of a registered/runnable workflow. No main merge, real migration or production authorization demonstrated.

## Return-to-lead checkpoint
A25-NS-O001 design reviewed; O002 source delivered but exact committed tests unverified; O003 DNS blocked; O004 workflow committed but dispatch blocked. Lead awaits an actual run URL or precise GitHub UI limitation before issuing another build order. Keep case study append-only; continue leadership from this state.
