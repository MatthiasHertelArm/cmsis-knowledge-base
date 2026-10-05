---
id: "alp-cmsis-rtx-create-manage-run-time-environment"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create and setup Keil MDK project: Manage Run-Time Environment"
summary: "You'll first be presented with the Manage Run-Time Environment dialog, which allows you to specify the CMSIS software components that will be used in the project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create/#manage-run-time-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll first be presented with the `Manage Run-Time Environment` dialog, which allows you to specify the CMSIS software components that will be used in the project.

Under `CMSIS`, select `CORE`, as well as `RTOS2 (API)` > `Keil RTX5`, in `Source` form. You'll also need to select `CMSIS` > `OS Tick (API)` > `SysTick`.

Under `Device`, select `Startup` (`C Startup`).

These are the minimal components needed for such an application. Click `OK`.

**Arm Development Studio:**
Run-time environment is managed by the `.rteconfig` file within the project.
