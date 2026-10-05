---
id: "frb-5-queue-management-5-6-5-more-realistic-queue-set-use-cases"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.6 Receiving From Multiple Queues / 5.6.5 More Realistic Queue Set Use Cases"
summary: "Part of: 5.6 Receiving From Multiple Queues"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-6-5-more-realistic-queue-set-use-cases"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.6 Receiving From Multiple Queues_

Example 5.3 demonstrated a very simplistic case; the queue set only
contained queues, and the two queues it contained were both used to send
a character pointer. In a real application, a queue set might contain
both queues and semaphores, and the queues might not all hold the same
data type. When this is the case, it is necessary to test the value
returned by `xQueueSelectFromSet()`, before using the returned value.
Listing 5.27 demonstrates how to use the value returned from
`xQueueSelectFromSet()` when the set has the following members:

- A binary semaphore.
- A queue from which character pointers are read.
- A queue from which `uint32_t` values are read.

Listing 5.27 assumes the queues and semaphore have already been created
and added to the queue set.



```c
/* The handle of the queue from which character pointers are received. */
QueueHandle_t xCharPointerQueue;

/* The handle of the queue from which uint32_t values are received. */
QueueHandle_t xUint32tQueue;

/* The handle of the binary semaphore. */
SemaphoreHandle_t xBinarySemaphore;

/* The queue set to which the two queues and the binary semaphore belong. */
QueueSetHandle_t xQueueSet;

void vAMoreRealisticReceiverTask( void *pvParameters )
{
    QueueSetMemberHandle_t xHandle;
    char *pcReceivedString;
    uint32_t ulRecievedValue;
    const TickType_t xDelay100ms = pdMS_TO_TICKS( 100 );

    for( ;; )
    {
        /* Block on the queue set for a maximum of 100ms to wait for one of the
           members of the set to contain data. */
        xHandle = xQueueSelectFromSet( xQueueSet, xDelay100ms );

        /* Test the value returned from xQueueSelectFromSet(). If the returned
           value is NULL then the call to xQueueSelectFromSet() timed out. If 
           the returned value is not NULL then the returned value will be the 
           handle of one of the set's members. The QueueSetMemberHandle_t 
           value can be cast to either a QueueHandle_t or a SemaphoreHandle_t.
           Whether an explicit cast is required depends on the compiler. */

        if( xHandle == NULL )
        {
            /* The call to xQueueSelectFromSet() timed out. */
        }
        else if( xHandle == ( QueueSetMemberHandle_t ) xCharPointerQueue )
        {
            /* The call to xQueueSelectFromSet() returned the handle of the 
               queue that receives character pointers. Read from the queue. 
               The queue is known to contain data, so a block time of 0 is 
               used. */
            xQueueReceive( xCharPointerQueue, &pcReceivedString, 0 );

            /* The received character pointer can be processed here... */
        }
        else if( xHandle == ( QueueSetMemberHandle_t ) xUint32tQueue )
        {
            /* The call to xQueueSelectFromSet() returned the handle of the 
               queue that receives uint32_t types. Read from the queue. The 
               queue is known to contain data, so a block time of 0 is used. */
            xQueueReceive(xUint32tQueue, &ulRecievedValue, 0 );

            /* The received value can be processed here... */
        }
        else if( xHandle == ( QueueSetMemberHandle_t ) xBinarySemaphore )
        {
            /* The call to xQueueSelectFromSet() returned the handle of the 
               binary semaphore. Take the semaphore now. The semaphore is 
               known to be available so a block time of 0 is used. */
            xSemaphoreTake( xBinarySemaphore, 0 );

            /* Whatever processing is necessary when the semaphore is taken 
               can be performed here... */
        }
    }
}
```
***Listing 5.27*** *Using a queue set that contains queues and semaphores*
