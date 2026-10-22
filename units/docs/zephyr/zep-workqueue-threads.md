---
id: "zep-workqueue-threads"
type: "concept"
domain: "rtos"
title: "Workqueue Threads"
summary: "A workqueue is a kernel object that uses a dedicated thread to process work items in a first in, first out manner. Each work item is processed by calling the function specified by the work item."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

A `workqueue` is a kernel object that uses a dedicated thread to process
work items in a first in, first out manner. Each work item is processed by
calling the function specified by the work item. A workqueue is typically
used by an ISR or a high-priority thread to offload non-urgent processing
to a lower-priority thread so it does not impact time-sensitive processing.

Any number of workqueues can be defined (limited only by available RAM). Each
workqueue is referenced by its memory address.

A workqueue has the following key properties:

* A **queue** of work items that have been added, but not yet processed.

* A **thread** that processes the work items in the queue. The priority of the
  thread is configurable, allowing it to be either cooperative or preemptive
  as required.

Regardless of workqueue thread priority the workqueue thread will yield
between each submitted work item, to prevent a cooperative workqueue from
starving other threads.

A workqueue must be initialized before it can be used. This sets its queue to
empty and spawns the workqueue's thread.  The thread runs forever, but sleeps
when no work items are available.
