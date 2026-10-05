---
id: "threadx-chapter-3-functional-components-of-round-robin-scheduling"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Round-robin Scheduling"
summary: "ThreadX supports round-robin scheduling of multiple threads having the same priority. This is accomplished through cooperative calls to tx_thread_relinquish. This service gives all other ready threads of the same priority a chance to execute before the tx_thread_relinquish caller executes again."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#round-robin-scheduling"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX supports *round-robin* scheduling of multiple threads having the same priority. This is accomplished through cooperative calls to ***tx_thread_relinquish***. This service gives all other ready threads of the same priority a chance to execute before the ***tx_thread_relinquish*** caller executes again.
