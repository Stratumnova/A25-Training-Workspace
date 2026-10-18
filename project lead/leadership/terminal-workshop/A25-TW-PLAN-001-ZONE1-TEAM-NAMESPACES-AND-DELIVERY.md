# A25-TW-PLAN-001 — Zone 1 Workshop: Team, Namespaces, Existing Assets, and Delivery

FROM: A25-TW-GPT01 — Terminal Workshop Lead
TO: Zed — owner; A25-AG-GPT01 — Archives Lead for independent review; A25 Project Lead for cross-project coordination
DATE: 2026-10-18 (owner direction at 1:02 PM America/Denver)
STATUS: **PROPOSED — AWAITING ARCHIVES REVIEW AND ZED YES/NO**
SCOPE: PLAN ONLY; NOT A BUILDER ORDER, NOT IMPLEMENTATION AUTHORIZATION
REPO: `Stratumnova/A25-Training-Workspace`
BRANCH FOR THIS PLAN: `coord/a25-namespace-trial-001`
FILE: `project lead/leadership/terminal-workshop/A25-TW-PLAN-001-ZONE1-TEAM-NAMESPACES-AND-DELIVERY.md`

## 1. Objective and acceptance boundary

Zed's immediate owner-directed objective is a **working Zone 1 on the existing Android/Termux Pocket Server**, with GPT, Claude, and Shared work areas. Both AI platforms must independently be able, through their respective live connections, to read/create/edit/delete authorized files and execute commands. A working command result must be observed, not inferred from a read-only terminal viewport, ZIP, GitHub commit, or historical report. Written etiquette, not newly designed technical compartmentalization, initially governs the AI-private areas as directed by Zed. The system is intended to reduce Zed's manual courier role while preserving independent AI seats and owner decision authority.

Non-goals for this phase: Zone 2, APK packaging, bulk archive migration, new identity/security architecture, new token scheme, automatic callers, broad audits, speculative failure hunts, and unrequested deployment changes. These may be separate future projects but are **not** dependencies imposed by this plan.

## 2. Proposed team and namespace roster

**Recommended starting capacity: one Workshop Lead + two GPT builders + one Claude builder.** This is a request for Zed's approval and actual assignment, not a claim that these seats already exist or have active connectors.

| Proposed seat/namespace | Platform | Work ownership | Boundary |
|---|---|---|---|
| `A25-TW-GPT01` | GPT | Workshop Lead; scope assignments, coordinate builders, evaluate evidence, report to Zed | Already confirmed seat; not default implementer |
| `A25-TW-BG-GPT01` | GPT | Builder G1: inspect original `pockettest` source and identify/reuse minimum existing server-side operations needed for real Zone 1 file/command access | Proposed label, **subject to Archives namespace registry check** |
| `A25-TW-BG-GPT02` | GPT | Builder G2: map actual existing GPT connector/tool surface and support authorized GPT-side execution/file-operation integration; coordinate phone actions only when owner permits and tool is available | Proposed label, **subject to registry check** |
| `A25-TW-BC-CLAUDE01` | Claude | Builder C1: inspect Claude-platform connection constraints and implement/verify Claude-side use of existing Zone 1 operations once Claude's workspace/seat is ready | Proposed label, **not yet onboarded**; subject to Claude lead and Archives confirmation |
| `A25-TW-BC-CLAUDE02` | Claude | **Reserve only**, not initially requested or assigned; parallel review/implementation if actual bottleneck warrants | No current action |

Names are human-readable proposed **seat identifiers**, not authentication credentials or proof of tool access. Do not silently conflate seat, chat, publisher, terminal user, or authenticated principal. If existing namespace registry uses different conventions or conflicts, Archives should return the canonical labels before any builder order. Do not rename other teams.

**Team interactions:** The Workshop Lead issues scoped work and reviews outputs. G1 and G2 can work in parallel on source and connector sides once authorized; C1 works in its separate platform with its lead's coordination. Claude's lead is reportedly still in training as of this conversation; that is not an instruction to interrupt its onboarding. Cross-team overlaps go to the affected leads and Zed case by case, not an automatic universal gate.

