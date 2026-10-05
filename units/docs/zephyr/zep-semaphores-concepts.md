---
id: "zep-semaphores-concepts"
type: "concept"
domain: "rtos"
title: "Semaphores: Concepts"
summary: "Any number of semaphores can be defined (limited only by available RAM). Each semaphore is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/semaphores.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/semaphores.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of semaphores can be defined (limited only by available RAM). Each
semaphore is referenced by its memory address.

A semaphore has the following key properties:

* A **count** that indicates the number of times the semaphore can be taken.
  A count of zero indicates that the semaphore is unavailable.

* A **limit** that indicates the maximum value the semaphore's count
  can reach.

A semaphore must be initialized before it can be used. Its count must be set
to a non-negative value that is less than or equal to its limit.

A semaphore may be **given** by a thread or an ISR. Giving the semaphore
increments its count, unless the count is already equal to the limit.

A semaphore may be **taken** by a thread. Taking the semaphore
decrements its count, unless the semaphore is unavailable (i.e. at zero).
When a semaphore is unavailable, a thread may choose to wait for it to be given.
Any number of threads may wait on an unavailable semaphore simultaneously.
When the semaphore is given, it is taken by the highest priority thread
that has waited longest.


**Note:** You may initialize a "full" semaphore (count equal to limit) to limit the number of threads able to execute the critical section at the same time. You may also initialize an empty semaphore (count equal to 0, with a limit greater than 0) to create a gate through which no waiting thread may pass until the semaphore is incremented. All standard use cases of the common semaphore are supported.


**Note:** The kernel does allow an ISR to take a semaphore, however the ISR must not attempt to wait if the semaphore is unavailable.
