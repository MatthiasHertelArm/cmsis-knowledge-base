---
id: "alp-zephyr-shell-4-uart-shell-run-shell-commands"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr UART shell on Arm Cortex-M: Run shell commands"
summary: "Type each of the following commands at the uart:~$ prompt:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell/#run-shell-commands"
license: "CC-BY-SA-4.0"
mode: "V"
---

Type each of the following commands at the `uart:~$` prompt:

```bash
kernel version
kernel uptime
kernel thread list
```

The output is similar to:

(figure: Zephyr UART shell terminal output showing the kernel version, kernel uptime, and kernel thread list commands and their responses at the uart:~$ prompt#center)

The `*` next to `shell_uart` in the thread list marks the currently running thread, which is the shell that executed the command.

**Note:**
Application log messages such as `LOG_INF` and `LOG_WRN` appear in the terminal together with the shell prompt. This is expected when both `CONFIG_SHELL=y` and `CONFIG_LOG=y` are enabled.
