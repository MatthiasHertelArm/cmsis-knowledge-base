---
id: "txmw-chapter-10-customer-user-events-inserting-user-defined-events"
type: "concept"
domain: "trace"
title: "Chapter 10 - Customer user events: Inserting User-Defined Events"
summary: "ThreadX provides the ability for developers to log their own user-defined events, providing even more useful information that can be viewed graphically by TraceX. User-defined event numbers range from"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter10.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter10.md#inserting-user-defined-events"
license: "MIT"
mode: "V"
---

ThreadX provides the ability for developers to log their own user-defined events, providing even more useful information that can be viewed graphically by TraceX. User-defined event numbers range from

**TX_TRACE_USER_EVENT_START** (4096) through **TX_TRACE_USER_EVENT_END** (65535), inclusive. The placement of
the events in the trace buffer is done via the ***tx_trace_user_event_insert***, defined in Chapter 5. The
following example calls insert two user-defined events into the current trace buffer on the target, namely user-defined event 4096 and event 4098:

```c
tx_trace_user_event_insert(4096, 1, 2, 3, 4);
tx_trace_user_event_insert(4098,0x100,0x200,0x300,0x400);
```
