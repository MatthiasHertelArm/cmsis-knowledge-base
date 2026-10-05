---
id: "ocp-ocp-tools-readmes-readme-5"
type: "concept"
domain: "project"
title: "ocp-tools-readmes README"
summary: "RTOS: FreeRTOS Real-Time Operating System ----------------------------------------- The real-time operating system FreeRTOS implements the resource management."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/RTOS/FreeRTOS/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/RTOS/FreeRTOS/README.md"
license: "Apache-2.0"
mode: "V"
---

RTOS: FreeRTOS Real-Time Operating System
-----------------------------------------
The real-time operating system [FreeRTOS](https://github.com/ARM-software/CMSIS-FreeRTOS) implements the resource management.

It is configured with the following settings:

- Minimal stack size \[words]: 768
- Total heap size \[bytes]: 24000
- Preemption interrupt priority: 128
- Event Recorder configuration
  - Initialize Event Recorder: 1

Refer to [Configure CMSIS-FreeRTOS](https://arm-software.github.io/CMSIS-FreeRTOS/General/html/cre_freertos_proj.html#cmsis_freertos_config) for a detailed description of all configuration options.
