---
id: "frb-5-queue-management-5-6-4-the-xqueueselectfromset-api-functi"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.6 Receiving From Multiple Queues / 5.6.4 The xQueueSelectFromSet() API Function"
summary: "Part of: 5.6 Receiving From Multiple Queues"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-6-4-the-xqueueselectfromset-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.6 Receiving From Multiple Queues_

`xQueueSelectFromSet()` reads a queue handle from the queue set.

When a queue or semaphore that is a member of a set receives data, the
handle of the receiving queue or semaphore is sent to the queue set, and
returned when a task calls `xQueueSelectFromSet()`. If a handle is
returned from a call to `xQueueSelectFromSet()` then the queue or
semaphore referenced by the handle is known to contain data and the
calling task must then read from the queue or semaphore directly.

> *Note: Do not read data from a queue or semaphore that is a member of a
> set unless the handle of the queue or semaphore has first been returned
> from a call to `xQueueSelectFromSet()`. Only read one item from a queue or
> semaphore each time the queue handle or semaphore handle is returned
> from a call to `xQueueSelectFromSet()`.*



```c
QueueSetMemberHandle_t xQueueSelectFromSet( QueueSetHandle_t xQueueSet,
                                            const TickType_t xTicksToWait );
```
***Listing 5.23*** *The xQueueSelectFromSet() API function prototype*

**xQueueSelectFromSet() parameters and return value**

- `xQueueSet`

  The handle of the queue set from which a queue handle or semaphore
  handle is being received (read). The queue set handle will have been
  returned from the call to `xQueueCreateSet()` used to create the queue
  set.

- `xTicksToWait`

  The maximum amount of time the calling task should remain in the
  Blocked state to wait to receive a queue or semaphore handle from the
  queue set, if all the queues and semaphore in the set are empty.

  If `xTicksToWait` is zero then `xQueueSelectFromSet()` will return
  immediately if all the queues and semaphores in the set are empty.

  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds to a time
  specified in ticks.

  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without timing out) provided `INCLUDE_vTaskSuspend` is set
  to 1 in FreeRTOSConfig.h.

- Return Value

  A return value that is not NULL will be the handle of a queue or
  semaphore that is known to contain data. If a block time was specified
  (`xTicksToWait` was not zero), then it is possible the calling task was
  placed into the Blocked state to wait for data to become available from
  a queue or semaphore in the set, but a handle was successfully read from
  the queue set before the block time expired. Handles are returned as a
  `QueueSetMemberHandle_t` type, which can be cast to either a `QueueHandle_t`
  type or `SemaphoreHandle_t` type.

  If the return value is NULL then a handle could not be read from the
  queue set. If a block time was specified (`xTicksToWait` was not zero)
  then the calling task was placed in the Blocked state to
  wait for another task or interrupt to send data to a queue or semaphore
  in the set, but the block time expired before that happened.



---
***Example 5.3*** *Using a Queue Set_

---

This example creates two sending tasks and one receiving task. The
sending tasks send data to the receiving task on two separate queues,
one queue for each task. The two queues are added to a queue set, and
the receiving task reads from the queue set to determine which of the
two queues contain data.

The tasks, queues, and the queue set are all created in `main()`—see
Listing 5.24 for its implementation.



```c
/* Declare two variables of type QueueHandle_t. Both queues are added
   to the same queue set. */
static QueueHandle_t xQueue1 = NULL, xQueue2 = NULL;

/* Declare a variable of type QueueSetHandle_t. This is the queue set
   to which the two queues are added. */
static QueueSetHandle_t xQueueSet = NULL;

int main( void )
{
    /* Create the two queues, both of which send character pointers. The 
       priority of the receiving task is above the priority of the sending 
       tasks, so the queues will never have more than one item in them at 
       any one time*/
    xQueue1 = xQueueCreate( 1, sizeof( char * ) );
    xQueue2 = xQueueCreate( 1, sizeof( char * ) );

    /* Create the queue set. Two queues will be added to the set, each of
       which can contain 1 item, so the maximum number of queue handles the 
       queue set will ever have to hold at one time is 2 (2 queues multiplied 
       by 1 item per queue). */
    xQueueSet = xQueueCreateSet( 1 * 2 );

    /* Add the two queues to the set. */
    xQueueAddToSet( xQueue1, xQueueSet );
    xQueueAddToSet( xQueue2, xQueueSet );

    /* Create the tasks that send to the queues. */
    xTaskCreate( vSenderTask1, "Sender1", 1000, NULL, 1, NULL );
    xTaskCreate( vSenderTask2, "Sender2", 1000, NULL, 1, NULL );

    /* Create the task that reads from the queue set to determine which of
       the two queues contain data. */
    xTaskCreate( vReceiverTask, "Receiver", 1000, NULL, 2, NULL );

    /* Start the scheduler so the created tasks start executing. */
    vTaskStartScheduler();

    /* As normal, vTaskStartScheduler() should not return, so the following
       lines will never execute. */
    for( ;; );
    return 0;
}
```
***Listing 5.24*** *Implementation of main() for Example 5.3*

