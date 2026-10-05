---
id: "threadx-chapter-3-functional-components-of-memory-byte-pools"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Memory Byte Pools"
summary: "ThreadX memory byte pools are similar to a standard C heap. Unlike the standard C heap, it is possible to have multiple memory byte pools. In addition, threads can suspend on a pool until the requested memory is available."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#memory-byte-pools"
license: "MIT"
mode: "V"
---

ThreadX memory byte pools are similar to a standard C heap. Unlike the standard C heap, it is possible to have multiple memory byte pools. In addition, threads can suspend on a pool until the requested memory is available.

Allocations from memory byte
pools are similar to traditional ***malloc*** calls, which include the amount of memory desired (in bytes). Memory is allocated from the pool in a *first-fit* manner; i.e., the first free memory block that satisfies the request is used. Excess memory from this block is converted into a new block and placed back in the free memory list. This process is called *fragmentation*.

Adjacent free memory blocks are *merged* together during a subsequent
allocation search for a large enough free memory block. This process
is called *defragmentation*.

Each memory byte pool is a public resource. ThreadX places no
constraints on how pools are used, except that memory byte services
cannot be called from ISRs.

### Creating Memory Byte Pools

Memory byte pools are created either during
initialization or during run-time by application threads. There
is no limit on the number of memory byte pools in an application.

### Pool Capacity

The number of allocatable bytes in a memory byte pool is slightly less than what was specified during creation. This is because management of the free memory area introduces some overhead. Each free memory block in the pool requires the equivalent of two C pointers of overhead. In addition, the pool is created with two blocks, a large free block and a small permanently allocated block at the end of the memory area. This allocated block is used to improve performance of the allocation algorithm. It eliminates the need to continuously check for the end of the pool area during merging.

During run-time, the amount of overhead in the pool typically increases. Allocations of an odd number of bytes are padded to ensure proper alignment of the next memory block. In addition, overhead increases as the pool becomes more fragmented.

### Pool's Memory Area

The memory area for a memory byte pool is specified during creation. Like other memory areas in ThreadX, it can be located anywhere in the target's address space. This is an important feature because of the considerable flexibility it provides. For example, if the target hardware has a high-speed memory area and a low-speed memory area, the user can manage memory allocation for both areas by creating a pool in each of them.

### Thread Suspension

Application threads can suspend while waiting for memory bytes from a pool. When sufficient contiguous memory becomes available, the suspended threads are given their requested memory and the threads are resumed.

If multiple threads are suspended on the same memory byte pool, they are given memory (resumed) in the order they were suspended (FIFO).

However, priority resumption is also possible if the application calls ***tx_byte_pool_prioritize*** prior to the byte release call that lifts thread suspension. The byte pool prioritize service places the highest priority thread at the front of the suspension list, while leaving all other suspended threads in the same FIFO order.

### Run-time Byte Pool Performance Information

ThreadX provides optional run-time byte pool performance information. If the ThreadX library and application is built with ***TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO***
defined, ThreadX accumulates the following information.

Total number for the overall system:

  - allocations

  - releases

  - fragments searched

  - fragments merged

  - fragments created

  - allocation suspensions

  - allocation timeouts

Total number for each byte pool:

  - allocations

  - releases

  - fragments searched

  - fragments merged

  - fragments created

  - allocation suspensions

  - allocation timeouts

This information is available at run-time through the services ***tx_byte_pool_performance_info_get*** and ***tx_byte_pool_performance_system_info_get***. Byte pool performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of "allocation suspensions" might suggest that the byte pool is too small.

### Memory Byte Pool Control Block TX_BYTE_POOL

The characteristics of each memory byte pool are found in its control block. It contains useful information such as the number of available bytes in the pool. This structure is defined in the ***tx_api.h*** file.

Pool control blocks can also be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Nondeterministic Behavior

Although memory byte pools provide the most flexible memory allocation, they also suffer from somewhat nondeterministic behavior. For example, a memory byte pool may have 2,000 bytes of memory available but may not be able to satisfy an allocation request of 1,000 bytes. This is because there are no guarantees on how many of the free bytes are contiguous. Even if a 1,000 byte free block exists, there are no guarantees on how long it might take to find the block. It is completely possible that the entire memory pool would need to be searched to find the 1,000 byte block.

> **Tip:** *As a result of the nondeterministic behavior of memory byte pools, it is generally good practice to avoid using memory byte services in areas where deterministic, real-time behavior is required. Many applications pre-allocate their required memory during initialization or run-time configuration.*

### Overwriting Memory Blocks

It is important to ensure that the user of allocated memory does not write outside its boundaries. If this happens, corruption occurs in an adjacent (usually subsequent) memory area. The results are unpredictable and often catastrophic for program execution.
