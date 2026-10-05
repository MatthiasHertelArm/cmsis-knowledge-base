---
id: "cfrt-introduction"
type: "concept"
domain: "rtos"
title: "Introduction"
summary: "FreeRTOS is one of the market-leading real-time operating systems (RTOS) for embedded microcontrollers."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

[FreeRTOS](https://www.freertos.org/) is one of the market-leading real-time operating systems (RTOS) for embedded microcontrollers.
It is professionally developed, [strictly quality controlled](https://www.freertos.org/FreeRTOS-Coding-Standard-and-Style-Guide.html),
robust, [supported](https://forums.freertos.org/) [(archive)](https://www.freertos.org/FreeRTOS_Support_Forum_Archive/freertos_support_forum_archive_index.html/),
free to [use in commercial products](https://www.freertos.org/a00114.html) without a requirement to expose proprietary source code,
and has [no IP infringement](https://www.freertos.org/differences-between-officially-supported-and-contributed-FreeRTOS-code.html) risk.

[**CMSIS-RTOS v2**](https://arm-software.github.io/CMSIS_6/latest/RTOS2/index.html) is a common API for real-time operating
systems (RTOS). It provides a standardized programming interface that is portable to many RTOS and enables software components
that can work across multiple RTOS systems. It supports the Armv8-M architecture, dynamic object creation, multi-core systems,
and has a binary-compatible interface across ABI-compliant compilers.

Using this software pack, users can choose between a native FreeRTOS implementation or one that adheres to the CMSIS-RTOS2 API
and uses FreeRTOS under the hood. The CMSIS-RTOS2 API enables programmers to create portable application code to be used with
different RTOS kernels (for example [Keil RTX5](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK/RTX5%20RTOS/)).

This documentation shows you:

- how to [create a new microcontroller project](#page_create_project) using FreeRTOS from scratch.
- various [examples](#page_example_projects) show you the usage of FreeRTOS in native and CMSIS-RTOS2 mode.
- the [technical data](#page_technical_data) of this implementation.
- [Revision history](#rev_hist).
