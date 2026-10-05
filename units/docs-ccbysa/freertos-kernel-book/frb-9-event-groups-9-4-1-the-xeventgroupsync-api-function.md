---
id: "frb-9-event-groups-9-4-1-the-xeventgroupsync-api-function"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.4 Task Synchronization Using an Event Group / 9.4.1 The xEventGroupSync() API Function"
summary: "Part of: 9.4 Task Synchronization Using an Event Group"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-4-1-the-xeventgroupsync-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 9.4 Task Synchronization Using an Event Group_

`xEventGroupSync()` is provided to allow two or more tasks to use an event
group to synchronize with each other. The function allows a task to set
one or more event bits in an event group, then wait for a combination of
event bits to become set in the same event group, as a single
uninterruptable operation.

The `xEventGroupSync()` `uxBitsToWaitFor` parameter specifies the calling
task's unblock condition. The event bits specified by `uxBitsToWaitFor`
will be cleared back to zero before `xEventGroupSync()` returns, if
`xEventGroupSync()` returned because the unblock condition had been met.




```c
EventBits_t xEventGroupSync( EventGroupHandle_t xEventGroup,
                             const EventBits_t uxBitsToSet,
                             const EventBits_t uxBitsToWaitFor,
                             TickType_t xTicksToWait );
```
***Listing 9.12*** *The xEventGroupSync() API function prototype*


**xEventGroupSync() parameters and return value**

- `xEventGroup`

  The handle of the event group in which event bits are to be set, and
  then tested. The event group handle will have been returned from the
  call to `xEventGroupCreate()` used to create the event group.

- `uxBitsToSet`

  A bit mask that specifies the event bit, or event bits, to set to
  1 in the event group. The value of the event group is updated by bitwise
  ORing the event group's existing value with the value passed in
  `uxBitsToSet`.

  As an example, setting `uxBitsToSet` to 0x04 (binary 0100) will result
  in event bit 2 becoming set (if it was not already set), while leaving
  all the other event bits in the event group unchanged.

- `uxBitsToWaitFor`

  A bit mask that specifies the event bit, or event bits, to test
  in the event group.

  For example, if the calling task wants to wait for event bits 0, 1
  and 2 to become set in the event group, then set `uxBitsToWaitFor` to 0x07
  (binary 111).

- `xTicksToWait`

  The maximum amount of time the task should remain in the Blocked
  state to wait for its unblock condition to be met.

  `xEventGroupSync()` will return immediately if `xTicksToWait` is zero, or
  the unblock condition is met at the time `xEventGroupSync()` is
  called.

  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds into a time
  specified in ticks.

  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without timing out), provided `INCLUDE_vTaskSuspend` is set
  to 1 in FreeRTOSConfig.h.

- Returned Value

  If `xEventGroupSync()` returned because the calling task's unblock
  condition was met, then the returned value is the value of the event
  group at the time the calling task's unblock condition was met (before
  any bits were automatically cleared back to zero). In this case the
  returned value will also meet the calling task's unblock condition.

  If `xEventGroupSync()` returned because the block time specified by the
  `xTicksToWait` parameter expired, then the returned value is the value of
  the event group at the time the block time expired. In this case the
  returned value will not meet the calling task's unblock
  condition.



---
***Example 9.2*** *Synchronizing tasks*

---

Example 9.2 uses `xEventGroupSync()` to synchronize three instances of a
single task implementation. The task parameter is used to pass into each
instance the event bit the task will set when it calls
`xEventGroupSync()`.

The task prints a message before calling `xEventGroupSync()`, and again
after the call to `xEventGroupSync()` has returned. Each message includes
a time stamp. This allows the sequence of execution to be observed in
the output produced. A pseudo random delay is used to prevent all the
tasks reaching the synchronization point at the same time.

See Listing 9.12 for the task's implementation.




