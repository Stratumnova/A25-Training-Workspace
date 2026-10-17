# 03 — Watchdog and Actions History

FROM: GPT — A25 Project Lead
FOR: Zed, Claude, builders and successor lead
DATE: 2026-10-16 (initial master archive)
RE: Red/green history, causes, corrections, exceptions and reviewer status
BASIS: GitHub Actions API queried for #20–#54; prior training report; directly inspected run #47 job log

## Verified run outcomes from GitHub API
The result column below is an API-observed workflow conclusion, **not** proof of a specific root cause. Explanations for #20–#37 are preserved in `training/ACTIONS-REPORTS-AND-LESSONS-2026-10-16.md`; some are based on sequential commits rather than re-reading every job log.

| Runs | Conclusions | Evidence / explanation |
|---|---|---|
| 20 | PASS | W6 checks, rename-safe diff |
| 21 | FAIL | W4 NUL-splitting defect |
| 22–23 | PASS, PASS | NUL fix, transient-edit fixtures |
| 24 | FAIL | Escaped newline fixture |
| 25 | PASS | Fixture fix |
| 26–27 | FAIL, FAIL | W5 regex regression; unmanifested protected report |
| 28–29 | PASS, PASS | W5 correction; full push-base wiring |
| 30 | FAIL | Live W2/W3 catch on outgoing handoff incorrectly placed in protected inbox |
| 31–37 | FAIL each | Malformed frozen baseline append; run #37 directly documented as 21 tests OK, W1 1 FAIL and 4 WARN |
| 38–42 | FAIL each | Documentation and incident notes; baseline still malformed; individual causes not rechecked |
| 43–45 | FAIL each | WD-35 partial implementation before exact-byte restore; individual job logs not rechecked |
| 46–47 | PASS, PASS | WD-35 restoration and static guard checks; #47 job log directly inspected |
| 48–54 | PASS each | GitHub API workflow conclusions; individual job logs not yet audited in this master archive |

### Individual run evidence — GitHub API
| Run | Commit prefix | Result | Run ID |
|---|---|---|---|
|20|2e16ebd5|PASS|38999267471|
|21|5a3e366a|FAIL|38999408110|
|22|109de319|PASS|38999416376|
|23|13407ac6|PASS|39000011708|
|24|611502f4|FAIL|39000095667|
|25|9ea3d83c|PASS|39000128176|
|26|da06a0a1|FAIL|39000219595|
|27|f540ea08|FAIL|39000339540|
|28|7442d735|PASS|39001681428|
|29|9d356f62|PASS|39001842965|
|30|20ec265a|FAIL|39001992709|
|31|a3ee1f67|FAIL|39002710816|
|32|efa2afb3|FAIL|39002713246|
|33|22554cd2|FAIL|39002726895|
|34|5a27fffc|FAIL|39002729292|
|35|363d023e|FAIL|39002911309|
|36|298464fe|FAIL|39003439014|
|37|96e03607|FAIL|39003453631|
|38|61b3f893|FAIL|39004625630|
|39|10c02cf2|FAIL|39004646275|
|40|a07c53f8|FAIL|39005375228|
|41|ce8ff224|FAIL|39005541912|
|42|a5357caf|FAIL|39005703270|
|43|bb46fa7d|FAIL|39005838831|
|44|9bbe0d05|FAIL|39005864042|
|45|2cb7d65a|FAIL|39005880114|
|46|891d0cfe|PASS|39005892301|
|47|fd0e4c82|PASS|39005925303|
|48|668373e7|PASS|39005960888|
|49|2a9b8d1d|PASS|39006448406|
|50|0b0b714a|PASS|39006452327|
|51|f53fbdbf|PASS|39006467741|
|52|9642b501|PASS|39006470450|
|53|f3a73dfa|PASS|39006481292|
|54|a7d15af2|PASS|39006491488|

Run URL format: `https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/<run-id>`. These are branch-local run numbers and results as observed; a later workflow run must be checked afresh.

## Sidecars, exceptions and review
- WD-30: GPT placed an outgoing note in `roundtable/inbox/`, without W2 digest and W3 DATE. Zed authorized one-time W3 exemption; sidecar in `exceptions/WD-30-handoff-exception.sidecar.md`. Original preserved; corrected outgoing note placed in `roundtable/gpt/`; hash for protected note in `manifests/ADDITIONS.sha256`.
- WD-35: original baseline lacked final LF; appended digest glued to previous line. Restoration was explicitly approved by Zed at 22:43 MDT and reviewed in design by Claude before blackout. Broken Git blob `bf3f3d85413deb94c1b36eee3ea4aabd414cddee` restored to original `e317b1c42668126141baecd797cad84b4a1d57fe`. Marker `manifests/W4_RESTORATIONS.txt`, sidecar `exceptions/WD-35-baseline-restoration.sidecar.md`. Actual implementation was GPT-only pending Claude review.
- Run #47 directly checked: 23 tests OK; W1–W6 validator 0 FAIL, 4 WARN. W3 WARNs: protected note missing DATE; inbox README missing headers; RT-001 missing BASIS/RE. W5 WARN: known corrected A25-F-002 historical collision.
- **Independent review boundary:** Claude's full ZIP audit and blackout implementation audit remain unverified; no claim of Claude approval for implemented WD-35 bytes or any subsequent GPT-only change. Green draft CI does not authorize main merge.

## Interpretation rule
Always report unit tests and actual-repository validation separately. Preserve historical red runs; do not erase them because a later run is green. For each future push log full commit, run ID, tests, exact FAIL/WARN, reviewer status, exception sidecar and next gate.
