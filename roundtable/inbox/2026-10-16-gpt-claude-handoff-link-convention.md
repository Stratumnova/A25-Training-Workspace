# A25 GPT → Claude handoff convention (2026-10-16)

**FROM:** GPT — A25 Project Lead
**FOR:** Claude — Independent Reviewer; Zed
**RE:** Copyable raw links and durable GitHub notes
**BASIS:** Zed's explicit instruction on 2026-10-16, following WD-27 review.

## Communication rule
For future Claude handoffs, GPT will:
1. Create a durable GitHub note on the development branch with the actual findings, commit references, validation state, unresolved items, and request to Claude.
2. Provide Zed a direct **copyable, commit-pinned raw.githubusercontent.com URL** for the note, plus source links Claude specifically needs.
3. Keep the user-facing message itself as the reference for the note, with the same facts and conclusions. Do not claim Claude has received it until confirmed.
4. Distinguish GitHub Actions PASS from independent code review and from full enforcement readiness.
5. Announce pushes that trigger GitHub Actions, then report observed results. No main merge without Zed's decision.

## WD-27 status at handoff
- WD-26 failed (3/21 tests) from the W5 regex regression.
- Corrected W5 source at `7442d735e5586bb1ed6c65e77c4750feafaeb2d2` passed GitHub Actions run `39001681428` (Run #28 in screenshot).
- Claude's Drive review `claude-originals/WD-27-claude-code-review-check-py-7442d73.md` (3,384 bytes) independently approves W5, identifies W4 missing push-base wiring, and requests workflow/exemption links.
- `manifests/W3_EXEMPT.txt` already exists with two approved exceptions; Git blob `8fb77033543157ab0e85ddf19a851351698caad4`.
- GPT pushed W4 workflow wiring at `9d356f62e8c5b9c178b2b07520ab22679165b6f7` to pass `A25_WD_BEFORE: ${{ github.event.before }}` to the actual repository validation step.
- The new workflow result was not yet independently confirmed at the time of this note.
- Remaining: verify workflow result; test intermediate bad commit in real CI; decide all-zero first-push base handling; consider WARN for invalid frontmatter; historical F-002 mechanical correction still deferred.
- No merge to main.

## Source links
Workflow: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/9d356f62e8c5b9c178b2b07520ab22679165b6f7/.github/workflows/watchdog-draft-tests.yml
W3 exemptions: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/7442d735e5586bb1ed6c65e77c4750feafaeb2d2/manifests/W3_EXEMPT.txt
W5 source: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/7442d735e5586bb1ed6c65e77c4750feafaeb2d2/watchdog/check.py

## Claude request
Please verify W4 workflow wiring against the pinned workflow file and report whether it satisfies the push-range review requirement. Note any remaining edge cases. No Drive copy or review receipt is assumed.
