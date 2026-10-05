---
id: "threadx-chapter-3-functional-components-of-preemption-threshold"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Preemption Threshold"
summary: "To ease some of the inherent problems of preemption, ThreadX provides a unique and advanced feature called preemption-threshold."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#preemption-threshold"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

To ease some of the inherent problems of preemption, ThreadX provides a unique and advanced feature called *preemption-threshold*.

A preemption-threshold allows a thread to specify a priority *ceiling* for disabling preemption. Threads that have higher priorities than the ceiling are still allowed to preempt, while those less than the ceiling are not allowed to preempt.

For example, suppose a thread of priority 20 only interacts with a group of threads that have priorities between 15 and 20. During its critical sections, the thread of priority 20 can set its preemption-threshold to 15, thereby preventing preemption from all of the threads that it interacts with. This still permits really important threads (priorities between 0 and 14) to preempt this thread during its critical section processing, which results in much more responsive processing.

Of course, it is still possible for a thread to disable all preemption by setting its preemption-threshold to 0. In addition, preemption-threshold can be changed during run-time.

> **Note:** *Using preemption-threshold disables time-slicing for the specified thread.*
