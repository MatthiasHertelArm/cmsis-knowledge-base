---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_delete"
summary: "This service deletes the specified event flags group. All threads suspended waiting for events from this group are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-delete"
license: "MIT"
mode: "V"
---

Delete event flags group

### Prototype

```c
UINT tx_event_flags_delete(TX_EVENT_FLAGS_GROUP *group_ptr);
```

### Description

This service deletes the specified event flags group. All threads suspended waiting for events from this group are resumed and given a TX_DELETED return status.

> **Important:** *The application must ensure that a set notify callback for this event flags group is completed (or disabled) before deleting the event flags group. In addition, the application must prevent all future use of a deleted event flags group.*

### Parameters

- *group_ptr*: Pointer to a previously created event flags group.

### Return Values

- **TX_SUCCESS** (0x00) Successful event flags group deletion.
- **TX_GROUP_ERROR** (0x06) Invalid event flags group pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_EVENT_FLAGS_GROUP my_event_flags_group;
UINT status;

/* Delete event flags group. Assume that the group has
already been created with a call to
tx_event_flags_create. */
status = tx_event_flags_delete(&my_event_flags_group);

/* If status equals TX_SUCCESS, the event flags group is
deleted. */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
