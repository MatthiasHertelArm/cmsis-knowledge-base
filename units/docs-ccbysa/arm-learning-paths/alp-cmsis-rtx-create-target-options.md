---
id: "alp-cmsis-rtx-create-target-options"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create and setup Keil MDK project: Target options"
summary: "Click Options for Target, to open that dialog. This is where build and other settings can be made."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create/#target-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

Click `Options for Target`, to open that dialog. This is where build and other settings can be made.

### Set FVP as debug target


### Configure the FVP

In the `Debug` tab, select `Models Cortex-M Debugger`. Click `Settings`, and browse for the FVP provided with MDK in the `Command` pane.
```
Keil_v5/ARM/avh-fvp/bin/models/FVP_MPS2_Cortex-M4_MDK.exe
```

**Note:**
MDK versions 5.37 and earlier will find the FVP at:

`Keil_v5/ARM/FVP/MPS2_Cortex-M/FVP_MPS2_Cortex-M4_MDK.exe`

In 5.38 and 5.39 the FVP is installed at:

`Keil_v5/ARM/VHT/VHT_MPS2_Cortex-M4_MDK.exe`

In 5.40 and later the FVP is installed at:

`Keil_v5/ARM/avh-fvp/bin/models/FVP_MPS2_Cortex-M4_MDK.exe`


**Arm Development Studio:**
Ignore this step for now. Debug configuration will be set up later.


### Compiler optimization options

Navigate to `C/C++ (AC6)` tab, and (optionally) change optimization level to `-O2` for high performance code.
You may also wish to disable Warnings, change language options, or other settings.

### Define memory map

Use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map to the linker.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

Navigate to the `Linker` tab, and de-select `Use Memory Layout from Target Dialog` (as you shall create your own).

Click the browse (`...`) button and create a text file in the same folder as the project.

Click `Edit` to open the file in the IDE. The following is a typical scatter file for the FVP.
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
**Arm Development Studio:**
The IDE recognizes `.sct` files as scatter files, and provides a graphical representation of the layout in a `Memory Map` tab.
