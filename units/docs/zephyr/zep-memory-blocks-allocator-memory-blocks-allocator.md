---
id: "zep-memory-blocks-allocator-memory-blocks-allocator"
type: "concept"
domain: "rtos"
title: "Memory Blocks Allocator: Memory Blocks Allocator"
summary: "Internally, the memory blocks allocator uses a bitmap to keep track of which blocks have been allocated. Each allocator, utilizing the sys_bitarray interface, gets memory blocks one by one from the backing buffer up to the requested number of blocks."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/sys_mem_blocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/sys_mem_blocks.rst"
license: "Apache-2.0"
mode: "V"
---

Internally, the memory blocks allocator uses a bitmap to keep track of
which blocks have been allocated. Each allocator, utilizing
the `sys_bitarray` interface, gets memory blocks one by one from
the backing buffer up to the requested number of blocks.
All the metadata about an allocator is stored outside of the backing
buffer. This allows the memory region of the backing buffer to be
powered down to conserve energy, as the allocator code never touches
the content of the buffer.
