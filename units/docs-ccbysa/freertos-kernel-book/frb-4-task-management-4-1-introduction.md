---
id: "frb-4-task-management-4-1-introduction"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.1 Introduction"
summary: "The concepts presented in this chapter are fundamental to understanding how to use FreeRTOS and how FreeRTOS applications behave. Therefore, this is the most detailed chapter in the book."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-1-introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

### 4.1.1 Scope

This chapter covers:

- How FreeRTOS allocates processing time to each task in an application.
- How FreeRTOS chooses which task should execute at any given time.
- How the relative priority of each task affects system behavior.
- The states that a task can exist in.

This chapter also discusses:

- How to implement tasks.
- How to create one or more instances of a task.
- How to use the task parameter.
- How to change the priority of a task that has already been created.
- How to delete a task.
- How to implement periodic processing using a task. (A later chapter
  describes how to do the same using software timers.)
- When the idle task will execute and how it can be used.

The concepts presented in this chapter are fundamental to understanding
how to use FreeRTOS and how FreeRTOS applications behave. Therefore,
this is the most detailed chapter in the book.
