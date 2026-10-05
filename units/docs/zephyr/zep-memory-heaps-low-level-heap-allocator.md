---
id: "zep-memory-heaps-low-level-heap-allocator"
type: "concept"
domain: "rtos"
title: "Memory Heaps: Low Level Heap Allocator"
summary: "The underlying implementation of the k_heap abstraction is provided a data structure named sys_heap. This implements exactly the same allocation semantics, but provides no kernel synchronization tools."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/heap.rst"
license: "Apache-2.0"
mode: "V"
---

The underlying implementation of the `k_heap`
abstraction is provided a data structure named `sys_heap`.  This
implements exactly the same allocation semantics, but
provides no kernel synchronization tools.  It is available for
applications that want to manage their own blocks of memory in
contexts (for example, userspace) where synchronization is unavailable
or more complicated.  Unlike `k_heap`, all calls to any `sys_heap`
functions on a single heap must be serialized by the caller.
Simultaneous use from separate threads is disallowed.


### Implementation


Internally, the `sys_heap` memory block is partitioned into "chunks"
of 8 bytes.  All allocations are made out of a contiguous region of
chunks.  The first chunk of every allocation or unused block is
prefixed by a chunk header that stores the length of the chunk, the
length of the next lower ("left") chunk in physical memory, a bit
indicating whether the chunk is in use, and chunk-indexed link
pointers to the previous and next chunk in a "free list" to which
unused chunks are added.

The heap code takes reasonable care to avoid fragmentation.  Free
block lists are stored in "buckets" by their size, each bucket storing
blocks within one power of two (i.e. a bucket for blocks of 3-4
chunks, another for 5-8, 9-16, etc...) this allows new allocations to
be made from the smallest/most-fragmented blocks available.  Also, as
allocations are freed and added to the heap, they are automatically
combined with adjacent free blocks to prevent fragmentation.

All metadata is stored at the beginning of the contiguous block of
heap memory, including the variable-length list of bucket list heads
(which depend on heap size).  The only external memory required is the
`sys_heap` structure itself.

The `sys_heap` functions are unsynchronized.  Care must be taken by
any users to prevent concurrent access.  Only one context may be
inside one of the API functions at a time.

The heap code takes care to present high performance and reliable
latency.  All `sys_heap` API functions are guaranteed to complete
within constant time.  On typical architectures, they will all
complete within 1-200 cycles.  One complexity is that the search of
the minimum bucket size for an allocation (the set of free blocks that
"might fit") has a compile-time upper bound of iterations to prevent
unbounded list searches, at the expense of some fragmentation
resistance.  This `CONFIG_SYS_HEAP_ALLOC_LOOPS` value may be
chosen by the user at build time, and defaults to a value of 3.
