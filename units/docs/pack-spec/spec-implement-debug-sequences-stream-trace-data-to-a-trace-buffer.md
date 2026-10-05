---
id: "spec-implement-debug-sequences-stream-trace-data-to-a-trace-buffer"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Stream trace data to a trace buffer"
summary: "Use a <tracetracebuffer> element to describe an on-device trace buffer. A single trace buffer may be unnamed. If a trace configuration provides multiple trace buffers, each one shall have a unique name attribute."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

Use a `<trace_tracebuffer>` element to describe an on-device trace buffer. A single trace
buffer may be unnamed. If a trace configuration provides multiple trace buffers, each one shall
have a unique **name** attribute.

Use the name with `BufferStreamOut` in the Trace Buffer format (mode `1`) and with
`TraceBufferSelected.` An empty string identifies the unnamed trace buffer.

A debug access sequence can collect trace data in a temporary buffer using `BufferRead` and
forward it with `BufferStreamOut` to the selected trace buffer in the debugger for further
processing.

The following example reads 32-bit values repeatedly from a fixed trace-data register, without
incrementing its address, and streams the result to the trace buffer named **ETB**:

```
<trace>
  <tracebuffer name="ETB"/>
</trace>

<sequences>
  <sequence name="TraceFlush">
    <control if="TraceBufferSelected(&quot;ETB&quot;)">
      <block>
        // Read 0x100 bytes from a fixed 32-bit trace-data register into buffer 0.
        // Mode 32 selects 32-bit reads; its increment bit is clear.
        BufferRead(0, 0, 0xE0042010, 0x100, 32);
        BufferStreamOut(0, 0, 0x100, "ETB", 1, 0);
      </block>
    </control>
  </sequence>
</sequences>
```
