---
id: "txmw-chapter-5-generating-trace-buffers-tx-trace-user-event-insert"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API / tx_trace_user_event_insert"
summary: "This service inserts the user event into the trace buffer. User event IDs must be greater than the constant TX_TRACE_USER_EVENT_START, which is defined to be 4096."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#tx-trace-user-event-insert"
license: "MIT"
mode: "V"
---

_Part of: Extended Event Trace API_

#### Insert user event

#### Prototype

```c
UINT tx_trace_user_event_insert (ULONG event_id, 
   ULONG info_field_1, ULONG info_field_2,
   ULONG info_field_3, ULONG info_field_4);
```

#### Description

This service inserts the user event into the trace buffer. User event IDs must be greater than the constant **TX_TRACE_USER_EVENT_START**, which is defined to be 4096. The maximum user event is defined by the constant **TX_TRACE_USER_EVENT_END**, which is defined to be 65535. All events within this range are available to the application. The information fields are application specific.

> **Important:** The ThreadX library and application must be built with **TX_ENABLE_EVENT_TRACE** defined in order to use event tracing.

#### Input Parameters

- **event_id**: Application-specific event identification and must start be greater than **TX_TRACE_USER_EVENT_START** and less than or equal to **TX_TRACE_USER_EVENT_END**.
- **info_field_1**: Application-specific information field.
- **info_field_2**: Application-specific information field.
- **info_field_3**: Application-specific information field.
- **info_field_4**: Application-specific information field.

#### Return Values
- **TX_SUCCESS** (0x00) Successful user event insert.
- **TX_NOT_DONE** (0x20) Event tracing is not enabled.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with trace enabled.

#### Allowed From

Initialization and threads

#### Example

```c
/* Insert user event 3000, with info fields of 1, 2, 3, 4. */ 

status = tx_trace_user_event_insert (3000, 1, 2, 3, 4);

/* If status is TX_SUCCESS the user event was inserted. */
```

#### See Also

tx_trace_enable, tx_trace_event_filter,
tx_trace_event_unfilter, tx_trace_disable,
tx_trace_isr_enter_insert, tx_trace_isr_exit_insert,
tx_trace_buffer_full_notify
