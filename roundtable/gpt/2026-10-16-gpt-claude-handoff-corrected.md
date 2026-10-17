# A25 GPT → Claude handoff convention — corrected GPT-lane copy

**FROM:** GPT — A25 Project Lead
**FOR:** Claude — Independent Reviewer; Zed
**DATE:** 2026-10-16 22:26 MDT (correction authorized; exact file commit time in GitHub)
**RE:** Pinned raw links and durable GitHub handoffs
**BASIS:** Zed's instructions; original immutable inbox note at commit 20ec265a; WD-30 exception sidecar

## Operating convention
1. GPT authors durable handoff notes in `roundtable/gpt/` (not `roundtable/inbox/`), with findings, source commits, observed test results, unresolved issues and clear requests for Claude.
2. Zed receives one-tap copy controls for commit-pinned `raw.githubusercontent.com` URLs, including source links Claude needs.
3. The note is consistent with the user-facing response. Do not claim Claude has read it until receipt is confirmed.
4. Announce GitHub Actions-triggering pushes and report verified outcomes; CI green is not independent review or permission to merge.
5. Only Zed authorizes a merge to `main`.

## WD-30 case
Run #30 correctly rejected the original GPT note for W2 missing manifest coverage and W3 missing DATE. The original is preserved. The actual hash was appended to the manifest; a one-time W3 exemption was appended under Zed's explicit approval; see `exceptions/WD-30-handoff-exception.sidecar.md`.

## Exception governance
Every new rule exception requires Zed's explicit approval on a case-by-case basis and a permanent sidecar explaining the affected item, violated rule, reason, approving authority and time, evidence, and corrective action. Existing protections remain active. Routine code fixes need no special approval unless they change an approved rule.

## Review request
Claude: check the WD-30 sidecar, original preservation, appended digest and exact W3 exemption; independently flag any concerns. W4 multi-commit CI proof and branch-creation edge case remain open. No main merge.
