---
id: "frb-4-task-management-4-12-1-a-recap-of-task-states-and-events"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.12 Scheduling Algorithms / 4.12.1 A Recap of Task States and Events"
summary: "The task that is actually running (using processing time) is in the Running state. On a single core processor there can only be one task in the Running state at any given time."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-12-1-a-recap-of-task-states-and-events"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.12 Scheduling Algorithms_

The task that is actually running (using processing time) is in the
*Running* state. On a single core processor there can only be one task in
the *Running* state at any given time. It is also possible to run FreeRTOS
on more than one core (asymmetric multiprocessing, or AMP), or have
FreeRTOS schedule tasks across multiple cores (symmetric
multiprocessing, or SMP). Neither of those scenarios are described here.

Tasks that are not actually running, but are not in either the Blocked
state or the *Suspended* state, are in the *Ready* state. Tasks in the Ready
state are available to be selected by the scheduler as the task to enter
the *Running* state. The scheduler will always choose the highest priority
Ready state task to enter the *Running* state.

Tasks can wait in the *Blocked* state for an event and they are automatically
moved back to the *Ready* state when the event occurs. Temporal events
occur at a particular time, for example, when a block time expires, and
are normally used to implement periodic or timeout behavior.
Synchronization events occur when a task or interrupt service routine
sends information using a task notification, queue, event group, message
buffer, stream buffer, or one of the many types of semaphore. They are
generally used to signal asynchronous activity, such as data arriving at
a peripheral.
