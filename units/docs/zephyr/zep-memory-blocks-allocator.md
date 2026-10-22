---
id: "zep-memory-blocks-allocator"
type: "concept"
domain: "rtos"
title: "Memory Blocks Allocator"
summary: "The Memory Blocks Allocator allows memory blocks to be dynamically allocated from a designated memory region, where:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/sys_mem_blocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/sys_mem_blocks.rst"
license: "Apache-2.0"
mode: "V"
---

The Memory Blocks Allocator allows memory blocks to be dynamically
allocated from a designated memory region, where:

* All memory blocks have a single fixed size.

* Multiple blocks can be allocated or freed at the same time.

* A group of blocks allocated together may not be contiguous.
  This is useful for operations such as scatter-gather DMA transfers.

* Bookkeeping of allocated blocks is done outside of the associated
  buffer (unlike memory slab). This allows the buffer to reside in
  memory regions where these can be powered down to conserve energy.
