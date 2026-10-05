---
id: "zep-spinlocks-spinlock-validation"
type: "concept"
domain: "rtos"
title: "Spinlocks: Spinlock validation"
summary: "A validation layer, enabled with CONFIG_SPIN_VALIDATE, is available to detect various misuses of spinlocks. It can detect the following:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

A validation layer, enabled with `CONFIG_SPIN_VALIDATE`, is available to detect
various misuses of spinlocks. It can detect the following:

* Recursive acquisition of a spinlock
* Release of a spinlock that is not held by the current context
* Out-of-order release of spinlocks (an outer lock released while an inner lock is still held)
* Context switching while a spinlock is held, or while interrupts are masked by a nested
  `irq_lock`

On a uniprocessor system, only the recursive acquisition check is meaningful. The other misuses
cannot occur, since there is no contention and interrupts are masked while the lock is held.
