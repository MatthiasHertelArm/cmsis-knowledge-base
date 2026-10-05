---
id: "alp-zephyr-shell-2-overview-how-the-zephyr-shell-subsystem"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Understand the Zephyr shell subsystem and backends: How the Zephyr shell subsystem works"
summary: "The Zephyr shell subsystem (CONFIG_SHELL=y) adds an interactive command-line interface to your firmware. After you enable the shell, you can inspect system state, run subsystem commands, and trigger application behavior at runtime without rebuilding or reflashing the application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/2_overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/2_overview/#how-the-zephyr-shell-subsystem-works"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Zephyr shell subsystem (`CONFIG_SHELL=y`) adds an interactive command-line interface to your firmware. After you enable the shell, you can inspect system state, run subsystem commands, and trigger application behavior at runtime without rebuilding or reflashing the application.

Several Zephyr subsystems register shell commands automatically. Common built-in modules include:

| Module | Example commands |
|--------|------------------|
| `kernel` | `version`, `uptime`, `thread list`, `thread stacks` |
| `net` | `iface`, `ping`, `dns`, `tcp` |
| `device` | `list` |
| `log` | `enable`, `disable`, `levels` |
| `shell` | `help`, `history`, `resize` |

For more information on the shell subsystem, see the [Zephyr shell documentation](https://docs.zephyrproject.org/latest/services/shell/index.html).
