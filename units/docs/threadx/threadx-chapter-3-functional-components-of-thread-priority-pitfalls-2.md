---
id: "threadx-chapter-3-functional-components-of-thread-priority-pitfalls-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Thread Priority Pitfalls"
summary: "Selecting thread priorities is one of the most important aspects of multithreading. It is sometimes very tempting to assign priorities based on a perceived notion of thread importance rather than determining what is exactly required during run-time."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#thread-priority-pitfalls"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

Selecting thread priorities is one of the most important aspects of multithreading. It is sometimes very tempting to assign priorities based on a perceived notion of thread importance rather than determining what is exactly required during run-time. Misuse of thread priorities can starve other threads, create priority inversion, reduce processing bandwidth, and make the application's run-time behavior difficult to understand.

As mentioned before, ThreadX SMP provides a priority-based, preemptive scheduling algorithm. Lower priority threads do not execute until there are no higher priority threads ready for execution. If a higher priority thread is always ready, the lower priority threads never execute. This condition is called *thread starvation*.

Most thread starvation problems are detected early in debug and can be solved by ensuring that higher priority threads don't execute continuously. Alternatively, logic can be added to the application that gradually raises the priority of starved threads until they get a chance to execute.

Another pitfall associated with thread priorities is *priority inversion*. Priority inversion takes place when a higher priority thread is suspended because a lower priority thread has a needed resource. Of course, in some instances it is necessary for two threads of different priority to share a common resource. If these threads are the only ones active, the priority inversion time is bounded by the time the lower priority thread holds the resource. This condition is both deterministic and quite normal. However, if threads of intermediate priority become active during this priority inversion condition, the priority inversion time is no longer deterministic and could cause an application failure.

There are principally three distinct methods of preventing nondeterministic priority inversion in ThreadX SMP. First, the application priority selections and run-time behavior can be designed in a manner that prevents the priority inversion problem. Second, lower priority threads can utilize *preemption-threshold* to block preemption from intermediate threads while they share resources with higher priority threads. Finally, threads using ThreadX SMP mutex objects to protect system resources may utilize the optional mutex *priority inheritance* to eliminate nondeterministic priority inversion.
