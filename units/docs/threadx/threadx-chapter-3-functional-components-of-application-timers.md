---
id: "threadx-chapter-3-functional-components-of-application-timers"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Application Timers"
summary: "Fast response to asynchronous external events is the most important function of real-time, embedded applications. However, many of these applications must also perform certain activities at predetermined intervals of time."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#application-timers"
license: "MIT"
mode: "V"
---

Fast response to asynchronous external events is the most important function of real-time, embedded applications. However, many of these applications must also perform certain activities at predetermined intervals of time.

ThreadX application timers provide applications with the ability to execute application C functions at specific intervals of time. It is also possible for an application timer to expire only once. This type of timer is called a *one-shot timer*, while repeating interval timers are called *periodic timers*.

Each application timer is a public resource. ThreadX places no constraints on how application timers are used.

### Timer Intervals

In ThreadX time intervals are measured by periodic timer interrupts. Each timer interrupt is called a timer *tick*. The actual time between timer ticks is specified by the application, but 10ms is the norm for most implementations. The periodic timer setup is typically found in the ***tx_initialize_low_level*** assembly file.

It is worth mentioning that the underlying hardware must have the ability to generate periodic interrupts for application timers to function. In some cases, the processor has a built-in periodic interrupt capability. If the processor doesn't have this ability, the user's board must have a peripheral device that can generate periodic interrupts.

> **Important:** *ThreadX can still function even without a periodic interrupt source. However, all timer-related processing is then disabled. This includes timeslicing, suspension time-outs, and timer services.*

### Timer Accuracy

Timer expirations are specified in terms of ticks. The specified expiration value is decreased by one on each timer tick. Because an application timer could be enabled just prior to a timer interrupt (or timer tick), the actual expiration time could be up to one tick early.

If the timer tick rate is 10ms, application timers may expire up to 10ms early. This is more significant for 10ms timers than 1 second timers. Of course, increasing the timer interrupt frequency decreases this margin of error.

### Timer Execution

Application timers execute in the order they become active. For example, if three timers are created with the same expiration value and activated, their corresponding expiration functions are guaranteed to execute in the order they were activated.

### Creating Application Timers

Application timers are created either during initialization or during run-time by application threads. There is no limit on the number of application timers in an application.

### Run-time Application Timer Performance Information

ThreadX provides optional run-time application timer performance information. If the ThreadX library and application are built with **TX_TIMER_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

- activations

- deactivations

- reactivations (periodic timers)

- expirations

- expiration adjustments

Total number for each application timer:

- activations

- deactivations

- reactivations (periodic timers)

- expirations

- expiration adjustments

This information is available at run-time through the services ***tx_timer_performance_info_get*** and ***tx_timer_performance_system_info_get***. Application Timer performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application.

### Application Timer Control Block TX_TIMER

The characteristics of each application timer are found in its control block. It contains useful information such as the 32-bit expiration identification value. This structure is defined in the ***tx_api.h*** file.

Application timer control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Excessive Timers

By default, application timers execute from within a hidden system thread that runs at priority zero, which is typically higher than any application thread. Because of this, processing inside application timers should be kept to a minimum.

It is also important to avoid, whenever possible, timers that expire every timer tick. Such a situation might induce excessive overhead in the application.

> **Important:** *As mentioned previously, application timers are executed from a hidden system thread. It is, therefore, important not to select suspension on any ThreadX service calls made from within the application timer's expiration function.*
