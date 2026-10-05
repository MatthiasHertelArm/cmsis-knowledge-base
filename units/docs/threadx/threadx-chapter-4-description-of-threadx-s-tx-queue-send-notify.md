---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-send-notify"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_send_notify"
summary: "Notify application when message is sent to queue"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-send-notify"
license: "MIT"
mode: "V"
---

Notify application when message is sent to queue

### Prototype

```c
UINT tx_queue_send_notify(
    TX_QUEUE *queue_ptr,
    VOID (*queue_send_notify)(TX_QUEUE *));
```

### Description

This service registers a notification callback function that is called whenever a message is sent to the specified queue. The processing of the notification callback is defined by the application.

> **Note:** *The application's queue send notification callback is not allowed to call any ThreadX API with a suspension option.*

### Parameters

- *queue_ptr*: Pointer to previously created queue.
- *queue_send_notify*: Pointer to application's queue send notification function. If this value is TX_NULL, notification is disabled.

### Return Values

- **TX_SUCCESS** (0x00) Successful registration of queue send notification.
- **TX_QUEUE_ERROR** (0x09) Invalid queue pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was compiled with notification capabilities disabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_QUEUE my_queue;
/* Register the "my_queue_send_notify" function for monitoring
messages sent to the queue "my_queue." */
status = tx_queue_send_notify(&my_queue, my_queue_send_notify);

/* If status is TX_SUCCESS the queue send notification function was
successfully registered. */
void my_queue_send_notify(TX_QUEUE *queue_ptr)
{
    /* A message was just sent to this queue! */
}
```

### See Also

- [Queue Services](#Queue_Services)
