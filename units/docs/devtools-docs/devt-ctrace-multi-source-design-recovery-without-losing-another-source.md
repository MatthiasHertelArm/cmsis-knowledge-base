---
id: "devt-ctrace-multi-source-design-recovery-without-losing-another-source"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Recovery without losing another source"
summary: "A protocol error can interrupt delivery partway through a formatter frame. Resetting the entire tree would also clear the deformatter's current source ID."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/multi-source-design.md#recovery-without-losing-another-source"
license: "Apache-2.0"
mode: "V"
---

A protocol error can interrupt delivery partway through a formatter frame. Resetting the entire tree would also
clear the deformatter's current source ID. Later frames need not repeat that ID, so a global reset could silently lose
or misattribute otherwise valid payload. Recovery therefore follows the route boundary:

1. Callbacks copy a stable batch of errors and packet observations. They do not reset decoders, write outputs, or
   throw through OpenCSD. Decisions occur after the synchronous data-path operation returns.
2. A recoverable error attributed to a known route discards only that route's transaction suffix at or after the
   failing offset. Earlier events and events from unaffected routes remain in order.
3. Only the affected packet-processor/full-decoder chain is reset. The deformatter, current ID, partially delivered
   frame, and other routes retain their state.
4. Bounded flush operations drain already unpacked frame segments before the next raw block. The root's processed
   byte count is the only raw-input cursor; consumed bytes are never re-fed.
5. The affected route stays in data loss until a real hardware synchronization appears, or closes its unresolved
   interval at end of input. Its semantic state clears incomplete DWT pairing and invalidates timestamp quality.

An unassignable error, deformatter failure, failed local reset, or exhausted progress bound aborts the input. The
migration originally removed every incomplete output after such a failure; the later CSV retention policy is
described below. Backend writer failures continue to affect only their own backend.
