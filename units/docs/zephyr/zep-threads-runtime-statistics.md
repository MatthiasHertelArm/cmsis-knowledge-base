---
id: "zep-threads-runtime-statistics"
type: "concept"
domain: "rtos"
title: "Threads: Runtime Statistics"
summary: "Thread runtime statistics can be gathered and retrieved if CONFIG_THREAD_RUNTIME_STATS is enabled, for example, total number of execution cycles of a thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

Thread runtime statistics can be gathered and retrieved if
`CONFIG_THREAD_RUNTIME_STATS` is enabled, for example, total number of
execution cycles of a thread.

By default, the runtime statistics are gathered using the default kernel
timer. For some architectures, SoCs or boards, there are timers with higher
resolution available via timing functions. Using of these timers can be
enabled via `CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS`.

Here is an example:

```c

k_thread_runtime_stats_t rt_stats_thread;

k_thread_runtime_stats_get(k_current_get(), &rt_stats_thread);

printk("Cycles: %llu\n", rt_stats_thread.execution_cycles);
```
The combined statistics for every thread in the system can be retrieved with
`k_thread_runtime_stats_all_get`, which reports the aggregate runtime
usage across all threads (including the idle thread). This is useful for
computing overall CPU utilization.

When `CONFIG_SCHED_THREAD_USAGE` is enabled, statistics
collection can be toggled at run time on a per-thread basis with
`k_thread_runtime_stats_enable` and
`k_thread_runtime_stats_disable`. Whether collection is currently active
for a thread can be checked with `k_thread_runtime_stats_is_enabled`.
Disabling collection for threads that do not need to be measured reduces the
bookkeeping overhead incurred on each context switch.
