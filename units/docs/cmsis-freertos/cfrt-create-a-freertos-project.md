---
id: "cfrt-create-a-freertos-project"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project"
summary: "The steps to create a microcontroller application using FreeRTOS are:"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md"
license: "Apache-2.0"
mode: "V"
---

The steps to create a microcontroller application using FreeRTOS are:

- Install the pack.
- In your IDE, create a new project and select a microcontroller device.

Then, you can basically choose between two options when creating a FreeRTOS project:

1. [Using the FreeRTOS API and kernel](#create_native_project).
2. [Using the CMSIS-RTOS2 API with an underlying FreeRTOS kernel](#create_cmsis_project).

Before starting, please review the brief summary of the [Pack Components](#pack_components) below to familiarize yourself with them.
