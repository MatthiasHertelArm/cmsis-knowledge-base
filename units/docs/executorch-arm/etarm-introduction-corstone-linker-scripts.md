---
id: "etarm-introduction-corstone-linker-scripts"
type: "concept"
domain: "edge-ai"
title: "Introduction: Corstone linker scripts"
summary: "The linker scripts point to the linker where to place various objects in memory when the application is loaded onto the target. In the arm_executor_runner.cpp application, we reuse the linker scripts from the core-platform project."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/ethos-u-porting-guide.md#corstone-linker-scripts"
license: "BSD-3-Clause"
mode: "V"
---

The linker scripts point to the linker where to place various objects in memory when the application is loaded onto the target.
In the `arm_executor_runner.cpp` application, we reuse the linker scripts from the core-platform project. Note that the Global Offset Table(.got symbols) needs to be 16-byte aligned. The linker scripts are highly specific to the memory map of system.
For example on the Corstone-300,  in order to allow us to build a lot of portable kernels, we relocate the portable kernels from the .text section, living in the ITCM, to a bigger memory.  Also on the Corstone-300. the linker script defines two
load regions- rom_exec and rom_dram corresponding to loading the application in the ITCM and in the DDR. When you deploy the application, the boot loader copies the two binaries from the rom_exec/rom_dram regions to their physical address in memory -
a process known as scatter loader. Upon powering on the device, the very first instruction that the Cortex-M executes is the ResetHandler function. The ResetHandler is the first entry in the Vector Interrupt Table, and the location of the Vector Interrupt 
Table is specified in the linker script(the `KEEP(*(.vectors))` symbol). The assembly boot code powering on the Cortex-M is itself defined in `core_software/cmsis_6/CMSIS/CoreValidation/Layer/Target/CM55S/RTE/Device/ARMCM55/startup_ARMCM55.c`.
The CMSIS start-up code for Cortex-M is added as part of the build system of the core-platform applications.
