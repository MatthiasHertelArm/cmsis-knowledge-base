---
id: "alp-zephyr-shell-1-installation-set-up-uart-terminal-tools"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Set up the Zephyr shell development environment: Set up UART terminal tools"
summary: "For the UART shell example, you'll need a serial terminal application on your host computer. You'll use the terminal application to connect to the Zephyr shell over the board's UART interface."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation/#set-up-uart-terminal-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

For the UART shell example, you'll need a serial terminal application on your host computer. You'll use the terminal application to connect to the Zephyr shell over the board's UART interface.

You can complete this Learning Path on Windows, macOS, and Linux host computers.

### Windows

Install [PuTTY](https://www.putty.org/index.html), which provides a lightweight serial terminal for UART communication on Windows.

### macOS

macOS includes a built-in UART terminal utility through the `screen` command, so you don't need additional software to connect to the shell.

### Linux

Linux includes `screen` in most distributions, so you don't need additional software to connect to the shell. If `screen` isn't installed, use your package manager to install it:

```bash
sudo apt install screen
```
**Note:**
Workbench for Zephyr supports multiple debug runners depending on the connected board. The FRDM-MCXN947 board uses the onboard CMSIS-DAP/LinkServer interface for flashing and debugging, and UART over USB for shell access.
