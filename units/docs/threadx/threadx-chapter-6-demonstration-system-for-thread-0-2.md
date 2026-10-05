---
id: "threadx-chapter-6-demonstration-system-for-thread-0-2"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX SMP: Thread 0"
summary: "The function thread_0_entry marks the entry point of the thread (lines 167-190). Thread_0 is the first thread in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter6.md#thread-0"
license: "MIT"
mode: "V"
---

The function ***thread_0_entry*** marks the entry point of the thread *(lines 167-190*). ***Thread_0*** is the first thread in the demonstration system to execute. Its processing is simple: it increments its counter, sleeps for 10 timer ticks, sets an event flag to wake up ***thread_5***, then repeats the sequence.

***Thread_0*** is the highest priority thread in the system. When its requested sleep expires, it will preempt any other executing thread in the demonstration.
