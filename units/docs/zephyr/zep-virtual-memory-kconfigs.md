---
id: "zep-virtual-memory-kconfigs"
type: "concept"
domain: "rtos"
title: "Virtual Memory: Kconfigs"
summary: "These are the Kconfigs that need to be enabled or defined for kernel to support virtual memory."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/virtual_memory.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/virtual_memory.rst"
license: "Apache-2.0"
mode: "V"
---

### Required


These are the Kconfigs that need to be enabled or defined for kernel to support
virtual memory.

* `CONFIG_MMU`: must be enabled for virtual memory support in
  kernel.

* `CONFIG_MMU_PAGE_SIZE`: size of a memory page. Default is 4KB.

* `CONFIG_KERNEL_VM_BASE`: base address of virtual address space.

* `CONFIG_KERNEL_VM_SIZE`: size of virtual address space.
  Default is 8MB.

* `CONFIG_KERNEL_VM_OFFSET`: kernel image starts at this offset
  from `CONFIG_KERNEL_VM_BASE`.


### Optional


* `CONFIG_KERNEL_DIRECT_MAP`: permits 1:1 mappings between
  virtual and physical addresses, instead of kernel choosing addresses within
  the virtual address space. This is useful for mapping device MMIO regions for
  more precise access control.
