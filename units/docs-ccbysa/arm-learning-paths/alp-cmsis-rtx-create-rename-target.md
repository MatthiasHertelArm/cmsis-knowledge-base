---
id: "alp-cmsis-rtx-create-rename-target"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create and setup Keil MDK project: Rename target"
summary: "A project can contain many targets, which refer to the platform that a particular build will run on. The default name is Target 1."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/create/#rename-target"
license: "CC-BY-SA-4.0"
mode: "V"
---

A project can contain many targets, which refer to the platform that a particular build will run on. The default name is `Target 1`. To give a meaningful name, click `Manage Project Items`, and rename the target (for example, to `FVP`), as well as optionally the `Source Group 1` (to `Source`) that will contain the source code. Arranging code in these folders allows for easy sharing across different target builds.

Click `OK` to save.

**Arm Development Studio:**
Default `Configuration` names are `Debug` and `Release`.

Name and other settings (see below) are managed in `Project Properties` (`Alt+Enter`), under `C/C++ Build` > `Settings`.
