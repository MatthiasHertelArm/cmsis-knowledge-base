---
id: "frb-5-queue-management-5-3-1-the-xqueuecreate-api-function"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.3 Using a Queue / 5.3.1 The xQueueCreate() API Function"
summary: "Listing 5.1 shows the xQueueCreate() function prototype. xQueueCreateStatic() has two additional parameters that point to the memory pre-allocated to hold the queue's data structure and data storage area, respectively."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-3-1-the-xqueuecreate-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.3 Using a Queue_

Listing 5.1 shows the `xQueueCreate()` function prototype.
`xQueueCreateStatic()` has two additional parameters that point to the
memory pre-allocated to hold the queue's data structure and data storage
area, respectively.



```c
QueueHandle_t xQueueCreate( UBaseType_t uxQueueLength, UBaseType_t uxItemSize );
```
***Listing 5.1*** *The xQueueCreate() API function prototype*


**xQueueCreate() parameters and return value:**

- `uxQueueLength`

  The maximum number of items that the queue being created can hold at
  any one time.

- `uxItemSize`

  The size in bytes of each data item that can be stored in the queue.

- Return value

  If NULL is returned, then the queue cannot be created because
  there is insufficient heap memory available for FreeRTOS to allocate the
  queue data structures and storage area. Chapter 2 provides more
  information on the FreeRTOS heap.

  If a non-NULL value is returned then the queue was created
  successfully and the returned value is the handle to the created
  queue.

`xQueueReset()` is an API function that restores a previously created queue
to its original empty state.
