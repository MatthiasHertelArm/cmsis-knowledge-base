---
id: "zep-workqueue-threads-work-item-lifecycle"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: Work Item Lifecycle"
summary: "Any number of work items can be defined. Each work item is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of **work items** can be defined. Each work item is referenced
by its memory address.

A work item is assigned a **handler function**, which is the function
executed by the workqueue's thread when the work item is processed. This
function accepts a single argument, which is the address of the work item
itself.  The work item also maintains information about its status.

A work item must be initialized before it can be used. This records the work
item's handler function and marks it as not pending.

A work item may be **queued** (`K_WORK_QUEUED`) by submitting it to a
workqueue by an ISR or a thread.  Submitting a work item appends the work item
to the workqueue's queue.  Once the workqueue's thread has processed all of
the preceding work items in its queue the thread will remove the next work
item from the queue and invoke the work item's handler function. Depending on
the scheduling priority of the workqueue's thread, and the work required by
other items in the queue, a queued work item may be processed quickly or it
may remain in the queue for an extended period of time.

A delayable work item may be **scheduled** (`K_WORK_DELAYED`) to a
workqueue; see Delayable Work.

A work item will be **running** (`K_WORK_RUNNING`) when it is running
on a work queue, and may also be **canceling** (`K_WORK_CANCELING`)
if it started running before a thread has requested that it be cancelled.

A work item can be in multiple states; for example it can be:

* running on a queue;
* marked canceling (because a thread used `k_work_cancel_sync()` to
  wait until the work item completed);
* queued to run again on the same queue;
* scheduled to be submitted to a (possibly different) queue

*all simultaneously*.  A work item that is in any of these states is **pending**
(`k_work_is_pending()`) or **busy** (`k_work_busy_get()`).

A handler function can use any kernel API available to threads. However,
operations that are potentially blocking (e.g. taking a semaphore) must be
used with care, since the workqueue cannot process subsequent work items in
its queue until the handler function finishes executing.

The single argument that is passed to a handler function can be ignored if it
is not required. If the handler function requires additional information about
the work it is to perform, the work item can be embedded in a larger data
structure. The handler function can then use the argument value to compute the
address of the enclosing data structure with `CONTAINER_OF`, and
thereby obtain access to the additional information it needs.

A work item is typically initialized once and then submitted to a specific
workqueue whenever work needs to be performed. If an ISR or a thread attempts
to submit a work item that is already queued the work item is not affected;
the work item remains in its current place in the workqueue's queue, and
the work is only performed once.

A handler function is permitted to re-submit its work item argument
to the workqueue, since the work item is no longer queued at that time.
This allows the handler to execute work in stages, without unduly delaying
the processing of other work items in the workqueue's queue.


**Important:** A pending work item *must not* be altered until the item has been processed by the workqueue thread. This means a work item must not be re-initialized while it is busy. Furthermore, any additional information the work item's handler function needs to perform its work must not be altered until the handler function has finished executing.
