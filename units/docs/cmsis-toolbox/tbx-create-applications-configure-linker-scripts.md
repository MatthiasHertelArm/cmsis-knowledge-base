---
id: "tbx-create-applications-configure-linker-scripts"
type: "concept"
domain: "project"
title: "Create Applications: Configure Linker Scripts"
summary: "A linker script file defines the physical memory layout for a .cproject.yml based. It may also allocate specific program sections (for example, DMA buffers or non-volatile variables) to special memory regions."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CreateApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/#configure-linker-scripts"
license: "Apache-2.0"
mode: "V"
---

A *linker script file* defines the physical memory layout for a `*.cproject.yml` based. It may also allocate specific program sections (for example, DMA buffers or non-volatile variables) to special memory regions. While complex devices may use a bespoke linker script to manage multi-core and multi-master bus systems, many single-core devices can use the [automatic linker script generation](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#automatic-linker-script-generation) of the **`csolution` Project Manager** which uses a generic *regions header file* in combination with a toolchain-specific *linker script template*.

The following section describes the usage of a *linker script template* and a *regions header file* which is combined by a C preprocessor into the final *linker script file*. It uses [auto-generated files](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#automatic-linker-script-generation), but the methods also apply somewhat to bespoke linker scripts.

The overall process to configure linker scripts for independent projects is:

1. Step: Review and adjust the physical memory layout in the *regions header file*.
2. Step: Optionally add specific program sections to the *linker script template* or change the default behaviour of that file.

### Regions Header File

An initial *regions header file* is generated based on the memory information coming from the used software packs (DFP and BSP). This file has the name `regions_<device_or_board>.h` and is located in the directory [`./RTE/Device/<device>`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#rte-directory-structure).

For memory with the [*default* attribute set](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory) in DFP or BSP, the following region settings are generated:

- The region \_\_ROM0 is the startup region and contains memory with the [*startup* attribute set](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory).
- The region \_\_RAM0 contains uninitialized memory, STACK and HEAP.
    - STACK default is 0x200.
    - HEAP default is 0xC00 for devices with more than 6KB RAM (otherwise, HEAP is set to 0).
- Contiguous memory with the same access (rw, rwx, rx) is combined into one region.

For memory with the [*default* attribute no set](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory) in DFP or BSP, the memory is listed under **resources that are not allocated to linker regions**.

The user may modify this generated *regions header file*:

- to adapt the physical memory layout of the project.
- to add **not allocated memory resources** to regions \_\_ROM*n* and \_\_RAM*n*.

**Example: `regions_B-U585-IOT02A.h` header file for a board**

```c
#ifndef REGIONS_B_U585I_IOT02A_H
#define REGIONS_B_U585I_IOT02A_H

//-------- <<< Use Configuration Wizard in Context Menu >>> --------------------
//------ With VS Code: Open Preview for Configuration Wizard -------------------

// <n> Auto-generated using information from packs
// <i> Device Family Pack (DFP):   Keil::STM32U5xx_DFP@3.0.0-dev0
// <i> Board Support Pack (BSP):   Keil::B-U585I-IOT02A_BSP@2.0.0-dev0

// <h> ROM Configuration
// =======================
// <h> __ROM0 (is rx memory: Flash from DFP)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region. Default: 0x08000000
//   <i> Contains Startup and Vector Table
#define __ROM0_BASE 0x08000000
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region. Default: 0x00200000
#define __ROM0_SIZE 0x00200000
// </h>

// <h> __ROM1 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __ROM1_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __ROM1_SIZE 0
// </h>

// <h> __ROM2 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __ROM2_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __ROM2_SIZE 0
// </h>

// <h> __ROM3 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __ROM3_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __ROM3_SIZE 0
// </h>

// </h>

// <h> RAM Configuration
// =======================
// <h> __RAM0 (is rwx memory: SRAM1_2 from DFP)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region. Default: 0x20000000
//   <i> Contains uninitialized RAM, Stack, and Heap
#define __RAM0_BASE 0x20000000
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region. Default: 0x00040000
#define __RAM0_SIZE 0x00040000
// </h>

// <h> __RAM1 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __RAM1_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __RAM1_SIZE 0
// </h>

// <h> __RAM2 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __RAM2_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __RAM2_SIZE 0
// </h>

// <h> __RAM3 (unused)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region.
#define __RAM3_BASE 0
//   <o> Region size [bytes] <0x0-0xFFFFFFFF:8>
//   <i> Defines size of memory region.
#define __RAM3_SIZE 0
// </h>

// </h>

// <h> Stack / Heap Configuration
//   <o0> Stack Size (in Bytes) <0x0-0xFFFFFFFF:8>
//   <o1> Heap Size (in Bytes) <0x0-0xFFFFFFFF:8>
#define __STACK_SIZE 0x00000200
#define __HEAP_SIZE 0x00000C00
// </h>

// <n> Resources that are not allocated to linker regions
// <i> rwx RAM:  SRAM3 from DFP:           BASE: 0x20040000  SIZE: 0x00080000
// <i> rwx RAM:  RAM-External from BSP:    BASE: 0x90000000  SIZE: 0x00800000
// <i> rx ROM:   Flash-External from BSP:  BASE: 0x70000000  SIZE: 0x04000000

#endif /* REGIONS_B_U585I_IOT02A_H */
```

### Linker Script Template

A [template *linker script file*](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#linker-script-templates) is copied to the directory [`./RTE/Device/<device>`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#rte-directory-structure). The user may modify this file:

- to specify program sections that require dedicated physical memory regions.
- to change the allocation behaviour of the linker script.

**Example: DMA section allocation in `ac6_linker_script.sct.src` linker script template**

```c
#if __RAM1_SIZE > 0
  RW_RAM1 __RAM2_BASE __RAM2_SIZE  {
    *(.RxDecripSection)               // added DMA descriptors
    *(.TxDecripSection)
    *(.driver.eth_mac0_rx_buf)
    *(.driver.eth_mac0_tx_buf)
   .ANY (+RW +ZI)
  }
#endif
```

!!! Note
    It is recommended to add a note to the *regions header file* about such user modifications as shown below:

```c
// <h> __RAM1 (is rwx memory: SRAM3 from DFP)
//   <o> Base address <0x0-0xFFFFFFFF:8>
//   <i> Defines base address of memory region. Default: 0x20040000
//   <i> Note: DMA descriptors and buffers are in this region
```
