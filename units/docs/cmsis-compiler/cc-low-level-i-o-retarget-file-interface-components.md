---
id: "cc-low-level-i-o-retarget-file-interface-components"
type: "concept"
domain: "core"
title: "Low-Level I/O Retarget: File Interface Components"
summary: "Standard C library functions interact with files in a same manner as with standard I/O streams and offer the same retargeting interface."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_io.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_io.md#file-interface-components"
license: "Apache-2.0"
mode: "V"
---

**CMSIS-Compiler:File Interface** software component provides generic shim layer interface between the C library and an arbitrary file system implementation.

Standard C library functions interact with files in a same manner as with standard I/O streams and offer the same retargeting interface. The existing interface is split to enable component interchangeability and fs_interface_api API is used to enable quick file system retargeting.

Default components are as follows:

 Component      | Description
:---------------|:------------
 **Breakpoint** | When the file stream is used, the application stops with [BKPT](https://developer.arm.com/documentation/100073/latest/The-Arm-C-and-C---Libraries/Support-for-building-an-application-with-the-C-library/Using-the-C-and-C---libraries-with-an-application-in-a-semihosting-environment?lang=en) instruction. No additional code is required.
 **Custom**     | Placeholder for custom fs_interface_api implementation

**Custom** component is available to enable access to fs_interface_api API header file when application provides an custom implementation. Custom implementation is typically needed when file system components do not provide its own implementation. To help you implement the functionality the File Interface:Custom component also provides the code template.
