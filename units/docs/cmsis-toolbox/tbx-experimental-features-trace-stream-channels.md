---
id: "tbx-experimental-features-trace-stream-channels"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Trace Stream Channels"
summary: "The trace stream channels are configured using the trace: node in target-set: of the .csolution.yml project file. The following trace stream <channels> may be used:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#trace-stream-channels"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

The trace stream channels are configured using the [`trace:`](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/pyOCD-Debugger.md#trace) node in `target-set:` of the `*.csolution.yml` project file. The following trace stream `<channels>` may be used:

`<channel>`   | Description
:-------------|:------------------------
SWO           | Serial-Wire Output: one-pin interface that sends trace information using [UART](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/pyOCD-Debugger.md#swo-uart) or Manchester mode (tbd).
TB            | [Embedded Trace Buffer or Micro Trace Buffer](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/pyOCD-Debugger.md#trace-buffer) that stores trace information in memory.
ER            | Event Recorder: uses code annotations that store program events in memory.

For `TB`, the trace buffer name is appended to the channel name when present. For example, a trace buffer named `MTB` uses the `TB_MTB` channel.

#### Selecting Trace Buffers

The optional `trace-buffer:` node under `trace:` in the [`debugger:`](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/YML-Input-Format.md#debugger) configuration selects a trace buffer. When multiple trace buffers are available, its value must match the name of the selected trace buffer. The [`trace-sinks:`](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/YML-CBuild-Format.md#debug-topology) node under `debug-topology:` in `*.cbuild-run.yml` lists PDSC `tracebuffer` elements and their names. The name value may be omitted when exactly one trace buffer is listed without a name.

For example, the following selects the `MTB` trace buffer:

```yml
debug-topology:
  trace-sinks:
    - serialwire:
    - tracebuffer: MTB
    - tracebuffer: ETB_0
```

```yml
debugger:
  trace:
    - trace-buffer: MTB
```

This selection lets DFP debug sequences use `TraceBufferSelected("MTB")`, and lets a `TraceFlush` sequence direct `BufferStreamOut` to the selected named trace buffer in the debugger.

#### Trace Formatting

Some trace stream channel types may transport formatted trace data from multiple source streams, e.g. ITM data from multiple processors in the system. For simplicity, the formatter is always enabled in this solution.

Trace stream channel | Formatter usage
:--------------------|:----------------
SWO                  | Not supported
TB                   | Always enabled
ER                   | Not supported
