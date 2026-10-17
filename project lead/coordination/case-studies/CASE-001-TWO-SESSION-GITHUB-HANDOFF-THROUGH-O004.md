# CASE-001 — Two ChatGPT Sessions Coordinating Through GitHub
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / future Claude reviewer
DATE: 2026-10-17 (owner-reported times, MDT)
RE: Case-study checkpoint through O004
BASIS: GitHub coordination orders, builder reports, lead source reviews, and Zed's relayed operating instructions
STATUS: ACTIVE CASE STUDY; O004 ISSUED, NOT YET EXECUTED

## Research question
Can two ChatGPT sessions on one user account act as distinct lead and builder roles, exchanging durable instructions, artifacts and evidence through GitHub without Zed copy-pasting complete work between sessions? Can the lead simultaneously keep a truthful case-study ledger and return to active project leadership?

## Roles and operating rule
- Zed: human owner, relay, tie-breaker, present human Watchdog; approves protected merges and reserved decisions.
- GPT: A25 Project Lead, issues orders, reviews independent GitHub evidence, maintains this case study and resumes next leadership task.
- LB-GPT01: builder, reads numbered GitHub orders, performs authorized bounded work, writes numbered GitHub reports, stops for review.
- Claude: future independent reviewer; not yet part of this trial.
- Golden Rule: **Truth and tech above lore. Always fail out loud.**
- Shared ChatGPT project context does not prove autonomous session-to-session access or authenticated AI seat. GitHub is the explicit communication medium. Zed still relays short prompts telling each session to read GitHub; the test does not establish unattended messaging.

## Architecture decision before trial
Zed selected `A25` as permanent root. Stratumnova repositories are legacy source material for controlled migration, with original names preserved as aliases and originals archived only after verified acceptance. Decision recorded in `project lead/archivist/A25-ROOT-NAMESPACE-DECISION.md` at commit `0ecb6079f66a46648ff9777bf1e88f1a2616a045`. Initial subsystem names remain proposals until ratified.

## GitHub trial channel
Repository: `Stratumnova/A25-Training-Workspace`.
Coordination branch: `coord/a25-namespace-trial-001`.
Orders: `project lead/coordination/orders/`.
Reports: `project lead/coordination/reports/`.
Reviews: `project lead/coordination/reviews/`.
Case studies: `project lead/coordination/case-studies/`.
Builder implementation branch: `build/a25-ns-o002-synthetic-prototype`.
Append-only numbered records; no main merge authorized.

## Chronological evidence and outcomes
### O001 — Design handoff
Lead order `A25-NS-O001` commit `26ba18775d5322c3bca29871725b2ddc2bd26cc4`.
Builder wrote namespace specification, migration ledger draft and synthetic collision examples, then report R001 at `96175c13a2862566c15820db00fa884be91e3f3e`. Lead independently fetched four files and reviewed. Result: design handoff PASS, not production ratification.
Lead review V001 commit `f7f4f02d7c7a0b1d749f7075a996ffbb236402cb`.

### O002 — Synthetic executable prototype
Lead order O002 commit `51e018d5eb5e7abdab36b32ee17450a41456039f`.
Builder committed Python registry, tests, README and synthetic public index on implementation branch at `1ffc4d613f1ab2121ba172838ba1c5961294daa4`. Report R002 at `d30363686ef7b1475357af2ef1d8bb8309c2371b`.
Builder reported 14 passing tests on a local prototype but explicitly said exact GitHub-committed bytes were **not** rerun because the execution environment could not resolve `raw.githubusercontent.com`. Lead independently fetched committed source and identified limitations: caller-supplied identity is not authentication; revisions overwrite latest in-memory state; ledger is neither durable nor hash-chained; two independent registry instances can allocate same ID. No claim of committed-code green. Lead review V002 commit `96a13ad7d1c75600fc42b83448d4fe08cbbd1538`.

### O003 — Exact committed byte verification
Lead order O003 commit `c35dd04a1705ccd6a9908bbc9afba49b1eaac3a2`.
Builder fetched four pinned source files through GitHub connector, reported Git blob SHA-1 identifiers, attempted a curl HEAD to raw.githubusercontent.com and received DNS failure `curl: (6) Could not resolve host: raw.githubusercontent.com`. Builder did not manually reconstruct files, did not execute tests against committed bytes, made no implementation changes, and submitted R003 at `35a727f7bf0a55c8c4b87b415c61358ffe4ddffb`. Lead independently retrieved R003. Result: **BLOCKED**, with honest disclosure and source identity recorded. This is a successful fail-loud behavior, not successful executable verification.

### O004 — Next test: GitHub Actions
Lead created O004 at commit `71341070cfa453edf93580a2fc15b26c4acd1b9d`. Proposed next experiment: have GitHub Actions check out exact implementation commit and execute `python3 -m unittest discover -v`, recording commit, Git blob IDs, Python version, test results, run URL and logs. Builder must first check existing workflows and restrictions, add a narrow read-only manual workflow only on its implementation branch, and report BLOCKED if dispatch is unavailable without changing main. **O004 has not yet been delivered to/executed by LB-GPT01 at this checkpoint.** No CI success claimed.

## Evidence and limitations
- Two complete GitHub-based lead-to-builder-to-lead cycles were observed through independently retrieved files, plus a third correctly blocked verification cycle.
- Zed did not paste full build orders or reports; Zed relayed short instructions and builder summaries. Lead and builder do not directly communicate without Zed prompting their turns.
- GitHub commit author and document FROM header do not authenticate a model/session identity.
- Builder's lack of uploaded ZIPs did not prevent design and synthetic work; no original ZIP content was ingested into prototype.
- GitHub source inspection is not equivalent to execution of committed bytes.
- No real migration, production authentication, Watchdog integration, protected file edit, or main merge demonstrated.
- A workflow definition being present will not prove a successful run; completed CI conclusion and logs are required.

## Lead's dual duty and return-to-work procedure
The lead is responsible for **both** A25 delivery and an accurate running case-study record. At every meaningful handoff:
1. Read the actual GitHub report/evidence, distinguish observed facts from claims and unresolved gaps.
2. Append a new case-study checkpoint or numbered addendum; never silently rewrite earlier observations.
3. Record current project decision, next test/order, pending approvals and exact commit references.
4. Return to lead role: issue or review the next scoped order, preserve scope boundaries and await builder report.
5. When a builder is blocked, do not conceal the blocker or claim green; choose a bounded alternate verification path.
6. Zed remains owner/tie-breaker. Claude may later independently audit the timeline and evidence.

## Current handoff checkpoint
- O001 design: delivered/reviewed.
- O002 synthetic code: delivered/source-reviewed; exact committed execution unverified.
- O003 exact execution: BLOCKED (DNS transfer limitation).
- O004 CI alternative: ISSUED; waiting for Zed to prompt builder.
- Next action: Zed relays short O004 instruction; builder attempts CI evidence and posts R004; lead fetches report and updates case study before advancing.
