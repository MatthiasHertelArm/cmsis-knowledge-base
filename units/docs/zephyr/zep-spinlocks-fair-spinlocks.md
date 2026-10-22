---
id: "zep-spinlocks-fair-spinlocks"
type: "concept"
domain: "rtos"
title: "Spinlocks: Fair spinlocks"
summary: "The default spinlock implementation is built on a single atomic_t variable and does not guarantee fairness between contending CPUs: It is possible for one CPU to repeatedly win the contention, thus starving the others."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

The default spinlock implementation is built on a single `atomic_t` variable and does not
guarantee fairness between contending CPUs:
It is possible for one CPU to repeatedly win the contention, thus starving the others.
Where this matters, enabling `CONFIG_TICKET_SPINLOCKS` switches to a ticket-based
implementation that grants a contended lock to requesting CPUs in FIFO order at the cost of a
slightly larger lock object.
