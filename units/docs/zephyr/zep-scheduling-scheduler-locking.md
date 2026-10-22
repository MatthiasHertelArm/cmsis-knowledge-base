---
id: "zep-scheduling-scheduler-locking"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Scheduler Locking"
summary: "A preemptible thread that does not wish to be preempted while performing a critical operation can instruct the scheduler to temporarily treat it as a cooperative thread by calling k_sched_lock."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

A preemptible thread that does not wish to be preempted while performing
a critical operation can instruct the scheduler to temporarily treat it
as a cooperative thread by calling `k_sched_lock`. This prevents
other threads from interfering while the critical operation is being performed.

Once the critical operation is complete the preemptible thread must call
`k_sched_unlock` to restore its normal, preemptible status.

If a thread calls `k_sched_lock` and subsequently performs an
action that makes it unready, the scheduler will switch the locking thread out
and allow other threads to execute. When the locking thread again
becomes the current thread, its non-preemptible status is maintained.


**Note:** Locking out the scheduler is a more efficient way for a preemptible thread to prevent preemption than changing its priority level to a negative value.
