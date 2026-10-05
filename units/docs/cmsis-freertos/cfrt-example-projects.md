---
id: "cfrt-example-projects"
type: "concept"
domain: "rtos"
title: "Example Projects"
summary: "This pack contains two example projects:"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/example_projects.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/example_projects.md"
license: "Apache-2.0"
mode: "V"
---

This pack contains two example projects:

- [Hello World](#example_hello_world)
- [TrustZone](#example_trustzone)

The first example shows how to configure a simple application using FreeRTOS with CMSIS-RTOS2,
whereas the second example shows how to use the FreeRTOS with CMSIS-RTOS2 in an application
that utilizes TrustZone secure/non-secure execution.

Provided examples use the [CMSIS Solution Project File Format](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/)
and can be built for multiple Cortex-M targets using [CMSIS Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/)
either from the command line or from Visual Studio Code by using [Arm Keil Studio Cloud extensions](https://developer.arm.com/documentation/108029/0000/?lang=en).

The **Examples** solution defines projects and build information for each project.
