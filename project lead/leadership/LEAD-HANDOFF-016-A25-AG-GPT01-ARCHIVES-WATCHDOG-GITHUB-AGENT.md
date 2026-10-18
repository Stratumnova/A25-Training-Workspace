# LEAD-HANDOFF-016 — A25 Archives, Watchdog and GitHub Agent Lead
Issuer: GPT A25 Project Lead
Owner directive: Zed, 2026-10-17 20:49 MDT (owner supplied)
Assigned seat: A25-AG-GPT01 — Archives & GitHub Automation Lead
Status: ADOPTED delegation of build leadership; implementation and new infrastructure NOT authorized by delegation alone.

## Mission and relationship
Take leadership of the Archives, Watchdog support tooling and GitHub agent/bot build. This seat replaces GPT A25 Project Lead as day-to-day leader **only for this build**. Its deliverables support GPT A25 Project Lead's Pocket Server and Roundtable Communication project, which remains coordinated by GPT A25 Project Lead. Zed is owner and final decision-maker. Watchdog is an owner-controlled oversight function, not a privilege the new agent may impersonate.

## Start with discovery, not reinvention
Inspect current Stratumnova/A25-Training-Workspace branch coord/a25-namespace-trial-001 and relevant existing repositories, archives, coordination reports, Watchdog rules and evidence. Inventory actual capabilities, work-in-progress and constraints; distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED, UNKNOWN. No assumptions that past completion reports mean working code. Preserve originals. Do not invent a new project topology or branch. Consult owner/Lead for authorization before protected modifications, external automations, credential creation, bots with write privileges, repository changes or deployments.

## Overall A25 purpose
Durable source of truth outside GPT/Claude chats; distinct GPT and Claude identities and independent evidence; append-only Roundtable conversation with cursors and recoverability; shared file read then controlled write; eventual authorized terminal operations on owner Android Pocket Server; low/no per-message API cost; cross-AI collaboration and easy fresh-session recovery. Existing official server build: Stratumnova/pockettest branch build/a25-pocket-server-roundtable, owner-approved 2026-10-17 20:02 MDT. NEVER branch from or modify it without specific GPT Pocket Server Lead order and owner-approved scope.

## Build workstreams (proposed; verify existing first)
A. Archive: inventory and index repos, ZIPs, original transcripts, reports and source evidence; record hashes, origin, immutable revisions, duplicate/supersession relations and retrieval paths. Do not silently rewrite source.
B. Watchdog: owner-facing read-only oversight, status and exception reporting, missing evidence, branch drift, report/test claim mismatch, permissions changes and unapproved actions. Escalate, do not autonomously grant approvals.
C. GitHub agent/bot: design least-privilege GitHub App or supported connector-based workflow to fetch/pin sources, create evidence receipts and approved reports, track issues/PRs, and assist recovery. Compare already-installed GitHub connector against new bot requirements before building. No stored personal access tokens in repo, no default broad write privileges, no autonomous merges/deletes.
D. Cross-AI relay: prototype GitHub/Drive exchange with explicit seat attribution, author/publisher separation, byte/hash read-back, idempotent retries, immutable records and cursor recovery. Never claim two-way realtime access without independently testing both clients.

## Authority and boundaries
A25-AG-GPT01 owns planning and routine implementation leadership for its delegated support build, reporting to Zed and coordinating interfaces with GPT A25 Project Lead. It cannot override the owner, change Pocket Server build scope, appoint itself Watchdog, authorize deployments, alter private archive custody rules, or create new repos/branches without Zed approval. Preserve A25 reference evidence rule and separation of seat, principal, author and publisher. Claude review independent, GPT builds, owner decides. Avoid interfering with active Claude02 O007 review.

## Initial deliverable
Produce A25-AG-R001-GPT01-BASELINE-AND-PLAN.md in existing coordination reports folder on coord/a25-namespace-trial-001. Include verified inventory of archive/Watchdog/GitHub-agent components, actual tool capabilities and permissions, candidate existing build location, risks, clear minimal staged plan and explicit decisions requiring owner approval. Do not create implementation branches, deploy, change credentials, or touch phone. Commit report and return full SHA; stop for owner/Lead review.

## Available tools to investigate (2026-10-17 ChatGPT-side discovery)
GitHub and Google Drive connectors installed and used; Plugin Creator installed; Superpowers installed; A25 GPT Terminal available but live operational state unknown. Slack and Vercel are available in catalog but not installed. Claude-side parity, auth and costs UNKNOWN. Reuse existing integrations before designing a custom bot.

## Immediate Pocket Server status
Official branch at fabedb661bb5161055534589c7517f7e0738139d, corrections committed, SDK/ASGI runtime unverified. Claude02 O007 independent re-review in progress. Do not claim it has passed or interfere.
