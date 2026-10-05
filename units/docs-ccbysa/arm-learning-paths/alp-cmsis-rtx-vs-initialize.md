---
id: "alp-cmsis-rtx-vs-initialize"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Initialize the Operating System"
summary: "Keil RTX5 is a feature-rich real-time operating system (RTOS). CMSIS and the CMSIS-RTOS2 API makes it easy to work with."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize/"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Keil RTX5](https://www2.keil.com/mdk5/cmsis/rtx) is a feature-rich real-time operating system (RTOS). CMSIS and the [CMSIS-RTOS2](https://arm-software.github.io/CMSIS_5/RTOS2/html/index.html) API makes it easy to work with.

When setting up the project's Run-Time Environment, ensure you add the appropriate system initialization code (`C Startup`).

Once this is done, the `RTX5` initialization code is typically the same. It involves setting up the `SysTick` timer with the [SystemCoreClockUpdate()](https://www.keil.com/pack/doc/CMSIS/Core/html/group__system__init__gr.html#gae0c36a9591fe6e9c45ecb21a794f0f0f) function, then initializing and starting the RTOS.
