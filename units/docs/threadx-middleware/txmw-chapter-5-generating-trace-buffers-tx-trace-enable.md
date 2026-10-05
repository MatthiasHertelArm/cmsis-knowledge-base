---
id: "txmw-chapter-5-generating-trace-buffers-tx-trace-enable"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API / tx_trace_enable"
summary: "tx_trace_event_filter, tx_trace_event_unfilter, tx_trace_disable, tx_trace_isr_enter_insert, tx_trace_isr_exit_insert, tx_trace_buffer_full_notify, tx_trace_user_event_insert"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#tx-trace-enable"
license: "MIT"
mode: "V"
---

_Part of: Extended Event Trace API_

Enable event tracing

#### Prototype

```c
UINT tx_trace_enable (VOID *trace_buffer_start,
     ULONG trace_buffer_size, ULONG registry_entries);
```

#### Description
This service enables event tracing inside ThreadX. The trace buffer and the maximum number of ThreadX objects are supplied by the
application.

> **Important:** The ThreadX library and application must be built with **TX_ENABLE_EVENT_TRACE** defined in order to use event tracing.

#### Input Parameters

- **trace_buffer_start**: Pointer to the start of the user-supplied trace buffer.
- **trace_buffer_size**: Total number of bytes in the memory for the trace buffer. The larger the trace buffer, the more entries it is able to store.
- **registry_entries**: Number of application ThreadX objects to keep in the trace registry. The registry is used to correlate object addresses with object names. This is highly useful for GUI trace analysis tools.

#### Return Values

- **TX_SUCCESS** (0x00) Successful event trace enable.
- **TX_SIZE_ERROR** (0x05) Specified trace buffer size is too small. It must be large enough for the trace header, the object registry, and at least one trace entry.
- **TX_NOT_DONE** (0x20) Event tracing was already enabled.
- **TX_FEATURE_NOT_ENABLED** (0xFF) System was not compiled with trace enabled.

#### Allowed From

Initialization and threads

#### Example

```c
UCHAR my_trace_buffer[64000];

/* Enable event tracing using the global "my_trace_buffer" memory and supporting a maximum of 30 ThreadX objects in the registry. */
status = tx_trace_enable (&my_trace_buffer, 64000, 30);

/* If status is TX_SUCCESS the event tracing is enabled. */
```

#### See Also

tx_trace_event_filter, tx_trace_event_unfilter,
tx_trace_disable, tx_trace_isr_enter_insert,
tx_trace_isr_exit_insert, tx_trace_buffer_full_notify,
tx_trace_user_event_insert
