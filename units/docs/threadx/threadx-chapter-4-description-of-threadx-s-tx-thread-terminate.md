---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-terminate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_terminate"
summary: "This service terminates the specified application thread regardless of whether the thread is suspended or not. A thread may call this service to terminate itself."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-terminate"
license: "MIT"
mode: "V"
---

Terminates the application thread

### Prototype

```c
UINT tx_thread_terminate(TX_THREAD *thread_ptr);
```
### Description

This service terminates the specified application thread regardless of whether the thread is suspended or not. A thread may call this service to terminate itself.

> **Note:** *It is the application's responsibility to ensure that the thread is in a state suitable for termination. For example, a thread should not be terminated during critical application processing or inside of other middleware components where it could leave such processing in an unknown state.*

> **Important:** *After being terminated, the thread must be reset for it to execute again.*

### Parameters

- *thread_ptr*: Pointer to application thread.

### Return Values
- **TX_SUCCESS** (0x00) Successful thread terminate.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads and timers

### Preemption Possible

Yes

### Example

```c
TX_THREAD my_thread;
UINT status;

/* Terminate the thread represented by "my_thread". */
status = tx_thread_terminate(&my_thread);

/* If status equals TX_SUCCESS, the thread is terminated
and cannot execute again until it is reset. */
```

### See Also

- [Thread Services](#Thread_Services)
