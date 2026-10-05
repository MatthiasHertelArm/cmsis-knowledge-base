---
id: "txmw-chapter-11-format-of-event-trace-b"
type: "concept"
domain: "trace"
title: "Chapter 11 - Format of event trace buffer"
summary: "ThreadX provides built-in event trace support for all ThreadX services, thread state changes, and user-defined events. To use event trace, simply build the ThreadX, NetX Duo, and FileX libraries with TX_ENABLE_EVENT_TRACE defined and enable tracing by calling the tx_trace_enable function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter11.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter11.md"
license: "MIT"
mode: "V"
---

ThreadX provides built-in event trace support for all ThreadX services, thread state changes, and user-defined events. To use event trace, simply build the ThreadX, NetX Duo, and FileX libraries with **TX_ENABLE_EVENT_TRACE** defined and enable tracing by calling the ***tx_trace_enable*** function. This chapter describes that process.
