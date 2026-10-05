---
id: "frb-7-interrupt-management-7-4-3-the-xsemaphoregivefromisr-api-func"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.4 Binary Semaphores Used for Synchronization / 7.4.3 The xSemaphoreGiveFromISR() API Function"
summary: "Part of: 7.4 Binary Semaphores Used for Synchronization"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-4-3-the-xsemaphoregivefromisr-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 7.4 Binary Semaphores Used for Synchronization_

Binary and counting semaphores[^16] can be 'given' using the
`xSemaphoreGiveFromISR()` function.

[^16]: Counting semaphores are described in a later section of this book.

`xSemaphoreGiveFromISR()` is the interrupt safe version of
`xSemaphoreGive()`, so has the `pxHigherPriorityTaskWoken` parameter that
was described at the start of this chapter.




```c
BaseType_t xSemaphoreGiveFromISR( SemaphoreHandle_t xSemaphore,
                                  BaseType_t *pxHigherPriorityTaskWoken );
```
***Listing 7.5*** *The xSemaphoreGiveFromISR() API function prototype*

**xSemaphoreGiveFromISR() parameters and return value**

- `xSemaphore`

  The semaphore being 'given'.

  A semaphore is referenced by a variable of type `SemaphoreHandle_t`,
  and must be explicitly created before being used.

- `pxHigherPriorityTaskWoken`

  It is possible that a single semaphore will have one or more
  tasks blocked on it waiting for the semaphore to become available.
  Calling `xSemaphoreGiveFromISR()` can make the semaphore available, and so
  cause a task that was waiting for the semaphore to leave the Blocked
  state. If calling `xSemaphoreGiveFromISR()` causes a task to leave the
  Blocked state, and the unblocked task has a priority higher than the
  currently executing task (the task that was interrupted), then,
  internally, `xSemaphoreGiveFromISR()` will set `*pxHigherPriorityTaskWoken`
  to `pdTRUE`.

  If `xSemaphoreGiveFromISR()` sets this value to `pdTRUE`, then normally a
  context switch should be performed before the interrupt is exited. This
  will ensure that the interrupt returns directly to the highest priority
  Ready state task.

- Return value

  There are two possible return values:

  - `pdPASS`

    `pdPASS` will be returned only if the call to `xSemaphoreGiveFromISR()`
    is successful.

  - `pdFAIL`

    If a semaphore is already available, it cannot be given, and
    `xSemaphoreGiveFromISR()` will return `pdFAIL`.



---
***Example 7.1*** *Using a binary semaphore to synchronize a task with an interrupt*

---

This example uses a binary semaphore to unblock a task from an interrupt
service routine, effectively synchronizing the task with the interrupt.

A simple periodic task is used to generate a software interrupt every
500 milliseconds. A software interrupt is used for convenience because
of the complexity of hooking into a real interrupt in some target
environments. Listing 7.6 shows the implementation of the periodic task.
Note that the task prints out a string both before and after the
interrupt is generated. This allows the sequence of execution to be
observed in the output produced when the example is executed.




```c
/* The number of the software interrupt used in this example. The code
   shown is from the Windows project, where numbers 0 to 2 are used by the
   FreeRTOS Windows port itself, so 3 is the first number available to the
   application. */
#define mainINTERRUPT_NUMBER 3

static void vPeriodicTask( void *pvParameters )
{
    const TickType_t xDelay500ms = pdMS_TO_TICKS( 500UL );

    /* As per most tasks, this task is implemented within an infinite loop. */
    for( ;; )
    {
        /* Block until it is time to generate the software interrupt again. */
        vTaskDelay( xDelay500ms );

        /* Generate the interrupt, printing a message both before and after
           the interrupt has been generated, so the sequence of execution is
           evident from the output.

           The syntax used to generate a software interrupt is dependent on
           the FreeRTOS port being used. The syntax used below can only be
           used with the FreeRTOS Windows port, in which such interrupts are
           only simulated. */
        vPrintString( "Periodic task - About to generate an interrupt.\r\n" );
        vPortGenerateSimulatedInterrupt( mainINTERRUPT_NUMBER );
        vPrintString( "Periodic task - Interrupt generated.\r\n\r\n\r\n" );
    }
}
```
***Listing 7.6*** *Implementation of the task that periodically generates a software interrupt in Example 7.1*


Listing 7.7 shows the implementation of the task to which the interrupt
processing is deferred—the task that is synchronized with the software
interrupt through the use of a binary semaphore. Again, a string is
printed out on each iteration of the task, so the sequence in which the
task and the interrupt execute is evident from the output produced when
the example is executed.

It should be noted that, while the code shown in Listing 7.7 is adequate
for Example 7.1, where interrupts are generated by software, it is not
adequate for scenarios where interrupts are generated by hardware
peripherals. A following sub-section describes how the structure of the
code needs to be changed to make it suitable for use with hardware
generated interrupts.




