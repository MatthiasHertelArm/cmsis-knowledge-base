---
id: "ocp-ocp-tools-readmes-readme-6"
type: "concept"
domain: "project"
title: "ocp-tools-readmes README"
summary: "RTOS: Keil RTX5 Real-Time Operating System ------------------------------------------"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/RTOS/RTX/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/RTOS/RTX/README.md"
license: "Apache-2.0"
mode: "V"
---

RTOS: Keil RTX5 Real-Time Operating System
------------------------------------------

The real-time operating system [Keil RTX5](https://arm-software.github.io/CMSIS-RTX/latest/index.html) implements the resource management. 

It is configured with the following settings:

- [Global Dynamic Memory size](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html#systemConfig): 24000 bytes
- [Default Thread Stack size](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html#threadConfig): 3072 bytes
- [Event Recorder Configuration](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html#evtrecConfig)
  - [Global Initialization](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html#evtrecConfigGlobIni): 1
    - Start Recording: 1

Refer to [Configure RTX v5](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html) for a detailed description of all configuration options.
