---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-deactivate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_deactivate"
summary: "This service deactivates the specified application timer. If the timer is already deactivated, this service has no effect."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-deactivate"
license: "MIT"
mode: "V"
---

Deactivate application timer

### Prototype

```c
UINT tx_timer_deactivate(TX_TIMER *timer_ptr);
```

### Description

This service deactivates the specified application timer. If the timer is already deactivated, this service has no effect.

### Parameters

- *timer_ptr*: Pointer to a previously created application timer.

### Return Values

- **TX_SUCCESS** (0x00) Successful application timer deactivation.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
UINT status;

/* Deactivate an application timer. Assume that the
application timer has already been created. */
status = tx_timer_deactivate(&my_timer);

/* If status equals TX_SUCCESS, the application timer is
now deactivated. */
```

### See Also

- [Timer Services](#Timer_Services)
