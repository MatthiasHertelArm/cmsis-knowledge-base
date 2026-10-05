---
id: "frb-10-task-notifications-10-3-7-task-notifications-used-in-periph"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.7 Task Notifications Used in Peripheral Device Drivers: UART Example"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-7-task-notifications-used-in-peripheral-device-drivers-uart-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

Peripheral driver libraries provide functions that perform common
operations on hardware interfaces. Examples of peripherals for which
such libraries are often provided include Universal Asynchronous
Receivers and Transmitters (UARTs), Serial Peripheral Interface (SPI)
ports, analog to digital converters (ADCs), and Ethernet ports. Examples
of functions typically provided by such libraries include functions to
initialize a peripheral, send data to a peripheral, and receive data
from a peripheral.

Some operations on peripherals take a relatively long time to complete.
Examples of such operations include a high precision ADC conversion, and
the transmission of a large data packet on a UART. In these cases the
driver library function could be implemented to poll (repeatedly read)
the peripheral's status registers to determine when the operation has
completed. However, polling in this manner is nearly always wasteful as
it utilizes 100% of the processor's time while no productive processing
is being performed. The waste is particularly expensive in a
multi-tasking system, where a task that is polling a peripheral might be
preventing the execution of a lower priority task that does have
productive processing to perform.

To avoid the potential for wasted processing time, an efficient RTOS
aware device driver should be interrupt driven, and give a task that
initiates a lengthy operation the option of waiting in the Blocked state
for the operation to complete. That way, lower priority tasks can
execute while the task performing the lengthy operation is in the
Blocked state, and no tasks use processing time unless they can use it
productively.

It is common practice for RTOS aware driver libraries to use a binary
semaphore to place tasks into the Blocked state. The technique is
demonstrated by the pseudo code shown in Listing 10.10, which provides the
outline of an RTOS aware library function that transmits data on a UART
port. In Listing 10.10:

- `xUART` is a structure that describes the UART peripheral, and holds
    state information. The `xTxSemaphore` member of the structure is a
    variable of type `SemaphoreHandle_t`. It is assumed the semaphore has
    already been created.

- The `xUART_Send()` function does not include any mutual exclusion
    logic. If more than one task is going to use the `xUART_Send()`
    function, then the application writer will have to manage mutual
    exclusion within the application itself. For example, a task may be
    required to obtain a mutex before calling `xUART_Send()`.

- The `xSemaphoreTake()` API function is used to place the calling task
    into the Blocked state after the UART transmission has been initiated.

- The `xSemaphoreGiveFromISR()` API function is used to remove the task
    from the Blocked state after the transmission has completed, which
    is when the UART peripheral's transmit end interrupt service routine
    executes.





```c
/* Driver library function to send data to a UART. */

BaseType_t xUART_Send( xUART *pxUARTInstance, 
                       uint8_t *pucDataSource, 
                       size_t uxLength )
{
    BaseType_t xReturn;

    /* Ensure the UART's transmit semaphore is not already available by 
       attempting to take the semaphore without a timeout. */
    xSemaphoreTake( pxUARTInstance->xTxSemaphore, 0 );

    /* Start the transmission. */
    UART_low_level_send( pxUARTInstance, pucDataSource, uxLength );

    /* Block on the semaphore to wait for the transmission to complete. If 
       the semaphore is obtained then xReturn will get set to pdPASS. If the 
       semaphore take operation times out then xReturn will get set to pdFAIL. 
       Note that, if the interrupt occurs between UART_low_level_send() being 
       called, and xSemaphoreTake() being called, then the event will be 
       latched in the binary semaphore, and the call to xSemaphoreTake() will 
       return immediately. */
    xReturn = xSemaphoreTake( pxUARTInstance->xTxSemaphore, 
                              pxUARTInstance->xTxTimeout );

    return xReturn;
}
/*-----------------------------------------------------------*/

/* The service routine for the UART's transmit end interrupt, which executes 
   after the last byte has been sent to the UART. */
void xUART_TransmitEndISR( xUART *pxUARTInstance )
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Clear the interrupt. */
    UART_low_level_interrupt_clear( pxUARTInstance );

    /* Give the Tx semaphore to signal the end of the transmission. If a task 
       is Blocked waiting for the semaphore then the task will be removed from
       the Blocked state. */
    xSemaphoreGiveFromISR( pxUARTInstance->xTxSemaphore, 
                           &xHigherPriorityTaskWoken );
    portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
}
```

***Listing 10.10*** *Pseudo code demonstrating how a binary semaphore can be used in a driver library transmit function*

The technique demonstrated in Listing 10.10 is perfectly workable, and
indeed common practice, but it has some drawbacks:

- The library uses multiple semaphores, which increases its RAM
  footprint.

- Semaphores cannot be used until they have been created, so a library
  that uses semaphores cannot be used until it has been explicitly
  initialized.

