---
id: "devt-ctrace-multi-source-design-scope-and-motivation"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Scope and motivation"
summary: "The existing SWO path decoded one ITM byte stream directly. Trace Buffer captures added a framing layer that can interleave several sources, each with its own processor metadata, timestamps, and protocol state."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/multi-source-design.md#scope-and-motivation"
license: "Apache-2.0"
mode: "V"
---

The existing SWO path decoded one ITM byte stream directly. Trace Buffer captures added a framing layer that can
interleave several sources, each with its own processor metadata, timestamps, and protocol state. Supporting them
required carrying source identity through decoding, diagnostics, filtering, and output generation.

The migration covered every already supported ITM-carried event family: software instrumentation, DWT data and
matches, exceptions, PC samples and sleep, DWT/PMU counters, timestamps, synchronization, overflow, and decoder issues.
DWT and PMU packets share their processor's ITM route; they do not require additional protocol decoders.

The scope remained one decoder-ready raw file per trace-run. Capture readout, trace-buffer wrap handling, and
chronological linearization belong to the producer. Instruction-trace protocols, Event Recorder decoding, simultaneous
raw inputs, FSYNC/HSYNC framing, and cross-processor clock correlation were outside this migration. Their current
status belongs in the [TODO list](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/todo.md), not in this historical record.
