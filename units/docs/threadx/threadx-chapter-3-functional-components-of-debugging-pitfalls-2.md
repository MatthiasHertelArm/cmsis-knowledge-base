---
id: "threadx-chapter-3-functional-components-of-debugging-pitfalls-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Debugging Pitfalls"
summary: "Debugging multithreaded applications is a little more difficult because the same program code can be executed from multiple threads. In such cases, a break-point alone may not be enough."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#debugging-pitfalls"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

Debugging multithreaded applications is a little more difficult because the same program code can be executed from multiple threads. In such cases, a break-point alone may not be enough. The debugger must also view the current thread pointer array ***_tx_thread_current_ptr[core]*** using a conditional breakpoint to see if the calling thread is the one to debug.

Much of this is being handled in multithreading support packages offered through various development tool vendors. Because of its simple design, integrating ThreadX SMP with different development tools is relatively easy.

Stack size is always an important debug topic in multithreading. Whenever unexplained behavior is observed, it is usually a good first guess to increase stack sizes for all threads—especially the stack size of the last thread to execute!

> **Important:** It is also a good idea to build the ThreadX SMP library with TX_ENABLE_STACK_CHECKING defined. This will help isolate stack corruption problems as early in the processing as possible!
