---
id: "rtx-operation-scheduler"
type: "concept"
domain: "rtos"
title: "operation: Scheduler"
summary: "RTX5 implements a low-latency preemptive scheduler. Major parts of RTX5 are executed in handler mode such as"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#scheduler"
license: "Apache-2.0"
mode: "V"
---

RTX5 implements a low-latency preemptive scheduler. Major parts of RTX5 are executed in handler mode such as

- `SysTick_Handler` used for time-based scheduling.
- `SVC_Handler` used for lock-based scheduling.
- `PendSV_Handler` used for interrupt-based scheduling.

In order to be low-latency with respect to ISR execution those system exceptions are configured to use the lowest priority groups available. The priorities are configured such that no preemption happens between them. Thus no interrupt critical sections (i.e. interrupt locks) are needed to protect the scheduler.

(figure: Thread scheduling and interrupt execution)

The scheduler combines priority and round-robin based context switches. The example depicted in the image above contains four threads (1, 2, 3, and 4). Threads 1 and 2 share the same priority, thread 3 has a higher one and thread 4 the highest (osThreadAttr_t::priority). As long as threads 3 and 4 are blocked the scheduler switches between thread 1 and 2 on a time-slice basis (round-robin). The time-slice for round-robin scheduling can be configured, see Round-Robin Timeout in systemConfig.

Thread 2 unblocks thread 3 by an arbitrary RTOS-call (executed in SVC handler mode) at time index 2. The scheduler switches to thread 3 immediately because thread 3 has the highest priority. Thread 4 is still blocked.

At time index 4 an interrupt (ISR) occurs and preempts the `SysTick_Handler`. RTX does not add any latency to the interrupt service execution. The ISR routine uses an RTOS-call that unblocks thread 4. Instead of switching to thread 4 immediately the PendSV flag is set to defer the context switching. The `PendSV_Handler` is executed right after the `SysTick_Handler` returns and the deferred context switch to thread 4 is carried out. As soon as highest priority thread 4 blocks again by using a blocking RTOS-call execution is switched back to thread 3 immediately during time index 5.

At time index 5 thread 3 uses a blocking RTOS-call as well. Thus the scheduler switches back to thread 2 for time index 6.

At time index 7 the scheduler uses the round-robin mechanism to switch to thread 1 and so on.
