---
id: "alp-asm-setup-mdk6-configure-solution-environment"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Setting up a Project in Keil Studio (VS Code): Configure solution environment"
summary: "VS Code allows complete configurability of all aspects of the project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6/#configure-solution-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

VS Code allows complete configurability of all aspects of the project.

Locate `vcpkg-configuration.json` within the project. This file defines the components used.

Right-click on this file, and select `Configure Arm Tools Environment` to open the configuration panel.

From the various pull-downs, ensure that the most up to date versions of the following are selected:

* Arm CMSIS-Toolbox
* Arm Compiler for Embedded
* Arm Debugger
* Arm Virtual Hardware for Cortex-M based on Fast Models
* Kitware's cmake tool
* Ninja Build

Others can be set as `None` as they are not needed for this example.

If you open `vcpkg-configuration.json` in the text editor you will see these set as selected. Close the file to save.

All necessary components will be downloaded and installed as necessary (if not already installed).
