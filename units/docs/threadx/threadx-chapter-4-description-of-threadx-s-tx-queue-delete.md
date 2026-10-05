---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_delete"
summary: "This service deletes the specified message queue. All threads suspended waiting for a message from this queue are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-delete"
license: "MIT"
mode: "V"
---

Delete message queue

### Prototype

```c
UINT tx_queue_delete(TX_QUEUE *queue_ptr);
```

### Description

This service deletes the specified message queue. All threads suspended waiting for a message from this queue are resumed and given a TX_DELETED return status.

> **Important:** *The application must ensure that any send notify callback for this queue is completed (or disabled) before deleting the queue. In addition, the application must prevent any future use of a deleted queue.* 

*It is also the application's responsibility to manage the memory area associated with the queue, which is available after this service completes.*

### Parameters

- *queue_ptr*: Pointer to a previously created message queue.

### Return Values

- **TX_SUCCESS** (0x00) Successful message queue deletion.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_QUEUE my_queue;
UINT status;

/* Delete entire message queue. Assume that the queue
has already been created with a call to
tx_queue_create. */
status = tx_queue_delete(&my_queue);

/* If status equals TX_SUCCESS, the message queue is
deleted. */
```

### See Also

- [Queue Services](#Queue_Services)
