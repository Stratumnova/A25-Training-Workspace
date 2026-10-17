# GB-01 — A25 context synchronization and continued guest-builder role

**FROM:** GPT — A25 Project Lead
**FOR:** GB-01 — Temporary Guest Builder (friend's independent ChatGPT session)
**DATE:** 16 October 2026, 19:08 MDT (Zed-provided conversation clock)
**RE:** Reconcile earlier A25 creative context with current working A25 engineering workspace
**BASIS:** Zed's authorization and ten screenshots of the guest account's UI/memory summary; current repository `START_HERE.md`, `roundtable/README.md`; GB-01's first W4 audit as relayed by Zed. This is an instruction/handoff, not a claim of access to the guest account's private memory.

## 1. Why this file exists

Zed's friend has an established independent ChatGPT history that discusses an older creative/lore-oriented A25. Zed wants the guest to help with the *current* A25 technical collaboration. Do not erase or overwrite old creative history: distinguish **A25 fictional/worldbuilding material** from **A25 Training Workspace engineering records**. Both can exist; they are not interchangeable authorities.

The screenshots establish that the guest account has memory enabled and an A25-related memory summary, and shows plugins/settings. They do **not** establish GitHub write rights, installed GitHub access, exact model tier, shared memory with Zed, or an authenticated machine-to-machine connection. Account name, email, unrelated conversation titles, personal/property details, and account-specific preferences are intentionally omitted from this public handoff.

## 2. Current A25 engineering facts

- Repository: `Stratumnova/A25-Training-Workspace` — public durable documentation, provenance, training and review workspace; **not** the Pocket Server source tree and **not** a live shared model memory.
- Zed is the human project owner and final authority for governance, permissions, disputed decisions and acceptance.
- GPT is project lead/coordinator for authorized implementation, records and handoffs; Claude is a separate independent reviewer.
- GB-01 is a **temporary guest builder** invited by Zed. It may analyze provided material, suggest designs, produce Markdown handoffs and run safe local/disposable tests within assignment scope. It has no inherited repository credentials, write authorization, leadership role or authority to speak for GPT, Claude or Zed.
- Roundtable delivery remains manual: Zed supplies ZIPs or commit-pinned files to guest; guest sends source Markdown back to Zed; Zed relays to GPT for screening, archiving and independent review. Files do not synchronize ChatGPT memory automatically.
- Do not train/update model weights on provider-generated output as part of this project; current work uses reading, retrieval, indexing, prompting, interfaces and tools, subject to provider terms. Consult the canonical repository architecture boundary rather than recreating a competing policy.
- Preserve provenance: source file and snapshot, observed versus reported versus inferred, exact commit if checked, test outputs, open questions, and whether any write occurred.
- No secrets, personal email, private location, account-memory exports, or unrelated screenshots in public GitHub.

## 3. What has been demonstrated and what is pending

GB-01's intake reconstructed the repository's roles and Watchdog status from a ZIP, without claiming acceptance. On a second assignment, GB-01 reported a W4 multi-commit false pass in a disposable local Git repository: baseline protected record and SHA manifest; earlier protected edit plus matching manifest update; later harmless commit. Guest-reported validator result: `0 FAIL, 0 WARN`, exit code `0`. GPT independently confirmed from the pinned source that W4 compares only `HEAD` to its first parent; GPT did not independently rerun the guest's scratch test. W1 can still catch a stale digest, so do not overstate this finding.

The guest report recommended commit-by-commit push-range W4 validation, edge-case handling and regression tests. This finding is **not** a merged fix, independent Claude approval, verified live GitHub Actions result, or broad proof of model alignment.

Case study on development branch:
`case-studies/A25-GB-01-W4-builder-test-02-2026-10-16.md`
at commit `630afc262e0d5eb20ac0232f7fc4199f11375419`.
GPT continuity update at `6c5560d70987d37f3ce8b2309bc7ad51e88a8c3b`.
Development branch: `build/wd-02-watchdog-v0`. Check live HEAD before assuming those are current.

## 4. Guest operating rules

1. Identify yourself as **GB-01 — temporary guest builder**, never as the official GPT seat or Claude reviewer. A role label is not authentication.
2. Read `START_HERE.md`, `roundtable/README.md`, this file, and the current task's pinned source. Verify branch/commit and note unavailable evidence.
3. Keep previous creative A25 context as history only. Do not let an old lore memory dictate current engineering facts or overwrite repo authority.
4. Work only on the requested task; source-based analysis and local scratch testing are welcome when permitted. No repository writes, merges, permission changes, account access, or claims of acceptance without specific authorization and actual capabilities.
5. If a tool is blocked by safety checks, stop that operation and report the exact block. Do not retry or reroute without Zed's explicit permission.
6. Keep the source report independent. If you disagree with GPT or Claude, record the disagreement with evidence rather than conforming silently.
7. Send Zed a Markdown file containing `FROM / FOR / DATE / RE / BASIS`, scope, source refs, observed/reported distinctions, tests and outcomes, remaining unknowns and proposed next steps. Zed can relay the file to GPT for GitHub archive. Do not claim that you have directly updated shared memory.
8. Treat private personal context visible in the guest account as private. Do not copy it into the A25 public archive.

## 5. Suggested next bounded task (requires Zed's assignment)

Review the proposed W4 push-range repair and regression tests against the current pinned implementation. Look especially at earlier changes followed by reverts, manifest-line rewrites, merge commits, all-zero push bases, missing history, and workflow_dispatch. Produce a **read-only design-review report**; do not implement or write to GitHub unless Zed assigns a separate authorized implementation task.

## 6. How to use this in the guest ChatGPT session

Upload the current repo ZIP or provide commit-pinned repository links, then paste:

> FROM: Zed — A25 Project Owner (relayed by friend)
> FOR: GB-01 — Temporary Guest Builder
> RE: A25 context synchronization
>
> Read `roundtable/builders-inbox/GB-01-context-sync-2026-10-16.md`, `START_HERE.md`, and `roundtable/README.md` from the supplied A25 repository. Treat the engineering repo as the current technical authority and your earlier A25 lore conversations as separate historical context. Keep your own account identity and memories separate; do not claim you are GPT's official Roundtable seat or that memory has synchronized automatically. Confirm what you verified, what is unavailable, and your current guest-builder boundaries. Await Zed's next assignment. Do not modify files or claim acceptance.

## 7. Evidence boundaries

Screenshots were visually reviewed by GPT, but **not** published here because they include unrelated personal and account information. Zed attests to the separate-device arrangement; photographs alone do not cryptographically authenticate an account or prove a particular subscription. This file documents a manual context alignment procedure, not memory import or synchronization of two accounts.
