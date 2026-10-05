---
id: "alp-zephyr-shell"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M"
summary: "Learn how to enable and configure the Zephyr shell subsystem on Arm Cortex-M, then build and run MQTT and UART shell backend examples using Workbench for Zephyr in Visual Studio Code."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Learn how to enable and configure the Zephyr shell subsystem on Arm Cortex-M, then build and run MQTT and UART shell backend examples using Workbench for Zephyr in Visual Studio Code.

**Who is this for:** This is an introductory topic for embedded developers who want to add an interactive command-line shell to a Zephyr RTOS application on Arm Cortex-M.

**Learning objectives:**

- Enable and tailor Zephyr shell (Kconfig/prj.conf) to produce a minimal CLI footprint
- Build and flash shell-enabled Zephyr apps using MQTT and UART shell backends on an Arm Cortex-M board
- Use the Zephyr shell for board bring-up, diagnostics, and interactive testing

**Prerequisites:**

- Basic familiarity with embedded C programming
- Visual Studio Code with the Workbench for Zephyr extension installed and configured
- Docker Desktop, Docker Engine, or another Docker-compatible runtime installed on your host computer (for the MQTT shell example, if you're not installing Mosquitto on host)
- A Zephyr-supported Arm Cortex-M board (for example, NXP FRDM-MCXN947)

**Steps:**

1. Set up the Zephyr shell development environment
2. Understand the Zephyr shell subsystem and backends
3. Build and run the Zephyr MQTT shell on Arm Cortex-M
4. Build and run the Zephyr UART shell on Arm Cortex-M

Time: about 30 minutes.
