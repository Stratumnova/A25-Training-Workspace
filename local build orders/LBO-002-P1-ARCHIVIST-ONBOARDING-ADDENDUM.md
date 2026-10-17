# LBO-002 — Archivist Onboarding Addendum (supersedes conflicting scope only)

FROM: GPT — A25 Project Lead
FOR: LB-GPT01
DATE: 2026-10-17, after Zed's 11:04 MDT direction
RE: Build the map as you inspect; all public Stratumnova repositories are part of A25 lineage
BASIS: Zed's direct clarification and LBO-002-P0 builder findings

## Naming
Use LBO-002-P0/P1/P2 phases, never 'Gate' for builder work. Pocket Server Gate terminology is reserved.

## Updated immediate mission
Make `project lead/archivist/README.md` the A25 master landing page. It, `REPOSITORY-DIRECTORY.md` and `TERMINOLOGY-AND-EVIDENCE.md` are lead-created onboarding seeds; preserve and extend them in a dedicated task branch. As you inspect each public repository, **write its landing page and file map incrementally**. Do not wait until the end to produce one monolithic report.

## Deliverables
1. A per-repo README, file map, terminology crosswalk and evidence report under `project lead/archivist/repositories/<slug>/` for all eight public repos.
2. A25 central navigation linking every repository and its per-repo maps, with revision, status, last verified and unresolved gaps.
3. Machine-readable index/schemas, offline retrieval, privacy and integrity tests from original P1 authorization; map must be usable by humans and by an index reader.
4. Markdown as searchable source of truth; one PDF per repository as a **derived, versioned export** when content is stable and the PDF pipeline is available. No PDF should claim deeper inspection than its underlying source.
5. A terminology crosswalk distinguishing Zed's names from artifact kind and technical implementation. Example: 'Key 5' in original lore is a prompt; same name in Pocket Server may refer to code. Verify exact paths before making implementation claims.
6. A source-anchored cross-repository lineage map, including original vault to lite compression, Toolbox to Build by Coin, Pocket Server to A25 training, and HalfAwake family to watch-panel concepts. Owner-stated links must be labeled as such until source verified.
7. A small retrieval demonstration: 'Where is Key 5 and what type of artifact is each?', 'Which Toolbox modules could become coins?', 'Where is Pocket Server authentication implemented versus proposed?', 'What HalfAwake control/watch features are actual code?' Return evidence, status and UNKNOWN for unverified claims.

## Work cadence
Inventory shallow first (README and full tree), then inspect significant files deeply. Commit the map as it grows, with exact source references and evidence labels. Avoid adding private repository or conversation contents to public A25. Preserve existing Watchdog and original repository histories. Do not copy or change original code.

## Scope/stop
P1 implementation and mapping scaffolding are authorized; deeper P2 content extraction and publication beyond public-safe references require lead review after P1 test report. Builder may propose detailed P2 mapping without executing unauthorized ingestion. No main merge, Watchdog modifications, Pocket Server changes, paid services, private exports, secrets or Drive writes without approval. Submit branch/commits/tests/CI/privacy audit and pending gaps.

## Handoff
Return a pinned raw URL for the updated A25 master directory and the P1 report. Claude review remains independent and pending.
