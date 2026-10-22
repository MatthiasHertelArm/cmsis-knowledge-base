---
id: "zep-memory-heaps-synchronized-heap-allocator"
type: "concept"
domain: "rtos"
title: "Memory Heaps: Synchronized Heap Allocator"
summary: "The simplest way to define a heap is statically, with the K_HEAP_DEFINE macro. This creates a static k_heap variable with a given name that manages a memory region of the specified size."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/heap.rst"
license: "Apache-2.0"
mode: "V"
---

### Creating a Heap


The simplest way to define a heap is statically, with the
`K_HEAP_DEFINE` macro.  This creates a static `k_heap` variable
with a given name that manages a memory region of the
specified size.

Heaps can also be created to manage arbitrary regions of
application-controlled memory using `k_heap_init`.


### Allocating Memory


Memory can be allocated from a heap using `k_heap_alloc`,
passing it the address of the heap object and the number of bytes
desired.  This functions similarly to standard C `malloc()`,
returning a NULL pointer on an allocation failure.

The heap supports blocking operation, allowing threads to go to sleep
until memory is available.  The final argument is a
`k_timeout_t` timeout value indicating how long the thread may
sleep before returning, or else one of the constant timeout values
`K_NO_WAIT` or `K_FOREVER`.

When a block with a specific alignment is required, `k_heap_aligned_alloc`
allocates a block whose start address is a multiple of a caller-supplied power-of-two
alignment.  `k_heap_calloc` allocates and zero-initializes an array.

The size of an existing allocation can be changed with `k_heap_realloc`,
which returns a block of the requested size while preserving the contents up to
the smaller of the old and new sizes.  As with the standard C `realloc()`, the
returned pointer may differ from the original.


### Releasing Memory


Memory allocated with `k_heap_alloc` must be released using
`k_heap_free`.  Similar to standard C `free()`, the pointer
provided must be either a `NULL` value or a pointer previously
returned by `k_heap_alloc` for the same heap.  Freeing a
`NULL` value is defined to have no effect.


### Enumerating Heaps


All heaps defined statically with `K_HEAP_DEFINE` are placed in a
dedicated linker section, which allows them to be enumerated at run time.
`k_heap_array_get` returns the address of the array of statically
defined heaps and the number of entries it contains.  This is primarily useful
for instrumentation and diagnostics that need to inspect every heap in the
system.
