# A25-TW Knowledge Index 001 — Study and communication map
DATE: 2026-10-18
FOR: A25-TW-GPT01
STATUS: ORIENTATION INDEX — NOT AN IMPLEMENTATION ORDER

## Read in order
1. `project lead/coordination/README.md` — verified existing two-session GitHub handoff protocol, authority, append-only records and truth/fail-loud principle.
2. `project lead/leadership/terminal-workshop/README.md` — leadership home, scope boundaries, folder rules and Drive restrictions.
3. `project lead/coordination/builders-inbox/A25-TW-GPT01-ONBOARDING-ACK-2026-10-18.md` — your confirmed appointment and owner priority, commit `f2bf0a74b39df4a27839c92d45206a8f1f8887b2`.
4. `project lead/coordination/orders/` — numbered work assignments, pinned to exact GitHub commit. Terminal Workshop prefix `A25-TW-O###-`.
5. `project lead/coordination/reports/` — builder execution/results reports, prefix `A25-TW-R###-`. Read the exact order and commit before evaluating a report.
6. `project lead/coordination/builders-inbox/` — uniquely named interim notes, terminal receipts, questions and blockers; this supplements, not replaces, formal reports.
7. `project lead/leadership/archives/` — archive reviews, dispositions and evidence-classification examples. Acceptance of a report is not deployment proof.
8. AV-R001 ZIP baseline and SHA receipts: `project lead/coordination/reports/A25-AV-R001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md` at `053d2e7868bfdd85d1659d40e8e7002e14d58a47`; `project lead/coordination/builders-inbox/A25-AB-NOTE-2026-10-18-TERMUX-ZIP-SHA256-RECEIPTS.md` at `a202ae461a6cbd051894a1280bfafbc67998619b`. These are orientation examples, not a new requirement to repeat archival work.

## Communication routes
**Zed → lead:** owner directives, priorities, approvals. Record durable adopted decisions with date/source, while protecting private instructions.

**Lead → builder/team:** create a numbered scoped order in `coordination/orders/`, include FROM/TO/DATE/BASIS/branch/source commit/expected report path/scope/stop conditions. Zed or authorized connector relays exact pinned order link; do not assume another AI sees this chat.

**Builder/team → lead:** builder reads pinned order, works only within authorization, writes a new report to `coordination/reports/`, returns path and full SHA; interim evidence goes to `coordination/builders-inbox/`.

**Lead → Zed:** independently fetch and assess report, distinguish claim from reproduced evidence, record acceptance or correction separately, and seek owner decision when required.

**Drive ↔ GitHub:** GitHub coordination branch is the durable order/report/decision trail. Drive is a separate owner workspace and reference store with stable file IDs; folder moves do not establish content parity. Claude is authorized to organize within its owner-approved Drive scope; GPT Archives and Gemini are read-only. No new Drive permissions are conferred by this index. For any source on Drive, record stable ID, version if available, access date and provenance; link to the record rather than copying sensitive material into public GitHub.

## Logging — what, when, how
- **Observation / test result:** log immediately after work, with tool, exact command or action, environment, time, output digest/log link, expected vs actual, and what remains UNKNOWN. Never equate terminal viewport with command execution.
- **Error / blocker:** log as soon as encountered; record operation, exact error, affected path/commit, whether any side effects occurred, reproducibility and safe next step. If GitHub safety-blocked, STOP and report to Zed; do not retry without explicit authorization.
- **Decision:** record when Zed or an authorized decision-maker accepts/rejects an option; include alternatives, rationale, source, effective scope and whether implementation was independently verified. Distinguish ADOPTED from VERIFIED.
- **Correction / conflict:** preserve originals and both conflicting findings; create a new dated correction/addendum and link both sources. Escalate unresolved GPT/Claude disagreement to GPT Project Lead.
- **Handoff:** after a discrete task, record exact source order, report path, full commit SHA, changed/unchanged files, checks performed, failures and next authorized action. Do not report success from prose alone.

## Evidence labels
REFERENCE = supplied source; HISTORICAL CLAIM = reported past event not independently checked; VERIFIED = reproducible direct evidence; ADOPTED = authorized decision; SUPERSEDED = replaced by later verified decision or implementation; UNKNOWN = unresolved. Historical reports, screenshots and AI statements cannot override current Zed instructions.

## Orientation completion
Lead reviews this index and the original records, identifies missing or inaccessible sources, prepares a short team study-material and build-order routing guide using existing folders, and reports its own understanding and open questions. No new architecture, implementation, security project or permission change is implied.
