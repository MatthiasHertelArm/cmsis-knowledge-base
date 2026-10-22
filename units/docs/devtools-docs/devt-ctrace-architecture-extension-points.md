---
id: "devt-ctrace-architecture-extension-points"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Extension points"
summary: "Implement a decoder that produces TraceEvent values, add it below src/decode, and select it in the control layer for the corresponding channel."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/architecture.md#extension-points"
license: "Apache-2.0"
mode: "V"
---

### Add a raw trace channel

Implement a decoder that produces `TraceEvent` values, add it below `src/decode`, and select it in the control layer
for the corresponding channel. A new protocol carried by formatted CoreSight input additionally needs an explicit
protocol route from configuration; an observed unknown formatter ID is deliberately not enough to choose a decoder.
Reuse the input descriptor, diagnostics, event selection, and output backends rather than creating a second raw-input
architecture.

### Add an event type

Extend the model and its stable type names first. Then update the relevant decoder, selection behavior, and every
backend that can represent the event. Tests should cover semantic mapping separately from backend serialization.

### Add an output backend

Derive from `TraceOutput`, implement its backend hooks, define backend-specific preflight requirements, and add it to
the output plan and lifecycle. The concrete destructor must call `abortNoexcept()` while its backend members are still
alive. Do not introduce backend-specific state into the decode pipeline or event model.
