---
id: "devt-ctrace-architecture-processing-state-and-ownership"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Processing state and ownership"
summary: "One DecodePipeline is created for each raw file. It owns the OpenCSD adapter and Cortex-M stream decoder, so protocol, formatter, timestamp, and DWT state survive arbitrary file-read boundaries."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#processing-state-and-ownership"
license: "Apache-2.0"
mode: "V"
---

One `DecodePipeline` is created for each raw file. It owns the OpenCSD adapter and Cortex-M stream decoder, so
protocol, formatter, timestamp, and DWT state survive arbitrary file-read boundaries. `RawFileReader` owns a single
64 KiB buffer; each `RawByteView` borrows that buffer only for the synchronous `DecodePipeline::push` call. Calling
`DecodePipeline::finish` flushes both the OpenCSD and Cortex-M layers before the pipeline is destroyed.

Both input formats use the same `OpenCSD DecodeTree` ownership boundary. `SINGLE` connects one synthetic, no-ATB-ID
route to one ITM decoder. `FRAME_FORMATTED` owns the frame deformatter and one route-bound ITM decoder for each
configured Trace Bus ID. Ctrace creates and feeds one tree at a time because OpenCSD's alternate logger and live-tree
registry use process-global state; the session restores the previously installed logger when it is destroyed. Each
file job finishes and releases its decoder before the next input starts. Route IDs and clocks remain local to that
input, so files can reuse Trace Bus IDs without sharing decoder state or output streams.

Ownership is deliberately split by responsibility while preserving one enclosing lifetime: `OpenCsdTreeSession`
owns the tree and configured decoder components. For formatted input, `OpenCsdFormattedItmSession` additionally owns
the route adapters, packet/frame monitors, and captured callback errors installed in that tree. For SINGLE input,
the decoder implementation owns the packet collector and error controller that `OpenCsdItmSession` connects
directly. Members are ordered so the tree is destroyed first, before any callback target or diagnostic state it can
reference. This keeps format-specific feed and recovery policy out of the low-level tree wrapper without weakening
callback lifetime safety.

`CortexMStreamDecoder` maintains an independent post-decoder for each normalized route. All post-decoders emit into
the same `TraceEventSink` while keeping route-specific timestamp and DWT state apart. Events buffered for timestamp
resolution are emitted independently per route. The sink observes semantic emission order, not a global raw-input or
chronological order across routes.

There is no application-wide event queue. `DecodeConsumers` forwards each event synchronously to the output
lifecycle and issue reporter.
