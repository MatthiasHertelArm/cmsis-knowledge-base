---
id: "zep-demand-paging-paging-statistics"
type: "concept"
domain: "rtos"
title: "Demand Paging: Paging Statistics"
summary: "Paging statistics can be obtained via various function calls when CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS is enabled:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/demand_paging.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/demand_paging.rst"
license: "Apache-2.0"
mode: "V"
---

Paging statistics can be obtained via various function calls when
`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS` is enabled:

* Overall statistics via `k_mem_paging_stats_get()`

* Per-thread statistics via `k_mem_paging_thread_stats_get()`
  if `CONFIG_DEMAND_PAGING_THREAD_STATS` is enabled

* Execution time histogram can be obtained when
  `CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM` is enabled, and
  `CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS` is defined.
  Note that the timing is highly dependent on the architecture,
  SoC or board. It is highly recommended that
  `k_mem_paging_eviction_histogram_bounds[]` and
  `k_mem_paging_backing_store_histogram_bounds[]`
  be defined for a particular application.

  * Execution time histogram of eviction algorithm via
    `k_mem_paging_histogram_eviction_get()`

  * Execution time histogram of backing store doing page-in via
    `k_mem_paging_histogram_backing_store_page_in_get()`

  * Execution time histogram of backing store doing page-out via
    `k_mem_paging_histogram_backing_store_page_out_get()`
