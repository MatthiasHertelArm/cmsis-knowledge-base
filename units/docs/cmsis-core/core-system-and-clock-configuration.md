---
id: "core-system-and-clock-configuration"
type: "concept"
domain: "core"
title: "System and Clock Configuration"
summary: "Functions for system and clock setup available in system__device.c."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_system_init.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_system_init.txt"
license: "Apache-2.0"
mode: "V"
---

Functions for system and clock setup available in system__device_.c.

Arm provides a template file **system__device_.c** that must be adapted by 
the silicon vendor to match their actual device. As a **minimum requirement**, 
this file must provide:
 -  A device-specific system configuration function, SystemInit.
 -  A global variable that contains the system frequency, SystemCoreClock. 

The file configures the device and, typically, initializes the oscillator (PLL) that is part 
of the microcontroller device. This file might export other functions or variables that provide 
a more flexible configuration of the microcontroller system.

**Note:** Please pay special attention to the static variable `SystemCoreClock.` This variable might be
used throughout the whole system initialization and runtime to calculate frequency/time related values.
Thus one must assure that the variable always reflects the actual system clock speed. Be aware that
a value stored to `SystemCoreClock` during low level initialization (i.e. `SystemInit())` might get
overwritten by C library startup code and/or .bss section initialization.
Thus its highly recommended to call SystemCoreClockUpdate at the beginning of the user `main()` routine.