The first sending task uses `xQueue1` to send a character pointer to the
receiving task every 100 milliseconds. The second sending task uses
`xQueue2` to send a character pointer to the receiving task every 200
milliseconds. The character pointers point to a string that identifies
the sending task. Listing 5.25 shows the implementation of both tasks.



```c
void vSenderTask1( void *pvParameters )
{
    const TickType_t xBlockTime = pdMS_TO_TICKS( 100 );
    const char * const pcMessage = "Message from vSenderTask1\r\n";

    /* As per most tasks, this task is implemented within an infinite loop. */

    for( ;; )
    {

        /* Block for 100ms. */
        vTaskDelay( xBlockTime );

        /* Send this task's string to xQueue1. It is not necessary to use a
           block time, even though the queue can only hold one item. This is 
           because the priority of the task that reads from the queue is 
           higher than the priority of this task; as soon as this task writes 
           to the queue it will be pre-empted by the task that reads from the 
           queue, so the queue will already be empty again by the time the 
           call to xQueueSend() returns. The block time is set to 0. */
        xQueueSend( xQueue1, &pcMessage, 0 );
    }
}

/*-----------------------------------------------------------*/

void vSenderTask2( void *pvParameters )
{
    const TickType_t xBlockTime = pdMS_TO_TICKS( 200 );
    const char * const pcMessage = "Message from vSenderTask2\r\n";

    /* As per most tasks, this task is implemented within an infinite loop. */
    for( ;; )
    {
        /* Block for 200ms. */
        vTaskDelay( xBlockTime );

        /* Send this task's string to xQueue2. It is not necessary to use a
           block time, even though the queue can only hold one item. This is 
           because the priority of the task that reads from the queue is 
           higher than the priority of this task; as soon as this task writes 
           to the queue it will be pre-empted by the task that reads from the 
           queue, so the queue will already be empty again by the time the 
           call to xQueueSend() returns. The block time is set to 0. */
        xQueueSend( xQueue2, &pcMessage, 0 );
    }
}
```
***Listing 5.25*** *The sending tasks used in Example 5.3*


The queues written to by the sending tasks are members of the same queue
set. Each time a task sends to one of the queues, the handle of the
queue is sent to the queue set. The receiving task calls
`xQueueSelectFromSet()` to read the queue handles from the queue set.
After the receiving task receives a queue handle from the set, it knows
the queue referenced by the received handle contains data, so it reads the
data from the queue directly. The data it reads from the queue is a
pointer to a string, which the receiving task prints out.

If a call to `xQueueSelectFromSet()` times out, it returns NULL. In Example
5.3, `xQueueSelectFromSet()` is called with an indefinite block time, so it
will never time out, and can only return a valid queue handle.
Therefore, the receiving task does not need to check to see if
`xQueueSelectFromSet()` returned NULL before using the returned value.

`xQueueSelectFromSet()` only returns a queue handle if the queue
referenced by the handle contains data, so it is not necessary to use a
block time when reading from the queue.

Listing 5.26 shows the implementation of the receive task.



```c
void vReceiverTask( void *pvParameters )
{
    QueueHandle_t xQueueThatContainsData;
    char *pcReceivedString;

    /* As per most tasks, this task is implemented within an infinite loop. */
    for( ;; )
    {
        /* Block on the queue set to wait for one of the queues in the set to
           contain data. Cast the QueueSetMemberHandle_t value returned from
           xQueueSelectFromSet() to a QueueHandle_t, as it is known all the 
           members of the set are queues (the queue set does not contain any 
           semaphores). */
        xQueueThatContainsData = ( QueueHandle_t ) xQueueSelectFromSet(
                                                     xQueueSet, portMAX_DELAY );

        /* An indefinite block time was used when reading from the queue set,
           so xQueueSelectFromSet() will not have returned unless one of the 
           queues in the set contained data, and xQueueThatContainsData cannot
           be NULL. Read from the queue. It is not necessary to specify a 
           block time because it is known the queue contains data. The block 
           time is set to 0. */
        xQueueReceive( xQueueThatContainsData, &pcReceivedString, 0 );

        /* Print the string received from the queue. */
        vPrintString( pcReceivedString );
    }
}
```
***Listing 5.26*** *The receive task used in Example 5.3*

Figure 5.7 shows the output produced by Example 5.3. It can be seen that
the receiving task receives strings from both sending tasks. The block
time used by `vSenderTask1()` is half of the block time used by
`vSenderTask2()`, which causes the strings sent by `vSenderTask1()` to print out
twice as often as those sent by `vSenderTask2()`.



* * *
   
***Figure 5.7*** *The output produced when Example 5.3 is executed*
* * *
