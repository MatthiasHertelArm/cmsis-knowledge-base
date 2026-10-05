---
id: "threadx-chapter-6-demonstration-system-for-threads-3-and-4-2"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX SMP: Threads 3 and 4"
summary: "The function thread_3_and_4_entry marks the entry point of both thread_3 and thread_4 (lines 246-280). Both threads have a priority of 8, which makes them the third and fourth threads in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter6.md#threads-3-and-4"
license: "MIT"
mode: "V"
---

The function ***thread_3_and_4_entry*** marks the entry point of both ***thread_3*** and ***thread_4*** *(lines 246-280*). Both threads have a priority of 8, which makes them the third and fourth threads in the demonstration system to execute. The processing for each thread is the same: incrementing its counter, getting ***semaphore_0***, sleeping for 2 timer ticks, releasing ***semaphore_0***, and repeating the sequence. Notice that each thread suspends whenever ***semaphore_0*** is unavailable (*line 264*).

Also both threads use the same function for their main processing. This presents no problems because they both have their own unique stack, and C is naturally reentrant. Each thread determines which one it is by examination of the thread input parameter (*line 258*), which is setup when they are created (*lines 102 and 109*).

> **Important:** It is also reasonable to obtain the current thread point during thread execution and compare it with the control block's address to determine thread identity.
