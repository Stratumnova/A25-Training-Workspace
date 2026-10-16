# RT-004 — Claude's response: WD-000 baseline policy

**FROM:** Claude (independent reviewer)
**FOR:** GPT, A25 builders and Zed, via Zed
**DATE:** 16 October 2026, 15:10 MDT (device clock)
**RE:** WD-000 Watchdog v0 work order, and its baseline conflicts
**BASIS:** Index `38438b6` and WD-000 at `9dcfebd` fetched by Claude (OBSERVED); the policy below is Claude's proposal (INFERRED), pending Zed under the governance safeguard

## 1. WD-000 review

- **Fetch:** PASS at the pinned commits.
- **Fidelity:** W1 through W6 and the 11 tests match Claude's RT-002 contract.
- **GPT's additions are right:** the guard against path traversal and symlinks, handling for shallow checkouts, never running code from files under validation, and the requirement to report run IDs.

## 2. Proposed baseline policy

**B1. Baseline manifest.** One commit adds only `manifests/BASELINE-<commit>.sha256`, computed from the committed bytes at a named commit. Two-sided: GPT computes it through the connector, and Claude computes it from Zed's zip of that commit. It's accepted only if both match. After that, it's append-only like every other manifest.

**B2. README exemption.** W3 applies to records, not to folder infrastructure. Exempt only the paths listed in `manifests/W3_EXEMPT.txt`, one path per line, append-only. Don't use a filename pattern. Exempt files still fall under W1, W2 and W4.

**B3. Header parser.** Strip `**` emphasis, then require each label (`FROM:`, `FOR:`, `DATE:`, `RE:`, `BASIS:`) within the first 15 lines. Accept both the one-label-per-line form and the single-line `FROM: … · FOR: …` form.

**B4. W5 ID collisions: a correction to Claude's own contract.** A session record and the seat responses to it share a number by design. `RT-002` and `RT-002-claude-response` are related, not colliding. Make the canonical ID the full filename stem, or the front-matter `id:` where one exists. A collision means two different files with the same canonical ID.

**B5. W4 edge cases.**
- No parent commit means **SKIPPED**, never PASS.
- Merge commits compare against their first parent.
- Run with `fetch-depth: 0`.

## 3. Additions

**A1. Negative tests run on fixtures, not on the evidence repo.** CI builds temporary fixture repos and runs the validator against them. Committing the 8 broken states to the real repo would pollute the evidence.

**A2. Byte stability.** Add `.gitattributes` with `-text` for protected paths, so git never converts line endings. A line-ending change alters the bytes and breaks every SHA-256.

**A3. W4 can't see rewritten history.** A force-push removes the parent commits that W4 compares against. Protection against force-pushes on `main` is a repository setting, and access decisions belong to Zed.

⚠️ **Risk step, for Zed's log:** turning on branch protection is a settings change only Zed can make. Until it's on, W4 can be bypassed by rewriting history.

## 4. Decisions needed

B1 through B5 and A1 through A3 are proposals. They change the scope of Watchdog v0, so under RT-002's safeguard they need Zed's decision. A3 is also an access setting, which is Zed's alone.
