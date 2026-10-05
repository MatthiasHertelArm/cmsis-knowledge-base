---
id: "threadx-chapter-3-functional-components-of-memory-block-pools"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Memory Block Pools"
summary: "Allocating memory in a fast and deterministic manner is always a challenge in real-time applications. With this in mind, ThreadX provides the ability to create and manage multiple pools of fixed-size memory blocks."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#memory-block-pools"
license: "MIT"
mode: "V"
---

Allocating memory in a fast and deterministic manner is always a challenge in real-time applications. With this in mind, ThreadX provides the ability to create and manage multiple pools of fixed-size memory blocks.

Because memory block pools consist of fixed-size blocks, there are never any fragmentation problems. Of course, fragmentation causes behavior that is inherently nondeterministic. In addition, the time required to allocate and free a fixed-size memory block is comparable to that of simple linked-list manipulation. Furthermore, memory block allocation and de-allocation is done at the head of the available list. This provides the fastest possible linked list processing and might help keep the actual memory block in cache.

Lack of flexibility is the main drawback of fixed-size memory pools. The block size of a pool must be large enough to handle the worst case memory requirements of its users. Of course, memory may be wasted if many different size memory requests are made to the same pool. A possible solution is to make several different memory block pools that contain different sized memory blocks.

Each memory block pool is a public resource. ThreadX places no constraints on how pools are used.

### Creating Memory Block Pools

Memory block pools are created either during initialization or during run-time by application threads. There is no limit on the number of memory block pools in an application.

### Memory Block Size

As mentioned earlier, memory block pools contain a number of fixed-size blocks. The block size, in bytes, is specified during creation of the pool.

> **Note:** *ThreadX adds a small amount of overhead—the size of a C pointer—to each memory block in the pool. In addition, ThreadX might have to pad the block size to keep the beginning of each memory block on proper alignment.*

### Pool Capacity

The number of memory blocks in a pool is a function of
the block size and the total number of bytes in the memory area supplied
during creation. The capacity of a pool is calculated by dividing the
block size
(including padding and the
pointer overhead bytes) into the total number of bytes in the supplied
memory area.

### Pool's Memory Area

As mentioned before, the memory area for the block pool is specified during creation. Like other memory areas in ThreadX, it can be located anywhere in the target's address space.

This is an important feature because of the considerable flexibility it provides. For example, suppose that a communication product has a highspeed memory area for I/O. This memory area is easily managed by making it into a ThreadX memory block pool.

### Thread Suspension

Application threads can suspend while waiting for a memory block from an empty pool. When a block is returned to the pool, the suspended thread is given this block and the thread is resumed.

If multiple threads are suspended on the same memory block pool, they are resumed in the order they were suspended (FIFO).

However, priority resumption is also possible if the application calls ***tx_block_pool_prioritize*** prior to the block release call that lifts thread suspension. The block pool prioritize service places the highest priority thread at the front of the suspension list, while leaving all other suspended threads in the same FIFO order.

### Run-time Block Pool Performance Information

ThreadX provides optional run-time block pool performance information. If the ThreadX library and application is built with **TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

  - blocks allocated

  - blocks released

  - allocation suspensions

  - allocation timeouts

Total number for each block pool:

  - blocks allocated

  - blocks released

  - allocation suspensions

  - allocation timeouts

This information is available at run-time through the services ***tx_block_pool_performance_info_get*** and ***tx_block_pool_performance_system_info_get***. Block pool performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of "allocation suspensions" might suggest that the block pool is too small.

### Memory Block Pool Control Block TX_BLOCK_POOL

The characteristics of each memory block pool are found in its control block. It contains information such as the number of memory blocks available and the memory pool block size. This structure is defined in the ***tx_api.h*** file.

Pool control blocks can also be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Overwriting Memory Blocks

It is important to ensure that the user of an allocated memory block does not write outside its boundaries. If this happens, corruption occurs in an adjacent (usually subsequent) memory area. The results are unpredictable and often fatal to the application.
