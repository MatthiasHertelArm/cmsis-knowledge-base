---
id: "zep-condition-variables-concepts"
type: "concept"
domain: "rtos"
title: "Condition Variables: Concepts"
summary: "Any number of condition variables can be defined (limited only by available RAM). Each condition variable is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/condvar.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/condvar.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of condition variables can be defined (limited only by available RAM). Each
condition variable is referenced by its memory address.

To wait for a condition to become true, a thread can make use of a condition
variable.

A condition variable is basically a queue of threads that threads can put
themselves on when some state of execution (i.e., some condition) is not as
desired (by waiting on the condition). The function
`k_condvar_wait` performs atomically the following steps;

#. Releases the last acquired mutex.
#. Puts the current thread in the condition variable queue.

Some other thread, when it changes said state, can then wake one (or more)
of those waiting threads and thus allow them to continue by signaling on
the condition using `k_condvar_signal` or
`k_condvar_broadcast` then it:

#. Re-acquires the mutex previously released.
#. Returns from `k_condvar_wait`.

Regardless of why the wait completes -- whether the thread was signaled, the
supplied timeout elapsed, or the wait was requested without blocking --
`k_condvar_wait` always returns with the associated mutex re-locked by
the calling thread.

A condition variable must be initialized before it can be used.
