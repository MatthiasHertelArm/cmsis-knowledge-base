---
id: "tbx-experimental-features-trace"
type: "concept"
domain: "project"
title: "Experimental Features: Trace"
summary: "Target execution data is captured through trace stream channels. The overall process has these steps:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#trace"
license: "Apache-2.0"
mode: "V"
---

Target execution data is captured through trace stream channels. The overall process has these steps:

1. Configure trace communication (how trace leaves the MCU) with the `target-set:` in `*.csolution.yml` (and optional settings in `*.dbgconf`).
2. Configure trace generation (what the MCU produces: ITM, DWT, etc.) with the `*.ctrace.yml` file.
3. Collect trace information (debugger receives and records the stream) into raw data files.
4. Analyze trace data files (host tools interpret the collected raw trace data files) and generate CSV and CTF files.

This section uses `<solution-set>` as the combined name of the `solution`, `target-type`, and `target-set` name, for example `SDS+AppKit-E8@HIL`.

!!! Note
    - Trace does not include SEGGER RTT, SystemView, or STDIO UART output. These features use separate data output paths.
