---
id: "zep-spinlocks-spinlocks-on-uniprocessor-systems"
type: "concept"
domain: "rtos"
title: "Spinlocks: Spinlocks on uniprocessor systems"
summary: "In a kernel built with CONFIG_SMP disabled, a spinlock does not actually spin. With only one CPU there is nothing to contend with, so k_spin_lock reduces to masking interrupts on the local CPU."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

In a kernel built with `CONFIG_SMP` disabled, a spinlock does not actually spin.
With only one CPU there is nothing to contend with, so `k_spin_lock` reduces to masking
interrupts on the local CPU.
This prevents both ISRs and context switches from observing the protected data mid-update, which is
all that is needed for mutual exclusion on a uniprocessor.
