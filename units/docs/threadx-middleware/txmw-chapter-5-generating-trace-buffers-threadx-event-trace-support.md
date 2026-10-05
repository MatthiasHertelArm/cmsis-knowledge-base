---
id: "txmw-chapter-5-generating-trace-buffers-threadx-event-trace-support"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: ThreadX Event Trace Support"
summary: "ThreadX provides built-in event trace support for all ThreadX services, thread state changes, and user-defined events. The ThreadX event-trace capability is primarily designed as a post-mortem tool to analyze the last \"n\" activities in the application."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#threadx-event-trace-support"
license: "MIT"
mode: "V"
---

ThreadX provides built-in event trace support for all ThreadX services, thread state changes, and user-defined events. The ThreadX event-trace capability is primarily designed as a post-mortem tool to analyze the last "n" activities in the application. From this information, the developer may spot problems and/or potential targets of optimization.

TraceX graphically displays the event trace buffer built by ThreadX. The following describes how to build the buffer and describes the underlying format of the buffer.
