# Claude Blackout Log 001 — WD-35 repair and training cleanup

**FROM:** GPT — A25 Project Lead
**FOR:** Zed; Claude — Independent Reviewer
**DATE:** 2026-10-16 after 23:17 MDT (commit timestamps in GitHub are definitive)
**RE:** Work completed without Claude and required re-review
**BASIS:** GitHub commits, Actions run #47 job log, Zed's prior WD-35 approval and current cleanup request

## Blackout starting point
Checkpoint `training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md`, commit `a5357caf44359924fddca6a8c90a4cdaf3d2c1c2`. Claude unavailable due to observed platform limit; no Claude review of the following implementation.

## Changes in chronological order
| Commit | File(s) | Why |
|---|---|---|
| `bb46fa7d68c13e83aebe8738d032bcf34a6b06ab` | `watchdog/check.py` | Require exact source/target Git blobs and exact marker/sidecar for WD-35 |
| `9bbe0d05ad4fd94ee1ea6589570e182703d0799e` | `manifests/W4_RESTORATIONS.txt` | Record authorized one-file restoration pair |
| `2cb7d65a5f3b0ce1d4ba1891fb023bb173681fdb` | `exceptions/WD-35-baseline-restoration.sidecar.md` | Explain violation, approval and repair |
| `891d0cfef58edb11176e9ce8585580781861501a` | `manifests/BASELINE-c498e84.sha256` | Restore exact frozen bytes (Git blob `e317b1c42668126141baecd797cad84b4a1d57fe`) |
| `fd0e4c827795e12f62da029af0f490c1145cf613` | `watchdog/test_wd35_guard.py` | Add two static guard/marker checks |

Source broken blob: `bf3f3d85413deb94c1b36eee3ea4aabd414cddee`; restored target: `e317b1c42668126141baecd797cad84b4a1d57fe`. These are Git blob hashes (SHA-1), not SHA-256. Original preserved in Git history; post-baseline protected note hash remains in `manifests/ADDITIONS.sha256`.

## CI evidence
- Runs #43–#45 FAIL as expected intermediate pushes before the restoration. Their exact job logs were not separately audited.
- Run #46: SUCCESS after byte-exact baseline restoration, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005892301
- Run #47: SUCCESS after tests, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005925303
- Run #47 job log directly inspected: **23 tests passed**, repository Watchdog **0 FAIL, 4 WARN**.
- W3 WARNs: inbox handoff note missing DATE (Zed-approved); historical inbox README missing five headers; historical RT-001 missing BASIS/RE.
- W5 WARN: known corrected historical `A25-F-002` collision.
- Push base was present in run #47: `A25_WD_BEFORE=891d0cfef58edb11176e9ce8585580781861501a`.
- The two new tests check guard text and marker exactness. They are **not** a full behavioral proof that every malicious rewrite fails; Claude should assess whether stronger isolated repository fixtures are required.

## Authorization and review boundary
Zed explicitly authorized this current manifest restoration at 22:43 MDT. Claude independently agreed to the exact-byte restoration design in WD-35 before blackout. The actual code, marker, sidecar, restore commit and tests are **GPT-only, pending Claude's independent review**. Do not claim the double-yes gate was exercised on these implementation bytes.

## Review tasks for Claude on return
1. Independently verify exact original baseline bytes and the WD-35 marker.
2. Check that W4 cannot be bypassed by a different path, altered blobs, or reused marker; recommend stronger behavioral regression fixtures.
3. Review all blackout commits and this log; reconcile Actions evidence.
4. Check whether all four remaining WARNs are acceptable, and whether W3 exemptions need further policy review.
5. Resume the interrupted full-repository ZIP audit; do not treat this green draft workflow as release or merge approval.

## Current status
Training/handoff files are no longer causing W1/W2 FAIL in the latest checked run. **23 tests PASS; 0 FAIL / 4 WARN** on the draft workflow. No merge to main. Claude audit and final independent review still open.
