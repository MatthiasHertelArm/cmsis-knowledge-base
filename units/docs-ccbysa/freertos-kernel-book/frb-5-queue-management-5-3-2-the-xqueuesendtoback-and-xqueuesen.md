---
id: "frb-5-queue-management-5-3-2-the-xqueuesendtoback-and-xqueuesen"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.3 Using a Queue / 5.3.2 The xQueueSendToBack() and xQueueSendToFront() API Functions"
summary: "As might be expected, xQueueSendToBack() sends data to the back (tail) of a queue, and xQueueSendToFront() sends data to the front (head) of a queue."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-3-2-the-xqueuesendtoback-and-xqueuesendtofront-api-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.3 Using a Queue_

As might be expected, `xQueueSendToBack()` sends data to the back (tail)
of a queue, and `xQueueSendToFront()` sends data to the front (head) of a
queue.

`xQueueSend()` is equivalent to, and exactly the same as,
`xQueueSendToBack()`.

> *Note: Never call `xQueueSendToFront()` or `xQueueSendToBack()` from an
> interrupt service routine. The interrupt-safe versions
>`xQueueSendToFrontFromISR()` and `xQueueSendToBackFromISR()` should be used
> in their place. These are described in Chapter 7.*




```c
BaseType_t xQueueSendToFront( QueueHandle_t xQueue,
                              const void * pvItemToQueue,
                              TickType_t xTicksToWait );
```
***Listing 5.2*** *The xQueueSendToFront() API function prototype*





```c
BaseType_t xQueueSendToBack( QueueHandle_t xQueue,
                             const void * pvItemToQueue,
                             TickType_t xTicksToWait );
```
***Listing 5.3*** *The xQueueSendToBack() API function prototype*


**xQueueSendToFront() and xQueueSendToBack() function parameters and return value**

- `xQueue`

  The handle of the queue to which the data is being sent (written).
  The queue handle will have been returned from the call to `xQueueCreate()`
  or `xQueueCreateStatic()` which are used to create the queue.

- `pvItemToQueue`

  A pointer to the data to be copied into the queue.

  The size of each item the queue can hold is set when the queue is
  created, so that many bytes are copied from `pvItemToQueue` into the queue
  storage area.

- `xTicksToWait`

  The maximum amount of time the task should remain in the Blocked
  state to wait for space to become available on the queue, should the
  queue already be full.
  
  Both `xQueueSendToFront()` and `xQueueSendToBack()` will return
  immediately if `xTicksToWait` is zero and the queue is already full.
  
  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds into a time
  specified in ticks.
  
  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without timing out), provided `INCLUDE_vTaskSuspend` is set
  to 1 in FreeRTOSConfig.h.

- Return value

  There are two possible return values:

  - `pdPASS`

    `pdPASS` is returned when data was successfully sent to the queue.

    If a block time was specified (`xTicksToWait` was not zero), then it is
    possible the calling task was placed into the Blocked state to wait for
    space to become available in the queue before the function returned,
    but data was successfully written to the queue before the block time
    expired.

  - `errQUEUE_FULL` (same value as `pdFAIL`)

    `errQUEUE_FULL` is returned if data could not be written to the queue
    because the queue was already full.

    If a block time was specified (`xTicksToWait` was not zero) then the
    calling task will have been placed into the Blocked state to wait for
    another task or interrupt to make space in the queue, but the specified
    block time expired before that happened.
