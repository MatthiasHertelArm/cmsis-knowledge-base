---
id: "zep-virtual-memory"
type: "concept"
domain: "rtos"
title: "Virtual Memory"
summary: "Virtual memory (VM) in Zephyr provides developers with the ability to fine tune access to memory. To utilize virtual memory, the platform must support Memory Management Unit (MMU) and it must be enabled in the build."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/virtual_memory.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/virtual_memory.rst"
license: "Apache-2.0"
mode: "V"
---

Virtual memory (VM) in Zephyr provides developers with the ability to fine tune
access to memory. To utilize virtual memory, the platform must support
Memory Management Unit (MMU) and it must be enabled in the build. Due to
the target of Zephyr mainly being embedded systems, virtual memory
support in Zephyr differs a bit from that in traditional operating
systems:

Mapping of Kernel Image
  Default is to do 1:1 mapping for the kernel image (including code and data)
  between physical and virtual memory address spaces, if demand paging
  is not enabled. Deviation from this requires careful manipulation of
  linker script.

Secondary Storage
  Basic virtual memory support does not utilize secondary storage to
  extend usable memory. The maximum usable memory is the same as
  the physical memory.

  * memory_management_api_demand_paging enables utilizing
    secondary storage as a backing store for virtual memory, thus
    allowing larger usable memory than the available physical memory.
    Note that demand paging needs to be explicitly enabled.

  * Although the virtual memory space can be larger than physical
    memory space, without enabling demand paging, all virtually
    mapped memory must be backed by physical memory.
