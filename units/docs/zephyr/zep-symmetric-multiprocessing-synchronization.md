---
id: "zep-symmetric-multiprocessing-synchronization"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing: Synchronization"
summary: "At the application level, core Zephyr IPC and synchronization primitives all behave identically under an SMP kernel. For example semaphores used to implement blocking mutual exclusion continue to be a proper application choice."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

At the application level, core Zephyr IPC and synchronization
primitives all behave identically under an SMP kernel.  For example
semaphores used to implement blocking mutual exclusion continue to be
a proper application choice.

At the lowest level, however, Zephyr code has often used the
`irq_lock`/`irq_unlock` primitives to implement fine grained
critical sections using interrupt masking.  These APIs continue to
work via an emulation layer (see below), but the masking technique
does not: the fact that your CPU will not be interrupted while you are
in your critical section says nothing about whether a different CPU
will be running simultaneously and be inspecting or modifying the same
data!


### Spinlocks


SMP systems provide a more constrained `k_spin_lock` primitive that
masks interrupts locally, like `irq_lock`, while also atomically
guarding a shared lock variable so that only one CPU enters the critical
section at a time. Unlike the legacy IRQ locks, spinlocks are separable and
must not be acquired recursively. See spinlocks for a full description,
including ticket spinlocks and the API reference.


### Legacy irq_lock() emulation


For the benefit of applications written to the uniprocessor locking
API, `irq_lock` and `irq_unlock` continue to work compatibly on
SMP systems with identical semantics to their legacy versions.  They
are implemented as a single global spinlock, with a nesting count and
the ability to be atomically reacquired on context switch into locked
threads.  The kernel will ensure that only one thread across all CPUs
can hold the lock at any time, that it is released on context switch,
and that it is re-acquired when necessary to restore the lock state
when a thread is switched in.  Other CPUs will spin waiting for the
release to happen.

The overhead involved in this process has measurable performance
impact, however.  Unlike uniprocessor apps, SMP apps using
`irq_lock` are not simply invoking a very short (often ~1
instruction) interrupt masking operation.  That, and the fact that the
IRQ lock is global, means that code expecting to be run in an SMP
context should be using the spinlock API wherever possible.


### Memory Coherence


Some multiprocessor architectures are *cache-incoherent*: the per-CPU caches are
not automatically kept consistent with each other, so data written by one CPU may
not be visible to another until it is flushed from the cache. On such systems,
shared kernel data structures must reside in memory that all CPUs observe
consistently.

When `CONFIG_KERNEL_COHERENCE` is enabled, the kernel places all
shared data into multiprocessor-coherent (generally uncached) memory. Thread
stacks remain cached, as does application memory explicitly declared with
`__incoherent`. This mode is intended only for SMP kernels running on
cache-incoherent architectures, and it carries an implicit API contract: any
memory passed to the kernel is assumed to be cache-coherent, so kernel data
structures must not be created in uncached regions.
