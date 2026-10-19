# A25 Workshop — Mapping and Blocker Escalation Rule
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Archives, Claude, builders, security pool
STATUS: ADOPTED owner directive

Continue bounded read-only phone/Termux mapping without requesting approval at every ordinary inspection. If any step is blocked by permissions, tool safety, access controls, unclear authorization, or a technical limitation, STOP that blocked step; return to Zed with the exact blocked item(s), observed error, intended purpose, and what approval would be needed. Wait for Zed to review and approve before attempting the blocked step again. Do not route around, retry with an alternate technique, expand scope, or silently reduce the intended investigation.

Unblocked, previously authorized read-only inspections may proceed. Never treat an owner's approval to inspect as permission to modify the phone. Existing prohibitions remain: no phone file creation/edit/deletion/moves, no service changes, app launches, root/privilege escalation, permission changes, sensitive/private app data access, or active testing. Stop at denied/sensitive areas and avoid repeated probes. Preserve findings with evidence labels VERIFIED / HISTORICAL CLAIM / ADOPTED / UNKNOWN and report them in additive GitHub notes. GitHub reporting separately owner-authorized.

This directive supersedes any workflow that asks Zed for permission at every routine read-only step; it does not supersede phone safety restrictions.
