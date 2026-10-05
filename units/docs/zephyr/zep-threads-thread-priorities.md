---
id: "zep-threads-thread-priorities"
type: "concept"
domain: "rtos"
title: "Threads: Thread Priorities"
summary: "A thread's priority is an integer value, and can be either negative or non-negative. Numerically lower priorities takes precedence over numerically higher values."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

A thread's priority is an integer value, and can be either negative or
non-negative.
Numerically lower priorities takes precedence over numerically higher values.
For example, the scheduler gives thread A of priority 4 *higher* priority
over thread B of priority 7; likewise thread C of priority -2 has higher
priority than both thread A and thread B.

The scheduler distinguishes between two classes of threads,
based on each thread's priority.

* A `cooperative thread` has a negative priority value.
  Once it becomes the current thread, a cooperative thread remains
  the current thread until it performs an action that makes it unready.

* A `preemptible thread` has a non-negative priority value.
  Once it becomes the current thread, a preemptible thread may be supplanted
  at any time if a cooperative thread, or a preemptible thread of higher
  or equal priority, becomes ready.


A thread's initial priority value can be altered up or down after the thread
has been started. Thus it is possible for a preemptible thread to become
a cooperative thread, and vice versa, by changing its priority.


**Note:** The scheduler does not make heuristic decisions to re-prioritize threads. Thread priorities are set and changed only at the application's request.

The kernel supports a virtually unlimited number of thread priority levels.
The configuration options `CONFIG_NUM_COOP_PRIORITIES` and
`CONFIG_NUM_PREEMPT_PRIORITIES` specify the number of priority
levels for each class of thread, resulting in the following usable priority
ranges:

* cooperative threads: (-`CONFIG_NUM_COOP_PRIORITIES`) to -1
* preemptive threads: 0 to (`CONFIG_NUM_PREEMPT_PRIORITIES` - 1)

For example, configuring 5 cooperative priorities and 10 preemptive priorities
results in the ranges -5 to -1 and 0 to 9, respectively.


### Meta-IRQ Priorities


When enabled (see `CONFIG_NUM_METAIRQ_PRIORITIES`), there is a special
subclass of cooperative priorities at the highest (numerically lowest)
end of the priority space: meta-IRQ threads.  These are scheduled
according to their normal priority, but also have the special ability
to preempt all other threads (and other meta-IRQ threads) at lower
priorities, even if those threads are cooperative and/or have taken a
scheduler lock. Meta-IRQ threads are still threads, however,
and can still be interrupted by any hardware interrupt.


**Note:** When a cooperative (or schedule-locked) thread that was preempted by a meta-IRQ thread resumes its execution after the meta-IRQ thread completes, it will be on the same CPU--assuming it was neither suspended nor aborted. This helps ensure that these threads are not unexpectedly shuffled to another CPU while in the midst of querying the properties associated with their own CPU.

This behavior makes the act of unblocking a meta-IRQ thread (by any
means, e.g. creating it, calling k_sem_give(), etc.) into the
equivalent of a synchronous system call when done by a lower
priority thread, or an ARM-like "pended IRQ" when done from true
interrupt context.  The intent is that this feature will be used to
implement interrupt "bottom half" processing and/or "tasklet" features
in driver subsystems.  The thread, once woken, will be guaranteed to
run before the current CPU returns into application code.

Unlike similar features in other OSes, meta-IRQ threads are true
threads and run on their own stack (which must be allocated normally),
not the per-CPU interrupt stack. Design work to enable the use of the
IRQ stack on supported architectures is pending.

Note that because this breaks the promise made to cooperative
threads by the Zephyr API (namely that the OS won't schedule other
thread until the current thread deliberately blocks), it should be
used only with great care from application code.  These are not simply
very high priority threads and should not be used as such.
