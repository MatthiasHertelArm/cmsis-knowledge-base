---
id: "threadx-chapter-2-installation-and-use-of-target-considerations"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: Target Considerations"
summary: "ThreadX requires between 2 KBytes and 20 KBytes of Read Only Memory (ROM) on the target."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#target-considerations"
license: "MIT"
mode: "V"
---

ThreadX requires between 2 KBytes and 20 KBytes of Read Only Memory (ROM) on the target. It also requires another 1 to 2 KBytes of the target's Random Access Memory (RAM) for the ThreadX system stack and other global data structures.

For timer-related functions like service call time-outs, time-slicing, and application timers to function, the underlying target hardware must provide a periodic interrupt source. If the processor has this capability, it is utilized by ThreadX. Otherwise, if the target processor does not have the ability to generate a periodic interrupt, the user's hardware must provide it. Setup and configuration of the timer interrupt is typically located in the ***tx_initialize_low_level*** assembly file in the ThreadX
distribution.

> **Note:** *ThreadX is still functional even if no periodic timer interrupt source is available. However, none of the timer-related services are functional.*

In function ***_tx_initialize_low_level***, the first-available RAM address is saved in global variable **_tx_initialize_unused_memory**. This address is later passed into ***tx_application_define*** (see ./chapter3.md#application-definition-function). The exception vector table and interrupt priorities may also be configured in ***_tx_initialize_low_level***.
