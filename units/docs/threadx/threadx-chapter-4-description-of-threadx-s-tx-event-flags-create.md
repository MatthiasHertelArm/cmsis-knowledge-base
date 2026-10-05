---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_create"
summary: "This service creates a group of 32 event flags. All 32 event flags in the group are initialized to zero. Each event flag is represented by a single bit."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-create"
license: "MIT"
mode: "V"
---

Create event flags group

### Prototype

```c
UINT tx_event_flags_create(
    TX_EVENT_FLAGS_GROUP *group_ptr,
    CHAR *name_ptr);
```

### Description

This service creates a group of 32 event flags. All 32 event flags in the group are initialized to zero. Each event flag is represented by a single bit.

### Parameters

- *group_ptr*: Pointer to an event flags group control block.
- *name_ptr*: Pointer to the name of the event flags group.

### Return Values

- **TX_SUCCESS** (0x00) Successful event group creation.
- **TX_GROUP_ERROR** (0x06) Invalid event group pointer. Either the pointer is **NULL** or the event group is already created.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_EVENT_FLAGS_GROUP my_event_group;
UINT status;

/* Create an event flags group. */
status = tx_event_flags_create(&my_event_group,
  "my_event_group_name");

/* If status equals TX_SUCCESS, my_event_group is ready
for get and set services. */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
