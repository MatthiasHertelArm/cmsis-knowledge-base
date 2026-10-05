---
id: "stream-memory-optimizations-buffer-sharing"
type: "concept"
domain: "cmsis-stream"
title: "Memory optimizations: Buffer sharing"
summary: "When several FIFOs are used as buffers then it may be possible to share the underlying memory for all of those buffers. This optimization is enabled by setting memoryOptimization to true in the configuration object:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Memory.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Memory.md#buffer-sharing"
license: "Apache-2.0"
mode: "V"
---

When several FIFOs are used as buffers then it may be possible to share the underlying memory for all of those buffers. This optimization is enabled by setting `memoryOptimization` to `true` in the configuration object:

```python
conf.memoryOptimization=True
```

The optimization depends on how the graph has been scheduled.

With the following graph there is a possibility for buffer sharing:

(figure: memory)

Without `memoryOptimization`, the FIFO are consuming 60 bytes (4*5 * 3 FIFOs). With `memoryOptimization`, only 40 bytes are needed.

You cannot share memory for the input / output of a node since a node needs both to read and write for its execution. This imposes some constraints on the graph.

The constraints are internally represented by a different graph that represents when buffers are live at the same time : the interference graph. The input / output buffers of a node are live at the same time (except for `Duplicate` node where the constraint is relaxed). Graph coloring is used to identify, from this graph of interferences, when memory for buffers can be shared. 

The interference graph is highly depend on how the compute graph is scheduled : a buffer is live when a write has taken place but no read has yet read the full content.

For the above compute graph and its computed schedule, the interference graph would be:

(figure: inter)



Adjacent vertices in the graph should use different colors. A coloring of this graph is equivalent to assigning memory areas. Graph coloring of the previous interference graph is giving the following buffer sharing:

(figure: fifos)

The dimension of the buffer is the maximum for all the edges using this buffers.

In the C++ code it is represented as:

```C++
#define BUFFERSIZE0 20
CG_BEFORE_BUFFER
uint8_t buf0[BUFFERSIZE0]={0};
```

`uint8_t` is used (instead of the `float32_t` of this example) because different edges of the graph may use different datatypes.

It is really important that you use the macro `CG_BEFORE_BUFFER` to align this buffer so that the alignment is coherent with the datatype used on all the FIFOs.

Note that liveliness analysis is currently very simple since it generates only an interval. But the activity of a FIFO should be a list of interval.  With a list of interval more buffer sharing would be possible (but it is not currently implemented).
