---
id: "alp-cmsis-rtx-vs-create-configure-the-solution-environ"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Create csolution project: Configure the solution environment"
summary: "VS Code allows complete configurability of all aspects of the project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create/#configure-the-solution-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

VS Code allows complete configurability of all aspects of the project.

- Locate `vcpkg-configuration.json` within the project. This file defines the components used.
- Right-click on this file and select **Configure Arm Tools Environment** to open the configuration panel.

From the dropdown menus, make sure to select the most up-to-date versions of the following:

- Arm CMSIS-Toolbox
- Arm Compiler for Embedded
- Arm Debugger
- Arm Virtual Hardware for Cortex-M based on Fast Models
- Kitware's CMake tool
- Ninja Build

Set all other tools to **None** as they are not needed for this example.

If you open `vcpkg-configuration.json` in the text editor, you’ll see these selections reflected. Close the file to save your changes.

All necessary components will be downloaded and installed as necessary (if not already installed).
