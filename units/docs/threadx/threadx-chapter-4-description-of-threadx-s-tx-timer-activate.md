---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-activate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_activate"
summary: "This service activates the specified application timer. The expiration routines of timers that expire at the same time are executed in the order they were activated."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-activate"
license: "MIT"
mode: "V"
---

Activate application timer

### Prototype

```c
UINT tx_timer_activate(TX_TIMER *timer_ptr);
```

### Description

This service activates the specified application timer. The expiration routines of timers that expire at the same time are executed in the order they were activated.

> **Note:** *An expired one-shot timer must be reset via* ***tx_timer_change*** *before it can be activated again.*

### Parameters

- *timer_ptr*: Pointer to a previously created application timer.

### Return Values

- **TX_SUCCESS** (0x00) Successful application timer activation.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer.
- **TX_ACTIVATE_ERROR** (0x17) Timer was already active or is a one-shot timer that has already expired.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
UINT status;

/* Activate an application timer. Assume that the
application timer has already been created. */
status = tx_timer_activate(&my_timer);

/* If status equals TX_SUCCESS, the application timer is
now active. */
```

### See Also

- [Timer Services](#Timer_Services)
