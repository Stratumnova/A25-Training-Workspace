# RN-001 FINDING-002 — Name, Timestamp and Scope Drift
FROM: GPT — A25 Project Lead
FOR: Zed
DATE: 2026-10-17 15:33 MDT (Zed-provided)
STATUS: OPEN — DO NOT COLLAPSE OR AUTO-RESOLVE

## Trigger
Claude report A25clauderecall_id001 (Drive ID 15fzkYQlfThEsemntyGnoUqA5hewAkF38) described Watchdog/Tripwire among A25 design concepts as PROPOSED, while the lead's prior A25 coordination review references a separate Watchdog implementation branch and historical runs. The source scopes differ; neither assertion is sufficient to conclude the other is false.

## Required handling
Every candidate project or component mapping must retain (1) exact source name and alias, (2) reporting session and seat, (3) original source path, branch and full commit or Drive ID, (4) claimed status with evidence class, (5) observation timestamp UTC vs event timestamp UTC, (6) implementation scope/component, and (7) unresolved reconciliation questions. Do not conflate design-stage idea with tested implementation, or historical status with current state. Preserve source statements verbatim in original reports. Reconcile by source revision and component boundaries, not majority vote or latest timestamp alone.

## Follow-up
When GPT Pocket Server recall arrives, compare its component taxonomy, branch/commit, timestamp and test evidence with Claude P1. Record any mismatch as an independent claim and request exact source checks before changing the canonical map. No prior report edits or main merge.

## Other example
Claude corrected Gate-01 event #3 timestamp (2026-10-08T05:02:21Z) previously mistaken for restart recovery timestamp. Recovery timestamp remains UNKNOWN. This demonstrates event-time vs observation-time distinction.

VERDICT: VALID ANTI-DRIFT STUDY FINDING; FACTUAL STATUS RECONCILIATION PENDING.
