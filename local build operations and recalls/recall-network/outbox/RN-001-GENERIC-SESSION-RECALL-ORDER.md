# RN-001 — Generic Cross-Session Project Recall Order
FROM: GPT — A25 Project Lead
FOR: Assigned GPT or Claude chat session
VIA: Zed
STATUS: READ-ONLY MEMORY / PROJECT INVENTORY; NO BUILDS
PARAMETERS: SESSION_ID=<Zed/Lead assigned>; PLATFORM=<GPT|CLAUDE>; PROJECT_SCOPE=<all projects or named subset>; REPORT_CHANNEL=<GitHub|Drive>; PRIOR_CHECKPOINT=<optional exact source>; DATE_UTC=<session time>

## A — Independent recall first
Before consulting tools or other AI reports, write and freeze what this chat knows about the assigned projects: project names/aliases, goals, architectures, components, repositories, branches, local folders, artifacts, decisions, tests, failures, current/last-known state, dependencies, blockers and next steps. Include Zed's decisions and pending questions, but do not answer on Zed's behalf. Label every assertion RECALL / OBSERVED / INFERRED / UNKNOWN. Keep a separate `not remembered` section.

## B — Source verification second
Only after freezing Phase A, inspect sources this session can actually access: prior conversation, project files, repository, Drive or authorized connector. For each important claim record source type, exact path/URL, commit/hash or file ID, observed_at UTC, whether personally verified or relayed, and status: PROPOSED / IMPLEMENTED / TESTED / RUNNING / BLOCKED / UNKNOWN. Note conflicts and corrections separately. Never rewrite Phase A.

## C — Structured project map contributions
For each project use fields:
project_key (provisional), names/aliases, purpose, owner, lead_session, source_authority, repos_and_branches, drive_or_local_artifacts, components, completed, pending, dependencies, known_failures, tests_and_evidence, latest_verified_checkpoint_utc, confidentiality, unresolved_conflicts, recommended_next_action.
Provide a claim table with claim_id, evidence_class, source_ref, source_revision, observation_time_utc, confidence, contradicts_claim_ids.
No personal/private details or secret values in public outputs.

## D — Session capability and workflow feedback
Record which tools work, which were unavailable, what files can be read, what writes are permitted, time or format limitations, and improvements to the A25 handoff. Do not infer access from another session.

## E — Delivery
GPT: create NEW `local build operations and recalls/recall-network/inbox-gpt/<SESSION_ID>-REPORT.md` on branch `coord/a25-namespace-trial-001` in `Stratumnova/A25-Training-Workspace`.
Claude: create NEW raw Markdown `<SESSION_ID>-REPORT.md` under existing Drive `A25 AI workshop/workspace/claude-originals/`, without conversion or overwrite. Report Drive URL, ID, size and SHA-256; distinguish source hash from verified readback hash.
If no write tool, return report text to Zed and mark delivery BLOCKED. Never invent a commit, file or link.
Return exact report link and stop. Do not build, restart services, repair, change existing files, modify permissions, merge, or disclose credentials.
