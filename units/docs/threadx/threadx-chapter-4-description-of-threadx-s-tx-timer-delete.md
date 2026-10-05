---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_delete"
summary: "This service deletes the specified application timer."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-delete"
license: "MIT"
mode: "V"
---

Delete application timer

### Prototype

```c
UINT tx_timer_delete(TX_TIMER *timer_ptr);
```

### Description

This service deletes the specified application timer.

> **Note:** *It is the application's responsibility to prevent use of a deleted timer.*

### Parameters

- *timer_ptr*: Pointer to a previously created application timer.

### Return Values

- **TX_SUCCESS** (0x00) Successful application timer deletion.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
UINT status;

/* Delete application timer. Assume that the application
timer has already been created. */
status = tx_timer_delete(&my_timer);

/* If status equals TX_SUCCESS, the application timer is
deleted. */
```

### See Also

- [Timer Services](#Timer_Services)
