---
id: "zep-spinlocks-suggested-uses"
type: "concept"
domain: "rtos"
title: "Spinlocks: Suggested uses"
summary: "Use a spinlock to protect a short critical section that is shared between threads and interrupt handlers, or between CPUs on an SMP system."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

Use a spinlock to protect a short critical section that is shared between
threads and interrupt handlers, or between CPUs on an SMP system.

Prefer another primitive when it fits better:

* `k_mutex` for a critical section that may be long, may block, or may
  sleep. Only threads can take a mutex.
* `k_sem` for signalling between contexts, and for counting access to a
  pool of resources.
* atomic services when the shared state is a single word that
  can be updated with one atomic operation, in which case no lock is needed.
