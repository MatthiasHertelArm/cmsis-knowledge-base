---
id: "threadx-chapter-3-functional-components-of-event-flags-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Event Flags"
summary: "Event flags provide a powerful tool for thread synchronization. Each event flag is represented by a single bit. Event flags are arranged in groups of 32."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#event-flags"
license: "MIT"
mode: "V"
---

Event flags provide a powerful tool for thread synchronization. Each event flag is represented by a single bit. Event flags are arranged in groups of 32.

Threads can operate on all 32 event flags in a group at the same time. Events are set by *tx_event_flags_set* and are retrieved by *tx_event_flags_get*.

Setting event flags is done with a logical AND/OR operation between the current event flags and the new event flags. The type of logical operation (either an AND or OR) is specified in the *tx_event_flags_set* call.

There are similar logical options for retrieval of event flags. A get request can specify that all specified event flags are required (a logical AND). Alternatively, a get request can specify that any of the specified event flags will satisfy the request (a logical OR). The type of logical operation associated with event flags retrieval is specified in the *tx_event_flags_get* call.

> **Important:** Event flags that satisfy a get request are consumed, i.e., set to zero, if **TX_OR_CLEAR** or **TX_AND_CLEAR** are specified by the request.

Each event flags group is a public resource. ThreadX SMP places no constraints on how event flags groups are used.

### Creating Event Flags Groups
Event flags groups are created either during initialization or during run-time by application threads. At the time of their creation, all event flags in the group are set to zero. There is no limit on the number of event flags groups in an application.

### Thread Suspension 
Application threads can suspend while attempting to get any logical combination of event flags from a group. After an event flag is set, the get requests of all suspended threads are reviewed. All the threads that now have the required event flags are resumed.

> **Important:** All suspended threads on an event flags group are reviewed when its event flags are set. This, of course, introduces additional overhead. Therefore, it is good practice to limit the number of threads using the same event flags group to a reasonable number.

### Event Flags Set Notification 
Some applications may find it advantageous to be notified whenever an event flag is set. ThreadX SMP provides this ability through the *tx_event_flags_set_notify* service. This service registers the supplied application notification function with the specified event flags group. ThreadX SMP will subsequently invoke this application notification function whenever an event flag in the group is set. The exact processing within the application notification function is determined by the application, but it typically consists of resuming the appropriate thread for processing the new event flag.
