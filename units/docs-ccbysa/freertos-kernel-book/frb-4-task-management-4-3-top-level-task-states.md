---
id: "frb-4-task-management-4-3-top-level-task-states"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.3 Top Level Task States"
summary: "An application may consist of many tasks. If the processor running the application includes a single core, then only one task may be executing at any given time."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-3-top-level-task-states"
license: "CC-BY-SA-4.0"
mode: "V"
---

An application may consist of many tasks. If the processor running the
application includes a single core, then only one task may be executing
at any given time. This implies that a task may exist in one of two
states: *Running* and *Not Running*. This simplistic model is considered
first. Later in this chapter we describe the several sub-states of the
*Not Running* state.

A task is in the *Running* state when the processor is executing that task's
code. When a task is in the *Not Running* state, the task is paused and its
state has been saved so that it may resume execution the next time the scheduler
decides it should enter the *Running* state. When a task resumes execution,
it does so from the instruction it was about to execute before it left the
*Running* state.




***

***Figure 4.1*** *Top level task states and transitions*
***

A task transitioned from the *Not Running* state to the *Running* state is
said to have been "switched in" or "swapped in". Conversely, a task
transitioned from the *Running* state to the *Not Running* state is said to
have been "switched out" or "swapped out". The FreeRTOS scheduler is the
only entity that can switch a task in and out of the *Running* state.
