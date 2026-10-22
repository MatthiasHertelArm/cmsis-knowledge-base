---
id: "zep-scheduling-preemptive-time-slicing"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Preemptive Time Slicing"
summary: "Once a preemptive thread becomes the current thread, it remains the current thread until a higher priority thread becomes ready, or until the thread performs an action that makes it unready."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

Once a preemptive thread becomes the current thread, it remains
the current thread until a higher priority thread becomes ready,
or until the thread performs an action that makes it unready.
Consequently, if a preemptive thread performs lengthy computations,
it may cause an unacceptable delay in the scheduling of other threads,
including those of equal priority.


To overcome such problems, a preemptive thread can perform cooperative
time slicing (as described above), or the scheduler's time slicing capability
can be used to allow other threads of the same priority to execute.


**Note:** For SMP, the behavior would be similar to the above UP image, except that Thread 1 would not immediately follow Thread 4. Instead it would be Thread 2, Thread 3, Thread 1, ....

The scheduler divides time on each CPU into a series of **time slices**, where
slices are measured in system clock ticks. The time slice size is configurable,
but this size can be changed while the application is running. Scheduling a
new thread causes the time slice timer to be reset.

At the end of every time slice, the scheduler checks to see if the current
thread is preemptible and, if so, implicitly invokes `k_yield`
on behalf of the thread. This gives other ready threads of the same priority
the opportunity to execute before the current thread is scheduled again. If no
other threads of equal priority are ready, then the current thread remains
the current thread.

Threads with a priority higher than specified limit are exempt from preemptive
time slicing, and are never preempted by a thread of equal priority.
This allows an application to use preemptive time slicing
only when dealing with lower priority threads that are less time-sensitive.


**Note:** The kernel's time slicing algorithm does *not* ensure that a set of equal-priority threads receive an equitable amount of CPU time, since it does not measure the amount of time a thread actually gets to execute. However, the algorithm *does* ensure that a thread never executes for longer than a single time slice without being required to yield.
