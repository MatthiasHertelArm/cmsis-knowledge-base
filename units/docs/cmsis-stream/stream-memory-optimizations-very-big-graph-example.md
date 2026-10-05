---
id: "stream-memory-optimizations-very-big-graph-example"
type: "concept"
domain: "cmsis-stream"
title: "Memory optimizations: Very big graph example"
summary: "The example below is obviously unrealistic for an embedded device. It is too big. But it is a good way to illustrate what the memory optimization can achieve."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Memory.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Memory.md#very-big-graph-example"
license: "Apache-2.0"
mode: "V"
---

The example below is obviously unrealistic for an embedded device. It is too big. But it is a good way to illustrate what the memory optimization can achieve.

There are 511 FIFOs in this graph. They use 261632 bytes of memory. But the graph has lot of parallelism. By following the computed schedule, it may be possible to reuse the FIFO buffers between different branches of the graph. 

When the memory optimization feature is enabled, the system is only using 16 buffers for a memory consumption of 8192 bytes.

**We thus go from 261632 bytes to just 8192 bytes for this graph.**

(figure: big_graph)
