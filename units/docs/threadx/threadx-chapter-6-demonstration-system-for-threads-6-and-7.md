---
id: "threadx-chapter-6-demonstration-system-for-threads-6-and-7"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Threads 6 and 7"
summary: "The function thread_6_and_7_entry marks the entry point of both thread_6 and thread_7 (lines 307-358). Both threads have a priority of 8, which makes them the fifth and sixth threads in the demonstration system to execute."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#threads-6-and-7"
license: "MIT"
mode: "V"
---

The function ***thread_6_and_7_entry*** marks the entry point of
both ***thread_6*** and ***thread_7*** (lines 307-358). Both
threads have a priority of 8, which makes them the fifth and sixth
threads in the demonstration system to execute. The processing for
each thread is the same: incrementing its counter, getting
***mutex_0*** twice, sleeping for 2 timer ticks, releasing
***mutex_0*** twice, and repeating the sequence. Notice that each
thread suspends whenever ***mutex_0*** is unavailable (line 325).

Also both threads use the same
function for their main processing. This presents no problems because
they both have their own unique stack, and C is naturally reentrant.
Each thread determines which one it is by examination of the thread
input parameter (line 319), which is setup when they are created
(lines 126 and 133).
