---
id: "zep-threads-thread-stack-objects"
type: "concept"
domain: "rtos"
title: "Threads: Thread Stack objects"
summary: "Every thread requires its own stack buffer for the CPU to push context. Depending on configuration, there are several constraints that must be met:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

Every thread requires its own stack buffer for the CPU to push context.
Depending on configuration, there are several constraints that must be
met:

- There may need to be additional memory reserved for memory management
  structures
- If guard-based stack overflow detection is enabled, a small write-protected
  memory management region must immediately precede the stack buffer
  to catch overflows.
- If userspace is enabled, a separate fixed-size privilege elevation stack must
  be reserved to serve as a private kernel stack for handling system calls.
- If userspace is enabled, the thread's stack buffer must be appropriately
  sized and aligned such that a memory protection region may be programmed
  to exactly fit.

The alignment constraints can be quite restrictive, for example some MPUs
require their regions to be of some power of two in size, and aligned to its
own size.

Because of this, portable code can't simply pass an arbitrary character buffer
to `k_thread_create`. Special macros exist to instantiate stacks
statically, prefixed with `K_KERNEL_STACK` and `K_THREAD_STACK`.

Additionally, stacks may be instantiated dynamically using
`k_thread_stack_alloc` and subsequently freed with
`k_thread_stack_free`.


### Kernel-only Stacks


If it is known that a thread will never run in user mode, or the stack is
being used for special contexts like handling interrupts, it is best to
define stacks using the `K_KERNEL_STACK` macros.

These stacks save memory because an MPU region will never need to be
programmed to cover the stack buffer itself, and the kernel will not need
to reserve additional room for the privilege elevation stack, or memory
management data structures which only pertain to user mode threads.

Attempts from user mode to use stacks declared in this way will result in
a fatal error for the caller.

If `CONFIG_USERSPACE` is not enabled, the set of `K_THREAD_STACK` macros
have an identical effect to the `K_KERNEL_STACK` macros.


### Thread stacks


If it is known that a stack will need to host user threads, or if this
cannot be determined, define the stack with `K_THREAD_STACK` macros.
This may use more memory but the stack object is suitable for hosting
user threads.

If `CONFIG_USERSPACE` is not enabled, the set of `K_THREAD_STACK` macros
have an identical effect to the `K_KERNEL_STACK` macros.
