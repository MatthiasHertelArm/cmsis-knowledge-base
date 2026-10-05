---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_timer_performance_info_get"
summary: "This service retrieves performance information about the specified application timer."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-timer-performance-info-get"
license: "MIT"
mode: "V"
---

Get timer performance information

### Prototype

```c
UINT tx_timer_performance_info_get(
    TX_TIMER *timer_ptr,
    ULONG *activates, 
    ULONG *reactivates,
    ULONG *deactivates, 
    ULONG *expirations,
    ULONG *expiration_adjusts);
```

### Description

This service retrieves performance information about the specified application timer.

> **Important:** *The ThreadX library and application must be built with* ***TX_TIMER_ENABLE_PERFORMANCE_INFO*** *defined for this service to return performance information.*

### Parameters
- *timer_ptr*: Pointer to previously created timer.
- *activates*: Pointer to destination for the number of activation requests performed on this timer.
- *reactivates*: Pointer to destination for the number of automatic reactivations performed on this periodic timer.
- *deactivates*: Pointer to destination for the number of deactivation requests performed on this timer.
- *expirations*: Pointer to destination for the number of expirations of this timer.
- *expiration_adjusts*: Pointer to destination for the number of internal expiration adjustments performed on this timer. These adjustments are done in the timer interrupt processing for timers that are larger than the default timer list size (by default timers with expirations greater than 32 ticks).

> **Note:** *Supplying a TX_NULL for any parameter indicates the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful timer performance get.
- **TX_PTR_ERROR** (0x03) Invalid timer pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_TIMER my_timer;
ULONG activates;
ULONG reactivates;
ULONG deactivates;
ULONG expirations;
ULONG expiration_adjusts;

/* Retrieve performance information on the previously created
timer. */
status = tx_timer_performance_info_get(&my_timer, &activates,
    &reactivates,&deactivates, &expirations,
    &expiration_adjusts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Timer Services](#Timer_Services)
