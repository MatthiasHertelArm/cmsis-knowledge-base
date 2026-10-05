---
id: "zep-demand-paging-backing-store"
type: "concept"
domain: "rtos"
title: "Demand Paging: Backing Store"
summary: "Backing store is responsible for paging in/out data page between their corresponding page frames and storage. These are the functions which must be implemented:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/demand_paging.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/demand_paging.rst"
license: "Apache-2.0"
mode: "V"
---

Backing store is responsible for paging in/out data page between
their corresponding page frames and storage. These are the functions
which must be implemented:

* `k_mem_paging_backing_store_init()` is called to
  initialized the backing store at `POST_KERNEL`.

* `k_mem_paging_backing_store_location_get()` is called to
  reserve a backing store location so a data page can be paged out.
  This `location` token is passed to
  `k_mem_paging_backing_store_page_out()` to perform actual
  page out operation.

* `k_mem_paging_backing_store_location_free()` is called to
  free a backing store location (the `location` token) which can
  then be used for subsequent page out operation.

* `k_mem_paging_backing_store_location_query()` is called to obtain
  the `location` token corresponding to storage content to be virtually
  mapped and paged-in on demand. Most useful with
  `CONFIG_DEMAND_MAPPING`.

* `k_mem_paging_backing_store_page_in()` copies a data page
  from the backing store location associated with the provided
  `location` token to the page pointed by `K_MEM_SCRATCH_PAGE`.

* `k_mem_paging_backing_store_page_out()` copies a data page
  from `K_MEM_SCRATCH_PAGE` to the backing store location associated
  with the provided `location` token.

* `k_mem_paging_backing_store_page_finalize()` is invoked after
  `k_mem_paging_backing_store_page_in()` so that the page frame
  struct may be updated for internal accounting. This can be
  a no-op.

To implement a new backing store, the functions mentioned above
must be implemented.
`k_mem_paging_backing_store_page_finalize()` can be an empty
function if so desired.
