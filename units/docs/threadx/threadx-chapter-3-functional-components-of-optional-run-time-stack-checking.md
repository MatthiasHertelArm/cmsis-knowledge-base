---
id: "threadx-chapter-3-functional-components-of-optional-run-time-stack-checking"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Optional Run-time Stack Checking"
summary: "ThreadX provides the ability to check each thread's stack for corruption during run-time. By default, ThreadX fills every byte of thread stacks with a 0xEF data pattern during creation."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#optional-run-time-stack-checking"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX provides the ability to check each thread's stack for corruption during run-time. By default, ThreadX fills every byte of thread stacks with a 0xEF data pattern during creation. If the application builds the ThreadX library with **TX_ENABLE_STACK_CHECKING** defined, ThreadX will examine each thread's stack for corruption as it is suspended or resumed. If stack corruption is detected, ThreadX will call the application's stack error handling routine as specified by the call to ***tx_thread_stack_error_notify***. Otherwise, if no stack error handler was specified, ThreadX will call the internal ***_tx_thread_stack_error_handler*** routine.