- Semaphores are generic objects that are applicable to a wide range
  of use cases; they include logic to allow any number of tasks to
  wait in the Blocked state for the semaphore to become available, and
  to select (in a deterministic manner) which task to remove from the
  Blocked state when the semaphore does become available. Executing
  that logic takes a finite time, and that processing overhead is
  unnecessary in the scenario shown is Listing 10.10, in which there
  cannot be more than one task waiting for the semaphore at any given
  time.

Listing 10.11 demonstrates how to avoid these drawbacks by using a task
notification in place of a binary semaphore.

> *Note: If a library uses task notifications, then the library's
> documentation must clearly state that calling a library function can
> change the calling task's notification state and notification value.*

In Listing 10.11:

- The `xTxSemaphore` member of the `xUART` structure has been replaced by
  the `xTaskToNotify` member. `xTaskToNotify` is a variable of type
  `TaskHandle_t`, and is used to hold the handle of the task that is
  waiting for the UART operation to complete.

- The `xTaskGetCurrentTaskHandle()` FreeRTOS API function is used to
  obtain the handle of the task that is in the Running state.

- The library does not create any FreeRTOS objects, so it does not incur
  a RAM overhead, and does not need to be explicitly initialized.

- The task notification is sent directly to the task that is waiting
  for the UART operation to complete, so no unnecessary logic is
  executed.

The `xTaskToNotify` member of the `xUART` structure is accessed from both a
task and an interrupt service routine, requiring that consideration be
given as to how the processor will update its value:

- If `xTaskToNotify` is updated by a single memory write operation, then
  it can be updated outside of a critical section, exactly as shown in
  Listing 10.11. This would be the case if `xTaskToNotify` is a 32-bit
  variable (`TaskHandle_t` was a 32-bit type), and the processor on
  which FreeRTOS is running is a 32-bit processor.

- If more than one memory write operation is required to update
  `xTaskToNotify`, then `xTaskToNotify` must only be updated from within a
  critical section—otherwise the interrupt service routine might
  access `xTaskToNotify` while it is in an inconsistent state. This
  would be the case if `xTaskToNotify` is a 32-bit variable, and the
  processor on which FreeRTOS is running is a 16-bit processor, as it
  would require two 16-bit memory write operations to update all
  32-bits.

Internally, within the FreeRTOS implementation, `TaskHandle_t` is a
pointer, so `sizeof( TaskHandle_t )` always equals `sizeof( void * )`.





```c
/* Driver library function to send data to a UART. */
BaseType_t xUART_Send( xUART *pxUARTInstance, 
                       uint8_t *pucDataSource, 
                       size_t uxLength )
{
    BaseType_t xReturn;

    /* Save the handle of the task that called this function. The book text
       contains notes as to whether the following line needs to be protected 
       by a critical section or not. */
    pxUARTInstance->xTaskToNotify = xTaskGetCurrentTaskHandle();

    /* Ensure the calling task does not already have a notification pending by 
       calling ulTaskNotifyTake() with the xClearCountOnExit parameter set to 
       pdTRUE, and a block time of 0 (don't block). */
    ulTaskNotifyTake( pdTRUE, 0 );

    /* Start the transmission. */
    UART_low_level_send( pxUARTInstance, pucDataSource, uxLength );

    /* Block until notified that the transmission is complete. If the 
       notification is received then xReturn will be set to 1 because the ISR 
       will have incremented this task's notification value to 1 (pdTRUE). If 
       the operation times out then xReturn will be 0 (pdFALSE) because this 
       task's notification value will not have been changed since it was 
       cleared to 0 above. Note that, if the ISR executes between the calls to
       UART_low_level_send() and the call to ulTaskNotifyTake(), then the 
       event will be latched in the task's notification value, and the call to 
       ulTaskNotifyTake() will return immediately. */
    xReturn = ( BaseType_t ) ulTaskNotifyTake( pdTRUE, 
                                               pxUARTInstance->xTxTimeout );

    return xReturn;
}
/*-----------------------------------------------------------*/

/* The ISR that executes after the last byte has been sent to the UART. */
void xUART_TransmitEndISR( xUART *pxUARTInstance )
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* This function should not execute unless there is a task waiting to be 
       notified. Test this condition with an assert. This step is not strictly
       necessary, but will aid debugging. configASSERT() is described in 
       section 12.2. */
    configASSERT( pxUARTInstance->xTaskToNotify != NULL );

    /* Clear the interrupt. */
    UART_low_level_interrupt_clear( pxUARTInstance );

    /* Send a notification directly to the task that called xUART_Send(). If 
       the task is Blocked waiting for the notification then the task will be 
       removed from the Blocked state. */
    vTaskNotifyGiveFromISR( pxUARTInstance->xTaskToNotify,
                            &xHigherPriorityTaskWoken );

    /* Now there are no tasks waiting to be notified. Set the xTaskToNotify 
       member of the xUART structure back to NULL. This step is not strictly 
       necessary but will aid debugging. */
    pxUARTInstance->xTaskToNotify = NULL;
    portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
}
```

