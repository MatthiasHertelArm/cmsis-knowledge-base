---
id: "alp-cmsis-rtx-vs-create-create-a-new-project"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Create csolution project: Create a new project"
summary: "Keil Studio projects are based on the CMSIS Solution standard."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create/#create-a-new-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Keil Studio projects are based on the [CMSIS Solution](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) standard.

1. Open VS Code and select **File** > **New File**. When prompted for the file type, select **New Solution** (**Arm CMSIS Solution**).
2. The **Create New Solution** dialog opens. Select the **Target Device** drop-down and search for `ARMCM4`.
3. From the **Templates, Reference Applications, and Examples** drop-down, select **Blank Solution**.
4. Ensure **Arm Compiler 6** is the selected compiler.
5. Enter an appropriate **Solution Name**. This defines the folder name the project is created into. You can also change the folder location if necessary.
6. Select **Create**. You'll be prompted to open the solution in the current window or a new window.
