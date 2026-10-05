---
id: "tbx-experimental-features-out-of-scope"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Out-of-Scope"
summary: "Experimental Features: Trace / Out-of-Scope"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#out-of-scope"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

- SEGGER RTT, SystemView, and STDIO UART output are not part of trace capture and use separate output paths.
- ITM channel 0 `printf` output should not be routed to trace analysis components. It should be shown in an output window or debug console.
