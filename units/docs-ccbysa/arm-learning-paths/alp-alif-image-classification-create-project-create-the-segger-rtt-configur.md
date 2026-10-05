---
id: "alp-alif-image-classification-create-project-create-the-segger-rtt-configur"
type: "concept"
domain: "edge-ai"
title: "create project: Create the SEGGER RTT configuration"
summary: "RTT (Real-Time Transfer) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring. Create the configuration file mv2_runner/SEGGER_RTT_Conf.h:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project/#create-the-segger-rtt-configuration"
license: "CC-BY-SA-4.0"
mode: "V"
---

RTT (Real-Time Transfer) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring. Create the configuration file `mv2_runner/SEGGER_RTT_Conf.h`:

```c
#ifndef SEGGER_RTT_CONF_H
#define SEGGER_RTT_CONF_H

#define SEGGER_RTT_MAX_NUM_UP_BUFFERS     (1)
#define SEGGER_RTT_MAX_NUM_DOWN_BUFFERS   (1)

#define SEGGER_RTT_BUFFER_SIZE_UP         (1024)
#define SEGGER_RTT_BUFFER_SIZE_DOWN       (16)

#define SEGGER_RTT_MODE_DEFAULT           SEGGER_RTT_MODE_NO_BLOCK_SKIP

#define SEGGER_RTT_PRINTF_BUFFER_SIZE     (256)

#endif
```
