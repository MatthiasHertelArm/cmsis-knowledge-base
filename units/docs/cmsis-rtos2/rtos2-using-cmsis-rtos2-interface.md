---
id: "rtos2-using-cmsis-rtos2-interface"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface"
summary: "This sections explains concepts for using CMSIS-RTOS2 interface. They are recommeded to follow for best reusability of the software across different platforms."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
license: "Apache-2.0"
mode: "V"
---

This sections explains concepts for using CMSIS-RTOS2 interface. They are recommeded to follow for best reusability of the software across different platforms.

 - rtos2_functionalities lists the OS services supported by CMSIS-RTOS2 API.
 - cmsis_os2_h explains how CMSIS-RTOS2 interface is defined and can be used along with the RTOS-specific files as well as part of CMSIS pack.
 - SystemStartup shows the flow for kernel initialization.
 - rtos_objects explains the approach to creating and using RTOS Objects.
 - CMSIS_RTOS_MemoryMgmt provides information about options for memory management with CMSIS-RTOS2.
 - CMSIS_RTOS_ProcessIsolation describes the CMSIS-RTOS2 concepts for protecting execution of critical software tasks against potential flaws in other parts of a program.

> **Note**
> - For the guidance on migration from CMSIS-RTOS API v1 to CMSIS-RTOS2, see section [Detailed API Function Differences](https://arm-software.github.io/CMSIS_5/latest/RTOS2/html/os2MigrationFunctions.html) in CMSIS 5 documentation.
