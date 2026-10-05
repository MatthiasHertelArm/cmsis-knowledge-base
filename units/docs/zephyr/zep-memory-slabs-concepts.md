---
id: "zep-memory-slabs-concepts"
type: "concept"
domain: "rtos"
title: "Memory Slabs: Concepts"
summary: "Any number of memory slabs can be defined (limited only by available RAM). Each memory slab is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/slabs.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/slabs.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of memory slabs can be defined (limited only by available RAM). Each
memory slab is referenced by its memory address.

A memory slab has the following key properties:

* The **block size** of each block, measured in bytes.
  It must be at least 4N bytes long on 32-bit platforms and at least 8N bytes
  long on 64-bit platforms, where N is greater than 0.

* The **number of blocks** available for allocation.
  It must be greater than zero.

* A **buffer** that provides the memory for the memory slab's blocks.
  It must be at least "block size" times "number of blocks" bytes long.

The memory slab's buffer must be aligned to an N-byte boundary, where N is a
power of 2. N must be at least 4 on 32-bit platforms and at least 8 on 64-bit
platforms. To ensure that all memory blocks in the buffer are similarly aligned
to this boundary, the block size must also be a multiple of N.

A memory slab must be initialized before it can be used. This marks all of
its blocks as unused.

A thread that needs to use a memory block simply allocates it from a memory
slab. When the thread finishes with a memory block,
it must release the block back to the memory slab so the block can be reused.

If all the blocks are currently in use, a thread can optionally wait
for one to become available.
Any number of threads may wait on an empty memory slab simultaneously;
when a memory block becomes available, it is given to the highest-priority
thread that has waited the longest.

More than one memory slab can be defined, if needed. This
allows for a memory slab with smaller blocks and others with larger-sized
blocks. Alternatively, a memory pool object may be used.


### Internal Operation


A memory slab's buffer is an array of fixed-size blocks,
with no wasted space between the blocks.

The memory slab keeps track of unallocated blocks using a linked list.
32-bit platforms use the first 4 bytes of each unused block to provide the
necessary linkage, while 64-bit platforms use the first 8 bytes of each
unused block.