```c
static void vHandlerTask( void *pvParameters )
{
    /* As per most tasks, this task is implemented within an infinite loop. */
    for( ;; )
    {
        /* Use the semaphore to wait for the event. The semaphore was created
           before the scheduler was started, so before this task ran for the
           first time. The task blocks indefinitely, meaning this function
           call will only return once the semaphore has been successfully
           obtained - so there is no need to check the value returned by
           xSemaphoreTake(). */
        xSemaphoreTake( xBinarySemaphore, portMAX_DELAY );

        /* To get here the event must have occurred. Process the event (in
           this Case, just print out a message). */
        vPrintString( "Handler task - Processing event.\r\n" );
    }
}
```
***Listing 7.7*** *The implementation of the task to which the interrupt processing is deferred (the task that synchronizes with the interrupt) in Example 7.1*


Listing 7.8 shows the ISR. This does very little other than 'give' the
semaphore to unblock the task to which interrupt processing is deferred.

Note how the `xHigherPriorityTaskWoken` variable is used. It is set to
`pdFALSE` before calling `xSemaphoreGiveFromISR()`, then used as the
parameter when `portYIELD_FROM_ISR()` is called. A context switch will be
requested inside the `portYIELD_FROM_ISR()` macro if
`xHigherPriorityTaskWoken` equals `pdTRUE`.

The prototype of the ISR, and the macro called to force a context
switch, are both correct for the FreeRTOS Windows port, and may be
different for other FreeRTOS ports. Refer to the port specific
documentation pages on the FreeRTOS.org website, and the examples
provided in the FreeRTOS download, to find the syntax required for the
port you are using.

Unlike most architectures on which FreeRTOS runs, the FreeRTOS Windows
port requires an ISR to return a value. The implementation of the
`portYIELD_FROM_ISR()` macro provided with the Windows port includes the
return statement, so Listing 7.8 does not show a value being returned
explicitly.




```c
static uint32_t ulExampleInterruptHandler( void )
{
    BaseType_t xHigherPriorityTaskWoken;

    /* The xHigherPriorityTaskWoken parameter must be initialized to
       pdFALSE as it will get set to pdTRUE inside the interrupt safe
       API function if a context switch is required. */
    xHigherPriorityTaskWoken = pdFALSE;

    /* 'Give' the semaphore to unblock the task, passing in the address of
       xHigherPriorityTaskWoken as the interrupt safe API function's
       pxHigherPriorityTaskWoken parameter. */
    xSemaphoreGiveFromISR( xBinarySemaphore, &xHigherPriorityTaskWoken );

    /* Pass the xHigherPriorityTaskWoken value into portYIELD_FROM_ISR().
       If xHigherPriorityTaskWoken was set to pdTRUE inside
       xSemaphoreGiveFromISR() then calling portYIELD_FROM_ISR() will request
       a context switch. If xHigherPriorityTaskWoken is still pdFALSE then
       calling portYIELD_FROM_ISR() will have no effect. Unlike most FreeRTOS
       ports, the Windows port requires the ISR to return a value - the return
       statement is inside the Windows version of portYIELD_FROM_ISR(). */
    portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
}
```
***Listing 7.8*** *The ISR for the software interrupt used in Example 7.1*

The `main()` function creates the binary semaphore, creates the tasks,
installs the interrupt handler, and starts the scheduler. The
implementation is shown in Listing 7.9.

The syntax of the function called to install an interrupt handler is
specific to the FreeRTOS Windows port, and may be different for other
FreeRTOS ports. Refer to the port specific documentation pages on the
FreeRTOS.org website, and the examples provided in the FreeRTOS
download, to find the syntax required for the port you are using.




```c
int main( void )
{
    /* Before a semaphore is used it must be explicitly created. In this
       example a binary semaphore is created. */
    xBinarySemaphore = xSemaphoreCreateBinary();

    /* Check the semaphore was created successfully. */
    if( xBinarySemaphore != NULL )
    {
        /* Create the 'handler' task, which is the task to which interrupt
           processing is deferred. This is the task that will be synchronized
           with the interrupt. The handler task is created with a high priority
           to ensure it runs immediately after the interrupt exits. In this
           case a priority of 3 is chosen. */
        xTaskCreate( vHandlerTask, "Handler", 1000, NULL, 3, NULL );

        /* Create the task that will periodically generate a software
           interrupt. This is created with a priority below the handler task
           to ensure it will get preempted each time the handler task exits
           the Blocked state. */
        xTaskCreate( vPeriodicTask, "Periodic", 1000, NULL, 1, NULL );

        /* Install the handler for the software interrupt. The syntax necessary
           to do this is dependent on the FreeRTOS port being used. The syntax
           shown here can only be used with the FreeRTOS windows port, where
           such interrupts are only simulated. */
        vPortSetInterruptHandler( mainINTERRUPT_NUMBER,
                                  ulExampleInterruptHandler );

        /* Start the scheduler so the created tasks start executing. */
        vTaskStartScheduler();
    }

    /* As normal, the following line should never be reached. */
    for( ;; );
}
```
***Listing 7.9*** *The implementation of main() for Example 7.1*


Example 7.1 produces the output shown in Figure 7.4. As expected,
`vHandlerTask()` enters the Running state as soon as the interrupt is
generated, so the output from the task splits the output produced by the
periodic task. Further explanation is provided in Figure 7.5.





* * *

***Figure 7.4*** *The output produced when Example 7.1 is executed*


***Figure 7.5*** *The sequence of execution when Example 7.1 is executed*
* * *
