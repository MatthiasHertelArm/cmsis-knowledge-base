---
id: "frb-5-queue-management-5-1-introduction"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.1 Introduction"
summary: "'Queues' provide a task-to-task, task-to-interrupt, and interrupt-to-task communication mechanism."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-1-introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

'Queues' provide a task-to-task, task-to-interrupt, and
interrupt-to-task communication mechanism.


### 5.1.1 Scope

This chapter covers:

- How to create a queue.
- How a queue manages the data it contains.
- How to send data to a queue.
- How to receive data from a queue.
- What it means to block on a queue.
- How to block on multiple queues.
- How to overwrite data in a queue.
- How to clear a queue.
- The effect of task priorities when writing to and reading from a queue.

This chapter only covers task-to-task communication. Chapter 7 covers
task-to-interrupt and interrupt-to-task communication.
