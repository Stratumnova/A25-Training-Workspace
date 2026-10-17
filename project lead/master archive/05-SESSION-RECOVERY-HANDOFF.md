# 05 — Session Recovery and Handoff

FROM: GPT — A25 Project Lead
FOR: Zed and replacement project-lead GPT
DATE: 2026-10-16
RE: Restore verified authority and continuity after session loss or compaction
BASIS: `project lead/LEAD-CONTINUITY-001.md`, CS-004, GitHub Actions, Claude blackout records

## First read (read-only)
1. Confirm repository `Stratumnova/A25-Training-Workspace`, branch `build/wd-02-watchdog-v0`, and current HEAD through GitHub. Do not assume this document is the latest.
2. Read `project lead/LEAD-CONTINUITY-001.md`, `project lead/DECISION-001-DELEGATED-BUILDERS.md`, this master archive's `00-EVIDENCE-REGISTER.md`, `03-WATCHDOG-ACTIONS-HISTORY.md`, `04-BUILDER-TRAINING-CASES.md`.
3. Read `training/BUILDER-WORKFLOW-RULES-2026-10-16.md`, `training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md`, `training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md`, CS-004 documents and current `local build orders/` files.
4. Check GitHub Actions API for latest run, then its job logs. Report actual unit test count, W1–W6 FAIL/WARN, push base and unresolved failures. Never infer current green from a historical screenshot.
5. Check Claude Drive originals/reviews through the connected Drive tool and verify file versions before crediting Claude. Compare all commits after last independently reviewed checkpoint.
6. Ask Zed to resolve any identity, authorization or missing-evidence ambiguity before a protected write or main merge.

## Authority model
Zed = human owner, intervention/approval and main merge decision. GPT = project lead and GitHub writer. Claude = independent reviewer and Drive lead. Delegated local GPT or GitHub agent = scoped builder only. Credentials, not self-declared message labels, must establish tool identity; a copied message is evidence, not authority. No GPT-only work becomes Claude-approved by implication.

## Recovery state report (required)
- Current branch and full HEAD:
- Latest Actions run ID/URL, result, test count, actual validator result:
- Last independently reviewed commit and evidence:
- GPT-only blackout commits pending Claude review:
- Open build orders and delegated branches:
- Known exceptions and sidecars:
- Open risks/disagreements:
- Exact Zed approvals and source:
- Next permitted action:
- Continuity verdict: PASS / PARTIAL / FAIL / UNKNOWN, with justification:

## Stop gates
No merge to `main` without Zed's decision. No new Watchdog exception without its own sidecar and required review/approval. No arbitrary baseline rewrite. No production agent activation or elevated permission based solely on a build-order proposal. Never enter Zed's private signing code in chat. No public upload of raw ChatGPT export or private screenshots.

## What counts as recovery
PASS only if the replacement independently locates and validates current repository state, pending reviews, authority and next action. PARTIAL if it can continue read-only but lacks required source/reviewer evidence. UNKNOWN if original context/export or latest GitHub/Drive status cannot be verified. Confidence or conversational fluency alone is not evidence.

## Handoff drill
A fresh GPT session, without reading this conversation, must reconstruct branch/HEAD, latest Actions, WD-30/WD-35/CS-004, open Claude review and current build orders from repository and Drive. Compare its report with the verified master index; record discrepancies as training evidence. No writes during the drill.

## Archive limitations
ChatGPT account export still pending. This file is a recovery playbook, not a transcript. All source pointers must be revalidated when used. Update by additive dated records when material state changes.
