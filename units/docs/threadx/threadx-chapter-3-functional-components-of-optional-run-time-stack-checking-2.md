---
id: "threadx-chapter-3-functional-components-of-optional-run-time-stack-checking-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Optional Run-time Stack Checking"
summary: "ThreadX SMP provides the ability to check each thread's stack for corruption during run-time. By default, ThreadX SMP fills every byte of thread stacks with a 0xEF data pattern during creation."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#optional-run-time-stack-checking"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX SMP provides the ability to check each thread's stack for corruption during run-time. By default, ThreadX SMP fills every byte of thread stacks with a 0xEF data pattern during creation. If the application builds the ThreadX SMP library with ***TX_ENABLE_STACK_CHECKING*** defined, ThreadX SMP will examine each thread's stack for corruption as it is suspended or resumed. If stack corruption is detected, ThreadX SMP will call the application's stack error handling routine as specified by the call to *tx_thread_stack_error_notify*. Otherwise, if no stack error handler was specified, ThreadX SMP will call the internal *_tx_thread_stack_error_handler* routine.
