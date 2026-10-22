---
id: "zep-threads-thread-introspection"
type: "concept"
domain: "rtos"
title: "Threads: Thread Introspection"
summary: "The kernel provides several interfaces for inspecting threads at run time."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel provides several interfaces for inspecting threads at run time.

**Identifying the current thread**
    `k_current_get` returns the thread id (`k_tid_t`) of the
    thread that is currently executing. This id can be passed to the other
    thread APIs to operate on the calling thread.

**Reading a thread's priority**
    `k_thread_priority_get` returns the current scheduling priority of a
    thread. This reflects any changes made since the thread was created, for
    example by `k_thread_priority_set`.

**Obtaining a thread's state**
    `k_thread_state_str` writes a human-readable representation of a
    thread's current state (for example `pending`, `suspended`, or
    `ready`) into a caller-supplied buffer. This is intended for diagnostic
    output and should not be parsed programmatically.

**Iterating over all threads**
    When `CONFIG_THREAD_MONITOR` is enabled,
    `k_thread_foreach` invokes a caller-supplied callback once for each
    thread in the system. It holds an internal lock that blocks thread creation
    and termination for the duration of the iteration, which guarantees a
    consistent snapshot of the thread list but can introduce latency
    proportional to the number of threads. `k_thread_foreach_unlocked`
    is a lower-latency variant that releases the lock around each callback at the
    cost of a less strictly consistent view.

**Querying stack usage**
    When `CONFIG_INIT_STACKS` and
    `CONFIG_THREAD_STACK_INFO` are enabled,
    `k_thread_stack_space_get` reports the number of unused bytes
    remaining in a thread's stack, computed by scanning the stack for its unused
    (still-initialized) region. This complements the build-time stack analysis
    tools and the runtime stack safety feature described below.

**Querying a pending timeout**
    A thread that is blocked on a timed operation (such as `k_sleep` or
    a kernel object operation with a timeout) has a pending timeout. Its
    remaining duration can be queried in ticks with
    `k_thread_timeout_remaining_ticks`, and the absolute system tick at
    which it will expire with `k_thread_timeout_expires_ticks`. Both
    return zero if the thread has no pending timeout.
