# A25 Recall Network — RN-001
STATUS: PILOT; no production automation, no cross-account authenticated identity.
GOAL: Collect independent recollections and source-verified updates from separate GPT/Claude chat sessions into one versioned A25 project catalog, without forcing shared conversational memory.

## Two storage lanes
GitHub `Stratumnova/A25-Training-Workspace` coordination branch: GPT orders, GPT reports, lead reviews, derived map and indexes.
Google Drive `A25 AI workshop/workspace/claude-originals/`: Claude-authored raw Markdown reports. GPT reads; never edits originals. Zed relays Drive link. GitHub holds references and lead responses.
Do not claim Google Drive provider-enforced seat isolation: both seats use same Google account. Preserve raw bytes/hash readback where possible.

## Protocol
1. Lead assigns each session a unique ID `RN-001-S001`, `RN-001-S002`, etc.; owner Zed chooses who receives orders.
2. Send generic order, plus project scope and reporting destination. Freeze Phase A unassisted recall before looking up evidence.
3. Phase B source verification: exact project names, repo/branch/commit, Drive URL/file ID, local artifact references, statuses and changes since last checkpoint. Mark OBSERVED, SOURCE-VERIFIED, REPORTED, INFERRED, UNKNOWN.
4. GPT sessions create unique report files in `recall-network/inbox-gpt/` on coordination branch. Claude sessions create unique raw Markdown in Drive `claude-originals/` and return URL/ID/hash.
5. Lead fetches, checks evidence, records disagreements as separate claims, then updates `PROJECT-MAP.md` and `SESSION-INDEX.md` additively. No silent authority promotion.
6. Reviews and follow-ups return through GitHub `recall-network/reviews/`, with commit-pinned raw URLs for Claude. Human owner approves access, deployment, destructive operations and main merges.
7. Source freshness: every claim carries observed_at UTC, source revision and scope; historical report never becomes current runtime proof.

## Limits
No secret values, private files, arbitrary phone filesystem access, background sync, unauthorized service changes or main merge. Missing source access is BLOCKED/UNKNOWN, not failure hidden as success. Report COMPLETE only means report submitted, not that tests passed.
