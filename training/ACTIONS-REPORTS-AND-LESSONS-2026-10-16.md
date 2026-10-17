# A25 Builder Training — GitHub Actions Reports and Failure Lessons

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude and future builders
**DATE:** 2026-10-16 (historical snapshot)
**RE:** Observed Actions history and interpretation
**BASIS:** GitHub Actions API workflow runs on `build/wd-02-watchdog-v0`, observed after run #37; selected job logs independently retrieved. Conclusions below refer to the draft workflow only.

## Read this before interpreting a green badge
The draft workflow has isolated Python tests and a separate actual-repository Watchdog check. A test PASS does not certify that the actual repository passed. Green CI is not independent review or authority to merge. Red CI can mean the Watchdog correctly caught a violation. Always retrieve the failed job logs and identify exact W-rules and paths.

## Run ledger (verified GitHub API, #20–#37)
| Run | Commit | Result | What changed / lesson |
|---|---|---|---|
| 20 | `2e16ebd5` | PASS | W6 write permission checks, rename-safe diff |
| 21 | `5a3e366a` | FAIL | W4 multi-commit implementation had NUL splitting defect |
| 22 | `109de319` | PASS | Corrected NUL split |
| 23 | `13407ac6` | PASS | Added transient-edit W4 fixtures |
| 24 | `611502f4` | FAIL | New W5/W6 fixtures had escaped-newline error |
| 25 | `9ea3d83c` | PASS | Fixture newline correction |
| 26 | `da06a0a1` | FAIL | W5 regex rejected descriptive ID suffixes; 18/21 tests passed |
| 27 | `f540ea08` | FAIL | Failure report in protected inbox path without proper manifest/header |
| 28 | `7442d735` | PASS | Corrected W5 parsing; RT filename namespace restriction |
| 29 | `9d356f62` | PASS | W4 push base wired through `A25_WD_BEFORE` |
| 30 | `20ec265a` | FAIL | GPT handoff note in protected inbox lacked W2 coverage and W3 DATE |
| 31 | `a3ee1f67` | FAIL | Incorrect baseline manifest append |
| 32 | `efa2afb3` | FAIL | W3 exemption recorded, malformed baseline persists |
| 33 | `22554cd2` | FAIL | Sidecar added, malformed baseline persists |
| 34 | `5a27fffc` | FAIL | Corrected GPT-lane handoff, malformed baseline persists |
| 35 | `363d023e` | FAIL | Future authorization design documented, malformed baseline persists |
| 36 | `298464fe` | FAIL | Separate ADDITIONS manifest introduced, malformed baseline persists |
| 37 | `96e03607` | FAIL | Recovery proposal; 21 tests OK; 1 W1 FAIL, 4 accepted WARN |

API evidence: https://github.com/Stratumnova/A25-Training-Workspace/actions/workflows/watchdog-draft-tests.yml
Individual run URL form: `https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/<run-id>`.

## Confirmed case studies
### W5 regression (runs 26 and 28)
An overly strict negative lookahead rejected descriptive filenames, disabling ID mismatch and collision detection. Claude suggested `(?=$|-)` and independently simulated parsing. Preserve older regression tests; a new test passing cannot justify breaking old tests.

### W2/W3 first live catch (run 30)
GPT mistakenly placed an outgoing handoff note in the protected incoming inbox without manifest coverage and a DATE header. The Watchdog correctly blocked it. Zed approved a one-time W3 exception, with an explanatory sidecar. Future outgoing notes go in `roundtable/gpt/`. This is a **real caught violation**, not a harmless false positive.

### W1 baseline append error (runs 31–37)
The frozen baseline manifest had no final newline. GPT appended a new hash, joining two entries into an invalid line. This changed a frozen file and made W1 fail. A separate `manifests/ADDITIONS.sha256` now covers the new inbox note, so W2 is resolved, but the corrupted baseline still causes W1 failure. Claude's WD-35 proposal is a digest-bound one-time W4 restoration; Zed explicitly approved this restoration at 22:43 MDT. The restoration has NOT yet been implemented or verified as of this snapshot.

## Run #37 exact interpretation
GitHub run: https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39003453631
- 21 unit tests OK.
- 1 FAIL: malformed glued baseline manifest line, W1.
- 4 WARN: three known W3 exemptions (original note, README, RT-001), one known historical W5 F-002 collision.
- W2 no longer fails due to ADDITIONS manifest.
- Expected *after successful restoration*: 0 FAIL / 4 WARN, subject to actual verification and any newly introduced checks.

## Required Actions report template for every future push
- Branch / full commit SHA / run ID and URL
- Trigger and whether full push-range base was provided
- Job status and final conclusion (not merely screenshot badge)
- Unit test count, failures and fixture changes
- Real-repository W1–W6 FAIL/WARN count and exact affected paths
- Root cause and classification: new regression, correctly caught violation, or expected intermediate red
- Independent review: who verified which evidence and any disagreement
- Correction commit and follow-up run
- Release readiness: no merge unless separately authorized

## Known limits
This ledger is a snapshot of #20–#37; earlier runs and future runs are not represented. Run summaries derive from GitHub Actions API and previous inspected job logs, with some intermediate failure explanations based on sequential commits rather than individually reread logs. Claude's independent run #37 check was relayed by Zed and attributed, not claimed as GPT's independent byte verification. A green result on the draft workflow does not prove a production deployment.
