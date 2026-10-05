---
id: "threadx-chapter-6-demonstration-system-for-thread-1"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Thread 1"
summary: "The function thread_1_entry marks the entry point of the thread (lines 193-216). Thread_1 is the second-to-last thread in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#thread-1"
license: "MIT"
mode: "V"
---

The function
***thread_1_entry*** marks the entry point of the thread *(lines
193-216*). ***Thread_1*** is the second-to-last thread in the
demonstration system to execute. Its processing consists of
incrementing its counter, sending a message to ***thread_2***
(*through* ***queue_0***), and repeating the sequence. Notice that
***thread_1*** suspends whenever ***queue_0*** becomes full (*line
207*).