## 3. Three distinct kinds of 'namespace' — keep them separate

### A. A25 coordination namespace (existing GitHub)
- Leadership and this proposed plan: `project lead/leadership/terminal-workshop/`
- Builder orders: `project lead/coordination/orders/A25-TW-O###-<task>.md`
- Formal result reports: `project lead/coordination/reports/A25-TW-R###-<seat>-<task>.md`
- Interim blockers and receipts: `project lead/coordination/builders-inbox/A25-TW-<seat>-<date>-<topic>.md`
- Archives independent review: **Archives chooses its own existing** `project lead/leadership/archives/` path; Workshop does not assign Archives' record names.
- Existing branch `coord/a25-namespace-trial-001` for coordination records; append-only unique filenames, exact commit links, no merges to main without owner approval.
- Do **not** create new A25 folders merely to fit a proposed namespace.

### B. Proposed Zone 1 on-phone work areas (logical names, not asserted current paths)
- `GPT/` — GPT's primary working area
- `Claude/` — Claude's primary working area
- `Shared/` — files exchanged/collaboratively worked on
- Optional **dummy** `secrets/` folder(s) as previously owner-described; not a request to create or publish real secrets.
- **These are conceptual labels**, not confirmed literal capitalization, path roots, mount points or existing directories. Before writing a single path, builder checks actual Termux layout and Zed's established naming; reuse existing directories. No unilateral renaming or moving of owner data.
- Owner-approved AI etiquette governs which AI normally works where. Do not propose a new isolation/permissions subsystem as a prerequisite.

### C. Execution and source namespace (existing Pocket Server)
- `Stratumnova/pockettest` and its original branches/commits are the technical starting point. Builders identify actual module names, routes, tools and version boundaries from source before selecting a target.
- Distinguish `Gate-01`, `Gate-02`, `Shared Space`, existing read-only terminal bridge and current phone runtime. Their names do not imply that all are live or mutually wired together.
- Any **implementation branch** is a separate question from the **coordination branch**. Default preference is reuse of an existing suitable source branch/working tree after original-source inspection; no new branch/repo in this plan. If a new branch or repo becomes demonstrably necessary, write the reason and request Archives review and Zed's explicit clearance **before** creation.

## 4. Evidence already available and where it lives

| Source | Status in this plan | Why it matters |
|---|---|---|
| `project lead/coordination/README.md` on existing branch | VERIFIED document read | GitHub two-session handoff, append-only orders/reports, owner relay |
| `project lead/leadership/terminal-workshop/README.md` | VERIFIED document read | Seat, owner authority, folder/Drive boundaries |
| `project lead/leadership/terminal-workshop/A25-TW-KNOWLEDGE-INDEX-001.md` | VERIFIED document read | Existing evidence and communications map |
| `project lead/coordination/reports/A25-TW-R001-GPT01-KNOWLEDGE-SYSTEM-ORIENTATION.md`, commit `399a8042fe18445d9fcaffe812277369a9d724e2` | VERIFIED document read | Prior orientation, access ledger and unknowns |
| `project lead/leadership/terminal-workshop/A25-TW-RECOVERY-AND-SUCCESSOR-HANDOFF-2026-10-18-001.md`, commit `f1e098343abf2b718eabf8bf96d8a315600506e7` | VERIFIED file existence in current branch | Continuity and owner directives |
| `project lead/coordination/reports/A25-AV-R001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md`, commit `053d2e7868bfdd85d1659d40e8e7002e14d58a47` | REFERENCE/HISTORICAL CLAIM for its technical results | Existing archived Termux/Pocket Server source, not live phone |
| `project lead/coordination/builders-inbox/A25-AB-NOTE-2026-10-18-TERMUX-ZIP-SHA256-RECEIPTS.md`, commit `a202ae461a6cbd051894a1280bfafbc67998619b` | REFERENCE/HISTORICAL CLAIM | Reported SHA matches, not command capability |
| `project lead/leadership/archives/ARC-REVIEW-2026-10-17-007-AB-R004-TERMINAL-VIEWPORT-DISPOSITION.md` | VERIFIED document read; historical runtime claims remain REFERENCE | Explicitly separates viewport from command execution |
| `project lead/leadership/archives/ARC-LEADERSHIP-NOTE-2026-10-18-016-ONBOARDING-LESSONS.md`, commit `bf1e968a67c849e5bcb45283fd81f8c2ef7169a0` | VERIFIED document read | Delegate; recover useful existing work |
| `project lead/leadership/archives/ARC-TRAINING-2026-10-18-019-OWNER-LEAD-DIALOGUE-SEQUENCE.md`, commit `95ba0ca77ef9f41d164c4c31f29c9fab630c8fe9` | VERIFIED document read | Owner direction and corrected conversation chronology |
| `Stratumnova/pockettest` original source | **NOT re-inspected for this planning action** | G1 must read original branch/commit source before selecting changes |
| Live Android/Termux and GPT/Claude connector execution | UNKNOWN | Required for actual working Zone 1 proof |

