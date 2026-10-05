---
id: "threadx-chapter-4-description-of-threadx-s-tx-timer-smp-core-exclude"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX SMP Services: tx_timer_smp_core_exclude"
summary: "Exclude timer execution on a set of cores"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter4.md#tx-timer-smp-core-exclude"
license: "MIT"
mode: "V"
---

Exclude timer execution on a set of cores

### Prototype

```C
UINT  tx_timer_smp_core_exclude(TX_TIMER *timer_ptr, ULONG exclusion_map);
```
### Description

This function excludes the specified timer from executing on the core(s) specified in the bit map called "*exclusion_map*." Each bit in "*exclusion_map*" represents a core (bit 0 represents core 0, etc.). If the bit is set, the corresponding core is excluded from executing the specified timer.

> **Important:** Use of processor exclusion may cause additional processing in the thread to core mapping logic in order to find the optimal match. This processing is bounded by the number of ready threads.

### Parameters

- **timer_ptr**: Pointer to timer to change the core exclusion.
- **exclusion_map**: Bit map where a sit bit indicates that that core is excluded. Supplying a 0 value enables the timer to execute on any core (default).

### Return Values

- **TX_SUCCESS** (0x00) Successful core exclusion.
- **TX_TIMER_ERROR** (0x0E) Invalid timer pointer.

### Allowed From

Initialization, ISRs, threads, and timers

### Example

```C
/* Exclude core 0 for "Timer 0". */
tx_timer_smp_core_exclude(&timer_0, 0x01);
```

### See Also

- [Timer SMP Services](#Timer_SMP_Services)
