---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_info_get"
summary: "This service retrieves information about the specified message queue."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about queue

### Prototype

```c
UINT tx_queue_info_get(
    TX_QUEUE *queue_ptr, 
    CHAR **name,
    ULONG *enqueued, 
    ULONG *available_storage
    TX_THREAD **first_suspended, 
    ULONG *suspended_count,
    TX_QUEUE **next_queue);
```

### Description

This service retrieves information about the specified message queue.

### Parameters

- *queue_ptr*: Pointer to a previously created message queue.
- *name*: Pointer to destination for the pointer to the queue's name.
- *enqueued*: Pointer to destination for the number of messages currently in the queue.
- *available_storage*: Pointer to destination for the number of messages the queue currently has space for.
- *first_suspended*: Pointer to destination for the pointer to the thread that is first on the suspension list of this queue.
- *suspended_count*: Pointer to destination for the number of threads currently suspended on this queue.
- *next_queue*: Pointer to destination for the pointer of the next created queue.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful queue information get.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_QUEUE my_queue;
CHAR *name;
ULONG enqueued;
ULONG available_storage;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_QUEUE *next_queue;
UINT status;

/* Retrieve information about the previously created
message queue "my_queue." */
status = tx_queue_info_get(&my_queue, &name,
    &enqueued, &available_storage,
    &first_suspended, &suspended_count,
    &next_queue);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Queue Services](#Queue_Services)
