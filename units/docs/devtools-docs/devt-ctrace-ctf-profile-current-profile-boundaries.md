---
id: "devt-ctrace-ctf-profile-current-profile-boundaries"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Current profile boundaries"
summary: "The profile remains version 1. Existing unformatted single-source input keeps its stream-0 byte layout and event schema unchanged; the generalized layout is used only for the newly supported formatted multi-route input."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/ctf-format.md#current-profile-boundaries"
license: "Apache-2.0"
mode: "V"
---

- Formatted, memory-aligned CoreSight frames carrying ITM/DWT are decoded and represented as separate route streams.
- The optional resolved processor name is encoded as stream-scoped environment metadata and private display context;
  `cmsis_trace_bus_id` remains the stable public routing field.
- Separate trace clock domains are represented, but Global Timestamp packets do not yet establish cross-stream
  synchronization. Each bundle contributing to XML must have one domain; different contributing bundles remain
  independent and their timestamps are not rebased.
- ETM and MTB instruction trace have no CTF event definitions yet.
- Event Recorder input has no CTF event definitions yet.
- Formatted input with FSYNC/HSYNC transport framing is not decoded; the current input contract requires complete,
  memory-aligned 16-byte formatter frames.
- ITM paging above stimulus port 31 is not supported.
- PMU counter assignments are not resolved to configured architectural event names.
- CTF records configured fixed clock frequencies but does not reconstruct stopped or changing trace clocks.

The profile remains version `1`. Existing unformatted single-source input keeps its stream-0 byte layout and event
schema unchanged; the generalized layout is used only for the newly supported formatted multi-route input. It adds
per-stream metadata and the private `ctrace_route` context while retaining `cmsis_trace_bus_id` and all public event
IDs, fields, enum values, and interpretations. A future incompatible change to those public contracts requires a
version review.
