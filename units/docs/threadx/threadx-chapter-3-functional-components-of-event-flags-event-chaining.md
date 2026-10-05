---
id: "threadx-chapter-3-functional-components-of-event-flags-event-chaining"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Event Flags Event-chaining"
summary: "The notification capabilities in ThreadX SMP can be used to \"chain\" various synchronization events together. This is typically useful when a single thread must process multiple synchronization events."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#event-flags-event-chaining"
license: "MIT"
mode: "V"
---

The notification capabilities in ThreadX SMP can be used to "chain" various synchronization events together. This is typically useful when a single thread must process multiple synchronization events. 

For example, instead of having separate threads suspend for a queue message, event flags, and a semaphore, the application can register a notification routine for each object. When invoked, the application notification routine can then resume a single thread, which can interrogate each object to find and process the new event. 

In general, *event-chaining* results in fewer threads, less overhead, and smaller RAM requirements. It also provides a highly flexible mechanism to handle synchronization requirements of more complex systems. 

### Run-time Event Flags Performance Information 
ThreadX SMP provides optional run-time event flags performance information. If the ThreadX SMP library and application is built with ***TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO*** defined, ThreadX SMP accumulates the following information.

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

This information is available at run-time through the services *tx_event_flags_performance_info_get* and *tx_event_flags_performance_system_info_get*. Event Flags performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of timeouts on the *tx_event_flags_get* service might suggest that the event flags suspension timeout is too short.

### Event Flags Group Control Block TX_EVENT_FLAGS_GROUP
The characteristics of each event flags group are found in its control block. It contains information such as the current event flags settings and the number of threads suspended for events. This structure is defined in the ***tx_api.h*** file. 

Event group control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.
