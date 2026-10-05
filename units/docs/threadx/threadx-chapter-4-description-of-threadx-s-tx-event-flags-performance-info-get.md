---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_performance_info_get"
summary: "Get event flags group performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-performance-info-get"
license: "MIT"
mode: "V"
---

Get event flags group performance information

### Prototype

```c
UINT tx_event_flags_performance_info_get(
    TX_EVENT_FLAGS_GROUP *group_ptr,
    ULONG *sets, ULONG *gets,
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about the specified event flags group.

> **Important:** *ThreadX library and application must be built with* **TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO*: *defined for this service to return performance information.*

### Parameters

- *group_ptr*: Pointer to previously created event flags group.
- *sets*: Pointer to destination for the number of event flags set requests performed on this group.
- *gets*: Pointer to destination for the number of event flags get requests performed on this group.
- *suspensions*: Pointer to destination for the number of thread event flags get suspensions on this group.
- *timeouts*: Pointer to destination for the number of event flags get suspension timeouts on this group.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful event flags group performance get.
- **TX_PTR_ERROR** (0x03) Invalid event flags group pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_EVENT_FLAGS_GROUP my_event_flag_group;
ULONG sets;
ULONG gets;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on the previously created event
flag group. */
status = tx_event_flags_performance_info_get(&my_event_flag_group,
    &sets, &gets, &suspensions,
    &timeouts);

/* If status is TX_SUCCESS the performance information was successfully
retrieved. */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
