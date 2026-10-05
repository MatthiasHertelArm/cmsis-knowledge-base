---
id: "threadx-chapter-3-functional-components-of-currently-executing-thread-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Currently Executing Thread"
summary: "As mentioned before, there is only one thread executing at any given time. There are several ways to identify the executing thread, depending on which thread is making the request."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#currently-executing-thread"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

As mentioned before, there is only one thread executing at any given time. There are several ways to identify the executing thread, depending on which thread is making the request.

A program segment can get the control block address of the executing thread by calling ***tx_thread_identify***. This is useful in shared portions of application code that are executed from multiple threads.

In debug sessions, users can examine the internal ThreadX SMP pointer array ***_tx_thread_current_ptr[core]***. It contains the control block address of the currently executing thread. If this pointer is NULL, no application thread is executing; i.e., ThreadX SMP is waiting in its scheduling loop for a thread to become ready.
