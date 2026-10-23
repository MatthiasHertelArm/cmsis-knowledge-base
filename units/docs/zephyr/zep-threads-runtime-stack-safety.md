---
id: "zep-threads-runtime-stack-safety"
type: "concept"
domain: "rtos"
title: "Threads: Runtime Stack Safety"
summary: "When CONFIG_THREAD_RUNTIME_STACK_SAFETY is enabled, the kernel provides routines that scan a thread's stack at runtime to determine how much of it remains unused."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

When `CONFIG_THREAD_RUNTIME_STACK_SAFETY` is enabled, the kernel
provides routines that scan a thread's stack at runtime to determine how much of
it remains unused. If the amount of unused stack space is found to have dropped
below a configurable per-thread threshold, a user-defined handler is invoked.

This feature is intended for use by monitoring software. The handler may, for
example, log a warning, suspend or abort the offending thread, or even reboot
the system. It complements the build-time stack analysis tools and the
hardware-based stack overflow detection by allowing a system to react *before*
a stack is exhausted.

Each thread has an *unused stack threshold*, expressed in bytes. When a stack
safety check finds that a thread's unused stack space is below this threshold,
the supplied handler is called. A threshold of 0 bytes (the default) disables
the check for that thread. The default threshold applied to newly created
threads is derived from
`CONFIG_THREAD_RUNTIME_STACK_SAFETY_DEFAULT_UNUSED_THRESHOLD_PCT`,
which expresses it as a percentage of each thread's total stack size.

The threshold for an individual thread can be set or queried at runtime:

* `k_thread_runtime_stack_unused_threshold_pct_set` sets the threshold
  as a percentage (0 to 99) of the thread's total stack size.
* `k_thread_runtime_stack_unused_threshold_set` sets the threshold as an
  absolute number of bytes.
* `k_thread_runtime_stack_unused_threshold_get` retrieves the current
  threshold (in bytes).

Two routines perform the actual check. Both accept a pointer that, on return,
receives the amount of unused stack space, and a
`k_thread_stack_safety_handler_t` handler (plus a user argument) that is
invoked if the threshold has been crossed:

* `k_thread_runtime_stack_safety_full_check` scans the entire stack to
  compute the exact amount of unused space.
* `k_thread_runtime_stack_safety_threshold_check` performs an
  abbreviated scan that only looks for evidence that the thread has crossed its
  configured threshold. This is cheaper than a full check but does not yield an
  exact measure of unused space.

Here is an example that configures a thread to invoke a handler once its unused
stack space drops below 10% of its total stack size:

```c

void stack_safety_handler(const struct k_thread *thread,
                          size_t unused_space, void *arg)
{
        printk("Thread %p low on stack: %zu bytes unused\n",
               thread, unused_space);
}

/* Trigger the handler once less than 10% of the stack remains unused */
k_thread_runtime_stack_unused_threshold_pct_set(my_tid, 10);

/* Periodically check the thread from a monitoring context */
k_thread_runtime_stack_safety_full_check(my_tid, NULL,
                                         stack_safety_handler, NULL);
```
