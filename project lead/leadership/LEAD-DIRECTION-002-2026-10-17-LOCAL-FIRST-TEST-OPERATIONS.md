# A25 Leadership Direction 002 — Local-first, Evidence-first Test Operations
DATE: 2026-10-17 16:47 MDT (Zed-provided)
FROM: GPT — A25 Project Lead
FOR: Zed
STATUS: DIRECTION ISSUED; NEW OPERATIONS REQUIRE SEPARATE AUTHORIZATION

## Owner acknowledgement
Zed confirmed leadership folder was viewed and requested direction. Zed favors continued GitHub and Google Drive communication between AI seats, Pocket Server as a controlled phone inspection/test surface, and local testing where GitHub Actions cannot expose runtime behavior. Zed asked whether local-first work makes sense.

## Lead decision
Adopt LOCAL-FIRST, EVIDENCE-FIRST with distinct roles:
- GitHub: source revisions, orders, immutable reports, reviews, test records, checkpoints, later independent CI.
- Drive: independent AI originals and supporting raw artifacts with source hashes and readback verification state.
- Pocket Server: owner-controlled, permissioned phone visibility and test surface; not a substitute for auth/security approval.
- Termux sandbox: reproduce device-specific runtime behavior and capture bounded logs under Zed authorization.
- GitHub Actions: independent regression gate after local evidence is understood, not the only test venue.

## Process
1. Identify target and acceptance criteria; pin source revisions and scope.
2. Run read-only source and recovery tests first; no phone actions needed for RN-001 initial pilot.
3. For future local code experiments: Zed approves commands, isolation and limits first; capture stdout/stderr, environment, command, exit code, time, source revision, expected vs actual result, and artifacts. Redact secrets.
4. Independent AI review of raw evidence; preserve disagreement.
5. Only then use CI to validate reproducibility where applicable; green CI is not proof of Android runtime.
6. Lead records PASS/FAIL/BLOCKED/UNKNOWN; Zed approves promoted checkpoints.
7. Never conflate demonstration in a read-only viewport with command authorization or production security.

## Immediate orders
O1: Fresh GPT chat executes read-only RN-001 recovery test from leadership manifest and test specification, freezes output, writes new report to coordination branch. No existing source edits, no phone or server actions.
O2: Separate fresh Claude chat executes same test independently, writes new Drive original, without seeing GPT answer.
O3: Lead scores each independently against 10-item rubric and reconciles; Watchdog/Archivist are NOT assumed implemented.
O4: After results, decide next smallest local prototype for archive index and validators; Zed approves any phone execution or source changes.

## Explicitly deferred
No local test execution yet; no GitHub Actions trigger or disabling CI; no server starts, security bypasses, changes to protected branches, credential handling or autonomous code execution.
