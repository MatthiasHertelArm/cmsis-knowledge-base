---
id: "zep-memory-blocks-allocator-concepts"
type: "concept"
domain: "rtos"
title: "Memory Blocks Allocator: Concepts"
summary: "Any number of Memory Blocks Allocator can be defined (limited only by available RAM). Each allocator is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/sys_mem_blocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/sys_mem_blocks.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of Memory Blocks Allocator can be defined (limited only by
available RAM). Each allocator is referenced by its memory address.

A memory blocks allocator has the following key properties:

* The **block size** of each block, measured in bytes.
  It must be at least 4N bytes long, where N is greater than 0.

* The **number of blocks** available for allocation.
  It must be greater than zero.

* A **buffer** that provides the backing store from which the memory blocks
  allocator will allocate blocks.
  It must be at least "block size" times "number of blocks" bytes long.

* A **blocks bitmap** to keep track of which block has been allocated.

The buffer must be aligned to an N-byte boundary, where N is a power of 2
larger than 2 (i.e. 4, 8, 16, ...). To ensure that all memory blocks in
the buffer are similarly aligned to this boundary, the block size must
also be a multiple of N.

Due to the use of internal bookkeeping structures and their creation,
each memory blocks allocator must be declared and defined at compile time.


### Internal Operation


Each buffer associated with an allocator is an array of fixed-size blocks,
with no wasted space between the blocks.

The memory blocks allocator keeps track of unallocated blocks using
a bitmap.
