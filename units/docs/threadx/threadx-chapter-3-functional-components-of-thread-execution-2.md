---
id: "threadx-chapter-3-functional-components-of-thread-execution-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution"
summary: "Scheduling and executing application threads is the most important activity of ThreadX SMP. A thread is typically defined as a semi-independent program segment with a dedicated purpose. The combined processing of all threads makes an application."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#thread-execution"
license: "MIT"
mode: "V"
---

Scheduling and executing application threads is the most important activity of ThreadX SMP. A thread is typically defined as a semi-independent program segment with a dedicated purpose. The combined processing of all threads makes an application.

Threads are created dynamically by calling *tx_thread_create* during initialization or during thread execution. Threads are created in either a *ready* or *suspended* state.

(figure: SMP Initialization Process)

**FIGURE 3. SMP Initialization Process**
