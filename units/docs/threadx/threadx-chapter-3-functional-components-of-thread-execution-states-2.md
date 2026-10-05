---
id: "threadx-chapter-3-functional-components-of-thread-execution-states-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Thread Execution States"
summary: "Understanding the different processing states of threads is a key ingredient to understanding the entire multithreaded environment. In ThreadX SMP, there are five distinct thread states: ready, suspended, executing, terminated, and completed."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#thread-execution-states"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

Understanding the different processing states of threads is a key ingredient to understanding the entire multithreaded environment. In ThreadX SMP, there are five distinct thread states: *ready*, *suspended*, *executing*, *terminated*, and *completed*. Figure 4 shows the thread state transition diagram for ThreadX SMP.

(figure: Thread Execution States)

**FIGURE 4. Thread State Transition**

A thread is in a *ready* state when it is ready for execution. A ready thread is not executed until it is the highest priority thread in ready state. When this happens, ThreadX SMP executes the thread, which then changes its state to *executing*.

If a higher-priority thread becomes ready, the executing thread reverts back to a *ready* state. The newly ready high-priority thread is then executed, which changes its logical state to *executing*. This transition between *ready* and *executing* states occurs every time thread preemption occurs.

At any given moment, only one thread is in an *executing* state. This is because a thread in the *executing* state has control of the underlying processor.

Threads in a *suspended* state are not eligible for execution. Reasons for being in a *suspended* state include suspension for time, queue messages, semaphores, mutexes, event flags, memory, and basic thread suspension. After the cause for suspension is removed, the thread is placed back in a *ready* state.

A thread in a *completed* state is a thread that has completed its processing and returned from its entry function. The entry function is specified during thread creation. A thread in a *completed* state cannot execute again.

A thread is in a *terminated* state because another thread or the thread itself called the *tx_thread_terminate* service. A thread in a *terminated* state cannot execute again.

> **Important:** If re-starting a completed or terminated thread is desired, the application must first delete the thread. It can then be re-created and re-started.
