---
id: "dap-overview"
type: "concept"
domain: "debug"
title: "Overview"
summary: "Many Arm Cortex processors implement CoreSight Debug Access Port (DAP) that equips them with powerful on-chip debug and trace capabilities. CMSIS-DAP standardizes and simplifies access to this functionality for embedded software developers."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/index.html"
license: "Apache-2.0"
mode: "V"
---

Many Arm Cortex processors implement CoreSight Debug Access Port ([DAP](https://developer.arm.com/documentation/102585/0000/what-is-a-debug-access-port)) that equips them with powerful on-chip debug and trace capabilities. **CMSIS-DAP** standardizes and simplifies access to this functionality for embedded software developers.

**CMSIS-DAP** is a protocol specification and a firmware implementation that enables standardized communication between two sides:

- On one side an Arm Cortex-based processor where an embedded application is executed,
- and on the other side a software debug tool that runs on a host computer.

CMSIS-DAP support can be implemented in a standalone debug unit, or also as a component integrated on a development board. The figure below illustrates the concept:

(figure: CMSIS-DAP Interface)

Connection with the target processor is possible over the physical interfaces supported by the CoreSight DAP: a 5-pin JTAG or a 2-pin Serial Wired Debug (SWD) interface. Additionally it can expose access to a UART for serial-to-USB communication. CMSIS-DAP supports target devices that contain one or more Arm Cortex cores.

For communication with the debugging program the USB connection is used. A broad set of DAP_Commands_gr enables uniform support for CMSIS-DAP independent on the actual probe.

The dap_firmware provides a template implementation of the CMSIS-DAP concept as well as several example projects for popular debug units.

Debug probes can be validated for compliance to CMSIS-DAP using the scripts explained in dap_validate.

> **Note**
> - CMSIS-DAP v1.x is _deprecated_ and is not recommended for new designs.
> - Use CMSIS-DAP v2.x instead that provides high-speed SWO trace streaming and does not require driver installation in modern operating systems (Mac OS, Linux, Windows). Refer to dap_drv_install for more information.
