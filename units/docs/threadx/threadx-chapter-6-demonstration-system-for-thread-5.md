---
id: "threadx-chapter-6-demonstration-system-for-thread-5"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Thread 5"
summary: "The function thread_5_entry marks the entry point of the thread (lines 283-305). Thread_5 is the second thread in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#thread-5"
license: "MIT"
mode: "V"
---

The function ***thread_5_entry*** marks the entry point of the
thread (lines 283-305). ***Thread_5*** is the second thread in the
demonstration system to execute. Its processing consists of
incrementing its counter, getting an event flag from ***thread_0***
(through ***event_flags_0***), and repeating the sequence. Notice
that ***thread_5*** suspends whenever the event flag in
***event_flags_0*** is not available (line 298).
