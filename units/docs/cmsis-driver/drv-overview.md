---
id: "drv-overview"
type: "concept"
domain: "drivers"
title: "Overview"
summary: "User applications and middleware components can control such peripherals using the CMSIS-Driver API and so achieve better code reuse and simpler integration in various ecosystems."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

**CMSIS-Driver** specifies generic driver interfaces for peripherals commonly used in embedded systems with Arm® Cortex® processors.

User applications and middleware components can control such peripherals using the [**CMSIS-Driver API**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/modules.html) and so achieve better code reuse and simpler integration in various ecosystems. The API is designed to be generic and independent of a specific RTOS making it reusable across a wide range of supported microcontroller devices.

The following block diagram shows an exemplary set up for various drivers.

(figure: Example use of CMSIS-Drivers with Middleware)

The standard CMSIS-Driver interfaces connect microcontroller peripherals with middleware that implements communication stacks, file system and graphic user interfaces.
