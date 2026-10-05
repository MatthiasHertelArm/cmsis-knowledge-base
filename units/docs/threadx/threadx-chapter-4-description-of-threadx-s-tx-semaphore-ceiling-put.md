---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-ceiling-put"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_ceiling_put"
summary: "Place an instance in counting semaphore with ceiling"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-ceiling-put"
license: "MIT"
mode: "V"
---

Place an instance in counting semaphore with ceiling

### Prototype

```c
UINT tx_semaphore_ceiling_put(
    TX_SEMAPHORE *semaphore_ptr,
    ULONG ceiling);
```

### Description

This service puts an instance into the specified counting semaphore, which in reality increments the counting semaphore by one. If the counting semaphore's current value is greater than or equal to the specified ceiling, the instance will not be put and a TX_CEILING_EXCEEDED error will be returned.

### Parameters

- *semaphore_ptr*: Pointer to previously created semaphore.
- *ceiling*: Maximum limit allowed for the semaphore (valid values range from 1 through 0xFFFFFFFF).

### Return Values

- **TX_SUCCESS (0x00)** Successful semaphore ceiling put.
- **TX_CEILING_EXCEEDED** (0x21) Put request exceeds ceiling.
- **TX_INVALID_CEILING** (0x22) An invalid value of zero was supplied for ceiling.
- **TX_SEMAPHORE_ERROR** (0x0C) Invalid semaphore pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_SEMAPHORE my_semaphore;

/* Increment the counting semaphore "my_semaphore" but make sure
that it never exceeds 7 as specified in the call. */
status = tx_semaphore_ceiling_put(&my_semaphore, 7);

/* If status is TX_SUCCESS the semaphore count has been
incremented. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
