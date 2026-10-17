# A25 Builder Training — Working Rules, Handoffs and Exception Authority (2026-10-16)

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and invited future builders
**DATE:** 2026-10-16 (training revision after Zed's 22:56 MDT instruction)
**RE:** Operational training for A25 and future projects
**BASIS:** Zed's directions at 22:26, 22:29, 22:43, 22:52 and 22:56 MDT; Claude's WD-30 and WD-35 reviews; observed GitHub Actions results. This is a new training document, not a rewrite of protected evidence.

## Seats and authority
- **Zed:** human owner and relay; sees exception proposals and agreements, can intervene and stop or change the action. Explicitly approved the current WD-35 baseline restoration at 22:43.
- **GPT:** A25 project lead, GitHub writer, implementation and evidence/report author. Announce every Actions-triggering push and verify its result. Do not silently modify approved records.
- **Claude:** independent reviewer, Drive writer; checks design, evidence, source code and actual results independently. Disagreement is preserved and escalated to Zed.
- **Invited builders:** scoped tasks only; no authority to self-approve Watchdog exceptions, impersonate permanent seats or merge to main.
- **GitHub:** source, code, commits, training and durable development evidence. **Drive:** Claude originals, independent reviews, cold copies. **Pocket Server:** future authoritative shared messaging/workspace after it is implemented and verified, not current live authority.

## Decision and exception workflow
1. GPT prepares a proposed change and concise impact report: file paths, rules affected, reason, evidence, before/after hashes when relevant, rollback/recovery, tests, and individual sidecar for any exception.
2. Claude independently reviews and explicitly says AGREE or DISAGREE. If disagreement, present both positions to Zed; no implicit approval.
3. **For Watchdog exceptions:** use a conspicuous line `EXCEPTION — GPT and Claude AGREE: <rule> on <file>`. Zed's 22:52 MDT direction states that when Zed relays both seats' agreement without intervening, the relay is Zed's pass-through authorization. If Zed intervenes, stop and resolve. Record the exact words and provenance; do not manufacture approval from silence or an unrelayed discussion.
4. Ordinary code/tests/docs work does not require exception approval merely because CI is red; follow the agreed review process. Do not use an exception to hide an ordinary fix.
5. After authorized push, GPT announces Actions, checks logs, records PASS/FAIL/WARN and actual scope. Green isolated tests do not certify repository validation, independent review or main merge.
6. No merge to `main` without Zed's decision. Protected history is append-only by default; no silent deletion or rewrite.

## Mandatory exception sidecar
One sidecar per flagged item for which a rule-breaking exception is authorized. Include: original path, rule(s), exact reason, evidence/run link, original and resulting digests where applicable, authorization basis with verbatim Zed wording or verified pass-through, who proposed/reviewed, correction/manifest pointers, implementation commit(s), and final CI status. **An AI-authored sidecar is evidence, not the approval credential.** Ordinary W2 coverage repairs should be distinguished from W3/W4 exceptions.

## Communication and handoffs
- Outgoing GPT records belong in `roundtable/gpt/`; `roundtable/inbox/` is for received seat messages, not GPT-authored notes.
- GPT writes the full durable note, then gives Zed a one-tap **Copy** control for the exact commit-pinned raw GitHub URL. Zed relays to Claude. Do not claim Claude read it until independently confirmed.
- Use **FROM / FOR / DATE / RE / BASIS** and separate OBSERVED, human-attested, proposed, and unverified statements. Preserve original wording when quoting authorization. A Git blob hash is not a SHA-256 digest.
- Claude's Drive review remains independently authored; preserve differences rather than silently harmonizing accounts.
- For future project handoffs include scope, branch/commit, known-green baseline, active failures, protected assets, source map, review decisions, evidence links, open questions, authorized next steps and explicit non-certifications.
- Do not paste secrets, tokens, signing keys, or private codes into AI chat or public GitHub.

## Watchdog interpretation
- W1 manifest hashes and formatting; W2 protected-file coverage; W3 message headers and exact approved exemptions; W4 protected-history and append-only manifest rules across the full pushed commit range; W5 canonical ID ownership/collisions; W6 workflow read-only permissions and no secrets.
- Run #30 correctly rejected a GPT-created inbox note for missing manifest coverage and DATE. This is a training case, not proof the system is broken. The note remains; Zed approved the one-time W3 exemption, and a sidecar documents it.
- WD-35: the baseline manifest was accidentally appended without a separating newline. `manifests/ADDITIONS.sha256` now covers the new protected note. The baseline remains corrupted pending narrowly scoped W4 restoration, already approved by Zed. Do not report this as repaired until actual CI confirms it.
- The current baseline was originally installed without a final LF. Future new manifests should end in LF; the historical baseline exception needs explicit treatment in code/review.
- The approved future authorization concept uses a **Zed-owned device/app/terminal** and a locally unlocked signing key; the server shows computed path, rule, digest and diff, while CI verifies a scoped signature. Add nonce, expiry, revocation and replay protection. **Design only, not deployed.** Never ask Zed to enter a code into AI chat.

## Builder release gates
- Record all Actions failures, not just green runs. Investigate the actual failing job logs.
- Every Actions-triggering push is announced; every conclusion is verified, not guessed.
- Preserve frozen baselines and immutable source evidence; separate post-baseline additions from baseline snapshots.
- An exception must never silently expand to other paths, rules, digests or commits.
- Require independent Claude review for exception mechanisms and final source links.
- If there is a red run, explain whether it is an expected intermediate state or a new regression; do not call a draft test suite a production gate.

## Open work
WD-35 exact-byte restoration and W4 digest-bound fixtures; W1 LF check with documented historical treatment; W4 push-range edge-case testing; W6 review; Claude verification of resulting CI; Pocket Server authorization implementation deferred. This document is training guidance, not a claim that those items are complete.
