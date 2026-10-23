---
id: "zep-user-mode"
type: "concept"
domain: "rtos"
title: "User Mode"
summary: "Zephyr offers the capability to run threads at a reduced privilege level which we call user mode. The current implementation is designed for devices with MPU hardware."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/index.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr offers the capability to run threads at a reduced privilege level
which we call user mode. The current implementation is designed for devices
with MPU hardware.

For details on creating threads that run in user mode, please see
lifecycle_v2.
