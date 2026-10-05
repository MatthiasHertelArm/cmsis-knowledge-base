---
id: "threadx-chapter-4-description-of-threadx-s-tx-event-flags-set"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_event_flags_set"
summary: "This service sets or clears event flags in an event flags group, depending upon the specified set-option. All suspended threads whose event flags request is now satisfied are resumed."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-event-flags-set"
license: "MIT"
mode: "V"
---

Set event flags in an event flags group

### Prototype

```c
UINT tx_event_flags_set(
    TX_EVENT_FLAGS_GROUP *group_ptr,
    ULONG flags_to_set,
    UINT set_option);
```

### Description

This service sets or clears event flags in an event flags group, depending upon the specified set-option. All suspended threads whose event flags request is now satisfied are resumed.

### Parameters

- *group_ptr*: 
Pointer to the previously created event flags group control block.
- *flags_to_set*: 
Specifies the event flags to set or clear based upon the set option selected.
- *set_option*: 
Specifies whether the event flags specified are ANDed or ORed into the current event flags of the group. The following are valid selections:
  - **TX_AND** (0x02)
  - **TX_OR** (0x00)

  Selecting TX_AND specifies that the specified event flags are **AND**ed into the current event flags in the group. This option is often used to clear event flags in a group. Otherwise, if TX_OR is specified, the specified event flags are **OR**ed with the current event in the group.

### Return Values
- **TX_SUCCESS** (0x00) Successful event flags set.
- **TX_GROUP_ERROR** (0x06) Invalid pointer to event flags group.
- **TX_OPTION_ERROR** (0x08) Invalid set-option specified.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_EVENT_FLAGS_GROUP my_event_flags_group;
UINT status;

/* Set event flags 0, 4, and 8. */
status = tx_event_flags_set(&my_event_flags_group,
    0x111, TX_OR);

/* If status equals TX_SUCCESS, the event flags have been
set and any suspended thread whose request was satisfied
has been resumed. */
```

### See Also

- [Event Flags Services](#Event_Flags_Services)
