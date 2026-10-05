---
id: "threadx-chapter-6-demonstration-system-for-observing-the-demonstration"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Observing the Demonstration"
summary: "Each of the demonstration threads increments its own unique counter. The following counters may be examined to check on the demo's operation:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#observing-the-demonstration"
license: "MIT"
mode: "V"
---

Each of the demonstration threads increments its own unique counter.
The following counters may be examined to check on the demo's
operation:

- thread_0_counter
- thread_1_counter
- thread_2_counter
- thread_3_counter
- thread_4_counter
- thread_5_counter
- thread_6_counter
- thread_7_counter

Each of these counters should continue to increase as the demonstration executes, with
***thread_1_counter*** and ***thread_2_counter*** increasing at the fastest rate.