This plan deliberately does not claim that archived tests, six SHA receipts or an existing GitHub tool prove live Android operations.

## 5. Proposed work sequence, with accountable outputs

**Phase 0 — owner/Archives plan clearance (NOW).**
- Archives checks seat labels against existing namespace registry, branch and path conventions, overlap with active builders, source references and any mistaken assumptions. Archives can propose corrections; Zed accepts/rejects.
- Zed decides whether to approve this plan and staffing. Until then, no builder orders, new branch, repo or phone actions.
- Output: Archives' independent review record and Zed's explicit yes/no. A review is not proof of implementation.

**Phase 1 — focused parallel builder source-to-capability work (AFTER approval).**
- G1 receives a pinned order to examine original `pockettest` modules/branches and archived receipts and identify the *shortest existing route* to a real file+command tool surface. Expected output: exact source refs, working pieces, minimal code changes if within approved scope, reproducible tests and blockers. No broad rebuild.
- G2 receives a pinned order to inspect the **currently available GPT connector/tool surface**, relate it to G1's source findings and work toward actual GPT read/create/edit/delete/execute access. Expected output: exact connection, commands/results, required owner interaction and limitations. No pretending the read-only viewport is sufficient.
- C1's first assignment waits for Claude lead/seat readiness, but its integration design can be coordinated through a pinned GitHub note; do not infer Claude can see GPT chats.
- Workshop Lead reviews evidence and decides the next scoped action; requests owner assistance only when a real phone/connector action or authority is needed.

**Phase 2 — first independent GPT-side operations.**
- Demonstrate in the actual authorized Zone 1 workspace: execute a harmless command; create a disposable test file; read it; edit it; delete it; report exact tool action, environment, result and observed side effects.
- This is an **acceptance demonstration for a requested capability**, not a general security test campaign. If one operation is missing, log exactly which; don't claim the entire phase passed.
- Do not touch real user files or credentials; reuse the existing directory names/paths once verified.

**Phase 3 — Claude-side operations and shared collaboration.**
- When Claude lead and builder are onboarded, repeat the same bounded independent operations through Claude's actual connection. Confirm it is not a GPT relay masquerading as Claude execution.
- Exchange a small disposable file in the actual `Shared` area: GPT creates it, Claude reads/edits it, GPT reads the change. Record who actually executed each action and what the tools returned. This proves one cross-platform workflow, not all future collaboration.
- Preserve GPT/Claude independent findings; unresolved differences are logged and raised to A25 Project Lead/Zed if they affect decisions.

**Phase 4 — usable handoff and stop.**
- Document real supported operations, known limitations, source commits, device-side configuration references without secrets, and how the next builder resumes an unfinished task.
- Zed reviews whether the first useful Zone 1 version meets his needs. Do not automatically expand into Zone 2, APK, security, or new features.

