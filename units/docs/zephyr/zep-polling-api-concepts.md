---
id: "zep-polling-api-concepts"
type: "concept"
domain: "rtos"
title: "Polling API: Concepts"
summary: "The polling API's main function is k_poll, which is very similar in concept to the POSIX poll function, except that it operates on kernel objects rather than on file descriptors."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/polling.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/polling.rst"
license: "Apache-2.0"
mode: "V"
---

The polling API's main function is `k_poll`, which is very similar
in concept to the POSIX `poll` function, except that it operates on
kernel objects rather than on file descriptors.

The polling API allows a single thread to wait concurrently for one or more
conditions to be fulfilled without actively looking at each one individually.

There is a limited set of such conditions:

- a semaphore becomes available
- a kernel FIFO contains data ready to be retrieved
- a kernel LIFO contains data ready to be retrieved
- a kernel message queue contains data ready to be retrieved
- a kernel pipe contains data ready to be retrieved, or has been closed
- a poll signal is raised

A thread that wants to wait on multiple conditions must define an array of
**poll events**, one for each condition.

All events in the array must be initialized before the array can be polled on.

Each event must specify which **type** of condition must be satisfied so that
its state is changed to signal the requested condition has been met.

Each event must specify what **kernel object** it wants the condition to be
satisfied for.

Each event must specify which **mode** of operation is used when the condition
is satisfied.

Each event can optionally specify a **tag** to group multiple events together,
at the user's discretion.

Apart from the kernel objects, there is also a **poll signal** pseudo-object
type that be directly signaled.

The `k_poll` function returns as soon as one of the conditions it
is waiting for is fulfilled. It is possible for more than one to be fulfilled
when `k_poll` returns, if they were fulfilled before
`k_poll` was called, or due to the preemptive multi-threading
nature of the kernel. The caller must look at the state of all the poll events
in the array to figure out which ones were fulfilled and what actions to take.

Currently, there is only one mode of operation available: the object is not
acquired. As an example, this means that when `k_poll` returns and
the poll event states that the semaphore is available, the caller of
`k_poll()` must then invoke `k_sem_take` to take
ownership of the semaphore. If the semaphore is contested, there is no
guarantee that it will be still available when `k_sem_take` is
called.
