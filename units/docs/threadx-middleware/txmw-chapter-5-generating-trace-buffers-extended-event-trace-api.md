---
id: "txmw-chapter-5-generating-trace-buffers-extended-event-trace-api"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Extended Event Trace API"
summary: "When ThreadX is built with TX_ENABLE_EVENT_TRACE defined, the following new event trace APIs are available to the application:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#extended-event-trace-api"
license: "MIT"
mode: "V"
---

When ThreadX is built with **TX_ENABLE_EVENT_TRACE** defined, the following new event trace APIs are available to the application:

- tx_trace_enable: *Enable event tracing*
- tx_trace_event_filter: *Filter specified event(s)*
- tx_trace_event_unfilter: *Unfilter specified event(s)*
- tx_trace_disable: *Disable event tracing*
- tx_trace_isr_enter_insert: *Insert ISR enter trace event*
- tx_trace_isr_exit_insert: *Insert ISR exit trace event*
- tx_trace_buffer_full_notify: *Register trace buffer full application callback*
- tx_trace_user_event_insert: *Insert user event*
