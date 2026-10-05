---
id: "threadx-chapter-6-demonstration-system-for-thread-2-2"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX SMP: Thread 2"
summary: "The function thread_2_entry marks the entry point of the thread (lines 219-243). Thread_2 is the last thread in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter6.md#thread-2"
license: "MIT"
mode: "V"
---

The function ***thread_2_entry*** marks the entry point of the thread *(lines 219-243*). ***Thread_2*** is the last thread in the demonstration system to execute. Its processing consists of incrementing its counter, getting a message from ***thread_1*** (through ***queue_0***), and repeating the sequence. Notice that ***thread_2*** suspends whenever ***queue_0*** becomes empty (*line 233*).

Although ***thread_1*** and ***thread_2*** share the lowest priority in the demonstration system (*priority 16*), they are also the only threads that are ready for execution most of the time. They are also the only threads created with time-slicing (*lines 87 and 93*). Each thread is allowed to execute for a maximum of 4 timer ticks before the other thread is executed.
