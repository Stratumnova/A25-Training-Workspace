# LEAD-STUDY-022 — Handoff Session Study Notes
Recorded: 2026-10-17 21:24 MDT, requested by Zed.
Audience: Future A25 leads, GPT/Claude reviewers, Roundtable training and Watchdog evidence studies.
Status: STUDY MATERIAL, not new authorization or test certification.

## Case A: contradictory builder order
O003 directed implementation but prohibited edits to protected main and creation of a branch, leaving no authorized code destination. GPT01 correctly stopped and reported BLOCKED (R002 commit 9ac5eed4a9a1f5f11efd1a19a78db6204a95ba97). Lead inspected existing branches; owner approved a single official build branch at 20:02 MDT. Lesson: an instruction to build does not implicitly authorize a destination; explicitly document where, why, when, for whom, and who approved it.

## Case B: independent review changes acceptance
GPT01 committed shared read O004 (442529a...) but could not execute MCP tests. Claude02's R001 reported independent isolated tests, identified non-discriminating symlink test, provider-object-only deny-all test, local anonymous proxy/tunnel exposure, and remote-access gap. Lead adopted findings as issues, not proof that SDK runtime works. O006 corrections committed (fabedb...), still zero executed MCP integration tests. Lesson: distinguish source presence, isolated test results, SDK integration and deployment. Preserve GPT/Claude disagreement and reproduce with original code.

## Case C: writer is not reviewer
Claude Writer A25-CW-CLAUDE01 published O005 handoff to Drive (ID 1cro418zgfdk6o8YMhDfFZaZ6fyREE67o), reported read-back 2446 bytes and SHA256 003313ff9e3cc4bca4d89a188a8645b8d73e3cf5d57d3dfdc9d24d1deb22543c. Lead fetched text independently, not exact hash. Writer's own instructions remained in published document; lead clarified they were historical publisher directions, not reviewer instructions. Lesson: distinguish document author, publisher, reviewer, authenticated principal, and owner; preserve literal records and clarify scope separately.

## Case D: builder continuity before reassignment
Archives Lead found namespace O001–O004 checkpoint but no verified exact-commit CI run. Owner confirmed existing LB-GPT01 chat is the original builder, not replacement. Lead recorded continuity requirement (Addendum 020). Lesson: capture ephemeral session-local evidence before changing work assignments; then compare against pinned original source. Memory alone is historical claim.

## Case E: screenshots and ownership
Owner showed actual chat-session names for GPT and Claude projects. Lead recorded map 019 without renaming chats or altering Claude's deliberately worded top statement: "Gpt is the leader and Zed is the watchdog/courier". Owner controls information exchange and approval; GPT has delegated technical leadership. Lesson: project UI labels establish an observed workspace map, not authenticated identity, connector access, or live cross-AI communication.

## Study checklist for future handoffs
- Is owner authorization explicit, dated, scoped and separate from lead delegation?
- Are repo, branch, pinned commit, exact path and permitted edit operations specified?
- Are REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN separated?
- Are tests identified by actual executed command, environment, source bytes, and outcome?
- Are independent reviewers given originals, not just prior conclusions?
- Are author, reviewer, publisher, seat and principal separate?
- Is the existing session's local history captured before reassignment?
- Are originals preserved and reports append-only?
- Are deployment, remote exposure, credentials and protected files outside scope unless separately approved?
- Can a fresh lead resume from the latest durable record without inventing completion?

## Open exercises
1. Reproduce O006 tests with pinned MCP dependencies and ASGI client; report exact results, not expected results.
2. Determine safe controlled remote access for two independent AI identities without anonymous public read.
3. Execute namespace prototype exact-commit tests/CI and reconcile Case Study 001 with R004 chronology.
4. Test five-message GitHub/Drive relay with author/publisher distinction, retries, cursors and fresh-session recovery.
5. Test Watchdog evidence consumption without permitting the bot to self-approve.

## Source pointers
LEAD-HANDOFF-021 companion; LEAD-PROJECT-MAP-019; LEAD-ADDENDUM-020; GPT R002/R003/R004; Claude02 R001 Drive ID 13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl; O007 review order. These are starting pointers: consult originals before accepting technical claims.
