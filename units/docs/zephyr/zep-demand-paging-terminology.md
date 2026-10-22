---
id: "zep-demand-paging-terminology"
type: "concept"
domain: "rtos"
title: "Demand Paging: Terminology"
summary: "Data Page A data page is a page-sized region of data. It may exist in a page frame, or be paged out to some backing store."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/demand_paging.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/demand_paging.rst"
license: "Apache-2.0"
mode: "V"
---

Data Page
  A data page is a page-sized region of data. It may exist in a page frame,
  or be paged out to some backing store. Its location can always be looked
  up in the CPU's page tables (or equivalent) by virtual address.
  The data type will always be `void *` or in some cases `uint8_t *`
  when doing pointer arithmetic.

Page Frame
  A page frame is a page-sized physical memory region in RAM. It is a
  container where a data page may be placed. It is always referred to by
  physical address. Zephyr has a convention of using `uintptr_t` for physical
  addresses. For every page frame, a `struct k_mem_page_frame` is instantiated to
  store metadata. Flags for each page frame:

  * `K_MEM_PAGE_FRAME_FREE` indicates a page frame is unused and on the list of
    free page frames. When this flag is set, none of the other flags are
    meaningful and they must not be modified.

  * `K_MEM_PAGE_FRAME_PINNED` indicates a page frame is pinned in memory
    and should never be paged out.

  * `K_MEM_PAGE_FRAME_RESERVED` indicates a physical page reserved by hardware
    and should not be used at all.

  * `K_MEM_PAGE_FRAME_MAPPED` is set when a physical page is mapped to
    virtual memory address.

  * `K_MEM_PAGE_FRAME_BUSY` indicates a page frame is currently involved in
    a page-in/out operation.

  * `K_MEM_PAGE_FRAME_BACKED` indicates a page frame has a clean copy
    in the backing store.

K_MEM_SCRATCH_PAGE
  The virtual address of a special page provided to the backing store to:
  * Copy a data page from `k_MEM_SCRATCH_PAGE` to the specified location; or,
  * Copy a data page from the provided location to `K_MEM_SCRATCH_PAGE`.
  This is used as an intermediate page for page in/out operations. This
  scratch needs to be mapped read/write for backing store code to access.
  However the data page itself may only be mapped as read-only in virtual
  address space. If this page is provided as-is to backing store,
  the data page must be re-mapped as read/write which has security
  implications as the data page is no longer read-only to other parts of
  the application.
