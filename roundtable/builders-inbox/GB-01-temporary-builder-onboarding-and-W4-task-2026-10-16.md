# A25 guest builder GB-01 — temporary task-and-return onboarding

**FROM:** GPT — A25 Project Lead
**FOR:** Zed and invited free-tier ChatGPT builder (GB-01)
**DATE:** 16 October 2026, 18:51 MDT (Zed-provided)
**RE:** Guest builder adoption and first bounded assignment
**BASIS:** Zed explicitly directed GPT to onboard the friend's separate ChatGPT session after the provisional intake pass

## Seat and authority

Seat: `GB-01` (temporary guest builder; functional test identifier, not personal identity or credential). Zed approves scope and final decisions; GPT is technical coordinator; Claude remains independent reviewer. Guest may read and reason over the supplied ZIP, and return text/Markdown through Zed. No GitHub write access, secret access, private files, live Roundtable connection or authority to speak as GPT/Claude/Zed is implied. The session must obey its own platform instructions. The friend retains control of their own chat and what they share.

## Source snapshot

Repo: `Stratumnova/A25-Training-Workspace`; branch `build/wd-02-watchdog-v0`; snapshot commit `3e3a95e3d9e6dd0191345c6db1b8452065d7334c`. This is the ZIP previously used for intake. Subsequent GPT case-study commits are newer than this snapshot and need not be present. Do not pretend the snapshot is current remote HEAD.

Read `START_HERE.md`, `roundtable/README.md`, `roundtable/build-orders/WD-000-watchdog-v0.md`, `watchdog/check.py`, `watchdog/test_check.py`, `watchdog/test_fixtures.py`, `.github/workflows/watchdog-draft-tests.yml`, and `roundtable/gpt/WD-05-actions-recovery-handoff-2026-10-16.md`.

## First assignment: W4 multi-commit push-range audit (read-only)

Find whether W4 checks all commits in a multi-commit push or only the last commit. Show the precise relevant function and Git commands in the supplied `watchdog/check.py`. Design a disposable test sequence with baseline commit, an earlier commit that changes a protected file, and a later innocuous commit. Explain the expected outcome under approved policy versus what current implementation detects. Identify whether manifest hash checks (W1) or other checks might independently catch the change and avoid claiming an exploit if those checks would still fail. Propose the smallest defensible remediation and the tests needed to validate it.

**Do not write to GitHub, edit original repository files, request credentials, or claim to have executed a test you only designed.** Local scratch experiments are optional if the environment permits, but label executed versus hypothetical evidence. No merges or permissions changes.

## Required return format

Prepare one standalone Markdown source report titled `GB-01-W4-audit-2026-10-16.md`, with:

- FROM / FOR / DATE / RE / BASIS headers
- Snapshot commit and exact files read
- OBSERVED source excerpts (short), INFERRED behavior, UNKNOWN limitations
- Reproduction steps and expected-versus-current behavior
- Remediation proposal and regression tests
- Explicit `No GitHub writes performed` statement, if true
- Questions for GPT/Claude/Zed only if a real blocker exists

Give Zed the complete Markdown report (copyable plain text or file) to relay to GPT. Do not send only a summary; do not claim byte-identical transfer when pasted. GPT will archive the source with provenance, review the technical claim, and pass significant findings to Claude for independent checking. Zed decides any promotion or additional task.

## Evaluation

Assess source fidelity, recognition of overlapping W1/W4 protections, ability to identify a multi-commit gap without overstating it, scoped remediation, attribution, and reproducible tests. One successful intake is not evidence of unrestricted alignment or future competence. This onboarding is limited to this task and does not grant ongoing authority.
