---
id: "frb-7-interrupt-management-7-4-2-the-xsemaphoretake-api-function"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.4 Binary Semaphores Used for Synchronization / 7.4.2 The xSemaphoreTake() API Function"
summary: "Part of: 7.4 Binary Semaphores Used for Synchronization"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-4-2-the-xsemaphoretake-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 7.4 Binary Semaphores Used for Synchronization_

'Taking' a semaphore means to 'obtain' or 'receive' the semaphore. The
semaphore can be taken only if it is available.

All the various types of FreeRTOS semaphore, except recursive mutexes,
can be 'taken' using the `xSemaphoreTake()` function.

`xSemaphoreTake()` must not be used from an interrupt service routine.




```c
BaseType_t xSemaphoreTake( SemaphoreHandle_t xSemaphore, TickType_t xTicksToWait );
```
***Listing 7.4*** *The xSemaphoreTake() API function prototype*

**xSemaphoreTake() parameters and return value**

- `xSemaphore`

  The semaphore being 'taken'.

  A semaphore is referenced by a variable of type `SemaphoreHandle_t`. It
  must be explicitly created before it can be used.

- `xTicksToWait`

  The maximum amount of time the task should remain in the Blocked
  state to wait for the semaphore if it is not already available.

  If `xTicksToWait` is zero, then `xSemaphoreTake()` will return
  immediately if the semaphore is not available.

  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds to a time
  specified in ticks.

  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without a timeout) if `INCLUDE_vTaskSuspend` is set to 1 in
  FreeRTOSConfig.h.

- Return value

  There are two possible return values:

  - `pdPASS`

    `pdPASS` is returned only if the call to `xSemaphoreTake()` was
    successful in obtaining the semaphore.

    If a block time was specified (`xTicksToWait` was not zero), then it is
    possible that the calling task was placed into the Blocked state to wait
    for the semaphore if it was not immediately available, but the semaphore
    became available before the block time expired.

  - `pdFALSE`

    The semaphore is not available.

    If a block time was specified (`xTicksToWait` was not zero), then the
    calling task will have been placed into the Blocked state to wait for
    the semaphore to become available, but the block time expired before
    this happened.
