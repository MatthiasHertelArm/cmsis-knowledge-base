---
id: "zep-spinlocks"
type: "concept"
domain: "rtos"
title: "Spinlocks"
summary: "A spinlock is the lowest-level mutual-exclusion primitive in Zephyr. It guards a brief critical section so that only one execution context can access a shared resource at a time."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

A spinlock is the lowest-level mutual-exclusion primitive in Zephyr.
It guards a brief critical section so that only one execution context can access a shared resource
at a time. A context that finds the lock already held "spins", busy waiting until the lock becomes
available, rather than blocking and yielding the CPU. This is why spinlocks are only appropriate for
short critical sections.

Acquiring a spinlock also masks interrupts on the local CPU for as long as the lock is held. This is
what makes a spinlock safe to share between threads and interrupt handlers: while a context holds
the lock, no ISR on the same CPU can preempt it and no other CPU can take the same lock, so neither
can observe or corrupt the protected data mid-update.
For these reasons, `k_spinlock` is the primary synchronization primitive used within the
Zephyr kernel itself, protecting access to its core data structures.

Application code may use it directly as well, but it is generally recommended to use a higher-level
synchronization primitive such as a `k_mutex` or `k_sem` instead.
