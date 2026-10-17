# A25 — Claude Blackout Checkpoint 001

**FROM:** GPT — A25 Project Lead
**FOR:** Claude — Independent Reviewer; Zed
**DATE:** 2026-10-16 23:16 MDT (Zed's instruction; GitHub commit time is authoritative for publication)
**RE:** Claude seat temporarily unavailable; continuity checkpoint and GPT-only change log
**BASIS:** Zed's screenshots at ~23:09 and ~23:12, Zed's 23:13 incident report and 23:16 instruction, GitHub branch and Actions API, existing A25 training/CS-004 records.

## 1. What happened
- At ~23:09 device time, Claude's `Rc Park` conversation displayed `Making room for more conversation...` while Zed was providing an A25 workspace ZIP and screenshots for file-by-file repository audit.
- At ~23:12 the UI displayed `Limit reached` with `Resets Saturday at 12:10 AM`. Claude's visible response area said `Reviewing the uploaded workspace and its branch history.`
- Zed reports that the review handoff was interrupted. **No evidence establishes permanent memory loss, deleted chat, failed upload, or a completed audit.** Treat the review as interrupted/UNKNOWN until Claude verifies receipt and completion.
- Zed authorized continuing work without Claude at 23:16 MDT, with durable notes of every action during the blackout for later independent review.

## 2. Baseline at blackout start
- Repository: `Stratumnova/A25-Training-Workspace`
- Development branch: `build/wd-02-watchdog-v0`; do not merge to `main` without Zed's decision.
- Verified pre-checkpoint HEAD: `ce8ff22417ffe8181f0e68af79be548ad8988922` (CS-004 incident note).
- Latest run at checkpoint creation: **#41 FAIL**, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005541912 ; runs #38–#40 also FAIL (GitHub API). Do not claim #41's exact cause without inspecting its logs. The previously confirmed persistent problem at #37 was the malformed baseline manifest, 1 W1 FAIL and 4 WARN, 21 tests passing.
- `manifests/BASELINE-c498e84.sha256` remains malformed after an incorrect append to a no-final-newline frozen baseline. `manifests/ADDITIONS.sha256` separately covers the new GPT inbox note.
- WD-35 controlled baseline restoration: **explicitly approved by Zed at 22:43 MDT, not yet implemented**. Claude previously independently reviewed the narrow digest-bound proposal. New W4 exceptions require sidecar and approval per Zed's 22:52 pass-through rule.
- Claude's file-by-file ZIP audit: **not verified complete**.
- Training on GitHub: `training/BUILDER-WORKFLOW-RULES-2026-10-16.md`, `training/ACTIONS-REPORTS-AND-LESSONS-2026-10-16.md`, `training/CS-004-CONTEXT-COMPACTION-AND-SESSION-CONTINUITY.md`, `training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md`.
- Drive training (Claude-authored): `training/DRIVE-WORKFLOW-RULES-2026-10-16.md`, `training/CLAUDE-REVIEW-LOG-AND-LESSONS-2026-10-16.md`; GPT read these before interruption. Claude agreed to GPT's workflow training; review of GPT's Actions training was still open.

## 3. Human instructions governing blackout work
- Zed 22:43: "You are the lead and have my approval for your updates on GitHub so long as you follow the sidecar rule and let me know when and why here so Claude and I can confirm it's correct before pushing to avoid a bad push. My approval for this current manifest is a go and further issues like this will follow a gpt builds the report and if Claude agrees and I can read it then we agree we will trust of roundtable and later code that trust."
- Zed 22:52: "If I paste a response where you and gpt agree to bypass my watchdog that means I'm letting it pass as agreed by me which is why you both have to tell me when you agree or disagree to do it. If I jump in that's me stopping the double yes trap and if I don't step in I'm letting the work flow move as it needs to and not held up Everytime a mistake is corrected as we will have many."
- Zed 23:16: "Make a checkpoint for Claude to grab from GitHub that lays out what happened and why and what are plan for it is. Also we will move forward without Claude but keeps notes along the way so he knows everything we did during its blackout."
- Interpretation: GPT can continue ordinary authorized development; **GPT-only work is not Claude-approved**. Do not invent a Claude vote. Existing specific WD-35 restoration approval remains in force; for any new exception that needs both seats' agreement, hold or ask Zed to decide explicitly rather than simulate Claude's assent.

## 4. Blackout work log protocol — mandatory
For every post-checkpoint push, append a dated entry to a **new, nonprotected GPT training/blackout log** recording:
- full commit SHA, branch, changed paths, reason and source authorization;
- whether an exception or sidecar was involved, and exactly who reviewed/approved;
- Actions run URL, final conclusion, unit tests, actual W1–W6 FAIL/WARN and root cause (mark unknown when not checked);
- any risks, unverified claims, and work Claude must inspect on return.
Never retroactively label a GPT-only commit `independently reviewed`. Preserve original source and logs. Do not hide red CI behind a later green run. If a log update itself triggers Actions, record it in the next report to avoid infinite self-reporting commits.

## 5. Recovery procedure when Claude returns
1. Claude reads this checkpoint and subsequent numbered blackout logs, not just a model-generated summary.
2. Verify actual ZIP receipt and branch/commit, audit coverage, and any files not included in the ZIP. Do not assume prior review finished.
3. Compare pre-blackout HEAD with latest HEAD and enumerate every commit/path; independently inspect exception sidecars and exact before/after hashes.
4. Recheck GitHub Actions logs, verify W1–W6 and regression fixtures, and issue AGREE/DISAGREE/NEEDS EVIDENCE for each substantive change.
5. Record `SEAT_RESUMED` and `RECOVERY_VERIFICATION` with PASS/PARTIAL/FAIL/UNKNOWN; reconcile discrepancies in durable records.
6. Resume double-yes exception workflow only after Claude's explicit independent review; no main merge without Zed's decision.

## 6. Next planned work during blackout (not yet done)
- Inspect latest failing Actions logs, confirm actual cause.
- Prepare exact-byte frozen baseline restoration with digest-bound one-time W4 authorization, sidecar quoting Zed, regression tests, and W1 LF rule for **new** manifests with historical baseline handled explicitly.
- Run and record CI after each push; distinguish expected intermediate red from regressions.
- Keep all changes on development branch. Record any deviation and its authority in blackout log.

## 7. Pointers
- CS-004 continuity protocol: `training/CS-004-CONTEXT-COMPACTION-AND-SESSION-CONTINUITY.md`
- Incident: `training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md`
- Recovery review request: `roundtable/gpt/2026-10-16-wd35-baseline-recovery-review.md`
- WD-30 sidecar: `exceptions/WD-30-handoff-exception.sidecar.md`
- Authorization design: `roundtable/gpt/2026-10-16-watchdog-human-authorization-design.md`
- GitHub Actions: https://github.com/Stratumnova/A25-Training-Workspace/actions/workflows/watchdog-draft-tests.yml

**Status:** checkpoint only. All work after HEAD `ce8ff224` is blackout-period work until Claude verifies it. No password/token authorization deployed. No main merge.
