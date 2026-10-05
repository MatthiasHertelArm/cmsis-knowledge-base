---
id: "threadx-chapter-3-functional-components-of-relative-time"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Relative Time"
summary: "In addition to the application timers mentioned previously, ThreadX provides a single continuously incrementing 32-bit tick counter. The tick counter or time is increased by one on each timer interrupt."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#relative-time"
license: "MIT"
mode: "V"
---

In addition to the application timers mentioned previously, ThreadX provides a single continuously incrementing 32-bit tick counter. The tick counter or *time* is increased by one on each timer interrupt.

The application can read or set this 32-bit counter through calls to ***tx_time_get*** and ***tx_time_set***, respectively. The use of this tick counter is determined completely by the application. It is not used internally by ThreadX.
