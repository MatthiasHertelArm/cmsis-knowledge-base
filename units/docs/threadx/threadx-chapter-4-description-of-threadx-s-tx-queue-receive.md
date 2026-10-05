---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-receive"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_receive"
summary: "This service retrieves a message from the specified message queue. The retrieved message is copied from the queue into the memory area specified by the destination pointer. That message is then removed from the queue."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-receive"
license: "MIT"
mode: "V"
---

Get message from message queue

### Prototype

```c
UINT tx_queue_receive(
    TX_QUEUE *queue_ptr,
    VOID *destination_ptr, 
    ULONG wait_option);
```

### Description

This service retrieves a message from the specified message queue. The retrieved message is **copied** from the queue into the memory area specified by the destination pointer. That message is then removed from the queue.

> **Important:** *The specified destination memory area must be large enough to hold the message; i.e., the message destination pointed to by* ***destination_ptr*** *must be at least as large as the message size for this queue. If the destination is not large enough, the behavior is undefined. That said, a typical consequence is memory corruption of an adjacent (usually subsequent) memory area.*

### Parameters

- *queue_ptr*: 
Pointer to a previously created message queue.
- *destination_ptr*: 
Location of where to copy the message.
- *wait_option*: 
Defines how the service behaves if the message queue is empty. The wait options are defined as follows:
  - **TX_NO_WAIT*: (0x00000000) - Selecting TX_NO_WAIT results in an immediate return from this service regardless of whether or not it was successful. This is the only valid option if the service is called from a non-thread; e.g.,  Initialization, timer, or ISR.
  - **TX_WAIT_FOREVER** (0xFFFFFFFF) - Selecting TX_WAIT_FOREVER causes the calling thread to suspend indefinitely until a message is available.
  - timeout value (0x00000001 through 0xFFFFFFFE) - Selecting a numeric value (1-0xFFFFFFFE) specifies the maximum number of timer-ticks to stay suspended while waiting for a message.

### Return Values

- **TX_SUCCESS** (0x00) Successful retrieval of message.
- **TX_DELETED** (0x01) Message queue was deleted while thread was suspended.
- **TX_QUEUE_EMPTY** (0x0A) Service was unable to retrieve a message because the queue was empty for the duration of the specified time to wait.
- **TX_WAIT_ABORTED** (0x1A) Suspension was aborted by another thread, timer, or ISR.
- **TX_QUEUE_ERROR** (0x09) Invalid message queue pointer.
- **TX_PTR_ERROR** (0x03) Invalid destination pointer for message.
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

/* Retrieve a message from "my_queue." If the queue is
empty, suspend until a message is present. Note that
this suspension is only possible from application
threads. */
status = tx_queue_receive(&my_queue, my_message,
    TX_WAIT_FOREVER);

/* If status equals TX_SUCCESS, the message is in
"my_message." */
```

### See Also

- [Queue Services](#Queue_Services)