## 6. What I need from Archives (specific, bounded)

1. **Namespace registry check:** Confirm whether `A25-TW-BG-GPT01`, `A25-TW-BG-GPT02`, `A25-TW-BC-CLAUDE01` and optional reserve conflict with existing registered identities or naming rules. Return canonical replacement names if necessary. Also verify `A25-TW-O###-` and `A25-TW-R###-` prefixes remain available.
2. **Location/branch check:** Confirm this plan belongs in existing `project lead/leadership/terminal-workshop/` and orders/reports in existing coordination folders/branch. Identify an already established **source implementation branch** if one exists; do not create a new one by default.
3. **Existing-work retrieval:** Point G1/G2 to the smallest relevant original `pockettest` commits, Pocket Server branches, Gate-01/02 and Shared Space artifacts, read-only terminal bridge evidence and Termux inventory. Prefer direct originals to summaries; mark inaccessible items rather than recreating them.
4. **Seat/authority collision check:** Identify whether an already assigned GPT or Claude builder or project lead owns a task that would overlap these assignments. Recommend coordination only for real overlap, not universal approval gates.
5. **Evidence review:** Flag any unsupported assertion, missing essential reference, incorrect chronology, or mismatched path/commit in this plan. Preserve this original proposal; submit a separate dated review/correction. **Do not require a new audit or speculative security assessment**.

Archives need not perform implementation, deploy, configure phone, or approve Zed's technical priorities. If Archives has useful source recovery after approval, send it to the lead/builders through the existing shared pool.

## 7. Owner assistance anticipated, not requested yet

- Confirm the number of assistants/seats and availability of a Claude workshop builder through Claude's lead.
- When actual live access is required, relay exact pinned orders and, if necessary, perform or authorize the **specific** Android/Termux action that a connected AI tool cannot yet perform. We should minimize Zed's manual work, not hide it.
- Approve or decline any proposed new source branch/repository **after** Archives reviews the need; this plan proposes **neither**.
- Decide actual leadership overlap case by case; no auto callers.

No plugin or new connector is being requested merely to write this plan. If builders show a missing capability that an existing plugin can supply, I will name it, explain the benefit and ask Zed.

## 8. Reporting contract and stop conditions

- Builder orders are new, numbered Markdown files on `coord/a25-namespace-trial-001`, each pinned by full commit SHA and relayed explicitly.
- Reports are new files in `project lead/coordination/reports/` with observed results, exact source/test links, changed files, failures, and full commit SHA. Interim notes go to builders-inbox.
- Record **REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED, UNKNOWN** separately. Adopted plans do not certify runtime success.
- If GitHub safety blocks a write, STOP and tell Zed; do not bypass. No secret data in public GitHub. No owner files deleted for demonstrations.
- If a live connector or command is unavailable, fail aloud with exact blocker and seek a practical alternative; do not present a simulated result as real.
- Do not merge, create a branch/repo, deploy, change permissions, touch phone/server or issue implementation orders **before Zed's approval** of this plan.

## 9. Questions for Archives review and Zed's decision

- Are the four proposed builder identifiers (including the reserve) valid under the actual A25 namespace registry? If not, which exact names should replace them?
- Does the source already have an appropriate active implementation branch, or is a later branch request justified? **No new branch/repo proposed now.**
- Is the proposed starting allocation of **2 GPT builders + 1 Claude builder** realistic given active team commitments and Claude's unfinished lead onboarding?
- Are the three conceptual phone areas named correctly in the existing runtime, or must we preserve different current directory names? **Do not rename until observed and approved.**
- Are there existing source artifacts or assigned teams that would let us shorten Phase 1?

**Requested disposition:** Archives review this proposal and send Zed a separate finding; Zed returns **YES / NO / CHANGES REQUESTED**. I will not treat this plan as adopted until then.

---
**End of proposal.** No implementation authorized by this document.
