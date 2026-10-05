---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-smp-core-exclude-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX SMP Services: tx_timer_smp_core_exclude_get"
summary: "This function returns the current core exclusion list."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter4.md#tx-timer-smp-core-exclude-get"
license: "MIT"
mode: "V"
---

Gets the timer's current core exclusion

### Prototype

```C
UINT tx_timer_smp_core_exclude_get(TX_TIMER *timer_ptr,
                         ULONG *exclusion_map_ptr);
```
### Description

This function returns the current core exclusion list.

### Parameters

- **timer_ptr**: Pointer to timer from which to retrieve the core exclusion.
- **exclusion_map_ptr**: Destination for current core exclusion bit map.

### Return Values

- **TX_SUCCESS**: (0x00) Successful retrieval of timer's core exclusion.
- **TX_TIMER_ERROR**: (0x0E) Invalid timer pointer.
- **TX_PTR_ERROR**: (0x03) Invalid exclusion destination pointer.

### Allowed From

Initialization, ISRs, threads, and timers

### Example

```C
ULONG excluded_cores;

/* Retrieve the core exclusion for "Timer 0". */
tx_timer_smp_core_exclude_get(&timer_0, &excluded_cores);
```
### See Also

- [Timer SMP Services](#Timer_SMP_Services)
