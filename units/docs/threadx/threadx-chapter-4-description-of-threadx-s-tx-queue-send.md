---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-send"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_send"
summary: "This service sends a message to the specified message queue. The sent message is copied to the queue from the memory area specified by the source pointer."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-send"
license: "MIT"
mode: "V"
---

Send message to message queue

### Prototype

```c
UINT tx_queue_send(
    TX_QUEUE *queue_ptr,
    VOID *source_ptr, 
    ULONG wait_option);
```

### Description

This service sends a message to the specified message queue. The sent message is **copied** to the queue from the memory area specified by the source pointer.

### Parameters
- *queue_ptr*: 
Pointer to a previously created message queue.
- *source_ptr*: 
Pointer to the message.
- *wait_option*: 
Defines how the service behaves if the message queue is full. The wait options are defined as follows:
  - **TX_NO_WAIT*: (0x00000000) - Selecting TX_NO_WAIT results in an immediate return from this service regardless of whether or not it was successful. *This is the only valid option if the service is called from a non-thread; e.g., Initialization, timer, or ISR*.
  - **TX_WAIT_FOREVER** (0xFFFFFFFF) - Selecting TX_WAIT_FOREVER causes the calling thread to suspend indefinitely until there is room in the queue.
  - timeout value (0x00000001 through 0xFFFFFFFE) - Selecting a numeric value (1-0xFFFFFFFE) specifies the maximum number of timer-ticks to stay suspended while waiting for room in the queue.

### Return Values

- **TX_SUCCESS** (0x00) Successful sending of message.
- **TX_DELETED** (0x01) Message queue was deleted while thread was suspended.
- **TX_QUEUE_FULL** (0x0B) Service was unable to send message because the queue was full for the duration of the specified time to wait.
- **TX_WAIT_ABORTED** (0x1A) Suspension was aborted by another thread, timer, or ISR.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.
- **TX_PTR_ERROR** (0x03) Invalid source pointer for message.
- **TX_WAIT_ERROR** (0x04) A wait option other than TX_NO_WAIT was specified on a call from a nonthread.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_QUEUE my_queue;
UINT status;
ULONG my_message[4];

/* Send a message to "my_queue." Return immediately,
regardless of success. This wait option is used for
calls from initialization, timers, and ISRs. */
status = tx_queue_send(&my_queue, my_message, TX_NO_WAIT);

/* If status equals TX_SUCCESS, the message is in the
queue. */
```

### See Also

- [Queue Services](#Queue_Services)
