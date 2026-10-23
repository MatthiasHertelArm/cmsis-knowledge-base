---
id: "devt-ctrace-message-system-design-typed-trace-transport"
type: "concept"
domain: "trace"
title: "ctrace message-system design: Typed trace transport"
summary: "TraceMessage contains a std::variant of supported parameter records, including TraceCounterPayload, TracePcSamplePayload, TraceRecovery, and TraceFlushTimeout. Producers choose a meaningful record instead of building prose or passing an untyped list through the decoder."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/message-system-design.md#typed-trace-transport"
license: "Apache-2.0"
mode: "V"
---

`TraceMessage` contains a `std::variant` of supported parameter records, including `TraceCounterPayload`,
`TracePcSamplePayload`, `TraceRecovery`, and `TraceFlushTimeout`. Producers choose a meaningful record instead of
building prose or passing an untyped list through the decoder. The output adapter converts that record into the
appropriate `MessageId` and arguments only when the output style is known.

The value also retains optional packet context, an optional timestamp range, and an abort phase. Missing data stays
optional: no formatter invents an offset, timestamp, source ID, native code, or payload value. The same byte-skip
record can therefore produce both representations:

```cpp
TraceByteSkip skipped;
skipped.byteCount = 24;
skipped.formatterOffset = 128;
skipped.reason = TraceByteSkipReason::MissingSync;

formatTraceMessage(skipped, MessageStyle::Detailed);
// 24 bytes skipped due to missing SYNC; first formatter group at raw offset 128
formatTraceMessage(skipped, MessageStyle::Compact);
// 24 bytes skipped: no SYNC
```

`makeTraceIssue` derives the normal semantic `TraceIssueCode` from a typed message. This code remains separate from
`MessageId`: recovery and CTF logic use the semantic issue code, while the catalog ID selects wording. Collector APIs
preserve severity, route, callback order and discontinuity policy while transporting the message object.

Messages travel through collector APIs and `OpenCsdTraceElement::errorMessage` into `TraceIssueEvent::message`.
`CortexMPostDecoder` completes `TraceMessage::timestampRange` when recovery timing becomes known; it does not append
prose. The CLI reporter retains both `MessageStyle::Compact` and `MessageStyle::Detailed`; its stderr sink selects
the presentation. The CSV mapper always chooses `MessageStyle::Compact`. The enclosing `TraceEvent` supplies the
raw position for detailed issue formatting, without inserting it into compact text.

The shared model has no OpenCSD dependency. [OpenCsdErrorController][error-controller] translates native enums into
`TraceNativeCategory`, retaining native error/response codes and normalized foreign text. `OpenCsdPacketCollector`
retains typed packet kind, original size and a copy of at most 16 preview bytes. `nullopt` distinguishes unavailable
bytes from an empty packet. Native strings are never parsed back into parameters.

`OpenCsdTreeSessionError` retains its structured setup operation and native detail. `OpenCsdFatalError` retains the
structured cause and processed-byte count, and `FileDecodeJob` copies the cause into `TraceDecodeAbort`. Exceptions
also expose the existing detailed `what()` text for ordinary exception handlers. Abort phases preserve DATA,
end-of-trace, WAIT flush, formatted drain, SINGLE reset and formatted route-reset context.
