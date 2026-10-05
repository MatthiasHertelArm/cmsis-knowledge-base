---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-performance-system-info-g"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_performance_system_info_get"
summary: "This service retrieves performance information about all event flags groups in the system."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-performance-system-info-get"
license: "MIT"
mode: "V"
---

Retrieve performance system information

### Prototype

```c
UINT tx_event_flags_performance_system_info_get(
    ULONG *sets,
    ULONG *gets,
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about all event flags groups in the system.

> **Important:** *ThreadX library and application must be built with* **TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- *sets*: Pointer to destination for the total number of event flags set requests performed on all groups.
- *gets*: Pointer to destination for the total number of event flags get requests performed on all groups.
- *suspensions*: Pointer to destination for the total number of thread event flags get suspensions on all groups.
- *timeouts*: Pointer to destination for the total number of event flags get suspension timeouts on all groups.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful event flags system performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG sets;
ULONG gets;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on all previously created event
flag groups. */
status = tx_event_flags_performance_system_info_get(&sets, &gets,
    &suspensions, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
