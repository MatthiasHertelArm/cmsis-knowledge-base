---
id: "alp-zephyr-vsworkbench-3-debug-install-and-configure-debug-ru"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Analyze and debug a Zephyr application: Install and configure debug runners"
summary: "Depending on your board, different debug utilities may be required. Workbench for Zephyr integrates and discovers several common runners:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/3_debug.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/3_debug/#install-and-configure-debug-runners"
license: "CC-BY-SA-4.0"
mode: "V"
---

Depending on your board, different debug utilities may be required. Workbench for Zephyr integrates and discovers several common runners:

- **OpenOCD**: Generic open-source debugger
- **LinkServer**: For NXP targets
- **STM32CubeProgrammer**: For STM32 boards
- **J-Link**: For SEGGER debug probes

Workbench for Zephyr will automatically detect these tools when they are installed in their default locations and available on your system `PATH`. If a tool is installed in a custom location, you can either update your `PATH` or configure your environment so that Workbench for Zephyr can find it.
