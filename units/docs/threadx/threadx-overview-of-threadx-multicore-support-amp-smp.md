---
id: "threadx-overview-of-threadx-multicore-support-amp-smp"
type: "concept"
domain: "rtos"
title: "Overview of ThreadX: Multicore support (AMP & SMP)"
summary: "Standard ThreadX is often used in an Asymmetric Multiprocessing (AMP) fashion, where a separate copy of ThreadX and the application (or Linux) executes on each core and communicate with each other via shared memory or an inter-processor communication …"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/overview-threadx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/overview-threadx.md#multicore-support-amp-smp"
license: "MIT"
mode: "V"
---

Standard ThreadX is often used in an Asymmetric Multiprocessing (AMP) fashion, where a separate copy of ThreadX and the application (or Linux) executes on each core and communicate with each other via shared memory or an inter-processor communication mechanism such as OpenAMP (ThreadX supports OpenAMP).

In environments where loading processors is highly dynamic, ThreadX Symmetric Multiprocessing (SMP) is available for the following processor families:

* ARM Cortex-Ax
* ARM Cortex-Rx
* ARM Cortex-A5x 64-bit
* Synopsys ARC HS

ThreadX SMP performs dynamic load balancing across *n* processors. It allows all ThreadX resources (queues, semaphores, event flags, memory pools, etc.) to be accessed by any thread on any core. ThreadX SMP enables the complete ThreadX API on all cores and introduces the following new APIs applicable to SMP operation:

* `UINT tx_thread_smp_core_exclude(TX_THREAD *thread_ptr, ULONG exclusion_map);`
* `UINT tx_thread_smp_core_exclude_get(TX_THREAD *thread_ptr, ULONG *exclusion_map_ptr);`
* `UINT tx_thread_smp_core_get(void);`
* `UINT tx_timer_smp_core_exclude(TX_TIMER *timer_ptr, ULONG exclusion_map);`
* `UINT tx_timer_smp_core_exclude_get(TX_TIMER *timer_ptr, ULONG *exclusion_map_ptr);`
