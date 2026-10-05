---
id: "zep-workqueue-threads-triggered-work"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: Triggered Work"
summary: "The k_work_poll_submit interface schedules a triggered work item in response to a poll event (see polling_v2), that will call a user-defined function when a monitored resource becomes available or poll signal is raised, or a timeout occurs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

The `k_work_poll_submit` interface schedules a triggered work
item in response to a **poll event** (see polling_v2), that will
call a user-defined function when a monitored resource becomes available
or poll signal is raised, or a timeout occurs.
In contrast to `k_poll`, the triggered work does not require
a dedicated thread waiting or actively polling for a poll event.

A triggered work item is a standard work item that has the following
added properties:

* A pointer to an array of poll events that will trigger work item
  submissions to the workqueue

* A size of the array containing poll events.

A triggered work item is initialized and submitted to a workqueue in a similar
manner to a standard work item, although dedicated kernel APIs are used.
When a submit request is made, the kernel begins observing kernel objects
specified by the poll events. Once at least one of the observed kernel
object's changes state, the work item is submitted to the specified workqueue,
where it remains queued until it is processed in the standard manner.


**Important:** The triggered work item as well as the referenced array of poll events have to be valid and cannot be modified for a complete triggered work item lifecycle, from submission to work item execution or cancellation.

An ISR or a thread may **cancel** a triggered work item it has submitted
as long as it is still waiting for a poll event. In such case, the kernel
stops waiting for attached poll events and the specified work is not executed.
Otherwise the cancellation cannot be performed.
