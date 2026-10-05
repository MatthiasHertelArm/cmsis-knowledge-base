---
id: "zep-memory-heaps-multi-heap-wrapper-utility"
type: "concept"
domain: "rtos"
title: "Memory Heaps: Multi-Heap Wrapper Utility"
summary: "The sys_heap utility requires that all managed memory be in a single contiguous block. It is common for complicated microcontroller applications to have more complicated memory setups that they still want to manage dynamically as a \"heap\"."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/heap.rst"
license: "Apache-2.0"
mode: "V"
---

The `sys_heap` utility requires that all managed memory be in a
single contiguous block.  It is common for complicated microcontroller
applications to have more complicated memory setups that they still
want to manage dynamically as a "heap".  For example, the memory might
exist as separate discontiguous regions, different areas may have
different cache, performance or power behavior, peripheral devices may
only be able to perform DMA to certain regions, etc...

For those situations, Zephyr provides a `sys_multi_heap` utility.
Effectively this is a simple wrapper around a set of one or more
`sys_heap` objects.  It should be initialized after its child heaps
via `sys_multi_heap_init`, after which each heap can be added
to the managed set via `sys_multi_heap_add_heap`.  No
destruction utility is provided; just as for `sys_heap`,
applications that want to destroy a multi heap should simply ensure
all allocated blocks are freed (or at least will never be used again)
and repurpose the underlying memory for another usage.

It has a single pair of allocation entry points,
`sys_multi_heap_alloc` and
`sys_multi_heap_aligned_alloc`.  These behave identically to
the `sys_heap` functions with similar names, except that they also
accept an opaque "configuration" parameter.  This pointer is
uninspected by the multi heap code itself; instead it is passed to a
callback function provided at initialization time.  This
application-provided callback is responsible for doing the underlying
allocation from one of the managed heaps, and may use the
configuration parameter in any way it likes to make that decision.

For modifying the size of an allocated buffer (whether shrinking
or enlarging it), you can use the
`sys_multi_heap_realloc` and
`sys_multi_heap_aligned_realloc` APIs.  If the buffer cannot be
enlarged on the heap where it currently resides,
any of the eligible heaps specified by the configuration parameter may be used.

When unused, a multi heap may be freed via
`sys_multi_heap_free`.  The application does not need to pass
a configuration parameter.  Memory allocated from any of the managed
`sys_heap` objects may be freed with in the same way.
