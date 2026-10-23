---
id: "zep-memory-heaps-system-heap"
type: "concept"
domain: "rtos"
title: "Memory Heaps: System Heap"
summary: "The system heap is a predefined memory allocator that allows threads to dynamically allocate memory from a common memory region in a malloc-like manner."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/heap.rst"
license: "Apache-2.0"
mode: "V"
---

The `system heap` is a predefined memory allocator that allows
threads to dynamically allocate memory from a common memory region in
a `malloc`-like manner.

Only a single system heap is defined. Unlike other heaps or memory
pools, the system heap cannot be directly referenced using its
memory address.

The size of the system heap is configurable to arbitrary sizes,
subject to space availability.

A thread can dynamically allocate a chunk of heap memory by calling
`k_malloc`. The address of the allocated chunk is
guaranteed to be aligned on a multiple of pointer sizes. If a suitable
chunk of heap memory cannot be found `NULL` is returned.

When the thread is finished with a chunk of heap memory it can release
the chunk back to the system heap by calling `k_free`.


### Defining the Heap Memory Pool


The size of the heap memory pool is specified using the
`CONFIG_HEAP_MEM_POOL_SIZE` configuration option.

By default, the heap memory pool size is zero bytes. This value instructs
the kernel not to define the heap memory pool object. The maximum size is limited
by the amount of available memory in the system. The project build will fail in
the link stage if the size specified can not be supported.

In addition, each subsystem (board, driver, library, etc) can set a custom
requirement by defining a Kconfig option with the prefix
`HEAP_MEM_POOL_ADD_SIZE_` (this value is in bytes). If multiple subsystems
specify custom values, the sum of these will be used as the minimum requirement.
If the application tries to set a value that's less than the minimum value, this
will be ignored and the minimum value will be used instead.

To force a smaller than minimum value to be used, the application may enable the
`CONFIG_HEAP_MEM_POOL_IGNORE_MIN` option. This can be useful
when optimizing the heap size and the minimum requirement can be more accurately
determined for a specific application.


### Allocating Memory


A chunk of heap memory is allocated by calling `k_malloc`.

The following code allocates a 200 byte chunk of heap memory, then fills it
with zeros. A warning is issued if a suitable chunk is not obtained.

```c

char *mem_ptr;

mem_ptr = k_malloc(200);
if (mem_ptr != NULL)) {
    memset(mem_ptr, 0, 200);
...
} else {
    printf("Memory not allocated");
}
```

### Releasing Memory


A chunk of heap memory is released by calling `k_free`.

The following code allocates a 75 byte chunk of memory, then releases it
once it is no longer needed.

```c

char *mem_ptr;

mem_ptr = k_malloc(75);
... /* use memory block */
k_free(mem_ptr);
```

### Suggested Uses


Use the heap memory pool to dynamically allocate memory in a
`malloc`-like manner.


### Configuration Options


Related configuration options:

* `CONFIG_HEAP_MEM_POOL_SIZE`


### API Reference
