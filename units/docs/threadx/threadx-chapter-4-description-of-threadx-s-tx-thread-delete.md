---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_delete"
summary: "This service deletes the specified application thread. Since the specified thread must be in a terminated or completed state, this service cannot be called from a thread attempting to delete itself."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-delete"
license: "MIT"
mode: "V"
---

Delete application thread

### Prototype

```c
UINT tx_thread_delete(TX_THREAD *thread_ptr);
```

### Description

This service deletes the specified application thread. Since the specified thread must be in a terminated or completed state, this service cannot be called from a thread attempting to delete itself.

> **Note:** *It is the application's responsibility to manage the memory area associated with the thread's stack, which is available after this service completes. In addition, the application must prevent the use of a deleted thread.*

### Parameters

- *thread_ptr*: Pointer to a previously created application thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread deletion.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_DELETE_ERROR** (0x11) Specified thread is not in a terminated or completed state.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads and timers

### Preemption Possible

No

### Example

```c
TX_THREAD my_thread;
UINT status;

/* Delete an application thread whose control block is
"my_thread". Assume that the thread has already been
created with a call to tx_thread_create. */
status = tx_thread_delete(&my_thread);

/* If status equals TX_SUCCESS, the application thread is
deleted. */
```

### See Also

- [Thread Services](#Thread_Services)
