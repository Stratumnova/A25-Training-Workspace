# WD-05 — GitHub Actions failures and verified recovery

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, builders
**DATE:** 16 October 2026, after 18:33 MDT (Zed clock)
**RE:** WD-03/WD-04 GitHub Actions failure-and-recovery case study
**BASIS:** Five earlier CI log archives and the new Zed-supplied `logs_105660203481.zip`; GitHub commits; Claude's independent reviews as relayed by Zed

## Observed chronology

| Repository commit | CI result | Finding |
|---|---|---|
| `44190693a540ba7df62da6eee9651e31ada1ce67` | FAIL, 0 tests | SyntaxError in `watchdog/check.py` frontmatter regex; both test modules failed import |
| `f1547f2ad39b16b17cfcd0c8b9aabbca76ccb46c` | PASS, 16/16 | Regex syntax corrected; isolated tests green, but no actual-repo step |
| `2c3172ef01dce268a279c8bee99ba54b323f93ae` | FAIL, 15/16 | Changed frontmatter parsing; existing `test_frontmatter_disagreement` fixture used undelimited `id:` |
| `f108284d6f91a44eca71ce9d5af556a952882929` | FAIL, 15/16 | Same unit-test regression; historical W3 exceptions had been added |
| `01c6a20e300e6530e20c3dc427e6992cbe8f0518` | FAIL, 15/16 | Same regression; actual-repo step added but not reached because tests failed |
| `8e8fd10a688ab1c74f531022339fab3cd6bf9167` | PASS, 16/16 and real-repo 0 FAIL / 3 WARN | Test inputs corrected to delimited YAML frontmatter; actual-repo validator ran successfully |

## What changed and why

- First failure: a misescaped regex made the module unimportable. Commit `f1547f2` corrected that line.
- Claude's code review then identified 7 FAIL / 1 WARN in a **simulation** of real-repository W1/W2/W3/W5. The live run had not yet occurred.
- Commit `2c3172e` adjusted inbox reply/session ID ownership, more-specific frontmatter IDs, single-line headers and `--no-renames`; commit `f108284` added two approved historical header exemptions; commit `01c6a20` added the actual-repository validator CI step.
- The new frontmatter-block requirement invalidated an old unit-test input that supplied `id:` without `---` boundaries. Commit `8e8fd10` updated three relevant fixture strings to use delimited YAML. The code was not loosened to make the test pass.

## Verified new run

Uploaded archive `logs_105660203481.zip`, run ID `105660203481`. Checkout confirms commit `8e8fd10a688ab1c74f531022339fab3cd6bf9167`. Python 3.11.17; all **16 tests PASS** in **0.329 s**. The additional `python watchdog/check.py` step ran on the actual repository and reported:

```text
WARN: W3 roundtable/inbox/README.md: BASIS,DATE,FOR,FROM,RE
WARN: W3 roundtable/sessions/2026-10-16/RT-001-gpt-status-and-zed-workflow.md: BASIS,RE
WARN: W5 historical corrected collision A25-F-002: case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md; legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md
WD-02 draft: 0 FAIL, 3 WARN
```

Token permissions: `Contents: read`, `Metadata: read`. Checkout used full history. The Node.js 20 deprecation warning was informational and did not fail this run.

## Lessons and remaining gates

- Differentiate import errors, failed assertions, and live-repository policy failures; do not report all as failed validation.
- Preserve historical records; apply approved narrow exceptions and document them.
- A green fixture suite alone does not certify live-repository behavior. The new actual-repo step supplies that evidence for this commit.
- **Not certified for merge:** Claude's remaining design gaps include multi-commit push coverage, stronger W6 permission checking, robust canonical IDs and correction evidence, and additional tests. These are open; the 16/16 PASS and 0 FAIL / 3 WARN do not prove them fixed.
- This report is additive; do not alter original CI logs, case studies, or protected records.
