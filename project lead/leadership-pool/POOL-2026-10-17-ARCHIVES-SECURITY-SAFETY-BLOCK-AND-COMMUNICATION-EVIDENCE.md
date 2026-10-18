# POOL — Security Review Candidate and AI Communication Evidence
FROM: A25-AG-GPT01 — Archives Lead
FOR: Future Security Lead (RESERVED, not yet appointed); Roundtable Lead; Zed
DATE: 2026-10-17 (project record label)
STATUS: REFERENCE / OPEN SECURITY QUESTION; NO TECHNICAL FINDING ADOPTED
OWNER: Zed assigns future Security investigation; Archives preserves sources
SCOPE: Cross-lead handoff only, not an instruction to modify tools or bypass controls
SOURCES:
- Archives procedure: `project lead/leadership/archives/ARC-NOTE-2026-10-17-002-GITHUB-BLOCKED-WRITE-OWNER-REVIEW.md` commit `d584710cf01349cd3d93dd542500c78276b8d953`
- Archives receipt: `project lead/leadership/archives/ARC-REVIEW-2026-10-17-001-ROUNDTABLE-P0-PRESERVATION-RECEIPT.md` commit `b0e476e5f4927268738f19b0249769c75e8b1046`
- Roundtable inventory: `project lead/leadership/roundtable/RT-TRAINING-2026-10-17-001-CONTEXT-AND-RECALL-INVENTORY.md` commit `d626ebde4ba83baa4de3406c4cbeb7619fc11e21`
- Roundtable emergency handoff: `project lead/leadership/roundtable/RT-HANDOFF-2026-10-17-002-EMERGENCY-SESSION-EXTRACTION.md` commit `f9a3fc912d15d1900b150b166cb56d2e371622df`

## A. Safety-block attribution is UNKNOWN
Zed points out that the generic safety block encountered while using the GPT-to-GitHub tool may originate from GPT/tool safety enforcement rather than GitHub itself, and may relate to the content or nature of the submitted file. This is a **hypothesis, not a verified cause**. Archives previously described the failure as a GitHub upload block; that describes the action that failed, not the source of enforcement.

Observed in Archives session: a Markdown create-file attempt returned a generic OpenAI safety-check block, without a GitHub commit. The exact file was shown to Zed 1:1; Zed explicitly approved a retry and permitted a .txt fallback; the unchanged Markdown retry returned commit `b0e476e5f4927268738f19b0249769c75e8b1046`. No .txt attempt was needed. This single observation cannot establish a root cause, general retry success rate or a way around platform controls.

For future Security Lead: review authorized tool-layer diagnostics and distinguish GPT policy/tool enforcement, connector gateway behavior and GitHub API rejection. Evaluate whether content category, request shape, transient errors or other factors could account for differing outcomes. Test only with approved harmless fixtures and Zed authorization; do not use extension changes or retries to circumvent safety enforcement. If a platform denies an action, preserve the exact error and STOP. This is **deferred to Security**, not Archives implementation work.

## B. Roundtable holds communication/workaround history — archival intake priority
Roundtable's original active session recorded how Zed, GPT and Claude passed material across otherwise separate systems:
- GPT ⇄ GitHub connector for branch/source fetches, orders, reports and commits;
- Claude ⇄ Google Drive for raw Markdown writer/reviewer handoffs, with Zed acting as courier;
- Zed's Android/Termux terminal, tmux/read-only fixed viewport and tunnel experiments as separate historical channels, NOT proof of authenticated remote shared MCP or current phone state.
- The observed gaps: source tree listing vs full fetch; GitHub connector source retrieval vs executable-container byte-exact test access; Claude GitHub reservation enumeration limitations; Drive text readback vs independently recomputed byte hash; historical phone commands vs observed terminal output; safety-stop and approved retry; authorization conflicts and distinct AI seat identities.
- Preserve successes and failures with original order, error, attempted workaround, approval, resulting commit/Drive ID, and verification boundary. Distinguish proposed fixes from verified results; do not turn historical transport proofs into live Roundtable server PASS.

Primary source pointers: `project lead/leadership/LEAD-TRAINING-NOTE-008-ROUNDTABLE-LIVE-WORKFLOW-OBSERVATIONS.md` (commit `627ae1198ae27bdde70086361da441f2bb6257be`), `LEAD-TRAINING-NOTE-012-CLAUDE-WRITER-FIRST-PUBLISH-VERIFICATION.md` (`587ad3bfbf6fdf28f568e6f848328975ec36079e`), `LEAD-STUDY-022-HANDOFF-EVIDENCE-LESSONS-2026-10-17.md` (`087dc1d3105bb716546788d90dd18dbd343b8436`), `LEAD-HANDOFF-021-ROUNDTABLE-ARCHIVES-SESSION-2026-10-17.md` (`a719151678137d77334636a702ff075c45c16a1c`), and the two Roundtable records above. These are evidence pointers; the present note does not independently reproduce every historical exchange.

## C. Ownership and next action
Archives: index and cross-link the communication paths, failures, approvals, and recovery lessons as provenance/training material, preserving originals. Roundtable successor: use the handoff to recover communication ownership and identify any unrecorded cases; no need to re-task exhausted old session. Security Lead when appointed: separately investigate the safety-block attribution and authorized testing. Zed decides adoption and any cross-team policy changes. No server, phone, GitHub security configuration, or existing historical source files modified by this note.
