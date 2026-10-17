# A25 Archivist — Master Directory (onboarding v0)

FROM: GPT — A25 Project Lead
FOR: Zed, LB-GPT01, Claude
DATE: 2026-10-17
RE: Single landing place for the Stratumnova ecosystem
BASIS: Zed's 11:04 MDT onboarding instruction; public repository inventory; LBO-002

## Mission
Every Stratumnova repository is part of the broader A25 lineage, including early experiments. Preserve original source in its own repository; build a navigable, provenance-backed map here. Map continuously while inspecting, not only at the end. The index is a derivative, not a replacement archive.

## Canonical landing places
- [Repository directory](REPOSITORY-DIRECTORY.md): all eight currently identified public repositories; their owner-defined roles, initial state and map status.
- [Terminology and evidence rules](TERMINOLOGY-AND-EVIDENCE.md): original name versus artifact type, interpretation, executable evidence and source authority.
- [LBO-002 assignment](../../local%20build%20orders/LBO-002-P1-ARCHIVIST-ONBOARDING-ADDENDUM.md): builder work plan and stop conditions.
- [Master Archive](../master%20archive/00-EVIDENCE-REGISTER.md): existing A25 evidence register.

## Expected workspace shape (builder to create, not yet implemented)
`project lead/archivist/repositories/<repo-slug>/README.md` — source-pinned landing page
`project lead/archivist/repositories/<repo-slug>/FILE-MAP.md` — file and directory inventory with artifact types and links
`project lead/archivist/repositories/<repo-slug>/TERMS.md` — original terminology and validated meanings
`project lead/archivist/repositories/<repo-slug>/REPORT.md` — verified findings, unresolved items, tests
`project lead/archivist/reports/` — cross-repository comparison and retrieval tests

PDFs are **later derived snapshots**, generated from source-controlled Markdown, with revision/date/hash and status. PDFs are not substitutes for searchable Markdown and machine-readable indexes. Do not add files or claims without checking their actual content.

## Policy
Public A25 holds only approved public-safe metadata and maps. No raw private chats, private repo listings, secrets, personal export, sensitive metadata or unapproved Google Drive mirrors. Record discovery does not confer access. Watchdog remains a separate independent check; integration is not yet operational. Pocket Server remains the runtime source; A25 remains the governance and catalog workspace. Gate refers only to Pocket Server stages; LBO uses Phases.

## Status
Onboarding created by project lead. Per-repository deep mapping and Archivist implementation not yet independently verified. Builder reports require exact branch, commit, evidence and tests. No merge to main without Zed.