***Listing 10.11*** *Pseudo code demonstrating how a task notification can be used in a driver library transmit function*

Task notifications can also replace semaphores in receive functions, as
demonstrated in pseudo code Listing 10.12, which provides the outline of
an RTOS aware library function that receives data on a UART port.
Referring to Listing 10.12:

- The `xUART_Receive()` function does not include any mutual exclusion
  logic. If more than one task is going to use the `xUART_Receive()`
  function, then the application writer will have to manage mutual
  exclusion within the application itself. For example, a task may be
  required to obtain a mutex before calling `xUART_Receive()`.

- The UART's receive interrupt service routine places the characters
  that are received by the UART into a RAM buffer. The `xUART_Receive()`
  function returns characters from the RAM buffer.

- The `xUART_Receive()` `uxWantedBytes` parameter is used to specify the
  number of characters to receive. If the RAM buffer does not already
  contain the requested number characters, then the calling task is
  placed into the Blocked state to wait to be notified that the number
  of characters in the buffer has increased. The `while()` loop is used
  to repeat this sequence until either the receive buffer contains the
  requested number of characters, or a timeout occurs.

- The calling task may enter the Blocked state more than once. The
  block time is therefore adjusted to take into account the amount of
  time that has already passed since `xUART_Receive()` was called. The
  adjustments ensure the total time spent inside `xUART_Receive()` does
  not exceed the block time specified by the `xRxTimeout` member of the
  `xUART` structure. The block time is adjusted using the FreeRTOS
  `vTaskSetTimeOutState()` and `xTaskCheckForTimeOut()` helper functions.





```c
/* Driver library function to receive data from a UART. */

size_t xUART_Receive( xUART *pxUARTInstance, 
                      uint8_t *pucBuffer,
                      size_t uxWantedBytes )
{
    size_t uxReceived = 0;
    TickType_t xTicksToWait;
    TimeOut_t xTimeOut;

    /* Record the time at which this function was entered. */
    vTaskSetTimeOutState( &xTimeOut );

    /* xTicksToWait is the timeout value - it is initially set to the maximum 
       receive timeout for this UART instance. */
    xTicksToWait = pxUARTInstance->xRxTimeout;

    /* Save the handle of the task that called this function. The book text 
       contains notes as to whether the following line needs to be protected 
       by a critical section or not. */
    pxUARTInstance->xTaskToNotify = xTaskGetCurrentTaskHandle();

    /* Loop until the buffer contains the wanted number of bytes, or a
       timeout occurs. */
    while( UART_bytes_in_rx_buffer( pxUARTInstance ) < uxWantedBytes )
    {
        /* Look for a timeout, adjusting xTicksToWait to account for the time
           spent in this function so far. */
        if( xTaskCheckForTimeOut( &xTimeOut, &xTicksToWait ) != pdFALSE )
        {
            /* Timed out before the wanted number of bytes were available, 
               exit the loop. */
            break;
        }

        /* The receive buffer does not yet contain the required amount of 
           bytes. Wait for a maximum of xTicksToWait ticks to be notified that 
           the receive interrupt service routine has placed more data into the 
           buffer. It does not matter if the calling task already had a 
           notification pending when it called this function, if it did, it
           would just iteration around this while loop one extra time. */
        ulTaskNotifyTake( pdTRUE, xTicksToWait );
    }

    /* No tasks are waiting for receive notifications, so set xTaskToNotify
       back to NULL. The book text contains notes as to whether the following 
       line needs to be protected by a critical section or not. */
    pxUARTInstance->xTaskToNotify = NULL;

    /* Attempt to read uxWantedBytes from the receive buffer into pucBuffer. 
       The actual number of bytes read (which might be less than uxWantedBytes)
       is returned. */
    uxReceived = UART_read_from_receive_buffer( pxUARTInstance, 
                                                pucBuffer,
                                                uxWantedBytes );
    return uxReceived;
}

/*-----------------------------------------------------------*/

/* The interrupt service routine for the UART's receive interrupt */
void xUART_ReceiveISR( xUART *pxUARTInstance )
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Copy received data into this UART's receive buffer and clear the
       interrupt. */
    UART_low_level_receive( pxUARTInstance );

    /* If a task is waiting to be notified of the new data then notify it now. */
    if( pxUARTInstance->xTaskToNotify != NULL )
    {
        vTaskNotifyGiveFromISR( pxUARTInstance->xTaskToNotify,
                                &xHigherPriorityTaskWoken );
        portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
    }
}
```

***Listing 10.12*** *Pseudo code demonstrating how a task notification can be used in a driver library receive function*
