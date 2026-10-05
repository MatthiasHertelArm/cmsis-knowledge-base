---
id: "core-overview"
type: "concept"
domain: "core"
title: "Overview"
summary: "The CMSIS-Core (Cortex-M) component implements the basic run-time system for Arm Cortex-M devices and gives the user access to the processor core and the device peripherals."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

The **CMSIS-Core (Cortex-M)** component implements the basic run-time system for Arm Cortex-M devices and gives the user access to the processor core and the device peripherals.

In detail it defines:

 - **Hardware Abstraction Layer (HAL)** for Cortex-M processor registers with standardized  definitions for the SysTick, NVIC, System Control Block registers, MPU registers, FPU registers, and core access functions.
 - **System exception names** to interface to system exceptions without having compatibility issues.
 - **Methods to organize header files** that makes it easy to learn new Cortex-M microcontroller products and improve software portability. This includes naming conventions for device-specific interrupts.
 - **Methods for system initialization** to be used by each MCU vendor. For example, the standardized `SystemInit()` function is essential for configuring the clock system of the device.
 - **Intrinsic functions** used to generate CPU instructions that are not supported by standard C functions.
 - A variable to determine the **system clock frequency** which simplifies the setup the SysTick timer.


The following sections provide details about the CMSIS-Core (Cortex-M):

 - using_pg explains the project setup and shows a simple program example.
\if ARMv8M
 - Using TrustZone® for Armv8-M describes how to use the security extensions available in the Armv8-M architecture.
\endif
 - cmsis_core_files describes the files of the CMSIS-Core (Cortex-M) in detail and explains how to adapt template files provided by Arm to silicon vendor devices.
 - coreMISRA_Exceptions_pg describes the violations to the MISRA standard.
 - [**API Reference**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/modules.html) describes the features and functions of the device_h_pg in detail.
 - [**Data Structures**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/annotated.html) describe the data structures of the device_h_pg in detail.
