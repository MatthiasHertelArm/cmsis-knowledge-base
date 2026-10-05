---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_info_get"
summary: "Retrieve information about an application timer"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about an application timer

### Prototype

```c
UINT tx_timer_info_get(
    TX_TIMER *timer_ptr, 
    CHAR **name,
    UINT *active,
    ULONG *remaining_ticks,
    ULONG *reschedule_ticks,
    TX_TIMER **next_timer);
```

### Description

This service retrieves information about the specified application timer.

### Parameters

- *timer_ptr*: Pointer to a previously created application timer.
- *name*: Pointer to destination for the pointer to the timer's name.
- *active*: Pointer to destination for the timer active indication. If the timer is inactive or this service is called from the timer itself, a **TX_FALSE** value is returned. Otherwise, if the timer is active, a **TX_TRUE** value is returned.
- *remaining_ticks*: Pointer to destination for the number of timer ticks left before the timer expires.
- *reschedule_ticks*: Pointer to destination for the number of timer ticks that will be used to automatically reschedule this timer. If the value is zero, then the timer is a one-shot and won't be rescheduled.
- *next_timer*: Pointer to destination for the pointer of the next created application timer.

> **Note:** *Supplying a **TX_NULL** for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful timer information retrieval.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
CHAR *name;
UINT active;
ULONG remaining_ticks;
ULONG reschedule_ticks;
TX_TIMER *next_timer;
UINT status;

/* Retrieve information about the previously created
application timer "my_timer." */
status = tx_timer_info_get(&my_timer, &name,
    &active,&remaining_ticks,
    &reschedule_ticks,
    &next_timer);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Timer Services](#Timer_Services)
