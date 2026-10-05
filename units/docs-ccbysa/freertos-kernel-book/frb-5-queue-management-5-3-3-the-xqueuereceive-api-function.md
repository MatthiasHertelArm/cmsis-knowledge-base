---
id: "frb-5-queue-management-5-3-3-the-xqueuereceive-api-function"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.3 Using a Queue / 5.3.3 The xQueueReceive() API Function"
summary: "xQueueReceive() receives (reads) an item from a queue. The received item is removed from the queue."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-3-3-the-xqueuereceive-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.3 Using a Queue_

`xQueueReceive()` receives (reads) an item from a queue. The received item
is removed from the queue.

> *Note: Never call `xQueueReceive()` from an interrupt service routine. The
> interrupt-safe `xQueueReceiveFromISR()` API function is described in
> Chapter 7.*



```c
BaseType_t xQueueReceive( QueueHandle_t xQueue,
                          void * const pvBuffer,
                          TickType_t xTicksToWait );
```
***Listing 5.4*** *The xQueueReceive() API function prototype*


**xQueueReceive() function parameters and return values**

- `xQueue`

  The handle of the queue from which the data is being received
  (read). The queue handle will have been returned from the call to
  `xQueueCreate()` or `xQueueCreateStatic()` used to create the queue.

- `pvBuffer`

  A pointer to the memory into which the received data will be copied.

  The size of each data item that the queue holds is set when the queue
  is created. The memory pointed to by `pvBuffer` must be at least large
  enough to hold that many bytes.

- `xTicksToWait`

  The maximum amount of time the task should remain in the Blocked
  state to wait for data to become available on the queue, if the
  queue is already be empty.

  If `xTicksToWait` is zero, then `xQueueReceive()` will return immediately
  if the queue is already empty.

  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds into a time
  specified in ticks.

  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without timing out) provided `INCLUDE_vTaskSuspend` is set
  to 1 in FreeRTOSConfig.h.

- Return value

  There are two possible return values:
  
  - `pdPASS`

    `pdPASS` is returned when data was successfully read from the queue.

    If a block time was specified (`xTicksToWait` was not zero), then it is
    possible the calling task was placed into the Blocked state to wait for
    data to become available on the queue, but data was successfully read
    from the queue before the block time expired.

  - `errQUEUE_EMPTY` (same value as `pdFAIL`)

    `errQUEUE_EMPTY` is returned if data cannot be read from the queue
    because the queue is already empty.

    If a block time was specified (`xTicksToWait` was not zero,) then the
    calling task will have been placed into the Blocked state to wait for
    another task or interrupt to send data to the queue, but the block time
    expired before that happened.
