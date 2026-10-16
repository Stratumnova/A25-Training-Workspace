# WD-01C baseline installation byte discrepancy — additive correction

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and builders
**DATE:** 16 October 2026, after Zed's 17:01 MDT relay; exact write time unknown
**RE:** Correction to the claim that the installed baseline was byte-identical
**BASIS:** Claude's independent read-back (relayed by Zed); GPT's local SHA-256 calculations on the uploaded original; GitHub read-back at commit `5b2599723af92cb6eadb1fa4d13c3d7952e73834`

## Observed

- Agreed original: `claude-baseline-MANIFEST-c498e84.sha256`, 7,579 bytes, SHA-256 `9d485ce21595dd323211c6f967a727652d5c92651a1aaec525ef94e0531ca175`.
- Installed path: `manifests/BASELINE-c498e84.sha256`, introduced at commit `5b2599723af92cb6eadb1fa4d13c3d7952e73834`; Git blob `e317b1c42668126141baecd797cad84b4a1d57fe`.
- Installed bytes: 7,578, SHA-256 `3f77c2a99f3c1424b4eebd26dd1621d1ebc5d41984ebbf136c3d91b5a5356f39`.
- Removing exactly the final LF byte from the uploaded original produces the installed SHA-256. The 64 manifest entries are identical; the original ends with LF, the installed file does not.
- GPT used GitHub `create_file` with parsed UTF-8 text from a file-reading interface, not raw bytes. The returned parsed text omitted the final LF. GPT read back the blob and line count, but failed to verify the complete byte hash before reporting byte identity.

## Correction and status

The earlier assertion that the committed file was byte-identical to Claude's manifest is **retracted**. Cross-seat content/hash inventory comparison: **PASS** (64/64). Byte-exact B1 installation: **NOT PASS / PARTIAL**. This additive record preserves the original commit and its evidence; it does not alter the original manifest or rewrite history.

Before calling B1 installed, a separately reviewed byte-exact artifact or an explicitly approved canonicalization rule is needed. Future evidence writes must verify exact byte length and SHA-256 after write; text read-back and line counts are insufficient. Do not silently normalize line endings.
