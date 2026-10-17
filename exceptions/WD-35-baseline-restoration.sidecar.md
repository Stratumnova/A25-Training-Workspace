# WD-35 restoration sidecar

FROM: GPT — A25 Project Lead
FOR: Zed and Claude
DATE: 2026-10-16
RE: One-time restoration of malformed baseline
BASIS: Zed 22:43 approval and Claude WD-35 design review

Affected: manifests/BASELINE-c498e84.sha256
Violation: W4 frozen manifest rewrite; W1 malformed glued line.
Reason: GPT appended a new digest to a baseline without a trailing newline. The correct new digest is now in manifests/ADDITIONS.sha256.
Broken Git blob: bf3f3d85413deb94c1b36eee3ea4aabd414cddee
Original Git blob: e317b1c42668126141baecd797cad84b4a1d57fe
These are Git blob IDs, not SHA-256. Target bytes are from commit 9d356f62.
Authorization: Zed expressly said at 22:43 MDT, "My approval for this current manifest is a go".
Review: Claude agreed to an exact-byte, narrowly scoped restoration in the WD-35 Drive review, before Claude's platform interruption.
Marker: manifests/W4_RESTORATIONS.txt
No general W4 bypass is approved. This implementation is GPT-only during Claude's blackout, pending independent code review.
