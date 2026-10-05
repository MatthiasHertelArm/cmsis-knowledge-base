---
id: "frb-4-task-management-4-12-4-prioritized-preemptive-scheduling"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.12 Scheduling Algorithms / 4.12.4 Prioritized Preemptive Scheduling without Time Slicing"
summary: "Prioritized Preemptive Scheduling without time slicing maintains the same task selection and preemption algorithms as described in the previous section, but does not use time slicing to share processing time between tasks of equal priority."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-12-4-prioritized-preemptive-scheduling-without-time-slicing"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.12 Scheduling Algorithms_

Prioritized Preemptive Scheduling without time slicing maintains the
same task selection and preemption algorithms as described in the
previous section, but does not use time slicing to share processing time
between tasks of equal priority.

The Table 5 shows the FreeRTOSConfig.h settings that configure the FreeRTOS
scheduler to use prioritized preemptive scheduling without time slicing.

As was demonstrated in Figure 4.19, if time slicing is used, and there is
more than one ready state task at the highest priority that is able to
run, then the scheduler selects a new task to enter the *Running* state
during each RTOS tick interrupt (a tick interrupt marking the end of a
time slice). If time slicing is not used, then the scheduler only
selects a new task to enter the *Running* state when either:

- A higher priority task enters the *Ready* state.

- The task in the *Running* state enters the *Blocked* or *Suspended* state.

There are fewer task context switches when time slicing is not used than
when time slicing is used. Therefore, turning time slicing off results
in a reduction in the scheduler's processing overhead. However, turning
time slicing off can also result in tasks of equal priority receiving
greatly different amounts of processing time, a scenario demonstrated by
Figure 4.21. For this reason, running the scheduler without time slicing
is considered an advanced technique that should only be used by
experienced users.




***

***Figure 4.21*** *Execution pattern that demonstrates how tasks of equal priority can
receive hugely different amounts of processing time when time slicing is not used*
***

Referring to Figure 4.21, which assumes `configIDLE_SHOULD_YIELD` is set to 0:

- Tick Interrupts

  Tick interrupts occur at times t1, t2, t3, t4, t5, t8, t11, t12 and
  t13.

- Task 1

  Task 1 is a high priority event driven task that spends most of its
  time in the *Blocked* state waiting for its event of interest. Task 1
  transitions from the *Blocked* state to the *Ready* state (and
  subsequently, as it is the highest priority *Ready* state task, on into
  the *Running* state) each time the event occurs. Figure 4.21 shows Task 1
  processing an event between times t6 and t7, then again between times
  t9 and t10.

- The Idle Task and Task 2

  The Idle task and Task 2 are both continuous processing tasks, and both
  have a priority of 0 (the idle priority). Continuous processing tasks do
  not enter the *Blocked* state.

  Time slicing is not being used, so an idle priority task that is in the
  *Running* state will remain in the *Running* state until it is preempted by
  the higher priority Task 1.

  In Figure 4.21 the Idle task starts running at time t1, and remains in the
  *Running* state until it is preempted by Task 1 at time t6, which is more
  than four complete tick periods after it entered the *Running* state.

  Task 2 starts running at time t7, which is when Task 1 re-enters the
  *Blocked* state to wait for another event. Task 2 remains in the Running
  state until it too is preempted by Task 1 at time t9, which is less than
  one tick period after it entered the *Running* state.

  At time t10 the Idle task re-enters the *Running* state, despite having
  already received more than four times more processing time than Task 2.
