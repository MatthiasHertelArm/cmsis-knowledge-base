---
id: "txmw-chapter-5-generating-trace-buffers-tx-trace-buffer-full-notify"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API / tx_trace_buffer_full_notify"
summary: "This service registers an application callback function that is called by ThreadX when the trace buffer becomes full. The application can then choose to disable tracing and/or possibly setup a new trace buffer."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#tx-trace-buffer-full-notify"
license: "MIT"
mode: "V"
---

_Part of: Extended Event Trace API_

#### Register trace buffer full application callback

#### Prototype

```c
VOID tx_trace_buffer_full_notify (VOID (*full_buffer_callback)(VOID *));
```

#### Description

This service registers an application callback function that is called by ThreadX when the trace buffer becomes full. The application can then choose to disable tracing and/or possibly setup a new trace buffer.

> **Important:** The ThreadX library and application must be built with **TX_ENABLE_EVENT_TRACE** defined in order to use event tracing.

#### Input Parameters

- **full_buffer_callback**: Application function to call when the trace buffer is full. A value of NULL disables the notification callback.

#### Return Values

**None**

#### Allowed From

ISRs

#### Example

```c
y_trace_is_full(void *trace_buffer_start)

{

     /* Application specific processing goes here! */

}

/* Register the "my_trace_is_full" function to be called whenever the trace buffer fills. */

status = tx_trace_buffer_full_notify (my_trace_is_full);

/* If status is TX_SUCCESS the "my_trace_is_full" function is registered. */
```

#### See Also

tx_trace_enable, tx_trace_event_filter, tx_trace_event_unfilter, tx_trace_disable, tx_trace_isr_enter_insert, tx_trace_isr_exit_insert,
tx_trace_user_event_insert