```c
static void vSyncingTask( void *pvParameters )
{
    const TickType_t xMaxDelay = pdMS_TO_TICKS( 4000UL );
    const TickType_t xMinDelay = pdMS_TO_TICKS( 200UL );
    TickType_t xDelayTime;
    EventBits_t uxThisTasksSyncBit;
    const EventBits_t uxAllSyncBits = ( mainFIRST_TASK_BIT  |
                                        mainSECOND_TASK_BIT |
                                        mainTHIRD_TASK_BIT );

    /* Three instances of this task are created - each task uses a different
       event bit in the synchronization. The event bit to use is passed into
       each task instance using the task parameter. Store it in the
       uxThisTasksSyncBit variable. */
    uxThisTasksSyncBit = ( EventBits_t ) pvParameters;

    for( ;; )
    {
        /* Simulate this task taking some time to perform an action by delaying
           for a pseudo random time. This prevents all three instances of this
           task reaching the synchronization point at the same time, and so
           allows the example's behavior to be observed more easily. */
        xDelayTime = ( rand() % xMaxDelay ) + xMinDelay;
        vTaskDelay( xDelayTime );

        /* Print out a message to show this task has reached its synchronization
           point. pcTaskGetTaskName() is an API function that returns the name
           assigned to the task when the task was created. */
        vPrintTwoStrings( pcTaskGetTaskName( NULL ), "reached sync point" );

        /* Wait for all the tasks to have reached their respective
           synchronization points. */
        xEventGroupSync( /* The event group used to synchronize. */
                         xEventGroup,

                         /* The bit set by this task to indicate it has reached
                            the synchronization point. */
                         uxThisTasksSyncBit,

                         /* The bits to wait for, one bit for each task taking
                            part in the synchronization. */
                         uxAllSyncBits,

                         /* Wait indefinitely for all three tasks to reach the
                            synchronization point. */
                         portMAX_DELAY );

        /* Print out a message to show this task has passed its synchronization
           point. As an indefinite delay was used the following line will only
           be executed after all the tasks reached their respective
           synchronization points. */
        vPrintTwoStrings( pcTaskGetTaskName( NULL ), "exited sync point" );
    }
}
```
***Listing 9.13*** *The implementation of the task used in Example 9.2*

The `main()` function creates the event group, creates all three tasks,
and then starts the scheduler. See Listing 9.14 for its implementation.




```c
/* Definitions for the event bits in the event group. */

#define mainFIRST_TASK_BIT ( 1UL << 0UL ) /* Event bit 0, set by the 1st task */
#define mainSECOND_TASK_BIT( 1UL << 1UL ) /* Event bit 1, set by the 2nd task */
#define mainTHIRD_TASK_BIT ( 1UL << 2UL ) /* Event bit 2, set by the 3rd task */

/* Declare the event group used to synchronize the three tasks. */
EventGroupHandle_t xEventGroup;

int main( void )
{
    /* Before an event group can be used it must first be created. */
    xEventGroup = xEventGroupCreate();

    /* Create three instances of the task. Each task is given a different
       name, which is later printed out to give a visual indication of which
       task is executing. The event bit to use when the task reaches its
       synchronization point is passed into the task using the task parameter. */
    xTaskCreate( vSyncingTask, "Task 1", 1000, mainFIRST_TASK_BIT, 1, NULL );
    xTaskCreate( vSyncingTask, "Task 2", 1000, mainSECOND_TASK_BIT, 1, NULL );
    xTaskCreate( vSyncingTask, "Task 3", 1000, mainTHIRD_TASK_BIT, 1, NULL );

    /* Start the scheduler so the created tasks start executing. */
    vTaskStartScheduler();

    /* As always, the following line should never be reached. */
    for( ;; );
    return 0;
}
```
***Listing 9.14*** *The main() function used in Example 9.2*

The output produced when Example 9.2 is executed is shown in Figure 9.5.
It can be seen that, even though each task reaches the synchronization
point at a different (pseudo random) time, each task exits the
synchronization point at the same time[^26] (which is the time at which
the last task reached the synchronization point).

[^26]: Figure 9.5 shows the example running in the FreeRTOS Windows port,
which does not provide true real time behavior (especially when
using Windows system calls to print to the console), and will
therefore show some timing variation.




* * *

***Figure 9.5*** *The output produced when Example 9.2 is executed*
* * *
