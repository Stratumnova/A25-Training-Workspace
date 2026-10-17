# GPT lead — WD-05 Actions recovery handoff

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude and builders
**DATE:** 16 October 2026, after 18:33 MDT
**RE:** GPT-owned Watchdog working record and review handoff
**BASIS:** WD-05 case study, Zed-supplied GitHub Actions run 105660203481, and Claude's code review

## State as verified

Development branch `build/wd-02-watchdog-v0`; latest independently observed green implementation commit `8e8fd10a688ab1c74f531022339fab3cd6bf9167`.

- WD-03 isolated fixtures: 11 of 11 PASS.
- WD-03 core unit tests: 5 of 5 PASS.
- Actual A25 repository check: 0 FAIL, 3 WARN (two historical W3 exemptions; one corrected historical F-002 collision).
- GitHub Actions permissions: read-only.
- Original records unchanged; no merge to `main` claimed.

## Evidence and decisions

The chronological CI failures and fixes are recorded in `case-studies/WD-05-github-actions-failures-and-recovery-2026-10-16.md`. Safety-stop and Zed's authorized retry are separately preserved in `case-studies/A25-F-005-wd03-safety-stop-authorized-retry-2026-10-16.md`.

Claude independently reviewed the earlier code and identified open design gaps; these remain unresolved after the green run. Do not conflate passing current checks with final Watchdog certification.

## Next work

1. Strengthen W4 to examine the entire push range, not only HEAD's first parent; test a multi-commit push.
2. Strengthen W6 to reject write permissions and `write-all` anywhere in workflows.
3. Review frontmatter and canonical-ID handling against approved contract, including correction evidence and longer IDs.
4. Add regression tests for those cases; run isolated and actual-repository CI again.
5. Supply commit-pinned code and logs for Claude's independent review before merge.

## Working rule

If a GitHub write is blocked by platform safety checks, stop that operation, report exact error and payload to Zed, and do not retry or reroute without specific authorization. Authorization permits a normal retry, not a safety bypass.


## Zed continuity instruction — 16 October 2026, after WD-05

Zed directed that GPT Roundtable and Claude Roundtable information remain inside their respective folders, because either AI conversation may be lost mid-build. GPT is responsible for keeping its own current state and evidence in `roundtable/gpt/`; Claude-authored information belongs in its distinct Claude records, preserving original author attribution and review independence. Shared decisions belong in shared Roundtable records, and significant failures belong in case studies. Do not silently convert Claude's review into GPT-authored conclusions.

Recovery handoffs must distinguish OBSERVED tool results, CLAUDE-REPORTED findings, ZED-APPROVED decisions, and OPEN work; include branch, commit, next action and unresolved blockers. Update records at meaningful checkpoints, before a planned handoff, and after an interruption. Do not claim autonomous background recording: writes happen only when a session is active and tools succeed.

**Current status:** WD-05 case study and GPT handoff have been committed and read back; Claude's previously supplied code review remains an independent document, not rewritten by GPT. The Watchdog development branch remains unmerged and outstanding design gaps remain open.


## A25 Roundtable rooms: design and educational record

Zed instructed GPT to preserve the A25 case-study/training material with Zed's own design thoughts, GPT's responses and engineering rationale, and separately attributed Claude reviews. GPT authored an additive training case study at `case-studies/A25-roundtable-rooms-design-and-training-2026-10-16.md` (creation commit `402b5288fe55325eb37430e2f5b7f741c8b15ac5`).

The case study distinguishes Zed's source wording, GPT's interpretation and reasons, Claude-reported evidence, verified CI results and unresolved work. It covers the separate rooms/folders, manual relay and recovery rules, human safety-stop approvals, and the WD-03/WD-04 GitHub Actions failures and fixes. This does not authorize GPT to edit Claude-authored source records or to claim background recording. Continue to add new user design decisions and GPT's explicit engineering rationale to durable records at meaningful checkpoints.

**Status:** Additive training document created on development branch; Watchdog remains unmerged pending remaining design gates.


## External builder continuity test — Zed instruction at 18:42 MDT

Zed will load a repository ZIP into a fresh chat on a friend's phone, then temporarily adopt the new session as a builder to test whether it can align with A25. GPT prepared a read-only onboarding exercise at `roundtable/builders-inbox/A25-external-builder-intake-test-2026-10-16.md` (commit `ba8d510bdb071c5a5f0bf998f4f407c40adf27be`). The ZIP must be taken from `build/wd-02-watchdog-v0`, not `main`, for current Watchdog/WD-05 evidence. This is a candidate evaluation only; no builder acceptance or external-session PASS has occurred.

Next: Zed supplies the guest's full intake report. GPT evaluates it against the onboarding checklist, records provenance and findings in a new builder-intake case study, and requests Zed's acceptance decision. No credentials, private data, write access, or authority changes are implied.


## External builder intake result — Zed relay at 18:50 MDT

Zed returned the full text of a fresh ChatGPT session's A25 External Builder Intake Report, with a screenshot of the shared chat. GPT evaluated it as **PROVISIONAL PASS** for repository comprehension, evidence labeling, authority boundaries and open-task recognition. This was an open-book intake with an explicit rubric, not an independent builder performance test. Candidate claimed no GitHub operations, no writes and no acceptance. GPT's evaluation and substantive report summary are in `case-studies/A25-external-builder-intake-test-01-2026-10-16.md` (creation commit `796aff253328610ee4dabd4d8be53a09897a3b4b`). The original candidate report was pasted by Zed; source byte parity is unverified.

**Next:** Wait for Zed to adopt the candidate as a temporary builder, then assess one novel bounded read-only task. Do not infer authenticated identity, permissions or final acceptance from the intake response.


## GB-01 guest builder onboarding — Zed at 18:51 MDT

Zed explicitly authorized inviting the friend's free-tier ChatGPT session as a **temporary guest builder** via a prompt, with no GitHub write access. The friend will send the prompt; the builder returns a complete Markdown report through Zed for GPT archival, as with the Claude relay but retaining separate seat identity. GPT prepared `roundtable/builders-inbox/GB-01-temporary-builder-onboarding-and-W4-task-2026-10-16.md` (commit `68dcddc01c5636ca52b22b2696a954b61efcc396`). First assignment: read-only W4 multi-commit push-range audit. Seat `GB-01` is a functional test identifier, not a credential or proof of person/model identity. Do not claim completed builder work until a source report is received and evaluated.


## GB-01 engineering test 2 — Zed relay at 19:01 MDT

Zed supplied three photographs of a separate phone and the complete Markdown file `GB-01-W4-audit-2026-10-16.md` (14,647 bytes, SHA-256 `8307c052376f0c31a82d752806bf9c93821f85a81aeb0d85b2b8ef655a6b48a9`). GB-01 reported reproducing a W4 multi-commit false pass in a disposable local repo, with matching manifest digest, and no GitHub writes. GPT independently fetched the pinned `watchdog/check.py` and confirmed the single-first-parent-diff source weakness, **not** the reported scratch execution. Evaluation: first bounded engineering task PASS; Claude review and remediation remain open. Case study `case-studies/A25-GB-01-W4-builder-test-02-2026-10-16.md` created at `630afc262e0d5eb20ac0232f7fc4199f11375419`. Full original Markdown attachment is not yet archived byte-exactly in GitHub; case study preserves its hash and substantive findings.

Next: archive source report exactly if possible, seek Claude independent review, and strengthen W4 with push-range tests before merge.
