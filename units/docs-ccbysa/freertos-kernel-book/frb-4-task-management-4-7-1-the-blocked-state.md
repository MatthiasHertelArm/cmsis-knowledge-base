---
id: "frb-4-task-management-4-7-1-the-blocked-state"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State / 4.7.1 The *Blocked* State"
summary: "Part of: 4.7 Expanding the Not Running State"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-1-the-blocked-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.7 Expanding the *Not Running* State_

A task waiting for an event is said to be in the 'Blocked' state, a
sub-state of the *Not Running* state.

Tasks can enter the *Blocked* state to wait for two different types of
events:

1. Temporal (time-related) events— these events occur either when a delay period
   expires or an absolute time is reached. For example, a task may
   enter the *Blocked* state to wait for 10 milliseconds to pass.

1. Synchronization events— these events originate from another task
   or interrupt. For example, a task may enter the *Blocked* state to
   wait for data to arrive on a queue. Synchronization events cover a
   broad range of event types.

FreeRTOS queues, binary semaphores, counting semaphores, mutexes,
recursive mutexes, event groups, stream buffers, message buffers, and
direct to task notifications can all create synchronization events.
Later chapters cover most of these features.

A task can block on a synchronization event with a timeout, effectively
blocking on both types of event simultaneously. For example, a task may
choose to wait for a maximum of 10 milliseconds for data to arrive on a
queue. The task will leave the *Blocked* state if data arrives within 10
milliseconds or if 10 milliseconds pass without data arriving.
