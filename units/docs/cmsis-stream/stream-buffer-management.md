---
id: "stream-buffer-management"
type: "concept"
domain: "cmsis-stream"
title: "Buffer management"
summary: "When the memoryOptimization is enabled, the memory may be reused for different FIFOs to minimize the memory usage. But the scheduling algorithm is not trying to optimize this."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Buffer.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Buffer.md"
license: "Apache-2.0"
mode: "V"
---

When the `memoryOptimization` is enabled, the memory may be reused for different FIFOs to minimize the memory usage. But the scheduling algorithm is not trying to optimize this. So depending on how the graph was scheduled, the level of sharing may be different.

If you need to share as much as possible memory (to minimize memory usage or the amount of memory copied), you can do it if you respect a fundamental constraint : the values in the FIFOs must have value semantic and not reference semantic. 

If you share memory, you are using reference semantic and it should be hidden from the graph : one could use a copy-on-write strategy with a reference count inside the shared buffers. The reference count could also be computed statically using C++ templates if the graph has no loops. Let's look at the two way of handling the reference count. Those examples are coming from the `example12`
