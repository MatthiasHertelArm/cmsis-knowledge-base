---
id: "txmw-chapter-5-generating-trace-buffers-tx-trace-disable"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API / tx_trace_disable"
summary: "This service disables event tracing inside ThreadX. This can be useful if the application wants to freeze the current event trace buffer and possibly transport it externally during run-time. Once disabled, the tx_trace_enable can be called to start tracing again."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#tx-trace-disable"
license: "MIT"
mode: "V"
---

_Part of: Extended Event Trace API_

#### Disable event tracing

#### Prototype

```c
UINT tx_trace_disable (VOID);
```

#### Description

This service disables event tracing inside ThreadX. This can be useful if the application wants to freeze the current event trace buffer and possibly transport it externally during run-time. Once disabled, the **tx_trace_enable** can be called to start tracing again.

> **Important:** The ThreadX library and application must be built with **TX_ENABLE_EVENT_TRACE** defined in order to use event tracing.

#### Input Parameters

None.

#### Return Values

- **TX_SUCCESS** (0x00) Successful event trace disable.
- **TX_NOT_DONE** (0x20) Event tracing was not enabled.
- **TX_FEATURE_NOT_ENABLED** (0xFF) System was not compiled with trace enabled.

#### Allowed From

Initialization and threads

#### Example 

```c
/* Disable event tracing. */ 
status = tx_trace_disable ();

/* If status is TX_SUCCESS the event tracing is disabled. */
```

#### See Also

tx_trace_enable, tx_trace_event_filter,
tx_trace_event_unfilter, tx_trace_isr_enter_insert,
tx_trace_isr_exit_insert, tx_trace_buffer_full_notify,
tx_trace_user_event_insert
