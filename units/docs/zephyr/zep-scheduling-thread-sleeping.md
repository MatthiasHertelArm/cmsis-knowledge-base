---
id: "zep-scheduling-thread-sleeping"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Thread Sleeping"
summary: "A thread can call k_sleep to delay its processing for a specified time period. During the time the thread is sleeping the CPU is relinquished to allow other ready threads to execute."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

A thread can call `k_sleep` to delay its processing
for a specified time period. During the time the thread is sleeping
the CPU is relinquished to allow other ready threads to execute.
Once the specified delay has elapsed the thread becomes ready
and is eligible to be scheduled once again.

A sleeping thread can be woken up prematurely by another thread using
`k_wakeup`. This technique can sometimes be used
to permit the secondary thread to signal the sleeping thread
that something has occurred *without* requiring the threads
to define a kernel synchronization object, such as a semaphore.
Waking up a thread that is not sleeping is allowed, but has no effect.
