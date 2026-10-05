---
id: "frb-5-queue-management-5-6-2-the-xqueuecreateset-api-function"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.6 Receiving From Multiple Queues / 5.6.2 The xQueueCreateSet() API Function"
summary: "Part of: 5.6 Receiving From Multiple Queues"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-6-2-the-xqueuecreateset-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.6 Receiving From Multiple Queues_

A queue set must be explicitly created before it can be used. At the
time of writing there is no implementation of `xQueueCreateSetStatic()`.
However queue sets are themselves queues, so it is possible to create a
set using pre-allocated memory by using a specially crafted call to
`xQueueCreateStatic()`.

Queues sets are referenced by handles, which are variables of type
`QueueSetHandle_t`. The `xQueueCreateSet()` API function creates a queue set
and returns a `QueueSetHandle_t` that references the created queue set.



```c
QueueSetHandle_t xQueueCreateSet( const UBaseType_t uxEventQueueLength);
```
***Listing 5.21*** *The xQueueCreateSet() API function prototype*


**xQueueCreateSet() parameters and return value**

- `uxEventQueueLength`

  When a queue that is a member of a queue set receives data, the
  handle of the receiving queue is sent to the queue set.
  `uxEventQueueLength` defines the maximum number of queue handles the queue
  set being created can hold at any one time.

  Queue handles are only sent to a queue set when a queue within the
  set receives data. A queue cannot receive data if it is full, so no
  queue handles can be sent to the queue set if all the queues in the set
  are full. Therefore, the maximum number of items the queue set will ever
  have to hold at one time is the sum of the lengths of every queue in the
  set.

  As an example, if there are three empty queues in the set, and each
  queue has a length of five, then in total the queues in the set can
  receive fifteen items (three queues multiplied by five items each)
  before all the queues in the set are full. In that example
  `uxEventQueueLength` must be set to fifteen to guarantee the queue set can
  receive every item sent to it.

  Semaphores can also be added to a queue set. Semaphores are covered
  later in this book. For the purposes of calculating the necessary
  `uxEventQueueLength`, the length of a binary semaphore is one, the length
  of a mutex is one, and the length of a counting semaphore is given by
  the semaphore's maximum count value.

  As another example, if a queue set will contain a queue that has a
  length of three, and a binary semaphore (which has a length of one),
  `uxEventQueueLength` must be set to four (three plus one).

- Return Value

  If NULL is returned, then the queue set cannot be created because
  there is insufficient heap memory available for FreeRTOS to allocate the
  queue set data structures and storage area. Chapter 3 provides more
  information on the FreeRTOS heap.

  If a non-NULL value is returned then the queue set was created
  successfully and the returned value is the handle to the created queue set.
