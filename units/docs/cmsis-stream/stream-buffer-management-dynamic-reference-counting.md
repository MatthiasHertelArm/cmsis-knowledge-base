---
id: "stream-buffer-management-dynamic-reference-counting"
type: "concept"
domain: "cmsis-stream"
title: "Buffer management: Dynamic reference counting"
summary: "Dynamic reference counting could make use of the C++ shared_ptr. The CMSIS-Stream FIFO would contain a shared_ptr pointing to a buffer. Most of the time, those FIFOs would have length 1 and would be optimized out by CMSIS-Stream."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Buffer.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Buffer.md#dynamic-reference-counting"
license: "Apache-2.0"
mode: "V"
---

Dynamic reference counting could make use of the C++ `shared_ptr`. The CMSIS-Stream FIFO would contain a `shared_ptr` pointing to a buffer. Most of the time, those FIFOs would have length 1 and would be optimized out by CMSIS-Stream.

The nodes would have to check for the reference count to know if they can modify the content of the buffer. If the buffer is shared, and the node needs to modify its content (algorithm using in-place modification), a copy of the buffer would be needed. Such copies could come from a memory pool of pre-allocated buffers.

At the end of a schedule iteration, the memory pool, would be reset.

In below graph, some of those ideas are illustrated:

* The `BufferSource` is generating a new buffer coming from a memory pool of pre-allocated buffers
* The `ProcessingNode` needs to generate a new buffer for the output and it gets the new buffer from a `BufferSource` on one of its inputs. The idea is to make the memory allocations visible in the graph rather than have them hidden inside the nodes
* The `inplace` node uses an algorithm that is modifying its input in-place. So, the input buffer, if it is shared, need to be duplicated. It is done by the `BufferCopy` node. `BufferCopy` will create a new copy only if the input buffer is shared.
* At the end of a schedule iteration of this graph, the memory pool is reset and the pre-allocated buffers can be reused for the next schedule iteration

(figure: dynamic)

There are some issues with the dynamic ref counting:

* It is difficult to know how many buffers will be needed:
  * `BufferCopy` will copy only in case of sharing
  * The level of sharing will depends on how the node executions have been scheduled
  * The other references to this node may no more be used when the `BufferCopy` node is executed
  * It makes it difficult to size the memory pool
* The nodes must check for the reference count. If they forget to do it, it may cause issues
