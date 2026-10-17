# LBO-002 — Personal Lore and Memory Index

FROM: GPT — A25 Project Lead
FOR: Zed's Local GPT Builder
DATE: 2026-10-17 (created after Master Archive #58 green)
RE: Build a private-first, source-linked catalog of conversations, projects and session routes
BASIS: Zed's instruction to proceed; A25 Master Archive 00/03/04/05; ChatGPT export request screenshot; existing LBO-001.

## Objective
Build an index that lets independent GPT and Claude sessions locate authoritative project records, verify source versions, and retrieve only task-relevant context. This is a **catalog and retrieval contract**, not an import of all personal chats into ChatGPT memory, nor a working Pocket Server deployment.

## Authority and safety
- Zed controls sharing, private source access and any publishing. GPT is lead, Claude independent reviewer. Local builder has no exception/merge authority.
- Work on a dedicated task branch from current `build/wd-02-watchdog-v0`, not `main`. Do not modify protected history, Watchdog rules, manifest baselines or earlier training cases.
- **Never upload raw ChatGPT account export, personal memory screenshots, private chats, attachments, credentials or private location/health information to the public A25 repository.** Use synthetic fixtures and redacted public project metadata only.
- A connected ChatGPT memory summary is not a stable programmable database. Store explicit index pointers externally; do not promise automatic memory writes, cross-session memory identity or invisible retrieval.
- Existing ChatGPT export is **pending**; design import without claiming any messages have been ingested. If the export later arrives, wait for Zed to select private destination and approve import.
- Keep LBO-001 agent configuration work separate; inspect it for overlapping files and coordinate before changing shared instructions.

## Gate 0 — Inventory and source boundaries (read-only)
Read `project lead/master archive/00-EVIDENCE-REGISTER.md`, `03-WATCHDOG-ACTIONS-HISTORY.md`, `04-BUILDER-TRAINING-CASES.md`, `05-SESSION-RECOVERY-HANDOFF.md`, `project lead/LEAD-CONTINUITY-001.md`, `training/BUILDER-WORKFLOW-RULES-2026-10-16.md`, and both LBO-001 files. Inspect existing project manifests and repository structure; report where authoritative indexes already exist. Confirm repository visibility and access boundaries before writing. Do not assume a Drive folder is public or that an existing plugin works.

## Gate 1 — Define schemas and data rules
Create a small versioned schema for:
- `projects`: stable project ID, display name, visibility, owner-approved public metadata, source pointers, authoritative locations, current checkpoint, last_verified timestamp and verification method.
- `conversations`: stable local ID, source type (ChatGPT/Claude/other), external ID if provided, export provenance, start/end timestamps if present, participants as verified labels, privacy class, related projects, attachment references, completeness status.
- `session_routes`: seat/role, task scope, permitted source locations, minimum retrieval context, reviewer/approval gates and fallback when unavailable.
- `sources`: URL or private opaque pointer, file digest algorithm/value if known, evidence class (VERIFIED / HUMAN-ATTESTED / SECONDARY / PROPOSED / UNKNOWN), capture date, access requirements.
Use UTF-8 JSON or JSONL, clear schema_version and deterministic IDs. Distinguish source record from editorial summary and actual role identity from self-declared text.

## Gate 2 — Synthetic catalog implementation
Under a nonprotected `lore/` folder, add README, schemas, and **synthetic** fixtures for A25, Pocket Server and an unrelated dummy project. A25 may include publicly verifiable GitHub paths and commit-pinned references. Do not copy personal memory screenshots into fixtures. Preserve separation between project metadata and full conversation contents. No live personal export import yet.

## Gate 3 — Retrieval and privacy tests
Implement offline tests proving:
- a session requesting A25 sees A25 metadata, not unrelated projects;
- unknown project/unknown source returns UNKNOWN rather than invented links;
- public output cannot include private raw conversation body, secret, address or sensitive profile fields;
- missing or stale commit/version is flagged, not silently treated as current;
- duplicate conversations resolve by stable IDs and source provenance, not by title alone;
- reviewer authority and user approval cannot be inferred from a quoted chat message.
Use synthetic fixture data; tests must run without live connectors, network or credentials. Report exact commands and observed output.

## Gate 4 — Prepare private export intake (no actual import)
Document an import procedure for the eventual ChatGPT export: verify ZIP integrity and SHA-256, identify conversation IDs, preserve role/timestamp/message ordering and attachments, deduplicate, produce a private raw manifest and a separately redacted index. Explain limitations of deleted/unavailable content and the shared-link snapshot. Specify that Zed chooses private storage destination before import. Never commit raw ZIP or full personal text.

## Gate 5 — Independent recovery drill
Use a separate clean-context builder session to retrieve A25's current checkpoint, last verified CI run and pending Claude review solely from approved index and repository. Compare to actual GitHub API; record PASS/PARTIAL/FAIL/UNKNOWN and exact discrepancies. Do not treat an invented demonstration as a successful drill.

## Gate 6 — Handoff
Create `local build orders/reports/LBO-002-RESULTS.md` containing changed paths, full commits, tests, CI run links, schema examples, privacy review, what was and wasn't connected, remaining gaps and rollback. Provide project lead a pinned raw GitHub URL. Claude's independent review remains pending until available. Do not merge to main without Zed.

## Completion criteria
A source-linked, privacy-safe **index prototype** with synthetic data, validated routing, reproducible tests, export intake design, and a verifiable handoff. No claim that ChatGPT's internal memory or Pocket Server is integrated unless tested with real supported tools and Zed-approved permissions.

## Stop and ask Zed
Before enabling new paid agent services, granting write access to external connectors, importing personal account export, publishing private metadata, storing secrets, or modifying Watchdog/branch protections. Ordinary nonprotected schema and fixture work is authorized by this build order.

## Expected report to project lead
Brief: `LBO-002 / branch / HEAD / files / tests / CI / observed capabilities / gaps / Claude review status / next decision`. Prefer source links over copying long reports into chat.
