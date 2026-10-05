---
id: "threadx-overview-of-threadx-threadx-execution-speed"
type: "concept"
domain: "rtos"
title: "Overview of ThreadX: ThreadX execution speed"
summary: "ThreadX achieves a sub-microsecond context switch on most popular processors and is faster overall than other commercial RTOSs. In addition to being fast, ThreadX is also highly deterministic."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/overview-threadx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/overview-threadx.md#threadx-execution-speed"
license: "MIT"
mode: "V"
---

ThreadX achieves a sub-microsecond context switch on most popular processors and is faster overall than other commercial RTOSs. In addition to being fast, ThreadX is also highly deterministic. It achieves the same fast performance whether there are 200 threads ready, or just one.

Here are some typical performance characteristics of ThreadX:

* Fast boot: ThreadX boots in fewer than 120 cycles.
* Optional removal of basic error checking: Basic ThreadX error checking can be skipped at compile time. This can be useful when the application code is verified and no longer requires error checking on each parameter. Skipping error checking can be done on a compilation unit, rather than system-wide.
* Picokernel design: Services are not layered on each other, eliminating unnecessary function call overhead.
* Optimized interrupt processing: Only scratch registers are saved/restored upon ISR entry/exit, unless preemption is necessary.
* Optimized API processing:

    |ThreadX Service  |Service Time in Microseconds*  |
    |---------|---------|
    |Thread Suspend  |0.6  |
    |Thread Resume  |0.6  |
    |Queue Send  |0.3  |
    |Queue Receive  |0.3  |
    |Get Semaphore  |0.2  |
    |Put Semaphore  |0.2  |
    |Context Switch  |0.4  |
    |Interrupt Response  |0.0 – 0.6  |

    **Performance figures based on typical processor running at 200 MHz*.
