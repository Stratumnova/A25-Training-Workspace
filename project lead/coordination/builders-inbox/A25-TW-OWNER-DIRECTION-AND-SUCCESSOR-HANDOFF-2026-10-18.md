# A25 Terminal Workshop — Owner Direction and Successor Handoff
DATE: 2026-10-18
FROM: A25-TW-GPT01, recording Zed's current owner instructions
STATUS: ADOPTED OWNER INTENT / IMPLEMENTATION NOT VERIFIED
BRANCH: coord/a25-namespace-trial-001
AUDIENCE: Workshop Lead successor, G1, G2, Project Lead, Archives

## Binding scope from owner conversation
Zed directs Workshop to construct **Zone 1**, one actual local Android/Termux working location analogous to an extra D: drive. GPT and Claude should independently work in the SAME workspace: create/read/edit/delete files, execute commands, build, run tests, inspect results, and collaborate on one project. Existing Stratumnova/pockettest Pocket Server/Gate/Shared Space and terminal bridge are starting assets, not a request to create a new architecture. The D: comparison is conceptual, not a literal Windows drive.

Owner expressly authorizes early-stage **local trust and LLM-script/folder conventions**, even if incomplete or unstable, for construction and testing. Workshop must not impose identity authentication, permission-matrix design, Watchdog, or a separate security review as prerequisites. Security team handles security design; Archives handles preservation/evidence. Report any suspected leak, port exposure, or defect clearly to responsible team; continue independently possible authorized work, without concealing failures or claiming a failed operation passed. Do not publish credentials or deliberately expose the device; avoid irreversible destructive operations. Owner remains ultimate authority and can stop or change course.

**Watchdog is a LATER shared project**: after GPT and Claude can collaborate on a single bot in Zone 1, build one Watchdog together inside Zone 1 and use that experience to improve Zone 1 there. Do not build Watchdog now as a gate.

Zone 1 target is primary daily development/test collaboration; GitHub and Drive are downstream storage/backup/CI after Zone 1 is proven. Until then preserve existing GitHub coordination and manual courier. Do not assert Zone 1 already exists or replace current reporting workflow.

## Current evidence
G1 read-only report: project lead/coordination/reports/A25-TW-R001-BG-GPT01-POCKET-SERVER-SOURCE-ROUTE.md. It identifies pockettest build/shared-space-v0 commit 9a419e925dff2de64ef948b7d6d8304eccf8387d as a source candidate, with Shared Space storage/transport helpers but no general file CRUD/command execution.
G2 read-only report: project lead/coordination/reports/A25-TW-R002-BG-GPT02-GPT-CONNECTOR-CAPABILITY.md. Actual GPT Terminal plugin in G2's session exposed terminal_status and terminal_view, both read-only, not terminal execution.
G1-G2 interface proposal: project lead/coordination/builders-inbox/A25-TW-G1-TO-G2-SOURCE-INTERFACE-2026-10-18.md; proposal, not adopted contract.
Archives source map: project lead/coordination/builders-inbox/A25-AG-GPT01-2026-10-18-ZONE1-SOURCE-AND-EVIDENCE-MAP.md at a01e624b8099af248539c518e8989bc94142d22c. Workshop verified 11 document and 6 source paths retrievable, not runtime functionality.
Owner direction: project lead/coordination/builders-inbox/A25-OWNER-DIRECTION-2026-10-18-ZONE1-DAILY-WORKSPACE.md.
Cross-platform relay test: A25-CL-CLAUDE01-2026-10-18-GITHUB-INBOX-TEST-001.md at 0e0ca425b5a1f5a2bdd1d2caed112821dff2c1ed, token acknowledged by Workshop; does NOT prove direct Claude GitHub access.

## Active team and operating process
G1 A25-TW-BG-GPT01 = Pocket Server/source builder. G2 A25-TW-BG-GPT02 = GPT connector builder. Claude C1/C2 standby; Zed conserved Claude usage until needed. Orders in project lead/coordination/orders; formal reports in project lead/coordination/reports; interim blockers/handoffs in project lead/coordination/builders-inbox. Use uniquely named new files; do not overwrite originals. On Zed's 'done', 'next', or 'status', Workshop Lead actually checks both inbox and reports, not guesses. No new repository or branch, no phone deployment without separate owner-coordinated live step. No automatic cross-chat connection.

## Acceptance sequence
(1) real local workspace and source-backed operations; (2) GPT real file create/read/edit/delete and harmless command/test with observed outputs; (3) Claude accesses same workspace and edits GPT-created project; (4) GPT reads changes and both test same project; (5) later Watchdog shared build. Record what actually happened, errors, paths (redacted if sensitive), commands, test results, and unknowns. Functional milestone does not require finished security design, but must be reproducible rather than asserted.

## Continuation
New lead reads this note, owner direction, current builder orders/reports and any newer inbox notes; preserve owner scope. Next scoped implementation orders O004/O005 are issued separately; check their exact filenames/commits. Resolve branch/source placement in G1, connector binding in G2. Owner may authorize live phone deployment when implementation is ready. Do not infer deployment from GitHub commits.
