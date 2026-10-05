---
id: "zep-virtual-memory-virtual-memory-mappings"
type: "concept"
domain: "rtos"
title: "Virtual Memory: Virtual Memory Mappings"
summary: "In general, most supported architectures set up the memory mappings at boot as following:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/virtual_memory.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/virtual_memory.rst"
license: "Apache-2.0"
mode: "V"
---

### Setting up Mappings at Boot


In general, most supported architectures set up the memory mappings at boot as
following:

* `.text` section is read-only and executable. It is accessible in
  both kernel and user modes.

* `.rodata` section is read-only and non-executable. It is accessible
  in both kernel and user modes.

* Other kernel sections, such as `.data`, `.bss` and `.noinit`, are
  read-write and non-executable. They are only accessible in kernel mode.

  * Stacks for user mode threads are automatically granted read-write access
    to their corresponding user mode threads during thread creation.

  * Global variables, by default, are not accessible to user mode threads.
    Refer to Memory Domains and Partitions on how to
    use global variables in user mode threads, and on how to share data
    between user mode threads.

Caching modes for these mappings are architecture specific. They can be
none, write-back, or write-through.

Note that SoCs have their own additional mappings required to boot where
these mappings are defined under their own SoC configurations. These mappings
usually include device MMIO regions needed to setup the hardware.



### Mapping Anonymous Memory


The unused physical memory can be mapped in virtual address space on demand.
This is conceptually similar to memory allocation from heap, but these
mappings must be aligned on page size and have finer access control.

* `k_mem_map` can be used to map unused physical memory:

  * The requested size must be multiple of page size.

  * The address returned is inside the virtual address space between
    `K_MEM_VM_FREE_START` and `K_MEM_VIRT_RAM_END`.

  * The mapped region is not guaranteed to be physically contiguous in memory.

  * Guard pages immediately before and after the mapped virtual region are
    automatically allocated to catch access issue due to buffer underrun
    or overrun.

* The mapped region can be unmapped (i.e. freed) via `k_mem_unmap`:

  * Caution must be exercised to give the pass the same region size to
    both `k_mem_map` and `k_mem_unmap`. The unmapping
    function does not check if it is a valid mapped region before unmapping.
