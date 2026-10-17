# A25 case study — external builder pause and Pocket Server dependency

FROM: GPT — A25 Project Lead
FOR: Zed and Roundtable participants
DATE: 2026-10-16 19:42 MDT (Zed-attested)
RE: GB-01 onboarding experiment, access limitations, and pause
BASIS: Zed's relayed decisions, GB-01 intake and W4 audit reports, photographed device screens, and GPT assessment. No independent device or network access claimed.

## Zed's decision (human authority)
"Zed to gpt@7:42 Oct 16
This shows us the weak spots and the need for the pocket server. I'm saying we are not ready for an outside unit helping right now until we get the rest finished. Add this to the case study and we will continue working past this invite for now."

Decision: pause further external-builder onboarding and resume internal A25/Pocket Server development. This is a pause, not a rejection of GB-01 or deletion of its work.

## Observations and limits
- GB-01 received an A25 repository ZIP on a separate phone, produced a read-only intake report, and was subsequently invited to act as a temporary guest builder with no repository write or governance authority. Zed photographed the other device as additional evidence of separate-device participation; photos do not independently authenticate an AI identity or prove isolation of information sources.
- GB-01 reported reproducing a W4 multi-commit false pass in a disposable local Git repository, with 0 FAIL / 0 WARN and exit code 0. This is guest-reported test evidence, not an independently repeated GPT test or a live repository exploit.
- Claude separately identified the multi-commit W4 issue in a code review. Independence of the two reviews is not proven.
- On the guest device Google Drive appeared locked/admin-restricted, preventing the proposed shared-Drive connection. A GitHub connector sign-in screen was shown; completion of authorization was not established. ChatGPT Remote settings concern pairing with a desktop, not shared AI filesystem access.
- Both phones and a laptop are available on a local network, but being on the same network does not itself grant AI sessions access to a shared folder.
- Manual ZIP and report relay was workable for a bounded test but remains an operational bottleneck and creates snapshot freshness and attribution risks.

## Engineering implications (GPT assessment, not Zed quotations)
The Pocket Server needs a deliberate shared-file interface with per-seat authorization, scoped inboxes, read-only common material, explicit provenance, version/digest checks, and safe write/approval boundaries before broad outside-builder participation. Local laptop storage may serve as a backend after interfaces and permissions are implemented and tested. No claim is made that these features already exist.

## Status and next gate
GB-01 guest work remains archived or relayed according to its actual evidence; do not imply a new permanent member or direct tool access. Pause invitations and shared-account integration. Continue internal development and revisit external onboarding only after Zed authorizes a tested shared-storage and access-control path.

## Provenance
Zed's 19:42 MDT message is directly supplied. Other GB-01 and Claude results are relayed or documented in earlier Roundtable exchanges. This record is a new synthesis, not a byte-exact copy of those source reports. Do not publish guest account names, emails, memory screenshots, or property details.
