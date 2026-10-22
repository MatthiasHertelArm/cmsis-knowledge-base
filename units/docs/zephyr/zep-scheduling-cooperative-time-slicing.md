---
id: "zep-scheduling-cooperative-time-slicing"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Cooperative Time Slicing"
summary: "Once a cooperative thread becomes the current thread, it remains the current thread until it performs an action that makes it unready."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

Once a cooperative thread becomes the current thread, it remains
the current thread until it performs an action that makes it unready.
Consequently, if a cooperative thread performs lengthy computations,
it may cause an unacceptable delay in the scheduling of other threads,
including those of higher priority and equal priority.


To overcome such problems, a cooperative thread can voluntarily relinquish
the CPU from time to time to permit other threads to execute.
A thread can relinquish the CPU in two ways:

* Calling `k_yield` puts the thread at the back of the scheduler's
  prioritized list of ready threads, and then invokes the scheduler.
  All ready threads whose priority is higher or equal to that of the
  yielding thread are then allowed to execute before the yielding thread is
  rescheduled. If no such ready threads exist, the scheduler immediately
  reschedules the yielding thread without context switching.

* Calling `k_sleep` makes the thread unready for a specified
  time period. Ready threads of *all* priorities are then allowed to execute;
  however, there is no guarantee that threads whose priority is lower
  than that of the sleeping thread will actually be scheduled before
  the sleeping thread becomes ready once again.
