---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_delete"
summary: "This service deletes the specified counting semaphore. All threads suspended waiting for a semaphore instance are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-delete"
license: "MIT"
mode: "V"
---

Delete counting semaphore

### Prototype
```c
UINT tx_semaphore_delete(TX_SEMAPHORE *semaphore_ptr);
```

### Description

This service deletes the specified counting semaphore. All threads suspended waiting for a semaphore instance are resumed and given a TX_DELETED return status.

> **Important:** *The application must ensure that a put notify callback for this semaphore is completed (or disabled) before deleting the semaphore. In addition, the application must prevent all future use of a deleted semaphore.*

### Parameters

- *semaphore_ptr*: Pointer to a previously created semaphore.

### Return Values

- **TX_SUCCESS** (0x00) Successful counting semaphore deletion.
- **TX_SEMAPHORE_ERROR** (0x0C) Invalid counting semaphore pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_SEMAPHORE my_semaphore;
UINT status;

/* Delete counting semaphore. Assume that the counting
semaphore has already been created. */
status = tx_semaphore_delete(&my_semaphore);

/* If status equals TX_SUCCESS, the counting semaphore is
deleted. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
