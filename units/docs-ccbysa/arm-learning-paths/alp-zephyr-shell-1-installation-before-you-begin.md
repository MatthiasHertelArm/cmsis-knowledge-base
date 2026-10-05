---
id: "alp-zephyr-shell-1-installation-before-you-begin"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Set up the Zephyr shell development environment: Before you begin"
summary: "In this section, you'll prepare your host computer and identify the hardware you need for two Zephyr shell examples. You'll use the shell over two transports:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you'll prepare your host computer and identify the hardware you need for two Zephyr shell examples. You'll use the shell over two transports:

- MQTT over Ethernet
- UART over a USB serial connection

Make sure that you have a working Zephyr development environment set up in Visual Studio Code with:

- The Workbench for Zephyr extension installed 
- A Zephyr SDK toolchain imported in Workbench
- A West workspace initialized

Before working through this Learning Path, complete [Build Zephyr projects with Workbench for Zephyr in VS Code](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/).

The two examples in this Learning Path have additional requirements:

- MQTT shell example: Docker Desktop, Docker Engine, or another Docker-compatible runtime on your host computer, if you're not installing Mosquitto on host. The board communicates with a Mosquitto broker running in a container.
- UART shell example: A USB cable to connect the development board to your host computer. The board exposes a shell prompt over the USB serial interface.
