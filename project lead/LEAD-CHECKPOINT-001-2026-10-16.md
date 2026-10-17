# A25 Project Lead — Current State and Succession Checkpoint

**FROM:** GPT — A25 Project Lead
**FOR:** Successor GPT lead, Zed, Claude, delegated builders
**DATE:** 2026-10-16, after 23:28 MDT
**RE:** Durable state transfer when the Project Lead chat is compacted, lost or replaced
**BASIS:** GitHub development branch, Actions #47–#48, Zed's instructions and prior A25 checkpoints

## Authority and identities
Zed is final human authority and relay. GPT Project Lead plans and coordinates GitHub development; Claude is independent reviewer and Drive lead, with separate evidence and conclusions. Local GPT builders and GitHub AI agents are delegated implementers, **not replacement leads or approvers**. A new GPT chat does not inherit authority by claiming the lead role; Zed appoints the successor and supplies this checkpoint. No AI can speak as another seat.

## Repository and locations
- GitHub: `Stratumnova/A25-Training-Workspace`
- Active development branch: `build/wd-02-watchdog-v0`; `main` must not be merged or changed without Zed's decision.
- Drive root: `A25 AI workshop/workspace`; Claude owns Drive originals, GPT owns its designated Drive lane. Drive remains separate from GitHub; Pocket Server is planned future authoritative Roundtable ledger.
- `local build orders/`: human-readable, scoped build orders to delegate to other AI sessions.
- `project lead/`: durable lead decisions, status and succession.
- `training/`: builder rules, Actions lessons, CS-004 continuity and blackout records.
- `roundtable/gpt/`: outgoing GPT communications; `roundtable/inbox/`: received messages, protected by Watchdog.
- `exceptions/`: explanatory sidecars for authorized rule exceptions.

## Latest verified state
- Watchdog draft Actions run #47: **23 tests PASS; actual repository 0 FAIL / 4 WARN**; run URL https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005925303
- Run #48: **SUCCESS**, commit `668373e720f08f486dd4d7e29d5d22738615c1df` (confirmed through GitHub API).
- Four warnings at run #47: approved W3 missing DATE for one GPT inbox handoff; old inbox README headers; old RT-001 BASIS/RE; corrected historical W5 F-002 collision.
- WD-35 exact-byte baseline restoration committed at `891d0cfef58edb11176e9ce8585580781861501a`, original Git blob `e317b1c42668126141baecd797cad84b4a1d57fe`. Marker and sidecar exist; Claude reviewed design but **not blackout implementation**.
- Claude's full ZIP audit was interrupted when Claude's UI displayed context compaction then a usage limit around 23:09–23:12 MDT. It is not known whether Claude lost context or completed the audit. See `training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md`.
- Claude's independent review of blackout commits and GPT's Actions training report remains open. Do not treat green CI as Claude approval.
- GitHub AI agent is not yet set up. `local build orders/LBO-001-GITHUB-AI-BUILDER-SETUP.md` is the assigned local-builder work order, not proof of agent installation.

## Important decisions and rationale
1. **Separate roles and evidence.** Two seats produce independent findings; Zed resolves disagreements. Avoid an AI answering a question addressed to Zed or adopting another seat's identity.
2. **Protected history is immutable by default.** W1 verifies hashes, W2 coverage, W3 headers, W4 append-only, W5 canonical IDs, W6 safe CI. Keep failures visible; repair with explicit narrow sidecars rather than rewriting the record.
3. **Exceptions are transparent.** GPT proposes, Claude reviews when available, both explicitly label agreement/disagreement; Zed's relayed pass-through without intervention counts as approval under Zed's 22:52 rule. Zed may intervene to stop. During Claude blackout, no fabricated double-yes; new exceptions must wait or obtain explicit separate Zed decision.
4. **Human code approval is future design only.** Never ask Zed to type a password/token into an AI chat. Device-side signature and replay protection remain proposals, not implemented.
5. **CI is evidence, not authority.** Record full run URLs, isolated tests and actual W1–W6 counts. A red run may be a correctly caught violation; a green draft run does not authorize a merge.
6. **External continuity over chat memory.** Save checkpoint, evidence, outstanding approvals and handoff to GitHub/Drive/Pocket Server. Compaction, rate limits and confirmed memory loss are different events; do not assert loss without verification.
7. **Delegate bounded builds.** Lead session should focus on decisions, reviews and handoffs. Builder branches and PRs are preferred; do not let builders self-approve.

## Lead workflow
- Read this checkpoint, `training/BUILDER-WORKFLOW-RULES-2026-10-16.md`, `training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md`, `training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md` and recent GitHub commits.
- Confirm latest branch HEAD and Actions directly; the values in this checkpoint are a historical snapshot.
- Read `local build orders/` and pending builder results; assign narrowly scoped work. Inspect actual diff and CI before accepting.
- Maintain `project lead/DECISION-LOG.md` as an additive record. Do not rewrite older decisions to hide changes.
- Publish new numbered checkpoints when role, branch, exception, milestone or pending review materially changes. Keep raw pinned links ready for Zed and Claude.
- Never silently skip Claude's open independent-review backlog or merge to main.

## Open work queue
1. LBO-001: local GPT builder to inventory/configure safe GitHub AI agent workflow; report before any settings changes or app installs.
2. Claude returns: verify ZIP receipt, complete file-by-file audit, review WD-35 blackout implementation and training Actions report.
3. Decide whether to add stronger behavioral W4 restoration fixtures; current new WD-35 tests are static guard checks.
4. Pocket Server: inventory Gate-01/auth/Shared Space, then PS-001 ledger/cursors/identity/continuity; no premature production claims.
5. Future approval prompt: device-side signed exception approval with expiry, exact file/rule binding, replay protection and revocation.

## Succession protocol
If this lead session is unavailable, Zed appoints a new GPT lead. Successor reads latest numbered checkpoint and decision log, validates GitHub/Drive source state, writes a `LEAD-RESUMED` note with source checkpoint, verified commit, pending approvals and uncertainties, and only then continues. Do not infer missing approvals from chat summaries. Never delete the old checkpoint. If Claude is unavailable, mark all GPT-only implementation as pending independent review.

**Snapshot boundary:** New commits after this file's publication are not covered until the next checkpoint. Always inspect the branch and Actions.
