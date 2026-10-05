---
id: "frb-7-interrupt-management-7-7-1-the-xqueuesendtofrontfromisr-and-x"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.7 Using Queues within an Interrupt Service Routine / 7.7.1 The xQueueSendToFrontFromISR() and xQueueSendToBackFromISR() API Functions"
summary: "Part of: 7.7 Using Queues within an Interrupt Service Routine"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-7-1-the-xqueuesendtofrontfromisr-and-xqueuesendtobackfromisr-api-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 7.7 Using Queues within an Interrupt Service Routine_

```c
BaseType_t xQueueSendToFrontFromISR( QueueHandle_t xQueue,
                                     const void *pvItemToQueue
                                     BaseType_t *pxHigherPriorityTaskWoken );
```
***Listing 7.19*** *The xQueueSendToFrontFromISR() API function prototype*




```c
BaseType_t xQueueSendToBackFromISR( QueueHandle_t xQueue,
                                    const void *pvItemToQueue
                                    BaseType_t *pxHigherPriorityTaskWoken );
```
***Listing 7.20*** *The xQueueSendToBackFromISR() API function prototype*


`xQueueSendFromISR()` and `xQueueSendToBackFromISR()` are functionally equivalent.

**xQueueSendToFrontFromISR() and xQueueSendToBackFromISR() parameters and return values**

- `xQueue`

  The handle of the queue to which the data is being sent (written).
  The queue handle will have been returned from the call to `xQueueCreate()`
  used to create the queue.

- `pvItemToQueue`

  A pointer to the item that is to be placed on the queue.

  The size of each item the queue will hold was defined when the queue was
  created, so this many bytes will be copied from `pvItemToQueue` into the
  queue storage area.

- `pxHigherPriorityTaskWoken`

  It is possible that a single queue will have one or more tasks
  blocked on it, waiting for data to become available. Calling
  `xQueueSendToFrontFromISR()` or `xQueueSendToBackFromISR()` can make data
  available, and so cause such a task to leave the Blocked state. If
  calling the API function causes a task to leave the Blocked state, and
  the unblocked task has a priority higher than the currently executing
  task (the task that was interrupted), then, internally, the API function
  will set `*pxHigherPriorityTaskWoken` to `pdTRUE`.

  If `xQueueSendToFrontFromISR()` or `xQueueSendToBackFromISR()` sets this
  value to `pdTRUE`, then a context switch should be performed before the
  interrupt is exited. This will ensure that the interrupt returns
  directly to the highest priority Ready state task.

- Return value

  There are two possible return values:

  - `pdPASS`

    `pdPASS` is returned only if data has been sent successfully to the queue.

  - `errQUEUE_FULL

    `errQUEUE_FULL` is returned if data cannot be sent to the queue because
    the queue is already full.
