---
id: "alp-zephyr-vsworkbench-3-debug-install-debug-runner-utilities"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Analyze and debug a Zephyr application: Install debug runner utilities"
summary: "To install debug tools for your specific board, go to Host Tools > Install Debug Tools in the Zephyr Workbench panel and select the tools applicable to your board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/3_debug.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/3_debug/#install-debug-runner-utilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

To install debug tools for your specific board, go to **Host Tools > Install Debug Tools** in the Zephyr Workbench panel and select the tools applicable to your board. You may need to press the refresh symbol to get the latest installation state for the selected/installed runners:

(figure: Install Debug Runners panel in Workbench for Zephyr showing a list of available debug runner tools including OpenOCD, J-Link, LinkServer, and STM32CubeProgrammer with status indicators and install buttons#center)

### Configure debug settings

Before starting a debug session, make sure your settings match your application and board configuration.

### Application configuration
Select your application and build config (for example, "primary"), then wait for values to load or build the project if needed.

### Program settings
The ELF executable path is auto-filled after build. You can optionally add a **CMSIS-SVD** file to enable register-level view.

### Debug server
Choose the runner from OpenOCD, J-Link, LinkServer, or PyOCD. If the system doesn't detect your runner automatically, enter the runner path manually. Select **Apply** to save your settings or launch debug directly.

(figure: Debug Manager panel in Workbench for Zephyr showing fields for selecting a debug runner, entering the runner executable path, and choosing a board profile#center)
