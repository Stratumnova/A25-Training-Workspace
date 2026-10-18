# A25-TW-O006 — G1 Source Test and Termux Installation Plan
FROM: A25-TW-GPT01 TO: A25-TW-BG-GPT01
DATE: 2026-10-18
STATUS: ACTIVE, FIRST IN SEQUENCE
Read owner handoff A25-TW-OWNER-DIRECTION-AND-SUCCESSOR-HANDOFF-2026-10-18.md and R004/R005 before work.

## Objective
Verify the existing Zone 1 source in Stratumnova/pockettest branch build/shared-space-v0 (last observed head 4c2f30364075fdf1dced1a297c7458891053d7f3), resolve the earlier failed local fetch/import test, and prepare exact owner-run Termux install/test steps for the existing Pocket Server. Do not start a new server or replace the viewport.

## Work
1. Inspect current branch source and tests, preserve existing Gate-01 behavior.
2. Run the Zone 1 tests using an accessible environment if possible; if unavailable, perform direct static inspection, identify exact blockers, and give reproducible commands for owner Termux. Do not label unexecuted tests PASS.
3. Verify/repair workspace tool code as needed on the existing branch; report changed paths, full commit, exact errors.
4. Prepare short, ordered commands to set A25_ZONE1_ROOT to an owner-chosen Termux-accessible folder, test, update the existing server, and validate one disposable file and one harmless command. Do not guess live phone paths or execute on the phone under this order.
5. Preserve existing A25 GPT Terminal terminal_view and terminal_status as-is. Actions are a SEPARATE entry/interface that must support view/inspection AND commands/file operations. G2 will handle the connector; avoid duplicating it.
6. Document failures, including observed tunnel/MCP errors if relevant, without diverting to speculative security redesign. No new branch/repo or live deployment.

## Deliverables
Post G2-facing readiness/interface note in builders-inbox, and formal report project lead/coordination/reports/A25-TW-R006-BG-GPT01-ZONE1-TEST-AND-TERMUX-PLAN.md with source SHA, actual tests and explicit owner phone steps. Return report path and commit SHA, stop. G2's next order is dependent on G1's report; if G1 fails or is blocked, owner should NOT activate G2 yet, but return here for repair decision.
