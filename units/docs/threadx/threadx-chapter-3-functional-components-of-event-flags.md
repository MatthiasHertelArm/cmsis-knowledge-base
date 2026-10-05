---
id: "threadx-chapter-3-functional-components-of-event-flags"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Event Flags"
summary: "Event flags provide a powerful tool for thread synchronization. Each event flag is represented by a single bit. Event flags are arranged in groups of 32."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#event-flags"
license: "MIT"
mode: "V"
---

Event flags provide a powerful tool for thread synchronization. Each event flag is represented by a single bit. Event flags are arranged in groups of 32. Threads can operate on all 32 event flags in a group at the same time. Events are set by ***tx_event_flags_set*** and are retrieved by ***tx_event_flags_get***.

Setting event flags is done with a logical AND/OR operation between the current event flags and the new event flags. The type of logical operation (either an AND or OR) is specified in the ***tx_event_flags_set*** call.

There are similar logical options for retrieval of event flags. A get request can specify that all specified event flags are required (a logical AND).

Alternatively, a get request can specify that any of the specified event flags will satisfy the request (a logical OR). The type of logical operation associated with event flags retrieval is specified in the ***tx_event_flags_get*** call.

> **Important:** *Event flags that satisfy a get request are consumed, i.e., set to zero, if* **TX_OR_CLEAR** *or* **TX_AND_CLEAR** *are specified by the request.*

Each event flags group is a public resource. ThreadX places no constraints on how event flags groups are used.

### Creating Event Flags Groups

Event flags groups are created either during initialization or during run-time by application threads. At the time of their creation, all event flags in the group are set to zero. There is no limit on the number of event flags groups in an application.

### Thread Suspension

Application threads can suspend while attempting to get any logical combination of event flags from a group. After an event flag is set, the get requests of all suspended threads are reviewed. All the threads that now have the required event flags are resumed.

> **Note:** *All suspended threads on an event flag group are reviewed when its event flags are set. This, of course, introduces additional overhead. Therefore, it is good practice to limit the number of threads using the same event flag group to a reasonable number.*

### Event Flags Set Notification

Some applications may find it advantageous to be notified whenever an event flag is set. ThreadX provides this ability through the ***tx_event_flags_set_notify*** service. This service registers the supplied application notification function with the specified event flags group. ThreadX will subsequently invoke this application notification function whenever an event flag in the group is set. The exact processing within the application notification function is determined by the application, but it typically consists of resuming the appropriate thread for processing the new event flag.

### Event Flags Event chaining

The notification capabilities in ThreadX can be used to "chain" various synchronization events together. This is typically useful when a single thread must process multiple synchronization events.

For example, instead of having separate threads suspend for a queue message, event flags, and a semaphore, the application can register a notification routine for each object. When invoked, the application notification routine can then resume a single thread, which can interrogate each object to find and process the new event.

In general, *event-chaining* results in fewer threads, less overhead, and smaller RAM requirements. It also provides a highly flexible mechanism to handle synchronization requirements of more complex systems.

### Run-time Event Flags Performance Information

ThreadX provides optional run-time event flags performance information. If the ThreadX library and application is built with **TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

  - event flags sets

  - event flags gets

  - event flags get suspensions

  - event flags get timeouts

Total number for each event flags group:

  - event flags sets

  - event flags gets

  - event flags get suspensions

  - event flags get timeouts

This information is available at run-time through the services ***tx_event_flags_performance_info_get*** and ***tx_event_flags_performance_system_info_get***. The performance information of event flags is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of timeouts on the ***tx_event_flags_get*** service might suggest that the event flags suspension timeout is too short.

### Event Flags Group Control Block TX_EVENT_FLAGS_GROUP

The characteristics of each event flags group are found in its control block. It contains information such as the current event flags settings and the number of threads suspended for events. This structure is defined in the ***tx_api.h*** file.

Event group control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.
