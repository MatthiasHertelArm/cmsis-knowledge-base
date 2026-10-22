---
id: "devt-ctrace-architecture-how-it-works-at-a-glance"
type: "concept"
domain: "trace"
title: "ctrace Architecture: How it works at a glance"
summary: "ctrace processes one solution set at a time and runs a separate file job for each supported raw input in that set. The README describes how configuration, raw inputs, and generated outputs are grouped by solution-set and channel names."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/architecture.md#how-it-works-at-a-glance"
license: "Apache-2.0"
mode: "V"
---

`ctrace` processes one solution set at a time and runs a separate file job for each supported raw input in that set.
The [README](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../README.md#trace-directory) describes how configuration, raw inputs, and generated outputs are grouped
by solution-set and channel names. The following path runs once per input, with fresh decoder and output state.

The main in-memory path is:

```text
command line + trace-run YAML + selected SWO/TB raw file
                    |
                    v
        TraceDirectoryJob / FileDecodeJob
       input descriptor, routes, output plan
                    |
                    v
           64 KiB non-owning byte views
                    |
                    v
          OpenCSD DecodeTree session
       SINGLE or FRAME_FORMATTED root
          route-bound ITM decoders
                    |
                    v
       routed OpenCsdTraceElement values
                    |
                    v
 CortexMStreamDecoder / CortexMPostDecoder
     timestamps, DWT pairing, quality
                    |
                    v
             TraceEvent values
                    |
                    v
              DecodeConsumers
        /               |               \
 diagnostics        CSV backend       CTF backend
```

The `TraceEvent` boundary is the central design point. Before it, code handles byte offsets, OpenCSD packets, decoder
recovery, and Cortex-M state. After it, code sees backend-independent events in semantic callback order,
without depending on OpenCSD types.

Formatter-skipped payload and initial ITM synchronization skips follow a separate `TraceByteSkip` path from the
OpenCSD adapter through `DecodePipeline` directly to `TraceEventSink::appendByteSkip` and `DecodeConsumers`. These
input annotations bypass route-local Cortex-M interpretation: they carry an observed ID, if known, but no decoded
event or timestamp. Consumers retain CSV `info` rows and report CLI Info; CTF does not encode these annotations.

The similarly named decode types are consecutive pipeline stages, not interchangeable implementations of one decoder
contract. `OpenCsdItmDecoder` decodes transport bytes, `CortexMStreamDecoder` routes normalized elements, and each
`CortexMPostDecoder` reconstructs semantic events with help from `DwtPacketDecoder`. Common interfaces exist only at
actual substitution boundaries such as `OpenCsdItmSessionInterface`, `OpenCsdTraceElementSink`, and `TraceEventSink`;
there is deliberately no common base class for all decode stages.
