---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-flush"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_flush"
summary: "This service deletes all messages stored in the specified message queue."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-flush"
license: "MIT"
mode: "V"
---

Empty messages in message queue

### Prototype

```c
UINT tx_queue_flush(TX_QUEUE *queue_ptr);
```

### Description

This service deletes all messages stored in the specified message queue.

If the queue is full, messages of all suspended threads are discarded. Each suspended thread is then resumed with a return status that indicates the message send was successful. If the queue is empty, this service does nothing.

### Parameters

- *queue_ptr*: Pointer to a previously created message queue.

### Return Values

- **TX_SUCCESS** (0x00) Successful message queue flush.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_QUEUE my_queue;
UINT status;

/* Flush out all pending messages in the specified message
queue. Assume that the queue has already been created
with a call to tx_queue_create. */
status = tx_queue_flush(&my_queue);

/* If status equals TX_SUCCESS, the message queue is
empty. */
```

### See Also

- [Queue Services](#Queue_Services)
