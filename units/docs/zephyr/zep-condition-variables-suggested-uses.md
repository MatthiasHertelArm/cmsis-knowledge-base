---
id: "zep-condition-variables-suggested-uses"
type: "concept"
domain: "rtos"
title: "Condition Variables: Suggested Uses"
summary: "Use condition variables with a mutex to signal changing states (conditions) from one thread to another thread. Condition variables are not the condition itself and they are not events. The condition is contained in the surrounding programming logic."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/condvar.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/condvar.rst"
license: "Apache-2.0"
mode: "V"
---

Use condition variables with a mutex to signal changing states (conditions) from
one thread to another thread.
Condition variables are not the condition itself and they are not events.
The condition is contained in the surrounding programming logic.

Mutexes alone are not designed for use as a notification/synchronization
mechanism. They are meant to provide mutually exclusive access to a shared
resource only.
