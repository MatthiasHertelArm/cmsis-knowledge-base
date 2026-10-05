---
id: "txmw-chapter-5-generating-trace-buffers-exporting-the-trace-buffer"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Exporting the Trace Buffer"
summary: "TraceX needs the trace buffer in a binary, Intel HEX, or Motorola S-Record file format on the host."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#exporting-the-trace-buffer"
license: "MIT"
mode: "V"
---

TraceX needs the trace buffer in a binary, Intel HEX, or Motorola S-Record file format on the host. The easiest way to accomplish this is to stop the target and instruct your debugger to dump the memory area you supplied to ***tx_trace_enable*** function into a file on the host.

> **Warning:** ***Be careful not to stop the target within a trace gathering code itself. Doing so can cause invalid trace information. If the program is halted within ThreadX, it is best to step over any trace insert macro before dumping the trace buffer.***

> **Important:** *Appendix D shows how to dump the trace buffer from within a variety of development tools.*
