---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-prioritize"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_prioritize"
summary: "This service places the highest priority thread suspended for ownership of the mutex at the front of the suspension list. All other threads remain in the same FIFO order they were suspended in."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-prioritize"
license: "MIT"
mode: "V"
---

Prioritize mutex suspension list

### Prototype

```c
UINT tx_mutex_prioritize(TX_MUTEX *mutex_ptr);
```

### Description

This service places the highest priority thread suspended for ownership of the mutex at the front of the suspension list. All other threads remain in the same FIFO order they were suspended in.

### Parameters

- *mutex_ptr*: Pointer to the previously created mutex.

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex prioritize.
- **TX_MUTEX_ERROR** (0x1C) Invalid mutex pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_MUTEX my_mutex;
UINT status;

/* Ensure that the highest priority thread will receive
ownership of the mutex when it becomes available. */
status = tx_mutex_prioritize(&my_mutex);

/* If status equals TX_SUCCESS, the highest priority
suspended thread is at the front of the list. The
next tx_mutex_put call that releases ownership of the
mutex will give ownership to this thread and wake it
up. */
```

### See Also

- [Mutex Services](#Mutex_Services)
