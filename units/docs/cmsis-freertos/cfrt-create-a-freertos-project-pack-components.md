---
id: "cfrt-create-a-freertos-project-pack-components"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project: Pack Components"
summary: "The CMSIS-FreeRTOS pack includes the following components and their variants:"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md#pack-components"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-FreeRTOS pack includes the following components and their variants:

| Component            | Variant                 | Description                                                                         |
|----------------------|-------------------------|-------------------------------------------------------------------------------------|
| CMSIS:RTOS2:FreeRTOS | Cortex-M                | CMSIS-RTOS2 API implementation based on the FreeRTOS kernel for Cortex-M.           |
|                      | Cortex-A                | Adds support for external IRQ controller on Cortex-A processors.                    |
| RTOS:CORE            | Cortex-M                | Core API for Cortex-M processors, providing task scheduling and communication.      |
|                      | Cortex-M MPU            | Adds support for the Memory Protection Unit (MPU) on Cortex-M processors.           |
|                      | Cortex-A                | Core API for Cortex-A processors.                                                   |
| RTOS:Config          | CMSIS RTOS2             | Configuration file tailored for the CMSIS-RTOS2 API.                                |
|                      | FreeRTOS                | Configuration file for native FreeRTOS API usage.                                   |
| RTOS:Coroutines      | -                       | Adds FreeRTOS Co-routine API.                                                       |
| RTOS:Event Groups    | -                       | Provides event group functionality for task synchronization and communication.      |
| RTOS:Heap            | Heap_1                  | A simple memory allocation scheme that does not permit memory to be freed.          |
|                      | Heap_2                  | Allows memory to be freed but does not coalesce adjacent free memory blocks.        |
|                      | Heap_3                  | Wraps the standard `malloc()` and `free()` functions for thread safety.             |
|                      | Heap_4                  | Coalesces adjacent free memory blocks to avoid fragmentation.                       |
|                      | Heap_5                  | Extends Heap_4 with the ability to span the heap across non-adjacent memory areas.  |
| RTOS:Message Buffer  | -                       | Enables tasks and interrupts to send and receive variable-length messages.          |
| RTOS:Stream Buffer   | -                       | Allows tasks and interrupts to send and receive continuous streams of data.         |
| RTOS:Timers          | -                       | Adds support for software timers, enabling delayed and periodic function execution. |
| RTOS:TrustZone       | -                       | Provides context management for execution in TrustZone secure domain.               |

> **NOTE**
>
> CMSIS-FreeRTOS 11.2.0 added support for TrustZone **domain detection from project** settings. Regardless of the build contexts
> (no TrustZone, TrustZone secure or non-secure domain) the below variants shall be used:
>
> - RTOS:CORE&Cortex-M
> - RTOS:CORE&Cortex-M MPU
