---
id: "zep-memory-protection-design-thread-resource-pools"
type: "concept"
domain: "rtos"
title: "Memory Protection Design: Thread Resource Pools"
summary: "A small subset of kernel APIs, invoked as system calls, require heap memory allocations. This memory is used only by the kernel and is not accessible directly by user mode."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

A small subset of kernel APIs, invoked as system calls, require heap memory
allocations. This memory is used only by the kernel and is not accessible
directly by user mode. In order to use these system calls, invoking threads
must assign themselves to a resource pool, which is a `k_heap`
object. Memory is drawn from a thread's resource pool using
`z_thread_malloc` and freed with `k_free`.

The APIs which use resource pools are as follows, with any alternatives
noted for users who do not want heap allocations within their application:

 - `k_stack_alloc_init` sets up a k_stack with its storage
   buffer allocated out of a resource pool instead of a buffer provided by the
   user. An alternative is to declare k_stacks that are automatically
   initialized at boot with `K_STACK_DEFINE()`, or to initialize the
   k_stack in supervisor mode with `k_stack_init`.

 - `k_msgq_alloc_init` sets up a k_msgq object with its
   storage buffer allocated out of a resource pool instead of a buffer provided
   by the user. An alternative is to declare a k_msgq that is automatically
   initialized at boot with `K_MSGQ_DEFINE()`, or to initialize the
   k_msgq in supervisor mode with `k_msgq_init`.

 - `k_poll` when invoked from user mode, needs to make a kernel-side
   copy of the provided events array while waiting for an event. This copy is
   freed when `k_poll` returns for any reason.

 - `k_queue_alloc_prepend` and `k_queue_alloc_append`
   allocate a container structure to place the data in, since the internal
   bookkeeping information that defines the queue cannot be placed in the
   memory provided by the user.

 - `k_object_alloc` allows for entire kernel objects to be
   dynamically allocated at runtime and a usable pointer to them returned to
   the caller.

The relevant API is `k_thread_heap_assign` which assigns
a k_heap to draw these allocations from for the target thread.

If the system heap is enabled, then the system heap may be used with
`k_thread_system_pool_assign`, but it is preferable for different
logical applications running on the system to have their own pools.
