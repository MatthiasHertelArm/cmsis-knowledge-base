---
id: "alp-context-switch-cortex-m-example"
type: "concept"
domain: "rtos"
title: "Learn about context switching on Arm Cortex-M processors: Example Arm DS project to demonstrate context switching operations"
summary: "There are a set of open source example projects that made available alongside the Armv8-M Memory Model and MPU User Guide. The source code for these example projects is available in the GitHub repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example/"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are a set of open source example projects that made available alongside the [Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/latest/). The source code for these example projects is available in the [GitHub repository](https://github.com/ARM-software/m-profile-user-guide-examples/tree/main/Memory_model/rtos_context_switch).

This example demonstrates simple real-time kernel context switching operations between two threads using MPU regions that are available in Arm Cortex-M processors.
You can build and run the example project using the versions of tools and software listed below:
  - [Arm Development Studio 2022.1](https://learn.arm.com/install-guides/armds/)
  - [Arm Compiler for Embedded 6.18](https://learn.arm.com/install-guides/armclang/)
  - [Fast Models Fixed Virtual Platforms (FVP) 11.18](https://learn.arm.com/install-guides/fm_fvp/fvp/)
  - CMSIS 5.8.0
