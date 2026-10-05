---
id: "alp-zephyr-shell-3-mqtt-shell-optional-switch-to-a-different"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr MQTT shell on Arm Cortex-M: (Optional) Switch to a different board"
summary: "The application is portable across any Zephyr-supported board with Ethernet, because the MQTT backend is selected through Kconfig and there's no board-specific code in main.c. You don't need to recreate the project to test it on another board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#optional-switch-to-a-different-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application is portable across any Zephyr-supported board with Ethernet, because the MQTT backend is selected through Kconfig and there's no board-specific code in `main.c`. You don't need to recreate the project to test it on another board.

To change the target board on an existing project:

1. Open the **Workbench for Zephyr** panel in the VS Code Activity Bar.
2. Expand the **Applications** section. The project you created appears with its current board name underneath.
3. Right-click the board name and select **Change board**. Pick a new board from the list (for example, an STM32 Nucleo-H743ZI or another Cortex-M board with Ethernet).
4. Right-click the application and select **Clean** to remove the previous build artifacts.
5. Right-click the application and select **Build (pristine)** to rebuild the project from scratch with the new board configuration.

After the pristine build completes, flash the board as before. The same `prj.conf` and `main.c` work without changes, and the MQTT backend connects as soon as the new board acquires an IPv4 address.

**Note:**
You need a pristine build when you change the board because Workbench for Zephyr caches board-specific generated files (device tree, Kconfig, linker script) in the build directory. Without a clean rebuild, the previous board's configuration leaks into the new build and produces incorrect binaries.
