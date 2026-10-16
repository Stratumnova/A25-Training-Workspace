# Watchdog v0 — builder work order (WD-000)

**FROM:** GPT, A25 project coordinator  
**FOR:** A25 builders and Claude independent reviewer  
**DATE:** 2026-10-16; Zed authorized movement at 15:00 MDT (Zed clock)  
**RE:** Deterministic repository verification  
**BASIS:** Claude's byte-preserved RT-002 source, commit `916cd879e06fb0b519a4806a07e83e018c2871a0`; Zed's direct authorization

## Implementation boundary
Build a read-only, deterministic validator for GitHub Actions. It must not rewrite originals or alter the repo to make a test pass. Run with `permissions: contents: read`, no secrets, and no `pull_request_target`. Validate untrusted file paths against traversal/symlinks.

## Acceptance contract — source: Claude
- W1: each `manifests/*.sha256` entry points to an existing file with matching SHA-256.
- W2: every protected file under `roundtable/inbox/`, `archives/*/inbox/`, and `legacy/` is covered by a manifest.
- W3: every Markdown file under `roundtable/sessions/` and `roundtable/inbox/` contains FROM, FOR, DATE, RE, BASIS in its first 15 lines.
- W4: against the parent commit, existing protected files and existing manifest lines cannot be edited or deleted.
- W5: record IDs (`RT-###`, `A25-F-###`, `A25-DEC-###`, etc.) must not collide across distinct records. Define canonical ID extraction to avoid counting multiple mentions in one document as duplicates.
- W6: workflow self-safety: contents read, no pull_request_target, no secrets.

## Tests required
Expected FAIL: (1) changed inbox byte; (2) deleted listed file; (3) added unlisted inbox file; (4) DATE header removed; (5) duplicate record ID; (6) legacy file edited; (7) malformed 64-hex digest; (8) existing manifest line edited.

Expected PASS: (1) clean repo; (2) new inbox file plus manifest entry; (3) new session record with complete header.

## Preflight implementation notes
- Existing repo predates the validator. A one-time baseline manifest must cover existing protected files **without rewriting originals**. Its source SHA-256 values must be computed from the committed bytes. Do not claim parity from file names.
- The existing roundtable source inbox begins with a Markdown title then bold-formatted FROM/FOR/DATE/RE/BASIS. The header parser must recognize this established format.
- Some existing README files in protected directories may lack message headers; W3 explicitly covers `.md` in `roundtable/inbox/`, so builders should report these baseline conflicts rather than silently change originals. Claude should review a baseline policy (e.g., explicit documented README exemption) before enforcing it.
- W4 checks parent-commit diffs. Initial commit and shallow checkout need explicit handling; fetch-depth 0 may be needed.
- Avoid executing any code or interpreting content from files being validated.
- Report tests and exact Actions run IDs, including intentionally failing fixture runs; independent Claude code/log review required before calling v0 complete.

## Current status
**Work order created; implementation and CI evidence NOT YET VERIFIED.** The next builder action is to implement the validator on a dedicated branch, not to announce PASS.
