---
id: "frb-4-task-management-4-7-expanding-the-not-running-state"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State"
summary: "So far, the created tasks have always had processing to perform and have never had to wait for anything—and since they never had to wait for anything, they were always able to enter the Running state."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-expanding-the-not-running-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

So far, the created tasks have always had processing to perform and have
never had to wait for anything—and since they never had to wait for anything,
they were always able to enter the *Running* state. Such 'continuous processing'
tasks have limited usefulness because they can only be created at the very lowest
priority. If they run at any other priority, they will prevent tasks of lower
priority from ever running at all.

To make these tasks useful, they must be re-written to be event-driven. An
event-driven task only has work (processing) to perform after an event
triggers it and cannot enter the *Running* state before that time.
The scheduler always selects the highest priority task that can run. If
a high-priority task cannot be selected because it is waiting for an
event, the scheduler must, instead, select a lower-priority task that
can run. Therefore, writing event-driven tasks means tasks can be
created at different priorities without the highest priority tasks
starving all the lower priority tasks of processing time.
