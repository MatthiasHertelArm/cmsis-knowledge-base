---
id: "frb-4-task-management-4-7-4-completing-the-state-transition-di"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State / 4.7.4 Completing the State Transition Diagram"
summary: "Part of: 4.7 Expanding the Not Running State"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-4-completing-the-state-transition-diagram"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.7 Expanding the *Not Running* State_

Figure 4.7 expands on the simplified state diagram to include all of the
*Not Running* sub-states described in this section. The tasks created in the
 examples so far have not used the *Blocked* or *Suspended* states. They have
 only transitioned between the *Ready* state and the *Running* state as shown by
 the bold lines in Figure 4.7.




***

***Figure 4.7*** *Full task state machine*
***


---
***Example 4.4*** *Using the *Blocked* state to create a delay_

---

All the tasks created in the examples presented so far have been
'periodic'—they have delayed for a period and then printed out their string,
before delaying once more, and so on. The delay has been generated very
crudely using a null loop—the task polled an incrementing
loop counter until it reached a fixed value. Example 4.3 clearly
demonstrated the disadvantage of this method. The higher priority task
remained in the *Running* state while it executed the null loop,
'starving' the lower priority task of any processing time.

There are several other disadvantages to any form of polling, not least
of which is its inefficiency. During polling, the task does not really
have any work to do, but it still uses the maximum processing time, and so
wastes processor cycles. Example 4.4 corrects this behavior by replacing
the polling null loop with a call to the `vTaskDelay()` API function, whose
prototype is shown in Listing 4.12. The new task definition is
shown in Listing 4.13. Note that the `vTaskDelay()` API function is
available only when `INCLUDE_vTaskDelay` is set to 1 in FreeRTOSConfig.h.

`vTaskDelay()` places the calling task into the *Blocked* state for a fixed
number of tick interrupts. The task does not use any processing time
while it is in the *Blocked* state, so the task only uses processing time
when there is actually work to be done.





```c
void vTaskDelay( TickType_t xTicksToDelay );
```

***Listing 4.12*** *The vTaskDelay() API function prototype*

**vTaskDelay parameters:**

- `xTicksToDelay`

  The number of tick interrupts that the calling task will remain
  in the *Blocked* state before being transitioned back into the Ready
  state.

  For example, if a task called `vTaskDelay( 100 )` when the tick count
  was 10,000, then it would immediately enter the *Blocked* state, and
  remain in the *Blocked* state until the tick count reached 10,100.

  The macro `pdMS_TO_TICKS()` can be used to convert a time specified in
  milliseconds into a time specified in ticks. For example, calling
  `vTaskDelay( pdMS_TO_TICKS( 100 ) )` results in the calling task remaining
  in the *Blocked* state for 100 milliseconds.





```c
void vTaskFunction( void * pvParameters )
{
    char * pcTaskName;
    const TickType_t xDelay250ms = pdMS_TO_TICKS( 250 );

    /*
     * The string to print out is passed in via the parameter. Cast this to a
     * character pointer.
     */
    pcTaskName = ( char * ) pvParameters;

    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Print out the name of this task. */
        vPrintLine( pcTaskName );

        /*
         * Delay for a period. This time a call to vTaskDelay() is used which
         * places the task into the Blocked state until the delay period has
         * expired. The parameter takes a time specified in 'ticks', and the
         * pdMS_TO_TICKS() macro is used (where the xDelay250ms constant is
         * declared) to convert 250 milliseconds into an equivalent time in
         * ticks.
         */
        vTaskDelay( xDelay250ms );
    }
}
```

***Listing 4.13*** *The source code for the example task after replacing the null loop
delay with a call to vTaskDelay()*

Even though the two tasks are still being created at different
priorities, both will now run. The output of Example 4.4, which is shown
in Figure 4.8, confirms the expected behavior.




***

```console
C:\Temp>rtosdemo
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
Task 2 is running
Task 1 is running
```

***Figure 4.8*** *The output produced when Example 4.4 is executed*
***

The execution sequence shown in Figure 4.9 explains why both tasks run,
even though they are created at different priorities. The execution of
the scheduler itself is omitted for simplicity.

The idle task is created automatically when the scheduler is started, to
ensure there is always at least one task that can run (at least one task
in the *Ready* state). [Section 4.8: The Idle Task and the Idle Task Hook](#48-the-idle-task-and-the-idle-task-hook)
describes the Idle task in more detail.




***

***Figure 4.9*** *The execution sequence when the tasks use vTaskDelay() in place of
the null loop*
***

Only the implementation of the two tasks has changed, not their
functionality. Comparing Figure 4.9 with Figure 4.4 demonstrates clearly
that this functionality is being achieved in a much more efficient
manner.

Figure 4.4 shows the execution pattern when the tasks use a null loop to
create a delay and so are always able to run. As a result, they use one
hundred percent of the available processor time between them. Figure 4.9
shows the execution pattern when the tasks enter the *Blocked* state for
the entirety of their delay period. They use processor time only when they
actually have work that needs to be performed (in this case simply a
message to be printed out), and as a result only use a tiny fraction of
the available processing time.

In the scenario shown in Figure 4.9, each time the tasks leave the *Blocked* state
they execute for a fraction of a tick period before re-entering the
Blocked state. Most of the time there are no application tasks that can
run (no application tasks in the *Ready* state) and, therefore, no
application tasks that can be selected to enter the *Running* state. While
this is the case, the idle task runs. The amount of processing time
allocated to the idle is a measure of the spare processing capacity in
the system. Using an RTOS can significantly increase the spare
processing capacity simply by allowing an application to be completely
event driven.

The bold lines in Figure 4.10 show the transitions performed by the tasks
in Example 4.4, with each task now transitioning through the *Blocked* state
before being returned to the *Ready* state.




***

***Figure 4.10*** *Bold lines indicate the state transitions performed by the tasks
in Example 4.4*
***
