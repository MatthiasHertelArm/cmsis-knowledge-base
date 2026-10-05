---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_delete"
summary: "This service deletes the specified mutex. All threads suspended waiting for the mutex are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-delete"
license: "MIT"
mode: "V"
---

Delete mutual exclusion mutex

### Prototype

```c
UINT tx_mutex_delete(TX_MUTEX *mutex_ptr);
```

### Description

This service deletes the specified mutex. All threads suspended waiting for the mutex are resumed and given a **TX_DELETED** return status.

> **Note:** *It is the application's responsibility to prevent use of a deleted mutex.*

### Parameters

- *mutex_ptr*: Pointer to a previously created mutex.

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex deletion.
- **TX_MUTEX_ERROR** (0x1C) Invalid mutex pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_MUTEX my_mutex;
UINT status;

/* Delete a mutex. Assume that the mutex
has already been created. */
status = tx_mutex_delete(&my_mutex);

/* If status equals TX_SUCCESS, the mutex is
deleted. */
```

### See Also

- [Mutex Services](#Mutex_Services)
