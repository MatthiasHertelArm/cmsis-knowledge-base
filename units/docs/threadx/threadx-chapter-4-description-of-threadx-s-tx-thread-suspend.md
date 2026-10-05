---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-suspend"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_suspend"
summary: "This service suspends the specified application thread. A thread may call this service to suspend itself."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-suspend"
license: "MIT"
mode: "V"
---

Suspend application thread

### Prototype

```c
UINT tx_thread_suspend(TX_THREAD *thread_ptr);
```

### Description

This service suspends the specified application thread. A thread may call this service to suspend itself.

> **Note:** *If the specified thread is already suspended for another reason, this suspension is held internally until the prior suspension is lifted. When that happens, this unconditional suspension of the specified thread is performed. Further unconditional suspension requests have no effect.*

After being suspended, the thread must be resumed by ***tx_thread_resume*** to execute again.

### Parameters

- *thread_ptr*: Pointer to an application thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread suspend.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_SUSPEND_ERROR** (0x14) Specified thread is in a terminated or completed state.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_THREAD my_thread;
UINT status;

/* Suspend the thread represented by "my_thread". */
status = tx_thread_suspend(&my_thread);

/* If status equals TX_SUCCESS, the application thread is
unconditionally suspended. */
```

### See Also

- [Thread Services](#Thread_Services)
