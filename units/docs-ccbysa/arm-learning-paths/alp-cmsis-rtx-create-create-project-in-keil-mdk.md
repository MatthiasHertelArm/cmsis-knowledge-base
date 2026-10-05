---
id: "alp-cmsis-rtx-create-create-project-in-keil-mdk"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create and setup Keil MDK project: Create project in Keil MDK"
summary: "In the MDK menu, navigate to Project > New uVision Project, and create a new project (recommend to locate in a new folder)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create/#create-project-in-keil-mdk"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the MDK menu, navigate to `Project` > `New uVision Project`, and create a new project (recommend to locate in a new folder).

**Arm Development Studio:**
When creating the project navigate to `File` > `New` > `Project...` > `C/C++` > `C Project`.

Then select `CMSIS C/C++ Project`, using `Arm Compiler for Embedded 6`.


### Select device

You'll then be prompted to `Select Device` for your project. A list of all devices with their CMSIS-Packs installed will be shown.

For this example, select `Arm` > `Arm Cortex-M4` > `ARMCM4`. Click `OK`.
