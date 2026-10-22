---
id: "devt-ctrace-architecture-scope"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Scope"
summary: "ctrace combines a trace-run configuration with raw CoreSight trace data and converts supported trace channels into backend-independent semantic events. Output backends consume these events to create CSV or CTF artifacts."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/architecture.md#scope"
license: "Apache-2.0"
mode: "V"
---

`ctrace` combines a trace-run configuration with raw CoreSight trace data and converts supported trace channels into
backend-independent semantic events. Output backends consume these events to create CSV or CTF artifacts.

The current profile supports unformatted ITM byte streams from SWO or explicitly declared TB input, and
memory-aligned formatted CoreSight input carrying ITM and DWT packets. Each configured ITM route supports the public
event selections `itm`, `dwt`, `event`, `pmu`, `exception`, `pcsample`, `global_ts`, `overflow`, and `error`.
Backend-specific representations are documented in the [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md), not in the decoder contract.
PC sampling accepts a four-byte PC or the one-byte status markers `0x00` (`CPU Sleeping`) and Armv8-M `0xff`
(`Trace prohibited`). Status markers preserve route, timestamp, and sample quality without a PC address.

Every matching SWO, TB, and named-TB raw input is processed independently and sequentially for each selected trace-run
configuration. Formatted input distributes bytes to configured ITM routes by Trace Bus ID; unformatted input uses
one synthetic route. Other protocols require explicit decoder integration, not guesses based on observed IDs.
Deferred inputs and decoders are tracked in the [TODO list](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/todo.md).

The architecture separates protocol decoding, semantic interpretation, and output generation. This keeps output
formats independent of OpenCSD and allows another raw trace channel to reuse the event model and output backends.
