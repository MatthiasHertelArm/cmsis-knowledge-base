---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-wait-abort"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_wait_abort"
summary: "This service aborts sleep or any other object suspension of the specified thread. If the wait is aborted, a TX_WAIT_ABORTED value is returned from the service that the thread was waiting on."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-wait-abort"
license: "MIT"
mode: "V"
---

Abort suspension of specified thread

### Prototype

```c
UINT tx_thread_wait_abort(TX_THREAD *thread_ptr);
```

### Description

This service aborts sleep or any other object suspension of the specified thread. If the wait is aborted, a **TX_WAIT_ABORTED** value is returned from the service that the thread was waiting on.

> **Note:** *This service does not release explicit suspension that is made by the tx_thread_suspend service.*

### Parameters

- *thread_ptr*: Pointer to a previously created application thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread wait abort.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_WAIT_ABORT_ERROR** (0x1B) Specified thread is not in a waiting state.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible
Yes

### Example

```c
TX_THREAD my_thread;
UINT status;

/* Abort the suspension condition of "my_thread." */
status = tx_thread_wait_abort(&my_thread);

/* If status equals TX_SUCCESS, the thread is now ready
again, with a return value showing its suspension
was aborted (TX_WAIT_ABORTED). */
```

### See Also

- [Thread Services](#Thread_Services)
