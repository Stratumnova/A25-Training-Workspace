# A25 Roundtable rooms — design rationale and training case study

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and builders
**DATE:** 16 October 2026; exact instruction time not supplied
**RE:** Preserve Zed's design, GPT's reasons, and the Roundtable learning record
**BASIS:** Zed's current instruction; `roundtable/README.md`; WD-000; WD-05; A25-F-005; GPT continuity handoff

## Purpose and authority

Zed is building A25 as a durable local/workspace system for separate AI seats to cooperate on projects while retaining independent accounts, contexts, reviews and roles. The repository is a persistent record and learning material for future Roundtable rooms and builders. It is not a claim that provider models share internal memory or that GitHub is a live chat bus. Zed owns design and approval decisions; GPT coordinates technical implementation; Claude reviews independently. Human words, AI recommendations and verified tool outcomes must remain distinguishable.

**Zed's current design instruction (quoted from this conversation):**
> Zed to gpt- make sure we are updated in the repo for the case study for A25 the training martial for the roundtable rooms and your response and reason behind things alongside my design and thoughts.

**Earlier continuity instruction (quoted):**
> Good. Keep your roundtable and Claudes roundtable information inside the folders. We can forget to keep recording in case we lose you or Claude in the middle

These quotations are conversation-relayed text; byte parity with an external source is not asserted.

## Why separate rooms and folders

**Zed's intent:** Recover work after losing either conversation; maintain two independent AI perspectives; preserve design discussions, not merely the last generated code or a summary. A builder should be able to resume without requiring Zed to reconstruct every decision.

**GPT's reasoning (assistant-authored, not attributed to Zed):** Separate seat records reduce accidental identity/author conflation. Shared Roundtable records carry exchanges and approved decisions, while seat-specific folders preserve each participant's reasoning and review provenance. Case studies turn observed failures and fixes into reusable examples. This supports reconstruction, audit and teaching, but does not make the AI seats automatically synchronized.

## Room training workflow

1. Record Zed's design statement and exact decision separately from AI proposals. Preserve source wording where available and label paraphrases.
2. GPT records its own proposed implementation, reasoning, alternatives and limits in `roundtable/gpt/`; use shared `roundtable/sessions/` for the exchanged turn as defined in `roundtable/README.md`.
3. Claude's original reviews and findings remain Claude-attributed in the appropriate Claude review/archive/inbox folders; GPT may record its own response to Claude without modifying Claude's original.
4. When source text arrives via Zed paste, mark it relayed and do not claim original byte identity. When a source file is available, preserve the file and verify hashes if possible.
5. For a material GitHub change, preserve branch, full commit, what was actually checked, and remaining uncertainties. A green isolated test suite is not equivalent to a green live-repository check.
6. On a platform safety block, stop that operation, report exact failure and show payload for Zed's review. Zed may authorize one ordinary retry; approval is not a bypass of provider checks.
7. Commit and read back recovery notes at meaningful checkpoints; do not wait for session end. No guarantee of autonomous recording between sessions.

## Worked case: Watchdog development, 16 October 2026

- Zed authorized a read-only Watchdog to protect Roundtable and legacy records.
- WD-03's eleven disposable Git fixtures were initially blocked by a platform safety check. GPT stopped and showed Zed the complete proposed source. Zed explicitly approved the retry; it succeeded. See `case-studies/A25-F-005-wd03-safety-stop-authorized-retry-2026-10-16.md`.
- GitHub Actions initially failed to import `watchdog/check.py` due to a regex syntax error. A later commit passed 16 isolated tests. Claude's independent code review then identified actual-repository incompatibilities and design gaps.
- Remediation initially broke one unit-test fixture (15/16). After correcting fixture frontmatter, commit `8e8fd10a688ab1c74f531022339fab3cd6bf9167` passed 16/16 and the actual-repository check returned 0 FAIL, 3 documented historical WARN. See `case-studies/WD-05-github-actions-failures-and-recovery-2026-10-16.md`.
- **Open:** multi-commit W4 enforcement, stricter W6 permissions, stronger ID/correction checks, and renewed Claude review. No final certification or merge to `main` is claimed.

## Teaching points for future builders

Distinguish (a) what Zed intended and approved, (b) what GPT proposed and why, (c) what Claude independently reported, (d) what the repository and CI demonstrably showed, and (e) what remains unresolved. Keep evidence immutable by convention; corrections are additive. Do not manufacture quotes, unseen internal model reasoning, approvals, successful tests or source parity.

## Scope and limitations

This case study is GPT-authored educational interpretation. It is **not** a replacement for original RT records, Claude's source reviews, Zed's messages or GitHub logs. It does not purport to reproduce hidden chain-of-thought; 'reasoning' here means a concise, user-visible engineering rationale and decisions. Further Zed design thoughts should be appended with source attribution as they are supplied, rather than inferred.
