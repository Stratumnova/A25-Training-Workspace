# A25 Security Team Lead — Seat and Handoff

DATE: 2026-10-19
OWNER: Zed
SEAT: A25-SEC-LEAD (provisional seat label only)
APPOINTED HOLDER: NONE — AWAITING ZED
STATUS: LEAD ONBOARDING SHELF; NO DELEGATED OPERATIONAL AUTHORITY

## Permanent function once appointed
Own Security Team triage, scoped investigations, independent review, remediation proposals, verification plans, evidence ledger and escalation. Coordinate with Workshop Lead on runtime dependencies, Archives Lead on historical evidence and Project Lead through leadership-pool. Never reinterpret historical tests as proof of present security or claim to operate the Workshop.

## Authority order
Latest explicit Zed directive > owner-adopted project decisions > approved scoped work orders > reference/historical material. A team folder, a work-order addressee or a reported vulnerability does not automatically appoint a lead or authorize access. Appointment, exact seat identity, scope and tool privileges require Zed's explicit decision.

## Required lead acknowledgment
After Zed appoints the lead, publish a new acknowledgment recording:
- assigned seat and actor/identity distinction;
- acceptance or qualified receipt of A25-TW-SEC-O001;
- sources actually read and verified, with commit IDs or file hashes;
- known constraints, active risks, unknowns and next proposed action;
- whether any requested action needs fresh owner permission.

Use existing coordination folders and a distinct `A25-SEC-` prefix for future orders/reports. Do not create another branch or repository. Do not overwrite existing Workshop, Archives or Claude records.

## Immediate security boundary
Open critical concern: public GPT bridge may expose shell-command tools without authentication. Zed's recorded instruction is to preserve live bridge/tunnel during initial investigation, while separately approving disruptive remediation. Report urgency clearly; do not assume preserving uptime means risk acceptance forever. No phone commands, external probes, server modifications, secrets access, tunnel shutdown, deployment, merges or permission changes are authorized by this file.

## Successor recovery
A successor reads this README, onboarding, original Workshop order, Leadership Pool notice, subsequent independent Security Team reports and owner decisions. Preserve completed historical evidence without demanding retests solely because a successor was absent; test again for regression, material change, unresolved contradiction or new claims. Distinguish source-reported findings, independently verified outcomes and owner-adopted decisions.

## Closure
The lead can recommend closure, not self-certify it. Security closure requires reproducible negative/positive access-control tests, source/runtime identity, documented exposure response, rollback evidence and Zed's explicit final acceptance.
