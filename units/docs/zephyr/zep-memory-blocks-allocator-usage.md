---
id: "zep-memory-blocks-allocator-usage"
type: "concept"
domain: "rtos"
title: "Memory Blocks Allocator: Usage"
summary: "A memory blocks allocator is defined using a variable of type sys_mem_blocks_t. It needs to be defined and initialized at compile time by calling SYS_MEM_BLOCKS_DEFINE."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/sys_mem_blocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/sys_mem_blocks.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Memory Blocks Allocator


A memory blocks allocator is defined using a variable of type
`sys_mem_blocks_t`. It needs to be defined and initialized
at compile time by calling `SYS_MEM_BLOCKS_DEFINE`.

The following code defines and initializes a memory blocks allocator
which has 4 blocks that are 64 bytes long, each of which is aligned
to a 4-byte boundary:

```c

SYS_MEM_BLOCKS_DEFINE(allocator, 64, 4, 4);
```
Similarly, you can define a memory blocks allocator in private scope:

```c

SYS_MEM_BLOCKS_DEFINE_STATIC(static_allocator, 64, 4, 4);
```
A pre-defined buffer can also be provided to the allocator where
the buffer can be placed separately. Note that the buffer **must**
have its alignment specified when it is defined.

```c

uint8_t __aligned(4) backing_buffer[64 * 4];
SYS_MEM_BLOCKS_DEFINE_WITH_EXT_BUF(allocator, 64, 4, backing_buffer);
```

### Allocating Memory Blocks


Memory blocks can be allocated by calling `sys_mem_blocks_alloc`.

```c

int ret;
uintptr_t blocks[2];

ret = sys_mem_blocks_alloc(allocator, 2, blocks);
```
If `ret == 0`, the array `blocks` will contain an array of memory
addresses pointing to the allocated blocks.


### Releasing a Memory Block


Memory blocks are released by calling `sys_mem_blocks_free`.

The following code builds on the example above which allocates 2 memory blocks,
then releases them once they are no longer needed.

```c

int ret;
uintptr_t blocks[2];

ret = sys_mem_blocks_alloc(allocator, 2, blocks);
... /* perform some operations on the allocated memory blocks */
ret = sys_mem_blocks_free(allocator, 2, blocks);
```

### Using Multi Memory Blocks Allocator Group


The following code demonstrates how to initialize an allocator group:

```c

sys_mem_blocks_t *choice_fn(struct sys_multi_mem_blocks *group, void *cfg)
{
    ... /* choose which allocator in the group to use based on cfg */
}

SYS_MEM_BLOCKS_DEFINE(allocator0, 64, 4, 4);
SYS_MEM_BLOCKS_DEFINE(allocator1, 64, 4, 4);

static sys_multi_mem_blocks_t alloc_group;

sys_multi_mem_blocks_init(&alloc_group, choice_fn);
sys_multi_mem_blocks_add_allocator(&alloc_group, &allocator0);
sys_multi_mem_blocks_add_allocator(&alloc_group, &allocator1);
```
To allocate and free memory blocks from the group:

```c

int ret;
uintptr_t blocks[1];
size_t blk_size;

ret = sys_multi_mem_blocks_alloc(&alloc_group, UINT_TO_POINTER(0),
                                 1, blocks, &blk_size);

ret = sys_multi_mem_blocks_free(&alloc_group, 1, blocks);
```
