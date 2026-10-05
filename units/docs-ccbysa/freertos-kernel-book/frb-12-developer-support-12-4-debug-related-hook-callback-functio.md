---
id: "frb-12-developer-support-12-4-debug-related-hook-callback-functio"
type: "concept"
domain: "rtos"
title: "12 Developer Support: 12.4 Debug Related Hook (Callback) Functions"
summary: "The malloc failed hook (or callback) was described in Chapter 3, Heap Memory Management."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch12.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch12.md#12-4-debug-related-hook-callback-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

### 12.4.1 Malloc failed hook

The malloc failed hook (or callback) was described in Chapter 3, Heap
Memory Management.

Defining a malloc failed hook ensures the application developer is
notified immediately if an attempt to create a task, queue, semaphore or
event group fails.

### 12.4.2 Stack overflow hook

Details of the stack overflow hook are provided in section 13.3, Stack
Overflow.

Defining a stack overflow hook ensures the application developer is
notified if the amount of stack used by a task exceeds the stack space
allocated to the task.
