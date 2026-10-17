# Stratumnova Archivist — Test Data and Privacy Policy v0

FROM: GPT — A25 Project Lead
FOR: Zed, LB-GPT01, Claude
DATE: 2026-10-17 11:11 MDT
RE: Owner's test-data classification and authorized leak testing
BASIS: Zed's direct instruction on Stratumnova as full build/testing material

## Owner intent
Stratumnova repositories and associated A25 materials form the broader development and testing ecosystem, including public-file mass-upload tests, synthetic private/public separation, fake passwords and fake tokens, leak detection and recovery. Materials may be sensitive **for the builder team** without representing real personal secrets. Existing public Stratumnova material is not automatically confidential solely because it resembles a private record.

## Separate three axes
1. Data class: PUBLIC, TEST-SENSITIVE, TEAM-RESTRICTED, REAL-PRIVATE.
2. Access policy: actor/principal, approved purpose, allowed surface and permitted action. A claimed AI seat or narrative identity is not an authenticated principal.
3. Test authorization: which fixture, test scope and expected exposure are permitted. Deliberate exposure of synthetic values in an isolated test must be distinguishable from an unauthorized leak.

## Handling rules
- PUBLIC: eligible for public repository maps and indexes, with provenance.
- TEST-SENSITIVE: **verified synthetic** fake passwords, fake tokens, mock personal data and simulated restricted records. May be used for controlled leakage and policy tests; mark fixture ID, synthetic verification and test scope.
- TEAM-RESTRICTED: builder-only project material; do not publish to a public repo solely because a team member can read it. Require explicitly approved publication.
- REAL-PRIVATE: actual passwords, API keys, personal exports, sensitive information or material not verified synthetic. Do not upload to public GitHub or expose through retrieval tests.
- UNKNOWN: quarantine from public publication until classified. An owner's broad safety statement does not prove every byte of every ZIP is synthetic.
- Never use fake credentials that accidentally authenticate to real services. Use unmistakable nonfunctional fixtures, e.g. `A25_FAKE_TOKEN_DO_NOT_USE_001`.
- Maintain fixture provenance and expected visibility. A test leak may be intentionally triggered only within an authorized synthetic test scope; log it as expected-test-exposure, not as blanket permission to publish restricted materials.
- Source archives remain authoritative; derived public maps can record safe metadata, verification and test results. ZIPs from local uploads are not automatically authorized for public upload.
- No raw secrets, real personal data or private conversation exports in public A25. No changes to Watchdog or protected files without separate approval.

## Initial acceptance tests
1. PUBLIC record is retrievable by public actor.
2. TEST-SENSITIVE fake token is withheld from unauthorized normal retrieval.
3. Authorized isolated leak test detects the synthetic token in an intentionally vulnerable fixture.
4. TEAM-RESTRICTED metadata can be discovered only as policy permits; content cannot be read by unauthorized actor.
5. UNKNOWN and REAL-PRIVATE content denied by default.
6. Source revision/hash conflicts and attempted cross-identity authorization are recorded and flagged.
7. Mass-upload sample rejects or quarantines records lacking validated classification.

## Scope
Policy document only. Does not claim these controls are implemented, that Watchdog is integrated, or that uploaded archives have been fully classified. The builder must validate actual contents before publishing.
