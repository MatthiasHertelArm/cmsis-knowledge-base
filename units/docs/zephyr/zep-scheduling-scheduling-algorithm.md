---
id: "zep-scheduling-scheduling-algorithm"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Scheduling Algorithm"
summary: "The kernel's scheduler selects the highest priority ready thread to be the current thread. When multiple ready threads of the same priority exist, the scheduler chooses the one that has been waiting longest."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

The kernel's scheduler selects the highest priority ready thread
to be the current thread. When multiple ready threads of the same priority
exist, the scheduler chooses the one that has been waiting longest.

A thread's relative priority is primarily determined by its static priority.
However, when both earliest-deadline-first scheduling is enabled
(`CONFIG_SCHED_DEADLINE`) and a choice of threads have equal
static priority, then the thread with the earlier deadline is considered
to have the higher priority. Thus, when earliest-deadline-first scheduling is
enabled, two threads are only considered to have the same priority when both
their static priorities and deadlines are equal. The routine
`k_thread_deadline_set` is used to set a thread's deadline.


**Note:** Execution of ISRs takes precedence over thread execution, so the execution of the current thread may be replaced by an ISR at any time unless interrupts have been masked. This applies to both cooperative threads and preemptive threads.

The kernel can be built with one of several choices for the ready queue
implementation, offering different choices between code size, constant factor
runtime overhead and performance scaling when many threads are added.

* Simple linked-list ready queue (`CONFIG_SCHED_SIMPLE`)

  The scheduler ready queue will be implemented as a simple unordered list, with
  very fast constant time performance for single threads and very low code size.
  This implementation should be selected on systems with constrained code size
  that will never see more than a small number (3, maybe) of runnable threads in
  the queue at any given time.  On most platforms (that are not otherwise using
  the red/black tree) this results in a savings of ~2k of code size.

* Red/black tree ready queue (`CONFIG_SCHED_SCALABLE`)

  The scheduler ready queue will be implemented as a red/black tree.  This has
  rather slower constant-time insertion and removal overhead, and on most
  platforms (that are not otherwise using the red/black tree somewhere) requires
  an extra ~2kb of code. The resulting behavior will scale cleanly and
  quickly into the many thousands of threads.

  Use this for applications needing many concurrent runnable threads (> 20 or
  so).  Most applications won't need this ready queue implementation.

* Traditional multi-queue ready queue (`CONFIG_SCHED_MULTIQ`)

  When selected, the scheduler ready queue will be implemented as the
  classic/textbook array of lists, one per priority.

  This corresponds to the scheduler algorithm used in Zephyr versions prior to
  1.12.

  It incurs only a tiny code size overhead vs. the "dumb" scheduler and runs in
  O(1) time in almost all circumstances with very low constant factor.  But it
  requires a fairly large RAM budget to store those list heads, and the limited
  features make it incompatible with features like deadline scheduling that
  need to sort threads more finely, and SMP affinity which need to traverse the
  list of threads.

  Typical applications with small numbers of runnable threads probably want the
  simple scheduler.


The wait_q abstraction used in IPC primitives to pend threads for later wakeup
shares the same backend data structure choices as the scheduler, and can use
the same options.

* Scalable wait_q implementation (`CONFIG_WAITQ_SCALABLE`)

  When selected, the wait_q will be implemented with a balanced tree.  Choose
  this if you expect to have many threads waiting on individual primitives.
  There is a ~2kb code size increase over `CONFIG_WAITQ_SIMPLE` (which may
  be shared with `CONFIG_SCHED_SCALABLE`) if the red/black tree is not
  used elsewhere in the application, and pend/unpend operations on "small"
  queues will be somewhat slower (though this is not generally a performance
  path).

* Simple linked-list wait_q (`CONFIG_WAITQ_SIMPLE`)

  When selected, the wait_q will be implemented with a doubly-linked list.
  Choose this if you expect to have only a few threads blocked on any single
  IPC primitive.
