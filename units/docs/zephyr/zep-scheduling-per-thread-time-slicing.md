---
id: "zep-scheduling-per-thread-time-slicing"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Per-Thread Time Slicing"
summary: "The time slice configured with k_sched_time_slice_set applies globally to every preemptible thread at or below a given priority. When CONFIG_TIMESLICE_PER_THREAD is enabled, an individual thread can instead be given its own time slice with k_thread_time_slice_set."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

The time slice configured with `k_sched_time_slice_set` applies globally
to every preemptible thread at or below a given priority. When
`CONFIG_TIMESLICE_PER_THREAD` is enabled, an individual thread
can instead be given its own time slice with `k_thread_time_slice_set`.
A per-thread slice takes precedence over the global value, and is applied even to
threads whose priority is above the global time-slicing limit.

In addition to a slice duration (expressed in ticks), a per-thread slice
registers a callback that the kernel invokes when the slice expires. This
callback runs in interrupt context while the affected thread is still the current
thread, and may, for example, adjust the thread's priority or slice for its next
execution, or suspend it.
