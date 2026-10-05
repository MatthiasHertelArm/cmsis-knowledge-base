---
id: "threadx-chapter-3-functional-components-of-execution-overview-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Execution Overview"
summary: "There are four types of program execution within a ThreadX SMP application: Initialization, Thread Execution, Interrupt Service Routines (ISRs), and Application Timers."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#execution-overview"
license: "MIT"
mode: "V"
---

There are four types of program execution within a ThreadX SMP application: Initialization, Thread Execution, Interrupt Service Routines (ISRs), and Application Timers.

Figure 1 on page 45 shows each different type of program execution. More detailed information about each of these types is found in subsequent sections of this chapter.

### Initialization
As the name implies, this is the first type of program execution in a ThreadX SMP application. Initialization includes all program execution between processor reset and the entry point of the *thread scheduling loop.*

> **Important:** Initialization is performed by or initiated by core 0, which is the default running core after reset.

### Thread Execution
After initialization is complete, each core running ThreadX SMP enters its thread scheduling loop. The scheduling loop looks for an application thread ready for execution on that core. When a ready thread is found, ThreadX SMP transfers control to it. After the thread is finished (or another higher-priority thread becomes ready), execution transfers back to the thread scheduling loop to find the next highest priority ready thread on each core.

This process of continually executing and scheduling threads is the most common type of program execution in ThreadX SMP applications.

(figure: Thread Execution)

**FIGURE 1. Types of Program Execution**

### Interrupt Service Routines (ISR)
Interrupts are the cornerstone of real-time systems. Without interrupts it would be extremely difficult to respond to changes in the external world in a timely manner. On detection of an interrupt, the processor saves key information about the current program execution (usually on the stack), then transfers control to a predefined program area. This predefined program area is commonly called an Interrupt Service Routine.

In most cases, interrupts occur during thread execution (or in the thread scheduling loop). However, interrupts may also occur inside of an executing ISR or an Application Timer.

All cores are allowed to process interrupts. The mapping of interrupts to cores is under the direct control of the application. The ThreadX SMP timer interrupt is by default assigned to core 0 for processing. Please see the code in *tx_timer_interrupt.S* for implementation of this assignment.

### Application Timers
Application Timers are similar to ISRs, except the hardware implementation (usually a single periodic hardware interrupt is used) is hidden from the application. Such timers are used by applications to perform time-outs, periodics, and/or watchdog services. Just like ISRs, Application Timers most often interrupt thread execution. Unlike ISRs, however, Application Timers cannot interrupt each other.

> **Note:** That like threads, application timers can be excluded from execution on any core.
