---
id: "frb-9-event-groups-9-3-5-the-xeventgroupgetstaticbuffer-api"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.3 Event Management Using Event Groups / 9.3.5 The xEventGroupGetStaticBuffer() API Function"
summary: "Part of: 9.3 Event Management Using Event Groups"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-3-5-the-xeventgroupgetstaticbuffer-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 9.3 Event Management Using Event Groups_

The `xEventGroupGetStaticBuffer()` API function provides a method to retrieve a pointer
to a buffer of a statically created event group. It is the same buffer that is supplied
at the time of creation of the event group.

*Note: Never call `xEventGroupGetStaticBuffer()` from an interrupt service
routine.




```c
BaseType_t xEventGroupGetStaticBuffer( EventGroupHandle_t xEventGroup,

StaticEventGroup_t ** ppxEventGroupBuffer );
```
***Listing 9.5*** *The xEventGroupGetStaticBuffer() API function prototype*


**xEventGroupGetStaticBuffer() parameters and return value**

- `xEventGroup`

  The event group for which to retrieve the buffer. This event group must
  be created by `xEventGroupCreateStatic()`.

- `ppxEventGroupBuffer`

  Used to return a pointer to the event groups's data structure buffer.
  It is the same buffer that is supplied at the time of creation.

- Return Value

  There are two possible return values:

  - `pdTRUE` will be returned if the buffer was successfully retrieved.

  - `pdFALSE` will be returned if the buffer was not successfully retrieved.


---
***Example 9.1*** *Experimenting with event groups*

---

This example demonstrates how to:

- Create an event group.
- Set bits in an event group from an interrupt service routine.
- Set bits in an event group from a task.
- Block on an event group.

The effect of the `xEventGroupWaitBits()` `xWaitForAllBits` parameter is
demonstrated by first executing the example with `xWaitForAllBits` set to
`pdFALSE`, and then executing the example with `xWaitForAllBits` set to
`pdTRUE`.

Event bit 0 and event bit 1 are set from a task. Event bit 2 is set from
an interrupt service routine. These three bits are given descriptive
names using the \#define statements shown in Listing 9.6.




```c
/* Definitions for the event bits in the event group. */
#define mainFIRST_TASK_BIT ( 1UL << 0UL )  /* Event bit 0, set by a task */
#define mainSECOND_TASK_BIT ( 1UL << 1UL ) /* Event bit 1, set by a task */
#define mainISR_BIT ( 1UL << 2UL )         /* Event bit 2, set by an ISR */
```
***Listing 9.6*** *Event bit definitions used in Example 9.1*


Listing 9.7 shows the implementation of the task that sets event bit 0
and event bit 1. It sits in a loop, repeatedly setting one bit, then the
other, with a delay of 200 milliseconds between each call to
`xEventGroupSetBits()`. A string is printed out before each bit is set to
allow the sequence of execution to be seen in the console.




```c
static void vEventBitSettingTask( void *pvParameters )
{
    const TickType_t xDelay200ms = pdMS_TO_TICKS( 200UL );

    for( ;; )
    {
        /* Delay for a short while before starting the next loop. */
        vTaskDelay( xDelay200ms );

        /* Print out a message to say event bit 0 is about to be set by the
           task, then set event bit 0. */
        vPrintString( "Bit setting task -\t about to set bit 0.\r\n" );
        xEventGroupSetBits( xEventGroup, mainFIRST_TASK_BIT );

        /* Delay for a short while before setting the other bit. */
        vTaskDelay( xDelay200ms );

        /* Print out a message to say event bit 1 is about to be set by the
           task, then set event bit 1. */
        vPrintString( "Bit setting task -\t about to set bit 1.\r\n" );
        xEventGroupSetBits( xEventGroup, mainSECOND_TASK_BIT );
    }
}
```
***Listing 9.7*** *The task that sets two bits in the event group in Example 9.1*


Listing 9.8 shows the implementation of the interrupt service routine
that sets bit 2 in the event group. Again, a string is printed out
before the bit is set to allow the sequence of execution to be seen in
the console. In this case however, because console output should not be
performed directly in an interrupt service routine,
`xTimerPendFunctionCallFromISR()` is used to perform the output in the
context of the RTOS daemon task.

As in previous examples, the interrupt service routine is triggered by a
simple periodic task that forces a software interrupt. In this example,
the interrupt is generated every 500 milliseconds.




```c
static uint32_t ulEventBitSettingISR( void )
{
    /* The string is not printed within the interrupt service routine, but is
       instead sent to the RTOS daemon task for printing. It is therefore
       declared static to ensure the compiler does not allocate the string on
       the stack of the ISR, as the ISR's stack frame will not exist when the
       string is printed from the daemon task. */
    static const char *pcString = "Bit setting ISR -\t about to set bit 2.\r\n";
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Print out a message to say bit 2 is about to be set. Messages cannot
       be printed from an ISR, so defer the actual output to the RTOS daemon
       task by pending a function call to run in the context of the RTOS
       daemon task. */
    xTimerPendFunctionCallFromISR( vPrintStringFromDaemonTask,
                                   ( void * ) pcString,
                                   0,
                                   &xHigherPriorityTaskWoken );

    /* Set bit 2 in the event group. */
    xEventGroupSetBitsFromISR( xEventGroup,
                               mainISR_BIT,
                               &xHigherPriorityTaskWoken );

    /* xTimerPendFunctionCallFromISR() and xEventGroupSetBitsFromISR() both
       write to the timer command queue, and both used the same
       xHigherPriorityTaskWoken variable. If writing to the timer command
       queue resulted in the RTOS daemon task leaving the Blocked state, and
       if the priority of the RTOS daemon task is higher than the priority of
       the currently executing task (the task this interrupt interrupted) then
       xHigherPriorityTaskWoken will have been set to pdTRUE.

       xHigherPriorityTaskWoken is used as the parameter to
       portYIELD_FROM_ISR(). If xHigherPriorityTaskWoken equals pdTRUE, then
       calling portYIELD_FROM_ISR() will request a context switch. If
       xHigherPriorityTaskWoken is still pdFALSE, then calling
       portYIELD_FROM_ISR() will have no effect.

       The implementation of portYIELD_FROM_ISR() used by the Windows port
       includes a return statement, which is why this function does not
       explicitly return a value. */

    portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
}
```
***Listing 9.8*** *The ISR that sets bit 2 in the event group in Example 9.1*


