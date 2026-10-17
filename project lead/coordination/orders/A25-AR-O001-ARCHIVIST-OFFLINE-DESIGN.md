# A25-AR-O001 — Offline Archivist Design, Existing Paths Only
FROM: GPT — A25 Project Lead
FOR: LB-GPT01 (builder)
DATE: 2026-10-17
STATUS: ORDERED — DESIGN AND INSPECTION ONLY
BASIS: Zed's direction to lead and repeated duplicate-path/source-drift failures; Leadership Directive 005; RN001-LOCAL-SOURCE-CHECKPOINT-001; RN001-ARCHIVIST-MINIMUM-PROTOTYPE-001.

## Mission
Inspect the existing A25-Training-Workspace coordination layout and RN-001 evidence references. Propose the smallest deterministic, offline, read-only Archivist implementation that indexes existing originals by reference without creating new folder trees or rewriting originals.

## Rules
1. Reuse the existing `project lead/coordination/orders/` and `reports/` handoff. Do not create a new repository, branch, folder, or implementation file in this order.
2. Review `project lead/coordination/README.md`, leadership Directive 005, Local Source Checkpoint 001 and Archivist Minimum Prototype 001, plus participant evidence index 002.
3. Inventory EXISTING candidate source-code/test locations in the current repo (do not assume one exists); recommend a precise file destination and explain why it is preferable to alternatives.
4. Design a minimal evidence schema, deterministic catalog build, error report, and at least six tests: missing source, timestamp confusion, branch conflation, unverified hash, outside-account 403 delivery, duplicate record.
5. Include explicit input/output file contract and privacy boundary. No phone commands, no live Pocket Server, no Actions run, no credential handling.
6. Do not infer that a design or historical test means current implementation is complete.
7. Record any inability to read source material as BLOCKED; do not fabricate.

## Deliverable
Write exactly ONE NEW report under `project lead/coordination/reports/A25-AR-R001-LB-GPT01.md` on `coord/a25-namespace-trial-001`. No other writes. Include inspected source refs, existing-path recommendation, schema, tests, risk notes, and implementation gate. Return report path and full commit SHA to Zed. Stop.

## Approval boundary
This order authorizes inspection and design report only. Lead will review before issuing any code-building order. Zed retains approval for new directories, prior-batch changes, local execution, protected merges, and server modifications.
