# A25 Workshop — Tunnel Metadata and Storage Reference Map Pass 09
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives
STATUS: VERIFIED read-only terminal metadata; owner-reported storage location

## Owner-reported evidence locations
Owner states checkpoint PDFs reside in emulator storage and in the 'Local AI workshop' folder in Documents storage. This is OWNER-REPORTED, not independently verified by phone inspection. Historical Oct 8 recovery index said PDFs were not committed with that index; this is not evidence of absence from emulator/Documents. No personal storage enumerated or PDFs opened.

## Verified running tunnel processes
Two cloudflared processes (PIDs 22097 and 30319 at observation) both reference the same local config ~/a25-workshop/gpt/config/cloudflared.yml and named tunnel a25-gpt-bridge. This establishes duplicate process references, not duplicate tunnels or incorrect operation.

## Verified file metadata only
- ~/a25-workshop/gpt/config/cloudflared.yml size 264, modified 2026-10-11 18:41 -0600, mode 600.
- ~/.cloudflared/pocket-gate02.token size 249, modified 2026-10-10 09:35 -0600, mode 600.
- ~/.cloudflared/pocket-gate02.toke size 249, modified 2026-10-10 09:33 -0600, mode 600.
- ~/.cloudflared/cert.pem size 282, modified 2026-10-11 17:33 -0600, mode 600.
No contents or credential values read. Similar sizes and names do not establish equality or active use.

## Bounded project config-name scan
Only ~/a25-workshop/gpt/config/cloudflared.yml matched selected tunnel/cloudflare/connector/mcp config filename patterns at depth <=3 across pockettest, pockettest-c1, pockettest-shared and Workshop. This does not establish absence of config in other directories, different names, remote plugin registries or hidden application data.

## Evidence classification
VERIFIED: local processes, config path references, metadata and bounded filename scan.
OWNER-REPORTED: emulator and Documents/Local AI workshop PDFs.
HISTORICAL CLAIM: Oct 8 Gate-02 tunnel and route checkpoint.
UNKNOWN: remote tunnel registration, connector/plugin registrations, duplicate credential contents, which credentials remain in use, whether parallel cloudflared processes are intended.
ADOPTED: map only; no modifications, cleanup, active testing or opening secrets.

## Next
Continue non-invasive mapping of connector references through public/project documentation or authorized metadata; do not access personal storage or credentials.
