---
id: "threadx-chapter-3-functional-components-of-thread-scheduling"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Thread Scheduling"
summary: "ThreadX schedules threads based on their priority. The ready thread with the highest priority is executed first. If multiple threads of the same priority are ready, they are executed in a first-in-first-out (FIFO) manner."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#thread-scheduling"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX schedules threads based on their priority. The ready thread with the highest priority is executed first. If multiple threads of the same priority are ready, they are executed in a *first-in-first-out* (FIFO) manner.
