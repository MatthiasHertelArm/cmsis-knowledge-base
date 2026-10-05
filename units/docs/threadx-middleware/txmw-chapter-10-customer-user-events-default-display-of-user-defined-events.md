---
id: "txmw-chapter-10-customer-user-events-default-display-of-user-defined-events"
type: "concept"
domain: "trace"
title: "Chapter 10 - Customer user events: Default Display of User-Defined Events"
summary: "By default, TraceX displays all user events with a default user-defined Event icon as described in Chapter 6."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter10.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter10.md#default-display-of-user-defined-events"
license: "MIT"
mode: "V"
---

(figure: User-defined event icon)

By default, TraceX displays all user events with a default user-defined Event icon as described in Chapter 6. Figure 28 shows the default user-defined event icon for events 452 and 453, which were placed in the event buffer via the previous
***tx_trace_user_event_insert*** examples.

(figure: Screenshot of the default display of user-defined events.)
**FIGURE 28**

Detailed information is also available for user-defined Events. Figure 28 shows the detailed event information for event 452, which has event number 4096 and shows the specified four information fields.

(figure: Screenshot of the detailed display of user-defined events.)
**FIGURE 29**
