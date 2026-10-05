---
id: "stream-memory-optimizations-buffers"
type: "concept"
domain: "cmsis-stream"
title: "Memory optimizations: Buffers"
summary: "Sometimes, a FIFO is in fact a buffer. In below graph, the source is writing 5 samples and the sink is reading 5 samples."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Memory.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Memory.md#buffers"
license: "Apache-2.0"
mode: "V"
---

Sometimes, a FIFO is in fact a buffer. In below graph, the source is writing 5 samples and the sink is reading 5 samples.

(figure: buffer)

The scheduling will obviously be something like:

`Source, Sink, Source, Sink ...`

In this case, the FIFO is used as a simple buffer. The read and the write are always taking place from the start of the buffer.

The schedule generator will detect FIFOs that are used as buffer and the FIFO implementation will be replaced by buffers : the third argument of the template (`isArray`) is set to one:

```C++
FIFO<float32_t,FIFOSIZE0,1,0> fifo0(buf1);
```
