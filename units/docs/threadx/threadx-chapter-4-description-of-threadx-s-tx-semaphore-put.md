---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-put"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_put"
summary: "This service puts an instance into the specified counting semaphore, which in reality increments the counting semaphore by one."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-put"
license: "MIT"
mode: "V"
---

Place an instance in counting semaphore

### Prototype

```c
UINT tx_semaphore_put(TX_SEMAPHORE *semaphore_ptr);
```

### Description

This service puts an instance into the specified counting semaphore, which in reality increments the counting semaphore by one.

> **Note:** *If this service is called when the semaphore is all ones (OxFFFFFFFF), the new put operation will cause the semaphore to be reset to zero.*

### Parameters

- *semaphore_ptr*: Pointer to the previously created counting semaphore control block.

### Return Values

- **TX_SUCCESS** (0x00) Successful semaphore put.
- **TX_SEMAPHORE_ERROR** (0x0C) Invalid pointer to counting semaphore.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_SEMAPHORE my_semaphore;
UINT status;

/* Increment the counting semaphore "my_semaphore." */
status = tx_semaphore_put(&my_semaphore);

/* If status equals TX_SUCCESS, the semaphore count has
been incremented. Of course, if a thread was waiting,
it was given the semaphore instance and resumed. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
