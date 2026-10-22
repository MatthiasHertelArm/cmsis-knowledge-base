---
id: "zep-virtual-memory-memory-map-overview"
type: "concept"
domain: "rtos"
title: "Virtual Memory: Memory Map Overview"
summary: "This is an overview of the memory map of the virtual memory address space. Note that the Z macros, which are used in code, may have different meanings depending on architecture and Kconfigs, which will be explained below."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/virtual_memory.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/virtual_memory.rst"
license: "Apache-2.0"
mode: "V"
---

This is an overview of the memory map of the virtual memory address space.
Note that the `Z_*` macros, which are used in code, may have different
meanings depending on architecture and Kconfigs, which will be explained
below.

```none

+--------------+ <- K_MEM_VIRT_RAM_START
| Undefined VM | <- architecture specific reserved area
+--------------+ <- K_MEM_KERNEL_VIRT_START
| Mapping for  |
| main kernel  |
| image        |
|              |
|              |
+--------------+ <- K_MEM_VM_FREE_START
|              |
| Unused,      |
| Available VM |
|              |
|..............| <- grows downward as more mappings are made
| Mapping      |
+--------------+
| Mapping      |
+--------------+
| ...          |
+--------------+
| Mapping      |
+--------------+ <- memory mappings start here
| Reserved     | <- special purpose virtual page(s) of size K_MEM_VM_RESERVED
+--------------+ <- K_MEM_VIRT_RAM_END
```
* `K_MEM_VIRT_RAM_START` is the beginning of the virtual memory address space.
  This needs to be page aligned. Currently, it is the same as
  `CONFIG_KERNEL_VM_BASE`.

* `K_MEM_VIRT_RAM_SIZE` is the size of the virtual memory address space.
  This needs to be page aligned. Currently, it is the same as
  `CONFIG_KERNEL_VM_SIZE`.

* `K_MEM_VIRT_RAM_END` is simply (`K_MEM_VIRT_RAM_START` + `K_MEM_VIRT_RAM_SIZE`).

* `K_MEM_KERNEL_VIRT_START` is the same as `z_mapped_start` specified in the linker
  script. This is the virtual address of the beginning of the kernel image at
  boot time.

* `K_MEM_KERNEL_VIRT_END` is the same as `z_mapped_end` specified in the linker
  script. This is the virtual address of the end of the kernel image at boot time.

* `K_MEM_VM_FREE_START` is the beginning of the virtual address space where addresses
  can be allocated for memory mapping. This depends on whether
  `CONFIG_ARCH_MAPS_ALL_RAM` is enabled.

  * If it is enabled, which means all physical memory are mapped in virtual
    memory address space, and it is the same as
    (`DT_CHOSEN_SRAM_ADDR` + `DT_CHOSEN_SRAM_SIZE`).

  * If it is disabled, `K_MEM_VM_FREE_START` is the same `K_MEM_KERNEL_VIRT_END` which
    is the end of the kernel image.

* `K_MEM_VM_RESERVED` is an area reserved to support kernel functions. For example,
  some addresses are reserved to support demand paging.
