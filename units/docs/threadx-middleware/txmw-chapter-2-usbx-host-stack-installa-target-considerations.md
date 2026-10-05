---
id: "txmw-chapter-2-usbx-host-stack-installa-target-considerations"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Target Considerations"
summary: "USBX requires between 24 KBytes and 64 KBytes of Read Only Memory (ROM) on the target in host mode. The amount of memory required is dependent on the type of controller used and the USB classes linked to USBX."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#target-considerations"
license: "MIT"
mode: "V"
---

USBX requires between 24 KBytes and 64 KBytes of Read Only Memory (ROM) on the target in host mode. The amount of memory required is dependent on the type of controller used and the USB classes linked to USBX. Another 32 KBytes of the target's Random Access Memory (RAM) are required for USBX global data structures and memory pool. This memory pool can also be adjusted depending on the expected number of devices on the USB and the type of USB controller. The USBX device side requires roughly 10-12 K of ROM depending on the type of device controller. The RAM memory usage depends on the type of class emulated by the device.

USBX also relies on ThreadX semaphores, mutexes, and threads for multiple thread protection, and I/O suspension and periodic processing for monitoring the USB bus topology.

### Product Distribution

USBX can be obtained from our public source code repository at <https://github.com/eclipse-threadx/usbx/>.

The following is a list of several important files in the repository:

- ***ux_api.h***: This C header file contains all system equates, data structures, and service prototypes.
- ***ux_port.h***: This C header file contains all development-tool-specific data definitions and structures.
- ***ux.lib***: This is the binary version of the USBX C library. It is distributed with the standard package.
- ***demo_usbx.c***: The C file containing a simple USBX demo

All filenames are in lower-case. This naming convention makes it easier to convert the commands to Unix development platforms.
