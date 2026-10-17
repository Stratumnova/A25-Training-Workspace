# WD-30 exception sidecar — GPT handoff inbox note

**FROM:** GPT — A25 Project Lead
**FOR:** Zed; Claude — Independent Reviewer
**DATE:** 2026-10-16 22:26 MDT (approval time stated by Zed)
**RE:** One-time W2/W3 remediation and authorized W3 exception
**BASIS:** GitHub Actions run #30 logs; Zed's explicit approval at 22:26 MDT; Claude's proposal

- **Affected original (immutable):** `roundtable/inbox/2026-10-16-gpt-claude-handoff-link-convention.md`
- **Original commit:** `20ec265a6766b77f6d9ba0bd52de7ff3bf27a32e`
- **Original SHA-256 (UTF-8 bytes):** `74c55aebce2845d9a25f39850463cf4c40570e09fac7d783bfc95fbacb63e53a`
- **Failure evidence:** Run #30, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39001992709 — W2 unmanifested and W3 missing DATE.
- **Why rule was broken:** GPT mistakenly committed an outgoing handoff convention note to protected inbound Roundtable inbox, without first appending its digest or including DATE. This was an error, not an emergency or planned exception.
- **W2 resolution:** Append a line for the actual original bytes to `manifests/BASELINE-c498e84.sha256`; never alter the original.
- **W3 exception:** Zed approved preserving this one missing-DATE note at 22:26 MDT on 2026-10-16; append exact-path reason to `manifests/W3_EXEMPT.txt`. The exemption acknowledges a violation; it does not rewrite history.
- **Corrected GPT-lane copy:** `roundtable/gpt/2026-10-16-gpt-claude-handoff-corrected.md`.
- **Authority:** Zed expressly approved this one exception and a standing rule: every NEW exemption requires Zed's explicit case-by-case approval. Zed additionally required an explanatory sidecar for each item whose Watchdog rule is broken and exception authorized.
- **Generalization:** New exemptions must have original path, rule, reason, approval and timestamp, immutable evidence, correction pointer, and an individual sidecar. An AI may propose but not self-approve a new exemption.
- **Limit:** This is a one-time W3 exception only; W2 was repaired through the normal append-only manifest mechanism. Do not treat this as blanket permission for future violations.
