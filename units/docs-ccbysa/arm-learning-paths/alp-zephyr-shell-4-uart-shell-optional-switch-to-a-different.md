---
id: "alp-zephyr-shell-4-uart-shell-optional-switch-to-a-different"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr UART shell on Arm Cortex-M: (Optional) Switch to a different board"
summary: "The application is portable across many Zephyr-supported boards because the UART shell backend is selected through Kconfig and there is no board-specific code in main.c."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell/#optional-switch-to-a-different-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application is portable across many Zephyr-supported boards because the UART shell backend is selected through Kconfig and there is no board-specific code in `main.c`.

To change the target board on an existing project:

1. Open the **Workbench for Zephyr** panel in the VS Code Activity Bar.
2. Expand the **Applications** section.
3. Right-click the board name and select **Change board**.
4. Right-click the application and select **Clean**.
5. Right-click the application and select **Build (pristine)**.

**Note:**
You need a pristine build when you change the board because Workbench for Zephyr caches board-specific generated files in the build directory.


After the pristine build completes, flash the board as before. The same `prj.conf` and `main.c` work without changes on any Zephyr-supported board with a USB UART interface.
