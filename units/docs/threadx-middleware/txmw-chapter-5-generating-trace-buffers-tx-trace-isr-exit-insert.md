---
id: "txmw-chapter-5-generating-trace-buffers-tx-trace-isr-exit-insert"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API / tx_trace_isr_exit_insert"
summary: "This service inserts the ISR entry event into the event trace buffer. It should be called by the application at the beginning of ISR processing. The supplied parameter should identify the ISR to the application."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#tx-trace-isr-exit-insert"
license: "MIT"
mode: "V"
---

_Part of: Extended Event Trace API_

#### Insert ISR exit event

#### Prototype

```c
VOID tx_trace_isr_exit_insert (ULONG isr_id);
```

#### Description

This service inserts the ISR entry event into the event trace buffer. It should be called by the application at the beginning of ISR processing. The supplied parameter should identify the ISR to the application.

> **Important:** The ThreadX library and application must be built with **TX_ENABLE_EVENT_TRACE** defined in order to use event tracing.

#### Input Parameters 

- **isr_id**: Application specific value to identify the ISR.

#### Return Values

**None**

#### Allowed From

ISRs

#### Example

```c
/* Insert trace event to identify the application's ISR with an ID of 3. */ 

status = tx_trace_isr_exit_insert (3);

/* If status is TX_SUCCESS the ISR exit event was inserted. */
```

#### See Also

tx_trace_enable, tx_trace_event_filter, tx_trace_event_unfilter, tx_trace_disable, tx_trace_isr_enter_insert, tx_trace_buffer_full_notify,
tx_trace_user_event_insert
