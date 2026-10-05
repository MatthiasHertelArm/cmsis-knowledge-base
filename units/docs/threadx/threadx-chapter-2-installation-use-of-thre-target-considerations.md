---
id: "threadx-chapter-2-installation-use-of-thre-target-considerations"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation & Use of ThreadX SMP: Target Considerations"
summary: "ThreadX SMP requires between 2 KBytes and 20 KBytes of Read Only Memory (ROM) on the target."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter2.md#target-considerations"
license: "MIT"
mode: "V"
---

ThreadX SMP requires between 2 KBytes and 20 KBytes of Read Only Memory (ROM) on the target. Another 1 to 2 KBytes of the target's Random Access Memory (RAM) are required for the ThreadX SMP system stack and other global data structures.

For timer-related functions like service call time-outs, time-slicing, and application timers to function, the underlying target hardware must provide a periodic interrupt source. If the processor has this capability, it is utilized by ThreadX SMP. Otherwise, if the target processor does not have the ability to generate a periodic interrupt, the user's hardware must provide it. Setup and configuration of the timer interrupt is typically located in the ***tx_initialize_low_level*** assembly file in the ThreadX SMP distribution.

> **Important:** ThreadX SMP is still functional even if no periodic timer interrupt source is available. However, none of the timer-related services are functional. Please review the supplied **readme_threadx.txt** file for any additional host system considerations and/or options.
