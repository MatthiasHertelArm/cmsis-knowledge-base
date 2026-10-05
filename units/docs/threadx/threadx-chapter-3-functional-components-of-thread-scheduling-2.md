---
id: "threadx-chapter-3-functional-components-of-thread-scheduling-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Thread Scheduling"
summary: "ThreadX SMP schedules threads based on their priority. The ready thread with the highest priority is executed first. If multiple threads of the same priority are ready, they are executed in a first-in-first-out (FIFO) manner."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#thread-scheduling"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX SMP schedules threads based on their priority. The ready thread with the highest priority is executed first. If multiple threads of the same priority are ready, they are executed in a *first-in-first-out* (FIFO) manner.

By default, ThreadX SMP schedules the "n" highest priority threads on the "n" available processors. If concurrent processing is only required on ready threads of the same priority, the ThreadX SMP library must be built with **TX_THREAD_SMP_EQUAL_PRIORITY** defined.

> **Note:** That all threads can be initially defaulted to only run on core 0, by building the ThreadX SMP library with **TX_THREAD_SMP_ONLY_CORE_0_DEFAULT** defined.
