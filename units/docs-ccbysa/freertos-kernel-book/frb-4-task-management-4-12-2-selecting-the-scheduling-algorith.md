---
id: "frb-4-task-management-4-12-2-selecting-the-scheduling-algorith"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.12 Scheduling Algorithms / 4.12.2 Selecting the Scheduling Algorithm"
summary: "The scheduling algorithm is the software routine that decides which Ready state task to transition into the Running state."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-12-2-selecting-the-scheduling-algorithm"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.12 Scheduling Algorithms_

The scheduling algorithm is the software routine that decides which
*Ready* state task to transition into the *Running* state.

All the examples so far have used the same scheduling algorithm, but the
algorithm can be changed using the `configUSE_PREEMPTION` and
`configUSE_TIME_SLICING` configuration constants. Both constants are
defined in FreeRTOSConfig.h.

A third configuration constant, `configUSE_TICKLESS_IDLE`, also affects
the scheduling algorithm, as its use can result in the tick interrupt
being turned off completely for extended periods.
`configUSE_TICKLESS_IDLE` is an advanced option provided specifically for
use in applications that must minimize their power consumption.
The descriptions provided in this section assume `configUSE_TICKLESS_IDLE`
is set to 0, which is the default setting if the constant is left
undefined.

In all possible single core configurations the FreeRTOS scheduler
selects tasks that share a priority in turn. This 'take it in turn'
policy is often referred to as 'Round Robin Scheduling'. A Round Robin
scheduling algorithm does not guarantee time is shared equally between
tasks of equal priority, only that *Ready* state tasks of equal priority
enter the *Running* state in turn.



***
| Scheduling Algorithm            | Prioritized | `configUSE_PREEMPTION` | `configUSE_TIME_SLICING` |
|---------------------------------|-------------|------------------------|--------------------------|
| Preemptive With Time Slicing    | Yes         | 1 | 1   |
| Preemptive Without Time Slicing | Yes         | 1 | 0   |
| Co-Operative                    | No          | 0 | Any |

***Table 5*** *The FreeRTOSConfig.h settings to configure the kernel scheduling algorithms*
* * *
