---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_info_get"
summary: "Retrieve information about event flags group"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about event flags group

### Prototype

```c
UINT tx_event_flags_info_get(
    TX_EVENT_FLAGS_GROUP *group_ptr,
    CHAR **name, ULONG *current_flags,
    TX_THREAD **first_suspended,
    ULONG *suspended_count,
    TX_EVENT_FLAGS_GROUP **next_group);
```

### Description

This service retrieves information about the specified event flags group.

### Parameters

- *group_ptr*: Pointer to an event flags group control block.
- *name*: Pointer to destination for the pointer to the event flags group's name.
- *current_flags*: Pointer to destination for the current set flags in the event flags group.
- *first_suspended*: Pointer to destination for the pointer to the thread that is first on the suspension list of this event flags group.
- *suspended_count*: Pointer to destination for the number of threads currently suspended on this event flags group.
- *next_group*: Pointer to destination for the pointer of the next created event flags group.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful event group information retrieval.
- **TX_GROUP_ERROR** (0x06) Invalid event group pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_EVENT_FLAGS_GROUP my_event_group;
CHAR *name;
ULONG current_flags;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_EVENT_FLAGS_GROUP *next_group;
UINT status;

/* Retrieve information about the previously created
event flags group "my_event_group." */
status = tx_event_flags_info_get(&my_event_group, &name,
    &current_flags,
    &first_suspended, &suspended_count,
    &next_group);
/* If status equals TX_SUCCESS, the information requested is
valid. */
```
### See Also

- [Event Flags Services](#Event_Flags_Services)
