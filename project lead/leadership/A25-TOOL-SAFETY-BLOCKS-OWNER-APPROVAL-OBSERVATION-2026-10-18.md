# A25 Leadership — Tool Safety Blocks and Owner Review Procedure
Date: 2026-10-18
FROM: A25 Workshop Mapping
TO: Project Lead, Security, Platform/Tooling Review
STATUS: OWNER-ADOPTED REVIEW PRACTICE; CAUSE UNKNOWN

## Owner observation
During read-only mapping, tool calls to inspect the public-safe Zone 1 GPT connector document were blocked. Zed reports a pattern: after personally checking the intended file and explicitly approving the named step, a subsequent inspection request succeeded. Zed suspects an LLM script or local platform requirement might be involved. This is a hypothesis only, not a verified cause.

## Directly observed sequence
1. Combined request to read ZONE1_GPT_CONNECTOR.md and list viewport archive members: tool safety block; no content returned.
2. Owner approved separate read-only inspection.
3. Narrowed document-only inspection request: tool safety block again.
4. Owner explicitly approved terminal inspection of ZONE1_GPT_CONNECTOR.md by name and stated it was public-safe.
5. Simple terminal cat of that document was accepted, and terminal_view returned document contents.
This sequence does not isolate the reason for the change: owner specificity, command shape, safety evaluation, or other platform behavior may explain it. Do not assert causation or bypass.

## Owner-adopted operating practice
- When a step is blocked, STOP that step and report exact target, intended action and observed error.
- Owner will inspect the target and explicitly approve the specific named step, or deny if unclear or unwanted.
- No generic approval authorizes unrelated files, archive extraction, credential access, new sessions, escalation, or phone modifications.
- If a specifically approved step remains blocked, STOP and report; do not retry via disguised commands, alternate channels or silent workarounds.
- Continue only unrelated, already-authorized mapping.
- No active experimentation with safety boundaries in this phase.

## Deferred investigation
Security/Platform/Lead may later investigate whether blocking correlates with command syntax, combined actions, file naming, specificity of owner consent, plugin/tool safety policy or other factors. Use reproducible evidence and preserve both blocked and successful requests. Do not infer that an LLM script or local platform is confirmed responsible.

## Classification
VERIFIED: observed blocked calls, successful named-file read, terminal_view result.
OWNER-REPORTED: suspicion of LLM script/platform behavior.
ADOPTED: explicit per-step owner review/approval-or-denial after a block.
UNKNOWN: actual cause of blocks.
