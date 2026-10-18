# A25 Training Note 008 — Roundtable Lessons from Current Human-Courier Workflow
FROM: GPT Project Lead
OWNER REQUEST: Zed, 2026-10-17 — "Make notes along the way for the training materials because how we work now shows what's needed for the roundtable table"
STATUS: Observations and requirements; not implementation or verified Roundtable functionality.

## Current real workflow (observed/owner-established)
- GPT builder uses existing GitHub channel; Claude reviewer uses existing Google Drive channel.
- GPT Project Lead can retrieve from both and compare/filter reports.
- Zed supplies owner directives and, until direct phone tools are operational, executes small explicit Termux commands.
- Existing read-only A25 terminal viewer lets GPT lead inspect shared terminal output. It does not itself execute commands.
- Distinct fresh builder/reviewer seats are assigned orders, with reports addressed to lead rather than raw troubleshooting directed at Zed.
- Existing Pocket Server hardened main is deny-all baseline; separate terminal viewpoint stays independent.
- Current milestone: main shared viewing -> test both AI reads -> stop -> restart -> retest both -> stop. Shared writes and owner-directed terminal execution are next-stage work.
- Goal is one phone/Pocket Server source of truth with GPT and Claude operating in the same designated files and tests, not permanent GitHub/Drive split.

## Training implications for Roundtable
1. Messages need explicit sender seat, recipient, owner directive reference, order ID, source locator/revision, and status; narrative identity alone is not authentication.
2. Lead-directed issue routing: builder and reviewer report failures to lead; lead filters and resolves routine issues; only decisions requiring owner input reach Zed.
3. Shared terminal evidence should be referenced as a command/observation pair with operator, viewer, output, timestamps when available, and what was NOT verified.
4. Separate intent, authorization, action, observation, and claim. A proposed command or test is not a completed execution.
5. Independent GPT and Claude reads of the same source should be compared using source locator/revision, not assumed equivalent from paraphrased reports.
6. The conversation itself is training evidence: record why owner rejected recurring security/identity planning and new folders, and preserve deferred-task commands ("do this; add that later") as binding sequence constraints.
7. Transport changes must not change the meaning of an order: GitHub/Drive courier now, Pocket Server shared Roundtable later.
8. Error reporting should fail loudly without asking owner to become the default debugger.
9. Human operator actions remain distinguished from AI tool actions; no AI may claim to have typed commands Zed executed.
10. Preserve successful and failed restart tests, including service shutdown, fresh connection and independent cross-seat verification.
11. Avoid proliferating project trees, branches, duplicate copies or alternate ledgers just to support reporting.

## Example Roundtable event types (design candidates, not implemented)
OWNER_DIRECTIVE; LEAD_ORDER; SEAT_ACK; SOURCE_READ; CHANGE_PROPOSAL; OWNER_COMMAND; COMMAND_EXECUTION; TEST_OBSERVATION; BLOCKER; REVIEW; LEAD_DECISION; CHECKPOINT; SERVER_STOP; SERVER_START.
Each event should identify evidence and actor, distinguish observed from claimed outcomes, and point back to existing artifacts.

## Current limitations
- Direct GPT/Claude shared phone read/write/terminal access has not yet been demonstrated.
- Shared terminal viewer is read-only for GPT.
- Claude's ability to read the same terminal directly is not established here.
- No new Roundtable schema, software, folders or security work are authorized by this note.

## Training practice
Append additional notes as actual interactions expose requirements or failures. Never silently edit prior observations; use numbered follow-on notes in this existing leadership folder. Do not allow documentation to delay the shared-view milestone.
