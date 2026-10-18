# LEAD-ADDENDUM-017 — Missing Archives / Namespace / Folder / Watchdog Context
Issuer: GPT A25 Pocket Server and Roundtable Communication Lead
To: Zed; A25-AG-GPT01; LB-GPT01; Claude reviewers and Writer
Owner relay: 2026-10-17 21:01 MDT
Status: HISTORICAL CONTEXT + VERIFIED REPO REFERENCES; NOT new build authorization.

## Purpose
Supplement LEAD-HANDOFF-016 and A25-AG-R001 without silently replacing either. Preserve earlier namespace and folder-organizer work. A25-AG-GPT01 is delegated lead for Archives, Watchdog support and GitHub Agent/Bot; GPT A25 Project Lead retains Pocket Server and Roundtable. Zed remains final authority and human Watchdog.

## Verified repository references
- Existing coordination README: `project lead/coordination/README.md`, branch `coord/a25-namespace-trial-001`. Defines pinned orders, append-only reports, Zed relay, provenance fields, no unauthorized merges and no public private-data upload. Historical generic wording about builder creating branches is superseded for Pocket Server by owner's single official build branch decision.
- Existing Archivist README: `project lead/archivist/README.md`. Explicit canonical landing place, `REPOSITORY-DIRECTORY.md` (eight then-identified public repos), `TERMINOLOGY-AND-EVIDENCE.md`, `project lead/master archive/00-EVIDENCE-REGISTER.md`. Proposed `repositories/<repo-slug>/README.md`, `FILE-MAP.md`, `TERMS.md`, `REPORT.md` and `archivist/reports/` are EXPECTED SHAPE, not proof folders/files were implemented. Privacy rules apply.
- New lead report `project lead/coordination/reports/A25-AG-R001-GPT01-BASELINE-AND-PLAN.md` at commit `2b7b2e3179502418b6530b5161d4bf3ce2653f7b`, independently retrieved by this lead. Report is inspection evidence and historical execution claims, not full verified operational state.
- Existing namespace work: `project lead/coordination/orders/A25-NS-O001...` through `A25-NS-O004...` and corresponding `reports/A25-NS-R001...` through `R004...` on coordination branch; LB-GPT01 is the historical assigned builder. Lead reviews A25-NS-V001/V002 and Case Study 001 were used during that work. Fetch pinned originals before declaring schema adopted or implementation complete. Do not issue overlapping work orders until status reconciled.
- Recall Network: `local build operations and recalls/recall-network/REGISTRY.md`, `outbox/RN-001-UNIVERSAL-RECALL-RULES.md`, and participant inboxes/reviews. IDs such as `A25gptrecall_idNNN` follow registry reservation rules; not interchangeable with seat, authenticated principal, file author or publisher. Fresh-session recovery tests are historical evidence and must not be treated as authoritative without originals.
- Watchdog: `watchdog/check.py`, `watchdog/test_check.py`, `watchdog/test_fixtures.py`, `watchdog/test_wd35_guard.py`, `.github/workflows/watchdog-draft-tests.yml`, branch `build/wd-02-watchdog-v0`. AG-R001 reports Actions run #65 success at its exact commit only. Existing WD-01A/01C baseline and WD-CI reviews are references for conflicts and frozen rules; inspect protected sources, don't overwrite them.

## Historical context to recover, NOT assumed verified
- LB-GPT01 completed four namespace orders/reports according to earlier conversation. Their actual source contents, exact adoption, and implementation status need fresh retrieval.
- Owner requested namespace and folder organizer work so independently named AI seats, repository scopes, originals, derived reports, orders, rooms, and recovery artifacts do not collapse into one ambiguous tree. Preserve source ownership and explicit provenance; distinguish physical paths from logical namespaces.
- A25 Recall Network RN-001 sought recoverable project history from independent GPT/Claude sessions. Repeated reports and corrections must remain distinct, and evidence retrieval limitations recorded.
- Watchdog review disputes, CI outcomes and historical Claude/GPT disagreements must remain side by side until verified against source. Do not let an agent self-approve or silently rewrite protected baselines.

## Recommended interface contracts for AG lead to investigate
1. Namespace registry: stable namespace ID, human-readable label, owning seat/role, allowed source/repo roots, privacy class, parent scope, reservation state, collision detection, supersession history. Keep AI seat claims distinct from actual authenticated principal.
2. Folder organizer: deterministic source-path inventory and proposed moves only; dry-run default; no destructive move/rename or public exposure of private paths. Existing paths stay canonical until Zed adopts migration.
3. Archivist: public-safe metadata pointer to original source, commit/hash, observed content type, source vs derived status, verification state, adoption and supersession. Archive index is NOT replacement source.
4. Watchdog: consume structured audit/evidence outputs, identify mismatches and unauthorized changes, report to owner; no autonomous approvals or enforcement rewrite.
5. GitHub agent: least privilege, read-first, pinned refs, append-only new reports, idempotent writes, separate publisher/author fields, and no unapproved merges.
6. Roundtable interface: messages and room membership are separate from repository folders; durable append-only event IDs, cursor-through semantics, unseen/context distinction, retry deduplication and post-restart recovery. Gate-01 historical proof does not imply Gate-02A is live.

## Decision / next action
A25-AG-GPT01 should read and reconcile original A25-NS orders, reports, lead reviews and Recall Network registry before choosing namespace/folder implementation ownership. Coordinate with existing LB-GPT01 instead of duplicating. Report gaps and proposed exact paths to Zed and GPT A25 Lead. No new branch/folder/credential/deployment authorization in this addendum. Claude02 O007 remains in progress and is unaffected.
