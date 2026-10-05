---
id: "alp-zephyr-shell-2-overview-how-shell-backends-work"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Understand the Zephyr shell subsystem and backends: How shell backends work"
summary: "The shell command tree is independent of the transport. The same commands can run over UART, RTT, MQTT, or another enabled backend. You can select a transport by setting a single Kconfig option, with no code changes in main.c."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/2_overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/2_overview/#how-shell-backends-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

The shell command tree is independent of the transport. The same commands can run over UART, RTT, MQTT, or another enabled backend. You can select a transport by setting a single Kconfig option, with no code changes in `main.c`.

You can enable multiple backends at the same time in a single application when the board has the required peripherals and memory. 

A minimal shell build with only the kernel and device modules adds roughly 10 to 15 KB to flash and a few hundred bytes to RAM on a Cortex-M target. The exact footprint depends on the modules enabled and the toolchain optimization level.

In this Learning Path, you'll work with two transports:

### MQTT backend

Enable the MQTT backend with `CONFIG_SHELL_BACKEND_MQTT=y`. The MQTT backend routes shell commands and responses over MQTT topics. The board subscribes to `<device_id>/sh/rx` for inbound commands and publishes responses to `<device_id>/sh/tx`. The backend is IPv4-only and connects automatically when the board has an IPv4 address.

### UART backend 

Enable the UART backend with `CONFIG_SHELL_BACKEND_SERIAL=y`. The UART backend routes shell commands and responses over the board's UART interface, accessible through a USB serial connection. Use PuTTY on Windows, or `screen` on macOS and Linux. This backend works on a wide range of Zephyr-supported development boards without the need for additional debug hardware.
