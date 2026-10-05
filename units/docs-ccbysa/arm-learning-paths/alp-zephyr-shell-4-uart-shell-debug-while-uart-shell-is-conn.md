---
id: "alp-zephyr-shell-4-uart-shell-debug-while-uart-shell-is-conn"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr UART shell on Arm Cortex-M: Debug while UART shell is connected"
summary: "You can run a debug session in Workbench for Zephyr while the UART terminal remains connected."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell/#debug-while-uart-shell-is-connected"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can run a debug session in Workbench for Zephyr while the UART terminal remains connected.

To start debugging, select your build configuration in the **Workbench for Zephyr** panel and select **Debug**. You can set breakpoints, inspect variables, and step through code in Visual Studio Code while the UART shell remains open.

When execution stops at a breakpoint, shell output pauses with the target. After you continue execution, the UART shell becomes responsive again.
