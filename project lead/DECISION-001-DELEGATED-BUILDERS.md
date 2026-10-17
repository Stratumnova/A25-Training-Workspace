# DECISION-001 — Delegated builders and durable project lead

FROM: GPT — A25 Project Lead
FOR: Zed, Claude and replacement lead sessions
DATE: 2026-10-16 23:28 MDT
RE: Adopt task orders and project-lead continuity files
BASIS: Zed's direct request; A25 CS-004 context/usage-limit incident and prior handoff difficulties

## Situation
Long conversations are prone to compaction and platform availability limits. A25 also needs more building capacity without mixing builder work, independent review, and human approval into one seat.

## Decision
Use local build orders/ for bounded assignments to separate AI sessions, starting with LBO-001 GitHub AI Agent Setup. Use project lead/ for durable decisions, evidence, rationale and session succession. GPT remains lead, Claude remains independent reviewer, Zed remains human owner. Delegated agents do not gain approval or merge authority.

## Why
Separating task execution from project decisions reduces context pressure, permits reproducible independent checks and makes a replacement lead able to reconstruct the work from GitHub without relying on chat memory. Explicit scopes and reports prevent a delegated builder from silently changing protected evidence.

## Controls
Build on task branches; verify available GitHub agent capability rather than assuming it exists. Use least privilege. No secret disclosure, automatic Watchdog bypass or main merge. Preserve sidecars and the GPT-only blackout log. Announce Actions and record actual results. Claude review is pending for blackout implementation.

## Evidence and state
At decision time, GitHub Actions #48 was green at 668373e720f08f486dd4d7e29d5d22738615c1df. LBO-001 and LEAD-CONTINUITY-001 were then created on the WD-02 development branch. Their new Actions outcomes must be checked separately; green at #48 is not proof of subsequent commits.

## Next gate
Local builder inventories agent support, proposes minimal setup and reports before enabling any higher-permission integration. Project lead checks the build-order report and Actions evidence; Claude audits independently when available. Zed decides any main merge.
