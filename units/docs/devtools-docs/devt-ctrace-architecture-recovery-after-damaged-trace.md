---
id: "devt-ctrace-architecture-recovery-after-damaged-trace"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Recovery after damaged trace"
summary: "For formatted input, the frame monitor counts skipped payload without a known source ID and payload assigned to NULL, reserved, or unconfigured IDs."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#recovery-after-damaged-trace"
license: "Apache-2.0"
mode: "V"
---

For formatted input, the frame monitor counts skipped payload without a known source ID and payload assigned to
NULL, reserved, or unconfigured IDs. Bounded accounting produces input annotations with the reason, observed ID
when known, byte count, and first formatter output group's raw offset. Counts are deformatted payload bytes,
excluding formatter control bytes; the offset is not the position of each discarded byte. The unassigned prefix
is reported after an assigned group appears or at end of input; skipped-ID totals are reported at end of input.
These Info records do not make the input fatal. No capture bytes are removed or rewritten by ctrace.

An already identified formatted route can also discard initial ITM bytes while seeking its first hardware sync.
The packet collector counts the deformatted bytes reported as `NOTSYNC`, rather than subtracting raw offsets across
interleaved formatter groups. If the route later reaches a committed real sync, it emits one `MissingSync` byte-skip
Info immediately before that sync, not a semantic warning or a manufactured sync. An existing route error/recovery
interval suppresses duplicate initial-loss accounting. The input annotation retains the observed ID and bypasses
output filters. This path covers initial formatted synchronization, not general SWO or malformed-packet recovery.

Recoverable OpenCSD packet errors establish a discontinuity on the affected route at the reported raw-file offset.
Callbacks before that offset are retained. Route-aware transaction buffering discards callbacks from the failing
route at or after it while retaining callbacks from other routes in their original order. Error callbacks only
capture a stable batch; rollback and reset decisions happen after the synchronous OpenCSD operation returns.

For a known ITM route, `ctrace` resets only that route's packet-processor/full-decoder chain. The formatted
deformatter, its current source ID, partially delivered frame, and every other route remain intact. A bounded root
flush drains already unpacked frame segments before the next aligned input block. The raw cursor advances only by the
byte count returned by the DecodeTree, so consumed bytes are never fed twice. OpenCSD resumes the affected route only
after finding a real ITM hardware-sync sequence; `ctrace` never inserts a synthetic sync sequence.

Bytes lost before resynchronization form one explicit route-bound `data-loss` interval. At its boundary, that route's
Cortex-M post-decoder flushes pending events, resets incomplete DWT correlation, and marks timestamps unreliable until
the stream supplies enough timing information again. A route that does not resynchronize closes its interval as
unresolved at end of input. The issue remains part of the ordered `TraceEvent` stream, so diagnostics and enabled
output backends observe the same recovery boundary.

Initial ITM synchronization is tracked independently per formatted route. At end of input, a configured route that
received payload but has no committed real hardware sync emits a route-bound `OpenCsdMissingSync` Error. A sync from
a rolled-back transaction does not satisfy this check. The error retains healthy route output and completed
diagnostic artifacts but makes the invocation fail. Routes with no received payload are not diagnosed as missing sync.

An error without a usable route, a deformatter error, failure to reset the route, repeated lack of decoder progress,
or an unsuccessful bounded wait/flush operation aborts the current raw-file job. The fatal-input output policy
retains committed CSV rows with a global abort record, but removes the incomplete CTF bundle. Only completed bundles
contribute to target-level XML.
