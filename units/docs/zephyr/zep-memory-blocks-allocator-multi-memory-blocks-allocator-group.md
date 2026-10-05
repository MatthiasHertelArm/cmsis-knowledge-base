---
id: "zep-memory-blocks-allocator-multi-memory-blocks-allocator-group"
type: "concept"
domain: "rtos"
title: "Memory Blocks Allocator: Multi Memory Blocks Allocator Group"
summary: "The Multi Memory Blocks Allocator Group utility functions are used to conveniently manage a group of allocators. A custom function may be written to choose which allocator managed by this group should be used for block allocation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/sys_mem_blocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/sys_mem_blocks.rst"
license: "Apache-2.0"
mode: "V"
---

The Multi Memory Blocks Allocator Group utility functions are used
to conveniently manage a group of allocators. A custom function may
be written to choose which allocator managed by this group should
be used for block allocation.

An allocator group should be initialized at runtime via
`sys_multi_mem_blocks_init`. Each allocator can then be
added via `sys_multi_mem_blocks_add_allocator`.

To allocate memory blocks from group,
`sys_multi_mem_blocks_alloc` is called with an opaque
"configuration" parameter. This parameter is passed directly to
the allocator choice function so that an appropriate allocator
can be chosen. After an allocator is chosen, memory blocks are
allocated via `sys_mem_blocks_alloc`.

Allocated memory blocks can be freed via
`sys_multi_mem_blocks_free`. The caller does not need to
pass a configuration parameter. The allocator code matches
the passed in memory addresses to find the correct allocator
and then memory blocks are freed via `sys_mem_blocks_free`.
