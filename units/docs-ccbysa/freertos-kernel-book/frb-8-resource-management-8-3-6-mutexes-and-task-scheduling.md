---
id: "frb-8-resource-management-8-3-6-mutexes-and-task-scheduling"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.6 Mutexes and Task Scheduling"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-6-mutexes-and-task-scheduling"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

If two tasks of different priority use the same mutex, then the FreeRTOS
scheduling policy makes the order in which the tasks will execute clear;
the highest priority task that is able to run will be selected as the
task that enters the Running state. For example, if a high priority task
is in the Blocked state to wait for a mutex that is held by a low
priority task, then the high priority task will pre-empt the low
priority task as soon as the low priority task returns the mutex. The
high priority task will then become the mutex holder. This scenario has
already been seen in Figure 8.5.

It is, however, common to make an incorrect assumption as to the order in
which the tasks will execute when the tasks have the same priority. If
Task 1 and Task 2 have the same priority, and Task 1 is in the Blocked
state to wait for a mutex that is held by Task 2, then Task 1 will not
pre-empt Task 2 when Task 2 'gives' the mutex. Instead, Task 2 will
remain in the Running state, and Task 1 will simply move from the
Blocked state to the Ready state. This scenario is shown in Figure 8.6,
in which the vertical lines mark the times at which a tick interrupt
occurs.




* * *
   
***Figure 8.6*** *A possible sequence of execution when tasks that have the same priority use the same mutex*
* * *

In the scenario shown in Figure 8.6, the FreeRTOS scheduler does *not*
make Task 1 the Running state task as soon as the mutex is available
because:

- Task 1 and Task 2 have the same priority, so unless Task 2 enters
  the Blocked state, a switch to Task 1 should not occur until the
  next tick interrupt (assuming `configUSE_TIME_SLICING` is set to 1 in
  FreeRTOSConfig.h).

- If a task uses a mutex in a tight loop, and a context switch
  occurred each time the task 'gave' the mutex, then the task would
  only ever remain in the Running state for a short time. If two or
  more tasks used the same mutex in a tight loop, then processing time
  would be wasted by rapidly switching between the tasks.

If a mutex is used in a tight loop by more than one task, and the tasks
that use the mutex have the same priority, then care must be taken to
ensure the tasks receive an approximately equal amount of processing
time. The reason the tasks might not receive an equal amount of
processing time is demonstrated by Figure 8.7, which shows a sequence of
execution that could occur if two instances of the task shown by Listing
8.15 are created at the same priority.




```c
/* The implementation of a task that uses a mutex in a tight loop. The task 
   creates a text string in a local buffer, then writes the string to a display.
   Access to the display is protected by a mutex. */

void vATask( void *pvParameter )
{
    extern SemaphoreHandle_t xMutex;
    char cTextBuffer[ 128 ];

    for( ;; )
    {
        /* Generate the text string – this is a fast operation. */
        vGenerateTextInALocalBuffer( cTextBuffer );

        /* Obtain the mutex that is protecting access to the display. */
        xSemaphoreTake( xMutex, portMAX_DELAY );

        /* Write the generated text to the display–this is a slow operation. */
        vCopyTextToFrameBuffer( cTextBuffer );

        /* The text has been written to the display, so return the mutex. */
        xSemaphoreGive( xMutex );
    }
}
```
***Listing 8.15*** *A task that uses a mutex in a tight loop*


The comments in Listing 8.15 note that creating the string is a fast
operation, and updating the display is a slow operation. Therefore, as
the mutex is held while the display is being updated, the task will hold
the mutex for the majority of its run time.

In Figure 8.7, the vertical lines mark the times at which a tick
interrupt occurs.




* * *
   
***Figure 8.7*** *A sequence of execution that could occur if two instances of the task shown by Listing 8.15 are created at the same priority*
* * *

Step 7 in Figure 8.7 shows Task 1 re-entering the Blocked state—that
happens inside the `xSemaphoreTake()` API function.

Figure 8.7 demonstrates that Task 1 will be prevented from obtaining the
mutex until the start of a time slice coincides with one of the short
periods during which Task 2 is not the mutex holder.

The scenario shown in Figure 8.7 can be avoided by adding a call to
`taskYIELD()` after the call to `xSemaphoreGive()`. This is demonstrated in
Listing 8.16, where `taskYIELD()` is called if the tick count changed while
the task held the mutex.




```c
void vFunction( void *pvParameter )
{
    extern SemaphoreHandle_t xMutex;
    char cTextBuffer[ 128 ];
    TickType_t xTimeAtWhichMutexWasTaken;

    for( ;; )
    {
        /* Generate the text string – this is a fast operation. */
        vGenerateTextInALocalBuffer( cTextBuffer );

        /* Obtain the mutex that is protecting access to the display. */
        xSemaphoreTake( xMutex, portMAX_DELAY );

        /* Record the time at which the mutex was taken. */
        xTimeAtWhichMutexWasTaken = xTaskGetTickCount();

        /* Write the generated text to the display–this is a slow operation. */
        vCopyTextToFrameBuffer( cTextBuffer );

        /* The text has been written to the display, so return the mutex. */
        xSemaphoreGive( xMutex );

        /* If taskYIELD() was called on each iteration then this task would
           only ever remain in the Running state for a short period of time, 
           and processing time would be wasted by rapidly switching between 
           tasks. Therefore, only call taskYIELD() if the tick count changed 
           while the mutex was held. */
        if( xTaskGetTickCount() != xTimeAtWhichMutexWasTaken )
        {
            taskYIELD();
        }
    }
}
```
***Listing 8.16*** *Ensuring tasks that use a mutex in a loop receive a more equal amount of processing time, while also ensuring processing time is not wasted by switching between tasks too rapidly*
