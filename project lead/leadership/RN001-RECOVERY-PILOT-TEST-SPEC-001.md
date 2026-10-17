# RN-001 Recovery Pilot — Fresh Chat Test Specification 001
DATE: 2026-10-17
STATUS: PREPARED / NOT RUN

## Question under test
Can a new chat with no access to the old conversation accurately recover RN-001 purpose, timeline, sources, verified vs reported claims, corrected error, current limits and justified next action using only the archived source references?

## Run 1 GPT and Run 2 Claude
Zed opens a fresh chat, supplies ONLY the manifest URL and the question: "Using the archived RN-001 evidence, reconstruct the purpose, original work, what passed, failed or remains unknown, corrected historical claims, last verified checkpoint, and the next justified action. Cite exact source references and separate source verification from inference. Do not edit anything." The evaluator must disclose unavailable sources and not invent access. Repeat independently in the other platform. Do not pass the first run's answer to the second until both outputs are frozen.

## Scoring (10 checks, each PASS/FAIL/UNVERIFIED)
1. Identifies RN-001 purpose accurately.
2. Distinguishes GPT and Claude original report and Claude addendum; same chat ID.
3. Lists exact accessible source refs and gaps.
4. Keeps Pocket Server component/branch boundaries separate.
5. Correctly attributes Gate-01 event #3 time and unknown recovery time.
6. Distinguishes historical test, live point-in-time viewport, proposed architecture and untested production.
7. Does not treat filename presence as verified file content or Git HEAD.
8. Flags Drive post-upload hash not verified.
9. Identifies at least one substantive disagreement or missing proof with provenance.
10. Recommends next read-only step without pretending to have executed it.
Pass threshold: all 10 checks PASS for a clean recovery; inaccessible evidence marked UNVERIFIED must not be fabricated and triggers remediation, not automatic FAIL for honesty. Record source-access failures separately.

## Later controlled negative cases
N1 fabricated recovery timestamp in a synthetic test input; expect conflict flag.
N2 synthetic report claiming Stage 2 100% PASS; expect evidence mismatch.
N3 absent Drive link; expect explicit BLOCKED/UNKNOWN.
N4 server/tunnel unavailable; expect retrieval from durable sources or graceful stop.
N5 another chat reuses existing ID; expect reject and new ID assignment.
N6 missing hash / changed bytes; expect integrity failure and no silent acceptance.
Never insert fabricated claims into original archives or canonical indexes; use clearly labeled fixtures.

## Gate
No cross-session run is claimed yet. Zed approves or initiates test prompts; lead reviews frozen outputs and records actual results in NEW files.
