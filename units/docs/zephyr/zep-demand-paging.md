---
id: "zep-demand-paging"
type: "concept"
domain: "rtos"
title: "Demand Paging"
summary: "Demand paging provides a mechanism where data is only brought into physical memory as required by current execution context. The physical memory is conceptually divided in page-sized page frames as regions to hold data."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/demand_paging.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/demand_paging.rst"
license: "Apache-2.0"
mode: "V"
---

Demand paging provides a mechanism where data is only brought into physical
memory as required by current execution context. The physical memory is
conceptually divided in page-sized page frames as regions to hold data.

The Zephyr kernel image itself is always resident in physical memory and is
never a candidate for eviction. Demand paging applies only to:

* anonymous memory mappings created at runtime via `k_mem_map()`, and
* memory placed in explicit on-demand linker sections via the
  `__ondemand_func` / `__ondemand_rodata` attributes when
  `CONFIG_LINKER_USE_ONDEMAND_SECTION` is enabled.

This is the same model used by every major operating system: the dispatch
path for an exception or interrupt is never on a pageable page, so a fault
during fault-handling is impossible by construction. Code or data added to
an `__ondemand_*` section is the contributor's explicit opt-in to make
that region pageable, and carries the responsibility of ensuring it is not
reached from the page-fault handler's own execution path.


**Note:** Earlier versions of Zephyr also supported a selective-pinning scheme based on `__pinned_* linker attributes that kept only the tagged subset of the kernel image resident and demand-paged the rest. That model was found to be both unsafe and/or very invasive: a CPU exception dispatch could target a thread's privileged stack on an evictable page, escalating to a double fault on x86 or a nested abort on ARM64 if that page had been evicted; and the contract that every byte on the fault-handler-reachable surface (scheduler, drivers, libc, locking primitives) be exhaustively tagged was impractical to establish once and unmaintainable thereafter. The pinned_*` attribute family, the corresponding Kconfig options (`LINKER_USE_PINNED_SECTION` / `LINKER_GENERIC_SECTIONS_PRESENT_AT_BOOT`) and the `K_*_PINNED_STACK_*` stack macros were removed in Zephyr 4.4. See `108773` for the full analysis.

* When the processor tries to access data and the data page exists in
  one of the page frames, the execution continues without any interruptions.

* When the processor tries to access the data page that does not exist
  in any page frames, a page fault occurs. The paging code then brings in
  the corresponding data page from backing store into physical memory if
  there is a free page frame. If there is no more free page frames,
  the eviction algorithm is invoked to select a data page to be paged out,
  thus freeing up a page frame for new data to be paged in. If this data
  page has been modified after it is first paged in, the data will be
  written back into the backing store. If no modifications is done or
  after written back into backing store, the data page is now considered
  paged out and the corresponding page frame is now free. The paging code
  then invokes the backing store to page in the data page corresponding to
  the location of the requested data. The backing store copies that data
  page into the free page frame. Now the data page is in physical memory
  and execution can continue.

There are functions where paging in and out can be invoked manually
using `k_mem_page_in()` and `k_mem_page_out()`.
`k_mem_page_in()` can be used to page in data pages
in anticipation that they are required in the near future. This is used to
minimize number of page faults as these data pages are already in physical
memory, and thus minimizing latency. `k_mem_page_out()` can be
used to page out data pages where they are not going to be accessed for
a considerable amount of time. This frees up page frames so that the next
page in can be executed faster as the paging code does not need to invoke
the eviction algorithm.

A data region can also be **pinned** in physical memory using
`k_mem_pin()`. This pages the region in if necessary and marks its page
frames so that the eviction algorithm will never select them, guaranteeing that
the region remains resident and that accesses to it never fault. This is a
stronger form of `k_mem_page_in()` and is appropriate for latency- or
safety-critical data that must always be available. A pinned region is later
released with `k_mem_unpin()`, which marks the page frames as evictable
again; unpinning does not itself evict the region, so it may be followed by
`k_mem_page_out()` if immediate eviction is desired.
