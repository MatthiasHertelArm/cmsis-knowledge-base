---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-prioritize"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_prioritize"
summary: "This service places the highest priority thread suspended for a message (or to place a message) on this queue at the front of the suspension list."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-prioritize"
license: "MIT"
mode: "V"
---

Prioritize queue suspension list

### Prototype

```c
UINT tx_queue_prioritize(TX_QUEUE *queue_ptr);
```

### Description

This service places the highest priority thread suspended for a message (or to place a message) on this queue at the front of the suspension list.

All other threads remain in the same FIFO order they were suspended in.

### Parameters

- *queue_ptr*: Pointer to a previously created message queue.

### Return Values

- **TX_SUCCESS** (0x00) Successful queue prioritize.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_QUEUE my_queue;
UINT status;

/* Ensure that the highest priority thread will receive
the next message placed on this queue. */
status = tx_queue_prioritize(&my_queue);

/* If status equals TX_SUCCESS, the highest priority
suspended thread is at the front of the list. The
next tx_queue_send or tx_queue_front_send call made
to this queue will wake up this thread. */
```

### See Also

- [Queue Services](#Queue_Services)
