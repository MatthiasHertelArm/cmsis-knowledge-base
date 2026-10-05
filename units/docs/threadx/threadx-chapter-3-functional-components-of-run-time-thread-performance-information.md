---
id: "threadx-chapter-3-functional-components-of-run-time-thread-performance-information"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Run-time Thread Performance Information"
summary: "ThreadX provides optional run-time thread performance information. If the ThreadX library and application is built with TX_THREAD_ENABLE_PERFORMANCE_INFO defined, ThreadX accumulates the following information."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#run-time-thread-performance-information"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX provides optional run-time thread performance information. If the ThreadX library and application is built with **TX_THREAD_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

  - thread resumptions

  - thread suspensions

  - service call preemptions

  - interrupt preemptions

  - priority inversions

  - time-slices

  - relinquishes

  - thread timeouts

  - suspension aborts

  - idle system returns

  - non-idle system returns

Total number for each thread:

  - resumptions

  - suspensions

  - service call preemptions

  - interrupt preemptions

  - priority inversions

  - time-slices

  - thread relinquishes

  - thread timeouts

  - suspension aborts

This information is available at run-time through the services ***tx_thread_performance_info_get*** and ***tx_thread_performance_system_info_get***. Thread performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of service call preemptions might
suggest the thread's priority and/or preemption-threshold is too low. Furthermore, a relatively low number of idle system returns might suggest that lower priority threads are not suspending enough.
