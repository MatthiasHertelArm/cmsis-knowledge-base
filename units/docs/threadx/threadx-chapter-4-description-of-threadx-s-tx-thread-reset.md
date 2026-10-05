---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-reset"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_reset"
summary: "This service resets the specified thread to execute at the entry point defined at thread creation. The thread must be in either a TX_COMPLETED or TX_TERMINATED state for it to be reset"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-reset"
license: "MIT"
mode: "V"
---

Reset thread

### Prototype

```c
UINT tx_thread_reset(TX_THREAD *thread_ptr);
```

### Description

This service resets the specified thread to execute at the entry point defined at thread creation. The thread must be in either a **TX_COMPLETED** or **TX_TERMINATED** state for it to be reset

> **Important:** *The thread must be resumed for it to execute again.*

### Parameters

- *thread_ptr*: Pointer to a previously created thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread reset.
- **TX_NOT_DONE** (0x20) Specified thread is not in a **TX_COMPLETED** or **TX_TERMINATED** state.
- **TX_THREAD_ERROR** (0x0E) Invalid thread pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example
```c
TX_THREAD my_thread;

/* Reset the previously created thread "my_thread." */

status = tx_thread_reset(&my_thread);

/* If status is TX_SUCCESS the thread is reset. */
```

### See Also

- [Thread Services](#Thread_Services)
