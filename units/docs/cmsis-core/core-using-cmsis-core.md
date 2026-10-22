---
id: "core-using-cmsis-core"
type: "concept"
domain: "core"
title: "Using CMSIS-Core"
summary: "To use the CMSIS-Core (Cortex-M) in an embedded software project at the following cmsis_device_files need to be added to the application:"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/using.md"
license: "Apache-2.0"
mode: "V"
---

To use the CMSIS-Core (Cortex-M) in an embedded software project at the following cmsis_device_files need to be added to the application:

 - startup_c_pg with reset handler and exception vectors.
 - system_c_pg with general device configuration (i.e. for clock and BUS setup).
 - device_h_pg gives access to processor core and all peripherals.

(figure: Using CMSIS-Core (Cortex-M) in a project)

The startup_c_pg is executed after reset and calls `SystemInit()` in the reset hander. After the system initialization the control is transferred to the C/C++ run-time library which performs initialization and calls the `main` function in the user code. In addition the startup_c_pg contains all exception and interrupt vectors and implements a default function for every interrupt. It may also contain stack and heap configurations for the user application.

The system_c_pg performs the setup for the processor clock. The variable SystemCoreClock indicates the CPU clock speed. In addition the file may contain functions for the memory BUS setup and clock re-configuration.

> **Note**
> - The files startup_c_pg and system_c_pg may require application specific adaptations and therefore should be copied into the application project folder prior configuration.

The device_h_pg provides access to the following device-specific functionalities:

 - peripheral_gr provides a standardized register layout for all peripherals. Optionally functions for device-specific peripherals may be available.
 - NVIC_gr can be accessed with standardized symbols and functions for the Nested Interrupt Vector Controller (NVIC) are provided.
 - intrinsic_CPU_gr allow to access special instructions, for example for activating sleep mode or the NOP instruction.
 - intrinsic_SIMD_gr provide access to the DSP-oriented instructions.
 - SysTick_gr function to configure and start a periodic timer interrupt.
 - ITM_Debug_gr are functions that allow printf-style I/O via the CoreSight Debug Unit and ITM communication.
