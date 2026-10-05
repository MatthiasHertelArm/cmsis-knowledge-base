---
id: "zep-symmetric-multiprocessing-cpu-mask"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing: CPU Mask"
summary: "It is often desirable for real time applications to deliberately partition work across physical CPUs instead of relying solely on the kernel scheduler to decide on which threads to execute."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

It is often desirable for real time applications to deliberately
partition work across physical CPUs instead of relying solely on the
kernel scheduler to decide on which threads to execute.  Zephyr
provides an API, controlled by the `CONFIG_SCHED_CPU_MASK`
kconfig variable, which can associate a specific set of CPUs with each
thread, indicating on which CPUs it can run.

By default, new threads can run on any CPU.  Calling
`k_thread_cpu_mask_disable` with a particular CPU ID will prevent
that thread from running on that CPU in the future.  Likewise
`k_thread_cpu_mask_enable` will re-enable execution.  There are also
`k_thread_cpu_mask_clear` and `k_thread_cpu_mask_enable_all` APIs
available for convenience.  For obvious reasons, these APIs are
illegal if called on a runnable thread.  The thread must be blocked or
suspended, otherwise an `-EINVAL` will be returned.

CPU mask filtering is supported with all three scheduler backends.
The performance impact differs by backend:

- `CONFIG_SCHED_SIMPLE` — O(N) linear scan of the run
  queue; every context switch walks the full list looking for the
  first eligible thread.
- `CONFIG_SCHED_SCALABLE` — O(N) in-order walk of the
  red/black tree; priority ordering is preserved but the full tree
  may be traversed when many threads are masked off.
- `CONFIG_SCHED_MULTIQ` — scans priority buckets
  from highest to lowest and walks the per-bucket list; worst case
  is O(P·N) where P is the number of occupied priority levels.

For workloads that use `CONFIG_SCHED_CPU_MASK_PIN_ONLY`,
each CPU maintains its own independent run queue, so the scheduler
needs only examine that queue with no mask filtering overhead.

Note that `k_thread_cpu_mask_clear`,
`k_thread_cpu_mask_enable_all`, and
`k_thread_cpu_mask_disable` are not permitted in
`CONFIG_SCHED_CPU_MASK_PIN_ONLY` mode because they can
produce a mask that is not exactly one bit, which violates the
invariant that every thread is pinned to precisely one CPU.
