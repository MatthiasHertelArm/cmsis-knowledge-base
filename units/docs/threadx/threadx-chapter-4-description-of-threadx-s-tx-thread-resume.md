---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-resume"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_resume"
summary: "This service resumes or prepares for execution a thread that was previously suspended by a tx_thread_suspend call. In addition, this service resumes threads that were created without an automatic start."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-resume"
license: "MIT"
mode: "V"
---

Resume suspended application thread

### Prototype

```c
UINT tx_thread_resume(TX_THREAD *thread_ptr);
```

### Description

This service resumes or prepares for execution a thread that was previously suspended by a ***tx_thread_suspend*** call. In addition, this service resumes threads that were created without an automatic start.

### Parameters

- *thread_ptr*: Pointer to a suspended application thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread resume.
- **TX_SUSPEND_LIFTED** (0x19) Previously set delayed suspension was lifted.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_RESUME_ERROR** (0x12) Specified thread is not suspended or was previously suspended by a service other than ***tx_thread_suspend***.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_THREAD my_thread;
UINT status;

/* Resume the thread represented by "my_thread". */
status = tx_thread_resume(&my_thread);

/* If status equals TX_SUCCESS, the application thread is
now ready to execute. */
```

### See Also

- [Thread Services](#Thread_Services)
