---
id: "zep-memory-slabs-implementation"
type: "concept"
domain: "rtos"
title: "Memory Slabs: Implementation"
summary: "A memory slab is defined using a variable of type k_mem_slab. It must then be initialized by calling k_mem_slab_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/slabs.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/slabs.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Memory Slab


A memory slab is defined using a variable of type `k_mem_slab`.
It must then be initialized by calling `k_mem_slab_init`.

The following code defines and initializes a memory slab that has 6 blocks
that are 400 bytes long, each of which is aligned to an 8-byte boundary.

```c

struct k_mem_slab my_slab;
char __aligned(8) my_slab_buffer[6 * 400];

k_mem_slab_init(&my_slab, my_slab_buffer, 400, 6);
```
Alternatively, a memory slab can be defined and initialized at compile time
by calling `K_MEM_SLAB_DEFINE`.

The following code has the same effect as the code segment above. Observe
that the macro defines both the memory slab and its buffer.

```c

K_MEM_SLAB_DEFINE(my_slab, 400, 6, 8);
```
Similarly, you can define a memory slab in private scope:

```c

K_MEM_SLAB_DEFINE_STATIC(my_slab, 400, 6, 8);
```

### Allocating a Memory Block


A memory block is allocated by calling `k_mem_slab_alloc`.

The following code builds on the example above, and waits up to 100 milliseconds
for a memory block to become available, then fills it with zeroes.
A warning is printed if a suitable block is not obtained.

```c

char *block_ptr;

if (k_mem_slab_alloc(&my_slab, (void **)&block_ptr, K_MSEC(100)) == 0) {
    memset(block_ptr, 0, 400);
...
} else {
    printf("Memory allocation time-out");
}
```

### Releasing a Memory Block


A memory block is released by calling `k_mem_slab_free`.

The following code builds on the example above, and allocates a memory block,
then releases it once it is no longer needed.

```c

char *block_ptr;

k_mem_slab_alloc(&my_slab, (void **)&block_ptr, K_FOREVER);
... /* use memory block pointed at by block_ptr */
k_mem_slab_free(&my_slab, (void *)block_ptr);
```

### Querying Slab Usage


The current utilization of a memory slab can be queried at run time.
`k_mem_slab_num_used_get` returns the number of blocks currently
allocated, and `k_mem_slab_num_free_get` returns the number of blocks
still available. When `CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION`
is enabled, `k_mem_slab_max_used_get` reports the peak number of blocks
that have been allocated simultaneously, and
`k_mem_slab_runtime_stats_get` returns these figures together in a
`sys_memory_stats` structure.
