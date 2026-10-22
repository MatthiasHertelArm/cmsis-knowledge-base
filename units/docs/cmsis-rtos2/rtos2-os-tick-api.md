---
id: "rtos2-os-tick-api"
type: "concept"
domain: "rtos"
title: "OS Tick API"
summary: "System tick timer interface for periodic RTOS Kernel Ticks defined in %os_tick.h"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

System tick timer interface for periodic RTOS Kernel Ticks defined in **%os_tick.h**
 

The **OS Tick API** is an interface to a system timer that generates the Kernel Ticks.

All Cortex-M processors provide an unified System Tick Timer that is typically used to generate the RTOS Kernel Tick. 

\if ARMCA
The Cortex-A processors do not implement an unified system timer and required a device specific implementation. 
\endif

CMSIS-RTOS2 provides in the directory CMSIS/RTOS2/Source several OS Tick implementations that can be used by any RTOS kernel.

Filename                 | OS Tick Implementation for...
:------------------------|:-----------------------------------------------------------------------
**%os_systick.c**         | Cortex-M SysTick timer
\if ARMCA
**%os_tick_gtim.c**       | Cortex-A Generic Timer (available in some devices)
**%os_tick_ptim.c**       | Cortex-A Private Timer (available in some devices)
\endif

**Note:** The above OS Tick source files implement `weak` functions which may be overwritten by user-specific implementations.
