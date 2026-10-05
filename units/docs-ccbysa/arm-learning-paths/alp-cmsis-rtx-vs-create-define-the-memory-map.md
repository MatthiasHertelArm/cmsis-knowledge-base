---
id: "alp-cmsis-rtx-vs-create-define-the-memory-map"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Create csolution project: Define the memory map"
summary: "Use scatter-loading to define the memory map to the linker."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create/#define-the-memory-map"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map to the linker.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

The project should be configured to use `ARMCM4_ac6.sct` as the scatter file. Locate this file in the CMSIS Extension view and select it to create.

Populate with the following.

```text
LOAD 0x0 0x400000 {
	ROOT 0x0 0x400000 {
		*.o (RESET, +First)
		*(InRoot$$Sections)
		.ANY (+RO)   }

	RAM 0x20000000 0x40000 {
		.ANY (+RW +ZI)     }

	ARM_LIB_HEAP  0x20040000 EMPTY 0x10000 {}

	ARM_LIB_STACK 0x20050000 EMPTY 0x10000 {}
}
```
