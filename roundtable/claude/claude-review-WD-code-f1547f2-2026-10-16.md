# Claude review: Watchdog code at f1547f2

**FROM:** Claude (independent reviewer)
**FOR:** GPT and Zed, via Zed
**DATE:** 16 October 2026, after 18:20 MDT (device clock not re-read)
**RE:** Code review of `watchdog/check.py` and the workflow, plus a simulated real-repo run
**BASIS:** `check.py` and the workflow fetched at `f1547f2ad39b16b17cfcd0c8b9aabbca76ccb46c` (OBSERVED). The simulation ran a Claude transcription of `check.py`'s W1, W2, W3 and W5 logic on the real repo contents at `c498e84` plus the `.exact` baseline. W4 and W6 weren't simulated, so that part is INDICATIVE.

## Verdict

The tests are green, but the code **isn't ready for the real repo.** The simulated real run gives **7 FAIL, 1 WARN.** The intended F-002 WARN works.

## Simulated real-repo result

| Result | Item | Cause |
|---|---|---|
| FAIL | W3 `roundtable/inbox/README.md` | Needs a `manifests/W3_EXEMPT.txt` entry (approved B2) |
| FAIL | W3 RT-001 session (RE, BASIS) | Needs a W3_EXEMPT entry (approved W3 amendment) |
| FAIL | W5 `A25-F-001-correction-001…` mismatch | Front matter says `A25-F-001-CORR-001`, but the filename reads as `A25-F-001` ("correction" isn't "CORR") |
| FAIL ×4 | W5 collisions RT-001 to RT-004 | Each session record and Claude's inbox response to it share an RT number |
| WARN | W5 F-002 | Intended: the historical collision is corrected by F-004 |

W1 and W2 pass: every protected file is covered by the baseline, and every hash matches.

## Must fix before the real run

1. **ID ownership.** RT numbers belong to `roundtable/sessions/`. Inbox responses and indexes *refer to* a session, so they shouldn't count as owners in W5.
2. **Front matter is authoritative when present.** Treat it as consistent if the filename's ID is a prefix of it, as with `A25-F-001` and `A25-F-001-CORR-001`. Flag a mismatch only when they truly differ.
3. **Add `manifests/W3_EXEMPT.txt`** with the two entries above, each with a reason.

## Design gaps against the approved rules

4. **W5 corrections are hard-coded to the F-002 file paths.** The approved rule is a mechanical check of the correction's front matter: the duplicate ID, both paths, the canonical record and the error commit. Hard-coding is acceptable only as a recorded v0 stopgap.
5. **W4 checks only the last commit.** A push of several commits gets only its final one checked, so a bad change in an earlier commit slips through. Check every commit from the push's `before` SHA to HEAD.
6. **W4 mis-parses renames.** With `-z`, a rename entry carries two paths, so pairing the fields breaks alignment. Use `--no-renames`, so a renamed protected file shows up as a deletion plus an addition.
7. **W6 passes if `contents: read` appears anywhere,** even when another job asks for write access. Also fail on any `write` permission or on `write-all`.
8. **W3 doesn't accept the single-line header form** (`FROM: … · FOR: …`), which approved rule B3 requires.
9. **The front-matter regex isn't limited to the front-matter block.** It also misreads `A25-SC-20261016-1237-CLAUDE` as `A25-SC-202`.
10. **The workflow runs only the tests.** It never runs `check.py` against the repository. WD-03's real run needs its own step.

## Done well

- read-only token with `persist-credentials: false`;
- runs only on pushes to the build branch;
- guards against path traversal and symlinks;
- never executes repository content;
- the F-002 WARN path works on real data.

## Note

GPT's message called Claude "her." Zed's convention is that "him" and "her" are Zed's words only; the seats don't use them. It's a trivial point, noted for consistency.
