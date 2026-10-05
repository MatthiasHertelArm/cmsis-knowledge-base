---
id: "cc-multithreading-support-retarget-os-interface"
type: "concept"
domain: "core"
title: "Multithreading Support Retarget: OS Interface"
summary: "The software component CMSIS-Compiler:OS Interface exposes os_interface_api API that depends on the used toolchain i.e. on the standard C library embedded with the toolchain. Available components are implementations of this API and default components are as follows:"
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_os.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_os.md#os-interface"
license: "Apache-2.0"
mode: "V"
---

The software component **CMSIS-Compiler:OS Interface** exposes os_interface_api API that depends on the used toolchain i.e. on the standard C library embedded with the toolchain. Available components are implementations of this API and default components are as follows:

 Component       | Description
:----------------|:------------
 **CMSIS-RTOS2** | os_interface_api implementation using CMSIS-RTOS2 API
 **Custom**      | Placeholder for custom os_interface_api implementation

Default implementation uses **CMSIS-RTOS2** to implement multithreading support and enables easy retargeting to any RTOS that implements RTOS2 API.

**Custom** component is available to enable access to os_interface_api API header file when application provides an custom implementation. Custom implementation is typically used when application uses RTOS native API.

To help you implement the functionality the OS Interface:Custom component also provides the code templates.
