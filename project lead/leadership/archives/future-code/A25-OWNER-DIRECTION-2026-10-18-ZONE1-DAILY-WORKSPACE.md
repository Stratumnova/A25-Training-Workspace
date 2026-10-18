# A25 Owner Direction — Zone 1 Daily Workspace and Downstream Storage
FROM: Zed — Owner (recorded by A25-AG-GPT01 Archives Lead)
DATE: 2026-10-18
STATUS: ADOPTED OWNER INTENT; NOT A CLAIM OF IMPLEMENTATION OR TEST SUCCESS
AUDIENCE: Archives; Project Lead and leadership pool; current Workshop build team

## Owner directive
Zone 1 must replace GitHub and Google Drive for **daily operations** among GPT and Claude. It is intended to be their **one shared working space** with comparable read/write capabilities. GitHub and Google Drive are to serve their intended downstream roles as storage, backup, delivery, and repository/CI destinations **after** work is developed and tested in Zone 1, not as the daily collaboration workspace during development.

Zone 1 needs the useful capabilities currently obtained from GitHub and Drive for **building, storing working artifacts, sharing, testing, retrieving, and investigating results** so the team can work in one place. The owner wants defects caught and resolved in Zone 1 where practical before a product is sent to GitHub Actions: fewer avoidable red runs, more validated green runs. When GitHub Actions does fail, preserve the failure evidence and work through it in Zone 1 when best, rather than using GitHub as the primary debugging workspace.

## Required distinction
- CURRENT VERIFIED BASELINE: Manual GitHub/Drive relay tests proved specific file exchanges between GPT and Claude. They did not prove Zone 1 exists or runs.
- ADOPTED TARGET: Zone 1 is the primary daily shared development and testing workspace. GitHub/Drive become downstream destinations and durable storage, not the normal work loop.
- EXPECTED DEVELOPMENT PRACTICE: Capture tests, logs, errors, failure causes, corrections, and retest evidence in Zone 1; publish mature outputs to GitHub and use GitHub Actions as a downstream validation gate.
- UNKNOWN: Exact Zone 1 feature inventory, interfaces, CI-equivalence, security implementation, and completed functionality must be determined from approved specifications and independently tested. Do not invent them from this note.
- NO GUARANTEE: Fewer red GitHub Actions runs is an engineering objective, not a promise that all runs will be green.

## Instructions to leads and builders
Preserve this owner intent without reinterpretation. Do not optimize the manual relay as a substitute for Zone 1. Identify any mismatch between current plans and this target for owner/Project Lead resolution before altering scope. This document is a directive on intended architecture and workflow, **not** authorization to deploy, change code, modify permissions, activate seats, or replace existing orders. Retain the manual relay only as a temporary reference/communication method until Zone 1 capabilities are verified.

## Evidence status
Owner direction: ADOPTED as requirements intent.
Current implementation of these capabilities: UNKNOWN, unless verified by separate tests.
Prior relay successes: reference evidence only, not proof of the new architecture.