Listing 9.9 shows the implementation of the task that calls
`xEventGroupWaitBits()` to block on the event group. The task prints out a
string for each bit that is set in the event group.

The `xEventGroupWaitBits()` `xClearOnExit` parameter is set to `pdTRUE`, so
the event bit, or bits, that caused the call to `xEventGroupWaitBits()` to
return will be cleared automatically before `xEventGroupWaitBits()`
returns.




```c
static void vEventBitReadingTask( void *pvParameters )
{
    EventBits_t xEventGroupValue;
    const EventBits_t xBitsToWaitFor = ( mainFIRST_TASK_BIT  |
                                         mainSECOND_TASK_BIT |
                                         mainISR_BIT );

    for( ;; )
    {
        /* Block to wait for event bits to become set within the event
           group. */
        xEventGroupValue = xEventGroupWaitBits( /* The event group to read */
                                                xEventGroup,

                                                /* Bits to test */
                                                xBitsToWaitFor,

                                                /* Clear bits on exit if the
                                                   unblock condition is met */
                                                pdTRUE,

                                                /* Don't wait for all bits. This
                                                   parameter is set to pdTRUE for the
                                                   second execution. */
                                                pdFALSE,

                                                /* Don't time out. */
                                                portMAX_DELAY );

        /* Print a message for each bit that was set. */
        if( ( xEventGroupValue & mainFIRST_TASK_BIT ) != 0 )
        {
            vPrintString( "Bit reading task -\t Event bit 0 was set\r\n" );
        }

        if( ( xEventGroupValue & mainSECOND_TASK_BIT ) != 0 )
        {
            vPrintString( "Bit reading task -\t Event bit 1 was set\r\n" );
        }

        if( ( xEventGroupValue & mainISR_BIT ) != 0 )
        {
            vPrintString( "Bit reading task -\t Event bit 2 was set\r\n" );
        }
    }
}
```
***Listing 9.9*** *The task that blocks to wait for event bits to become set in Example 9.1*


The `main()` function creates the event group, and the tasks, before
starting the scheduler. See Listing 9.10 for its implementation. The
priority of the task that reads from the event group is higher than the
priority of the task that writes to the event group, ensuring the
reading task will pre-empt the writing task each time the reading task's
unblock condition is met.




```c
int main( void )
{
    /* Before an event group can be used it must first be created. */
    xEventGroup = xEventGroupCreate();

    /* Create the task that sets event bits in the event group. */
    xTaskCreate( vEventBitSettingTask, "Bit Setter", 1000, NULL, 1, NULL );

    /* Create the task that waits for event bits to get set in the event
       group. */
    xTaskCreate( vEventBitReadingTask, "Bit Reader", 1000, NULL, 2, NULL );

    /* Create the task that is used to periodically generate a software
       interrupt. */
    xTaskCreate( vInterruptGenerator, "Int Gen", 1000, NULL, 3, NULL );

    /* Install the handler for the software interrupt. The syntax necessary
       to do this is dependent on the FreeRTOS port being used. The syntax
       shown here can only be used with the FreeRTOS Windows port, where such
       interrupts are only simulated. */
    vPortSetInterruptHandler( mainINTERRUPT_NUMBER, ulEventBitSettingISR );

    /* Start the scheduler so the created tasks start executing. */
    vTaskStartScheduler();

    /* The following line should never be reached. */
    for( ;; );
    return 0;
}
```
***Listing 9.10*** *Creating the event group and tasks in Example 9.1*


The output produced when Example 9.1 is executed with the
`xEventGroupWaitBits()` `xWaitForAllBits` parameter set to `pdFALSE` is shown
in Figure 9.3. In Figure 9.3, it can be seen that, because the
`xWaitForAllBits` parameter in the call to `xEventGroupWaitBits()` was set
to `pdFALSE`, the task that reads from the event group leaves the Blocked
state and executes immediately every time any of the event bits are set.




* * *

***Figure 9.3*** *The output produced when Example 9.1 is executed with xWaitForAllBits set to pdFALSE*
* * *

The output produced when Example 9.1 is executed with the
`xEventGroupWaitBits()` `xWaitForAllBits` parameter set to `pdTRUE` is shown
in Figure 9.4. In Figure 9.4 it can be seen that, because the
`xWaitForAllBits` parameter was set to `pdTRUE`, the task that reads from
the event group only leaves the Blocked state after all three of the
event bits are set.




* * *

***Figure 9.4*** *The output produced when Example 9.1 is executed with xWaitForAllBits set to pdTRUE*
* * *
