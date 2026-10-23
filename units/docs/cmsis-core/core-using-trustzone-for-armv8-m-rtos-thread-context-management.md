---
id: "core-using-trustzone-for-armv8-m-rtos-thread-context-management"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M: RTOS Thread Context Management"
summary: "To provide a consistent RTOS thread context management for Armv8-M TrustZone across the various real-time operating systems (RTOS), the CMSIS-Core (Cortex-M) includes header file tz_context.h with API definitions."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/using_tz.md#rtos-thread-context-management"
license: "Apache-2.0"
mode: "V"
---

To provide a consistent RTOS thread context management for Armv8-M TrustZone across the various real-time operating systems (RTOS), the CMSIS-Core (Cortex-M) includes header file **tz_context.h** with API definitions.

A *non-secure application* which uses an RTOS and calls *secure* library modules requires the management of the *secure* stack space. Since *secure state* registers cannot be accessed by the RTOS that runs in *non-secure state* secure functions implement the thread context switch.

As the *non-secure state* and *secure state* parts of an application are separated, the API for managing the *secure* stack space should be standardized. Otherwise the *secure* library modules would force the *non-secure state* application to use a matching RTOS implementation.

(figure: RTOS Thread Context Management for Armv8-M TrustZone)

To allocate the context memory for threads, an RTOS kernel that runs in *non-secure state* calls the interface functions defined by the header file **tz_context.h**. The **TZ Context** functions themselves are part of the *secure state* application. An minimum implementation is provided as part of RTOS2 and should handle the secure stack for the thread execution. However it is also possible to implement the context memory management system with additional features such as access control to *secure state* memory regions using an MPU.

The API functions of **TZ Context** are described in the chapter [API Reference](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/modules.html) under trustzone_functions - context_trustzone_functions.

CMSIS-Core provides a template implementation of **TZ Contenxt** in `CMSIS\Core\Template\ARMv8-M\tz_context.c` file.

Refer to Example_TrustZone for RTOS examples that demonstrate how to use the RTOS Thread Context Management.
