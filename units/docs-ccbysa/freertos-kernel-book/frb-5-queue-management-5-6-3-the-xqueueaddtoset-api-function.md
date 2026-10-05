---
id: "frb-5-queue-management-5-6-3-the-xqueueaddtoset-api-function"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.6 Receiving From Multiple Queues / 5.6.3 The xQueueAddToSet() API Function"
summary: "Part of: 5.6 Receiving From Multiple Queues"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-6-3-the-xqueueaddtoset-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.6 Receiving From Multiple Queues_

`xQueueAddToSet()` adds a queue or semaphore to a queue set. Semaphores
are described later in this book.



```c
BaseType_t xQueueAddToSet( QueueSetMemberHandle_t xQueueOrSemaphore,
                           QueueSetHandle_t xQueueSet );
```
***Listing 5.22*** *The xQueueAddToSet() API function prototype*

**xQueueAddToSet() parameters and return value**

- `xQueueOrSemaphore`

  The handle of the queue or semaphore that is being added to the queue set.

  Queue handles and semaphore handles can both be cast to the `QueueSetMemberHandle_t` type.

- `xQueueSet`

  The handle of the queue set to which the queue or semaphore is being added.

- Return Value

  There are two possible return values:

  1. `pdPASS`

      This indicates the queue set was created successfully.

  1. `pdFAIL`

     This indicates the queue or semaphore could not be added to the queue set.

  Queues and binary semaphores can only be added to a set when they are
  empty. Counting semaphores can only be added to a set when their count
  is zero. Queues and semaphores can only be a member of one set at a time.
