---
id: "frb-4-task-management-4-7-5-the-vtaskdelayuntil-api-function"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State / 4.7.5 The vTaskDelayUntil() API Function"
summary: "Part of: 4.7 Expanding the Not Running State"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-5-the-vtaskdelayuntil-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.7 Expanding the *Not Running* State_

`vTaskDelayUntil()` is similar to `vTaskDelay()`. As just demonstrated, the
`vTaskDelay()` parameter specifies the number of tick interrupts that
should occur between a task calling `vTaskDelay()`, and the same task once
again transitioning out of the *Blocked* state. The length of time the
task remains in the blocked state is specified by the `vTaskDelay()`
parameter, but the time at which the task leaves the blocked state is
relative to the time at which `vTaskDelay()` was called.

The parameters to `vTaskDelayUntil()` specify, instead, the exact tick
count value at which the calling task should be moved from the Blocked
state into the *Ready* state. `vTaskDelayUntil()` is the API function to use
when a fixed execution period is required (where you want your task to
execute periodically with a fixed frequency), as the time at which the
calling task is unblocked is absolute, rather than relative to when the
function was called (as is the case with `vTaskDelay()`).




```c
void vTaskDelayUntil( TickType_t * pxPreviousWakeTime,
                      TickType_t xTimeIncrement );
```

***Listing 4.14*** *vTaskDelayUntil() API function prototype*

**vTaskDelayUntil() parameters**

- `pxPreviousWakeTime`

  This parameter is named on the assumption that `vTaskDelayUntil()`
  is being used to implement a task that executes periodically and with a
  fixed frequency. In this case, `pxPreviousWakeTime` holds the time at
  which the task last left the *Blocked* state (was 'woken' up). This time
  is used as a reference point to calculate the time at which the task
  should next leave the *Blocked* state.

  The variable pointed to by `pxPreviousWakeTime` is updated
  automatically in the `vTaskDelayUntil()` function; it would not
  normally be modified by the application code, but must be initialized to
  the current tick count before its first use. Listing 4.15 demonstrates how
  to initialise the variable.

- `xTimeIncrement`

  This parameter is also named on the assumption that
  `vTaskDelayUntil()` is being used to implement a task that executes
  periodically and with a fixed frequency that is set by the
  `xTimeIncrement` value.

  `xTimeIncrement` is specified in 'ticks'. The macro `pdMS_TO_TICKS()` can
  be used to convert a time specified in milliseconds into a time
  specified in ticks.


---
***Example 4.5*** *Converting the example tasks to use vTaskDelayUntil()*

---

The two tasks created in Example 4.4 are periodic tasks, but using
`vTaskDelay()` does not guarantee that the frequency at which they run is
fixed, as the time at which the tasks leave the *Blocked* state is
relative to when they call `vTaskDelay()`. Converting the tasks to use
`vTaskDelayUntil()` instead of `vTaskDelay()` solves this potential problem.





```c
void vTaskFunction( void * pvParameters )
{
    char * pcTaskName;
    TickType_t xLastWakeTime;

    /*
     * The string to print out is passed in via the parameter. Cast this to a
     * character pointer.
     */
    pcTaskName = ( char * ) pvParameters;

    /*
     * The xLastWakeTime variable needs to be initialized with the current tick
     * count. Note that this is the only time the variable is written to
     * explicitly. After this xLastWakeTime is automatically updated within
     * vTaskDelayUntil().
     */
    xLastWakeTime = xTaskGetTickCount();

    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Print out the name of this task. */
        vPrintLine( pcTaskName );

        /*
         * This task should execute every 250 milliseconds exactly. As per
         * the vTaskDelay() function, time is measured in ticks, and the
         * pdMS_TO_TICKS() macro is used to convert milliseconds into ticks.
         * xLastWakeTime is automatically updated within vTaskDelayUntil(), so
         * is not explicitly updated by the task.
         */
        vTaskDelayUntil( &xLastWakeTime, pdMS_TO_TICKS( 250 ) );
    }
}
```

***Listing 4.15*** *The implementation of the example task using vTaskDelayUntil()*

The output produced by Example 4.5 is exactly as per that shown for Example 4.4
in Figure 4.8.


---
***Example 4.6*** *Combining blocking and non-blocking tasks*

---

The previous examples examined the behavior of both polling and blocking
tasks in isolation. This example re-enforces what we have already said regarding
the expected system behavior and demonstrates the execution sequence when the
two schemes are combined, as follows:

1. Two tasks are created at priority 1. These do nothing other than continuously
   print out a string.

   These tasks never make API function calls that could cause them to enter the
   *Blocked* state, so are always in either the Ready or the *Running* state.
   Tasks of this nature are called 'continuous processing' tasks, as they always
   have work to do (albeit rather trivial work, in this case).
   Listing 4.16 shows the source code for the continuous processing tasks.

1. A third task is then created at priority 2, which is above the priority of
   the other two tasks. The third task also just prints out a string, but this
   time periodically, so it uses the `vTaskDelayUntil()` API function to place
   itself into the *Blocked* state between each print iteration.

Listing 4.17 shows the source code of the periodic task.





```c
void vContinuousProcessingTask( void * pvParameters )
{
    char * pcTaskName;

    /*
     * The string to print out is passed in via the parameter. Cast this to a
     * character pointer.
     */
    pcTaskName = ( char * ) pvParameters;

    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /*
         * Print out the name of this task. This task just does this repeatedly
         * without ever blocking or delaying.
         */
        vPrintLine( pcTaskName );
    }
}
```

***Listing 4.16*** *The continuous processing task used in Example 4.6*





```c
void vPeriodicTask( void * pvParameters )
{
    TickType_t xLastWakeTime;

    const TickType_t xDelay3ms = pdMS_TO_TICKS( 3 );

    /*
     * The xLastWakeTime variable needs to be initialized with the current tick
     * count. Note that this is the only time the variable is explicitly
     * written to. After this xLastWakeTime is managed automatically by the
     * vTaskDelayUntil() API function.
     */
    xLastWakeTime = xTaskGetTickCount();

    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Print out the name of this task. */
        vPrintLine( "Periodic task is running" );

        /*
         * The task should execute every 3 milliseconds exactly – see the
         * declaration of xDelay3ms in this function.
         */
        vTaskDelayUntil( &xLastWakeTime, xDelay3ms );
    }
}
```

***Listing 4.17*** *The periodic task used in Example 4.6*

Figure 4.11 shows the output produced by Example 4.6, with an explanation of the
observed behavior given by the execution sequence shown in Figure 4.12.



***

```console
Continuous task 2 running
Continuous task 2 running
Periodic task is running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 2 running
Continuous task 2 running
Continuous task 2 running
Continuous task 2 running
Continuous task 2 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Continuous task 1 running
Periodic task is running
Continuous task 2 running
Continuous task 2 running
```

***Figure 4.11*** *The output produced when Example 4.6 is executed*
***




***

***Figure 4.12*** *The execution pattern of Example 4.6*
***
