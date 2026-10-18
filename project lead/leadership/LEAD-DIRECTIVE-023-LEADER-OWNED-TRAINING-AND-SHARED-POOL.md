# LEAD-DIRECTIVE-023 — Leader-owned training and cross-project leadership pool
FROM: Zed (owner direction), recorded by A25-AG-GPT01
DATE: 2026-10-17 21:48 MDT (owner-supplied)
STATUS: ADOPTED OWNER DIRECTION; implementation limited to documentation
SCOPE: All A25 leaders; Archives Lead records this directive

## Owner's direction
1. Training materials stay clean and under leadership custody. Only a leader adds to training materials. Each leader maintains training notes for their own domain in their leadership area. Archives lead owns Archives training; Roundtable lead owns Roundtable training. The future Academy is a separate joint decision, not an automatic dumping ground.
2. When Zed requests a training-material entry, place it in the responsible leader's leadership notes. Also provide a separate shareable handoff item in the leadership pool for other leaders to pull into their own records if relevant. Do not silently edit another leader's notes.
3. Cross-project concerns, discoveries, dependencies and useful information belong in the leadership pool. The receiving project leader reviews and explicitly adopts or rejects them in their own area. The future Security leader/team may consume security-related flags; Archives/Watchdog only flag and preserve evidence, not independently own deeper security engineering.
4. Keep builder-level working materials, tests, raw evidence and implementation reports in their existing lower-level project paths. Leaders curate training; builders do not directly promote their reports into leadership training.
5. Original sources and previous decisions remain unchanged. An incoming pool note is a message, not automatically a verified fact or a new order.

## Existing locations and new interface
- Leadership notes: existing `project lead/leadership/` (current shared leadership area). Leader-specific subfolders are not presumed to exist; do not invent migrations.
- Cross-project inbox: `project lead/leadership-pool/` with README and append-only notes.
- Builder orders/reports: existing `project lead/coordination/orders/` and `reports/`.
- Source evidence: original repository/file/commit remains authoritative.

## Operating rule
Leader creates a new uniquely named note in the pool with FROM, TO, DATE, PROJECT, TYPE, SOURCE, evidence status, action requested, owner and disposition. Receiving leader may reference or copy it to their own leadership record, preserving original attribution and linking source. No auto-approval, auto-security escalation or autonomous changes. No retroactive modification of earlier training.
## Open design question
Dedicated per-leader leadership subfolders and Academy organization are future decisions. Existing files stay canonical until separately approved.
