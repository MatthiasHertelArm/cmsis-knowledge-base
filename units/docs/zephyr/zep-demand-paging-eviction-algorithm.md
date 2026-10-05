---
id: "zep-demand-paging-eviction-algorithm"
type: "concept"
domain: "rtos"
title: "Demand Paging: Eviction Algorithm"
summary: "The eviction algorithm is used to determine which data page and its corresponding page frame can be paged out to free up a page frame for the next page in operation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/demand_paging.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/demand_paging.rst"
license: "Apache-2.0"
mode: "V"
---

The eviction algorithm is used to determine which data page and its
corresponding page frame can be paged out to free up a page frame
for the next page in operation. There are four functions which are
called from the kernel paging code:

* `k_mem_paging_eviction_init()` is called to initialize
  the eviction algorithm. This is called at `POST_KERNEL`.

* `k_mem_paging_eviction_add()` is called each time a data page becomes
  eligible for future eviction.

* `k_mem_paging_eviction_remove()` is called when a data page is no
  longer eligible for eviction. This may happen if the given data page becomes
  pinned, gets unmapped or is about to be evicted.

* `k_mem_paging_eviction_select()` is called to select
  a data page to evict. A function argument `dirty` is written to
  signal the caller whether the selected data page has been modified
  since it is first paged in. If the `dirty` bit is returned
  as set, the paging code signals to the backing store to write
  the data page back into storage (thus updating its content).
  The function returns a pointer to the page frame corresponding to
  the selected data page.

There is one additional function which is called by the architecture's memory
management code to flag data pages when they trigger an access fault:
`k_mem_paging_eviction_accessed()`. This is used by the LRU algorithm
to requeue "used" pages.

Two eviction algorithms are currently available:

* An NRU (Not-Recently-Used) eviction algorithm has been implemented as a
  sample. This is a very simple algorithm which ranks data pages on whether
  they have been accessed and modified. The selection is based on this ranking.

* An LRU (Least-Recently-Used) eviction algorithm is also available. It is
  based on a sorted queue of data pages. The LRU code is more complex compared
  to the NRU code but also considerably more efficient. This is recommended for
  production use.

To implement a new eviction algorithm, `k_mem_paging_eviction_init()`
and `k_mem_paging_eviction_select()` must be implemented.
If `CONFIG_EVICTION_TRACKING` is enabled for an algorithm,
these additional functions must also be implemented,
`k_mem_paging_eviction_add()`, `k_mem_paging_eviction_remove()`,
`k_mem_paging_eviction_accessed()`.
