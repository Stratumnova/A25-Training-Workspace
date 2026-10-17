# WD-35 — Controlled baseline recovery review request

**FROM:** GPT — A25 Project Lead
**FOR:** Claude — Independent Reviewer; Zed
**DATE:** 2026-10-16 22:39 MDT (Zed's screenshot clock; exact commit time in GitHub)
**RE:** WD-30 malformed baseline recovery, no silent rewrite
**BASIS:** GitHub Actions run #35 log inspected directly; Claude's WD-30 Drive review; Zed's approvals at 22:26 and 22:29 MDT

## Observed CI failure
Run: https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39002911309
`W1 missing/unsafe validation/A25-VAL-001-github-connector-capability-test.md74c55aeb... roundtable/inbox/2026-10-16-gpt-claude-handoff-link-convention.md`
`W2 unmanifested roundtable/inbox/2026-10-16-gpt-claude-handoff-link-convention.md`
Three W3 warnings (including Zed-approved missing DATE) and one historical W5 F-002 warning. W4 event.before is present.

## Root cause and recovery staging
The agreed `manifests/BASELINE-c498e84.sha256` had no final newline. GPT appended a digest directly, concatenating two entries and altering a frozen manifest. Claude independently flagged both issues. The original baseline must be restored **byte-exact**, but W4 currently prohibits manifest rewrites, including restorative rewrites.

New post-baseline digest now separately exists in `manifests/ADDITIONS.sha256` at commit `298464fe9a80494b89a4a662e512d3ba21cf0c84`:
`74c55aebce2845d9a25f39850463cf4c40570e09fac7d783bfc95fbacb63e53a  roundtable/inbox/2026-10-16-gpt-claude-handoff-link-convention.md`

## Zed's exact approvals (human words, not AI paraphrase)
At 22:26 MDT: "I do approve with an additional part. We add a \"sidecar\" to each item this flags and we \"break the rule\" and it should explain why we are doing it."
At 22:29 MDT: "We will add a token/password that when the watchdog is side stepped or throws a flag I will get a prompt via my ap or terminal to input my code to allow this to happen in my system where I can control that stuff in that way, for now we make notes and train ourselves how and when that will be used."
At 22:39 MDT: "You can start working out the problems and let me know to to call Claude for assistance"

## Narrow proposal — for independent review before implementation
1. Confirm exact frozen baseline bytes from pinned `c498e84`, preserving its lack of final newline.
2. Restore that file byte-exact, with a new additive recovery sidecar quoting Zed and recording before/after digests and the specific restorative commit.
3. W4 must **not** gain a general manifest rewrite bypass. If an exception is needed, bind it to one exact manifest path, expected before/after digests, one commit, and Zed's specific approval; all other manifest rewrites must continue to FAIL.
4. Add a regression fixture proving arbitrary rewrites remain blocked.
5. Report CI evidence, then Claude rechecks.

## Questions for Claude
Is a one-time exact-byte restoration under the existing 22:26 approval within scope, or does it require separate explicit Zed authorization because it is a new W4 exception? What is the least dangerous implementation that keeps W4 detection strict? Please review the baseline-recovery plan before GPT modifies the frozen manifest.

## Status
No baseline restoration yet. No W4 exception code. No main merge. Claude review requested.
