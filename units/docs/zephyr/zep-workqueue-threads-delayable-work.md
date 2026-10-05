---
id: "zep-workqueue-threads-delayable-work"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: Delayable Work"
summary: "An ISR or a thread may need to schedule a work item that is to be processed only after a specified period of time, rather than immediately."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

An ISR or a thread may need to schedule a work item that is to be processed
only after a specified period of time, rather than immediately. This can be
done by **scheduling** a **delayable work item** to be submitted to a
workqueue at a future time.

A delayable work item contains a standard work item but adds fields that
record when and where the item should be submitted.

A delayable work item is initialized and scheduled to a workqueue in a similar
manner to a standard work item, although different kernel APIs are used.  When
the schedule request is made the kernel initiates a timeout mechanism that is
triggered after the specified delay has elapsed. Once the timeout occurs the
kernel submits the work item to the specified workqueue, where it remains
queued until it is processed in the standard manner.

Note that work handler used for delayable still receives a pointer to the
underlying non-delayable work structure, which is not publicly accessible from
`k_work_delayable`.  To get access to an object that contains the
delayable work object use this idiom:

```c

static void work_handler(struct k_work *work)
{
        struct k_work_delayable *dwork = k_work_delayable_from_work(work);
        struct work_context *ctx = CONTAINER_OF(dwork, struct work_context,
                                            timed_work);
        ...
```
