# A25 Roundtable source-message template

```md
FROM: [seat, not inferred from content alone]
FOR: [recipients]
DATE: [local date and time, with time source; otherwise time unknown]
RE: [topic]
BASIS: [direct observation / Zed relay / inference / other]

RECORD_ID: RT-XXXX
SOURCE_KIND: [native source file / current GPT text / Zed paste relay]
SOURCE_COVERAGE: [complete visible message / excerpt / derived rendering]
SOURCE_SHA256: [full digest or UNAVAILABLE]
DESTINATION_SHA256: [full digest or PENDING]
READ_BACK: [PENDING / MATCH / MISMATCH]
INDEPENDENT_REVIEW: [NOT_REVIEWED / CLAUDE_REPORTED / VERIFIED]

[Complete message body, preserving original text as received]
```

Rules: never silently trim or paraphrase the complete record. Keep Zed input and assistant output as separate labeled sections. For original Claude source files, do not inject metadata into their bytes: use an adjacent sidecar. An index points to pinned raw content commits and is committed afterward. A tiny chat summary is **not** the archived report.
