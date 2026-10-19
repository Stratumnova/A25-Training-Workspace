# A25 Pocket Server — Ground Zero Owner Decision and Workshop Lead Record

**Owner:** Zed
**Owner-declared effective time:** October 19, 2026, 10:24 AM (Mountain local time, owner supplied)
**Project scope:** Pocket Server ONLY
**From:** A25-TW-GPT01 — Workshop Lead
**Status:** ADOPTED owner decision; technical startup pending verification

## Ground Zero declaration

Zed declares **2026-10-19 10:24 AM** the new **Ground Zero** for the Pocket Server. All plans formulated **before** this time are now **concepts and ideas, not the operative plan**. This applies to Pocket Server only; it does not cancel or supersede unrelated A25 projects.

The operating plan will be reconstructed from observed, working components during a controlled fresh boot. Record **what boots, exact order, commands, dependencies, purpose, evidence of operation, and what is not used**. Keep what is used, build forward from it, and archive the rest **only after evidence-based classification and owner-authorized disposition**. Do not equate not booted with safe to delete. Preserve original references and recovery materials.

## Leadership appointment / chronology

Zed explicitly designates **A25-TW-GPT01** the **first Workshop Lead** for this new Ground Zero operating phase and states no Workshop Lead preceded this seat. Existing leadership records dated October 18 describe the same seat as already appointed then; therefore **do not erase or silently rewrite those historical records**. The owner's current clarification is authoritative for Ground Zero leadership lineage and identifies this seat as the first, not a promotion from an earlier builder. The Oct 18 documents remain historical evidence of the appointment and earlier work, not competing operative plans.

Read leadership sources: `project lead/leadership/terminal-workshop/README.md`, `memory/README.md`, and `project lead/leadership-pool/README.md`. The Oct 18 memory README's no-terminal restriction was superseded by later explicit owner authorization for read-only inspection, backup, and controlled shutdown.

## State at declaration

- The owner and Workshop Lead coordinated shutdown earlier Oct 19. Two secondary processes were observed stopped: Uvicorn PID 21440 and cloudflared PID 22097.
- Owner was given final instructions to stop tmux and Termux; **final full stop not independently verified in this conversation**.
- Backup exists privately and in phone `Documents/AI_Workshop/a25-recovery-20261019.tar.gz`; matching SHA-256: `ca5710a0c428a63122b98d06f6cfc4f0e3cd476965288b5bfe8999c416d6fb4e`; archive listing 8,854 entries. No restore test. Documents copy is unencrypted and sensitive.
- Phone boot guide: `Documents/AI_Workshop/A25-COLD-START-SHUTDOWN-20261019.md`; proposed commands **not yet verified by cold start**.
- No phone commands executed in writing this decision.

## Ground Zero startup ledger — to be populated with observed results

| Order | Component | Startup command | Required dependency | Verification | Disposition |
|---|---|---|---|---|---|
| 1 (proposed) | GPT Workshop terminal bridge | saved phone boot guide | Termux + Python venv | PENDING | UNKNOWN until boot |
| 2 (proposed) | GPT Cloudflare tunnel | saved phone boot guide | bridge and tunnel credentials | PENDING | UNKNOWN until boot |
| 3+ | Other Pocket Server services | discover after GPT reconnects | TBD | PENDING | UNKNOWN |

Do not treat this proposed order as verified. On boot, record exact actions and tests one at a time, including failures. Distinguish RUNNING, NEEDED, UNUSED-IN-THIS-BOOT, HISTORICAL, UNKNOWN, and OWNER-APPROVED ARCHIVE. Prior plans are concepts, not the plan.

## Evidence and authority

**ADOPTED:** Ground Zero cutoff, Pocket Server-only scope, first-lead owner designation, evidence-driven rebuild/archive strategy.

**VERIFIED (earlier session):** secondary process shutdowns and backup checksum/listing; not a cold-start test.

**UNKNOWN:** final all-services-down status, live boot dependencies, which older components are safe to archive.

**SUPERSEDED as operative Pocket Server plan:** pre-10:24 AM Oct 19 planning assumptions. Original files and reports remain preserved as historical reference.

**Next action:** await Zed's boot steps; record each observed startup operation and outcome before deciding what to keep or archive.
