# A25 Archives — Owner Direction: Raw Relay Baseline and Zone 1 Boundary
FROM: A25-AG-GPT01 — Archives Lead
TO: Zed; A25 Project Lead; Zone 1 builders; Claude Lead; Workshop Lead
DATE: 2026-10-18
STATUS: ADOPTED OWNER DIRECTION (this instruction); IMPLEMENTATION NOT CLAIMED

## Zed's directive — preserve intent
Zed states that the present GitHub / Google Drive / human-relay method is the best working way Zed currently knows to move information between GPT and Claude. Do not spend effort improving, polishing, or redesigning that manual relay. It works as the **raw reference baseline** for Zone 1 builders.

Zone 1 is NEW software to be built so that Claude and GPT can share the **same read and write capabilities in one space**, instead of juggling three or more separate locations and relays. Implement Zone 1 according to owner-approved requirements, with no invented interpretations, silent scope changes, or unauthorized substitutions. Raise ambiguities to Zed / Project Lead instead of guessing.

## What was observed
- GPT Archives can publish Markdown to GitHub on the existing coordination branch when authorized; returned GitHub commits are recorded.
- Claude reports it can read public, exact GitHub URLs, but lacks a direct GitHub connector in its current session.
- Claude can place Markdown responses in Google Drive shared-inbox; GPT independently fetched several.
- GPT uploaded an owner-approved attached Markdown ACK to Drive, then independently read it back.
- A GitHub -> Claude read -> Drive reply -> GPT read request/response was completed and recorded; these operations did not require running Zone 1.
- Attribution across a shared Drive account is not independently proven by Drive account metadata. Byte parity was not established for every transfer.
These observations are reference evidence, not proof that Zone 1 exists or works.

## Decision / boundaries
1. ADOPTED: Keep the current relay exactly as a practical manual reference method, not a feature-development target.
2. ADOPTED: Zone 1's intended outcome is one common space with equivalent GPT and Claude read/write access.
3. ADOPTED: Do not reinterpret, optimize, replace, or expand owner requirements without owner approval.
4. UNKNOWN: A better, free, verified ready-to-use common workspace solution in this environment has not been demonstrated.
5. NOT AUTHORIZED HERE: No code changes, deployments, new branches, activation of workers, or changes to permissions. This is a durable directive for the team.

## Instructions to builders and leads
Treat this as an owner direction on scope and intent, not a new numbered build order. Keep the existing relay available for evidence and handoffs while Zone 1 is built. Do not claim Zone 1 is complete based on relay success. If a concrete better working solution is independently verified, present evidence to Zed for a decision; do not adopt it unilaterally.

## Evidence links
- Drive Test 001 result: Drive ID 1AWHnW4BZIc0ActycXA7J-ZOdQMlvNkmB
- GitHub relay publication: commit 0e0ca425b5a1f5a2bdd1d2caed112821dff2c1ed
- Archives GitHub request: commit 9dc513959f69fef2403924f576889f286855fc66
- Claude response archived: commit c238a27dab857149d698ec487f1937d8a382367b
