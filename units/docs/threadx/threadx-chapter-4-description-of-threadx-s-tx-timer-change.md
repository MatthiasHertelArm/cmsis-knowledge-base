---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-change"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_change"
summary: "This service changes the expiration characteristics of the specified application timer. The timer must be deactivated prior to calling this service."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-change"
license: "MIT"
mode: "V"
---

Change application timer

### Prototype

```c
UINT tx_timer_change(
    TX_TIMER *timer_ptr,
    ULONG initial_ticks, 
    ULONG reschedule_ticks);
```

### Description

This service changes the expiration characteristics of the specified application timer. The timer must be deactivated prior to calling this service.

> **Note:** *A call to the* ***tx_timer_activate*** *service is required after this service in order to start the timer again.*

### Parameters

- *timer_ptr*: Pointer to a timer control block.
- *initial_ticks*: Specifies the initial number of ticks for timer expiration. Legal values range from 1 through 0xFFFFFFFF.
- *reschedule_ticks*: Specifies the number of ticks for all timer expirations after the first. A zero for this parameter makes the timer a *one-shot* timer. Otherwise, for periodic timers, legal values range from 1 through 0xFFFFFFFF.

> **Note:** *An expired one-shot timer must be reset via*
***tx_timer_change*** *before it can be activated again.*

### Return Values

- **TX_SUCCESS** (0x00) Successful application timer change.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer.
- **TX_TICK_ERROR** (0x16) Invalid value (a zero) supplied for initial ticks.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
UINT status;

/* Change a previously created and now deactivated timer
to expire every 50 timer ticks, including the initial
expiration. */
status = tx_timer_change(&my_timer,50, 50);

/* If status equals TX_SUCCESS, the specified timer is
changed to expire every 50 ticks. */

/* Activate the specified timer to get it started again. */
status = tx_timer_activate(&my_timer);
```

### See Also

- [Timer Services](#Timer_Services)
