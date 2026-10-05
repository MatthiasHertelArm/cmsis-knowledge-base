---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_create"
summary: "This service creates an application timer with the specified expiration function and periodic."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-create"
license: "MIT"
mode: "V"
---

Create application timer

### Prototype

```c
UINT tx_timer_create(
    TX_TIMER *timer_ptr, 
    CHAR *name_ptr,
    VOID (*expiration_function)(ULONG),
    ULONG expiration_input, 
    ULONG initial_ticks,
    ULONG reschedule_ticks, 
    UINT auto_activate);
```

### Description

This service creates an application timer with the specified
expiration function and
periodic.

### Parameters

- *timer_ptr*: Pointer to a timer control block
- *name_ptr*: Pointer to the name of the timer.
- *expiration_function*: Application function to call when the timer expires.
- *expiration_input*: Input to pass to expiration function when timer expires.
- *initial_ticks*: Specifies the initial number of ticks for timer expiration. Legal values range from 1 through 0xFFFFFFFF.
- *reschedule_ticks*: Specifies the number of ticks for all timer expirations after the first. A zero for this parameter makes the timer a *one-shot* timer. Otherwise, for periodic timers, legal values range from 1 through 0xFFFFFFFF.

  > **Note:** *After a one-shot timer expires, it must be reset via   tx_timer_change before it can be activated again.*

- *auto_activate*: Determines if the timer is automatically activated during creation. If this value is **TX_AUTO_ACTIVATE** (0x01) the timer is made active. Otherwise, if the value **TX_NO_ACTIVATE** (0x00) is selected, the timer is created in a non-active state. In this case, a subsequent ***tx_timer_activate*** service call is necessary to get the timer actually started.

### Return Values

- **TX_SUCCESS** (0x00) Successful application timer creation.
- **TX_TIMER_ERROR** (0x15) Invalid application timer pointer. Either the pointer is NULL or the timer is already created.
- **TX_TICK_ERROR** (0x16) Invalid value (a zero) supplied for initial ticks.
- **TX_ACTIVATE_ERROR** (0x17) Invalid activation selected.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
UINT status;

/* Create an application timer that executes
"my_timer_function" after 100 ticks initially and then
after every 25 ticks. This timer is specified to start
immediately! */
status = tx_timer_create(&my_timer,"my_timer_name",
    my_timer_function, 0x1234, 100, 25,
    TX_AUTO_ACTIVATE);

/* If status equals TX_SUCCESS, my_timer_function will
be called 100 timer ticks later and then called every
25 timer ticks. Note that the value 0x1234 is passed to
my_timer_function every time it is called. */
```

### See Also

- [Timer Services](#Timer_Services)
