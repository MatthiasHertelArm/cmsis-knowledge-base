---
id: "threadx-overview-of-threadx-advanced-technology"
type: "concept"
domain: "rtos"
title: "Overview of ThreadX: Advanced technology"
summary: "ThreadX is notable for its preemption-threshold scheduling. This feature is unique to ThreadX and has been the subject of extensive academic research."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/overview-threadx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/overview-threadx.md#advanced-technology"
license: "MIT"
mode: "V"
---

ThreadX is notable for its preemption-threshold scheduling. This feature is unique to ThreadX and has been the subject of extensive academic research. You can learn more from the paper [Scheduling Fixed-Priority Tasks with Preemption Threshold](https://ieeexplore.ieee.org/document/811269), by Yun Wang (Concordia University) and Manas Saksena (University of Pittsburgh).

Key capabilities of ThreadX:

* Complete and Comprehensive Multitasking Facilities
  * Threads, application timers, message queues, counting semaphores, mutexes, event flags, block, and byte memory pools
* Priority-Based Preemptive Scheduling
* Priority Flexibility – Up to 1024 Priority Levels
* Cooperative Scheduling
* Preemption-Threshold – Unique to ThreadX, helps reduce context switches and help guarantee schedulability (per academic research)
* Memory Protection via ThreadX MODULES
* Fully Deterministic
* Event Trace – Capture last *n* system/application events
* Event Chaining – Register an application-specific "notify" callback function for each ThreadX communication or synchronization object
* ThreadX MODULES with Optional Memory Protection
* Run-Time Performance Metrics
  * Number of thread resumptions
  * Number of thread suspensions
  * Number of solicited thread pre-emptions
  * Number of asynchronous thread interrupt pre-emptions
  * Number of thread priority inversions
  * Number of thread relinquishes
* Execution Profile Kit (EPK)
* Separate Interrupt Stack
* Run-Time Stack Analysis
* Optimized Timer Interrupt Processing
