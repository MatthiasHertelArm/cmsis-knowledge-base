---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-set-notify"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_set_notify"
summary: "Notify application when event flags are set"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-set-notify"
license: "MIT"
mode: "V"
---

Notify application when event flags are set

### Prototype

```c
UINT tx_event_flags_set_notify(
    TX_EVENT_FLAGS_GROUP *group_ptr,
    VOID (*events_set_notify)(TX_EVENT_FLAGS_GROUP *));
```

### Description

This service registers a notification callback function that is called whenever one or more event flags are set in the specified event flags group. The processing of the notification callback is defined by the

### Parameters
- *group_ptr*: Pointer to previously created event flags group.
- *events_set_notify*: Pointer to application's event flags set notification function. If this value is TX_NULL, notification is disabled.

### Return Values

- **TX_SUCCESS** (0x00) Successful registration of event flags set notification.
- **TX_GROUP_ERROR** (0x06) Invalid event flags group pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was compiled with notification capabilities disabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_EVENT_FLAGS_GROUP my_group;

/* Register the "my_event_flags_set_notify" function for monitoring
event flags set in the event flags group "my_group." */
status = tx_event_flags_set_notify(&my_group, my_event_flags_set_notify);

/* If status is TX_SUCCESS the event flags set notification function
was successfully registered. */
void my_event_flags_set_notify(TX_EVENT_FLAGS_GROUP *group_ptr)

/* One or more event flags was set in this group! */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
