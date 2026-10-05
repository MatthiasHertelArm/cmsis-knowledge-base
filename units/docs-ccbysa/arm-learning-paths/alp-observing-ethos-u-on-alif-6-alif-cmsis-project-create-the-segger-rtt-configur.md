---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-create-the-segger-rtt-configur"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Create the SEGGER RTT configuration"
summary: "Real-Time Transfer (RTT) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#create-the-segger-rtt-configuration"
license: "CC-BY-SA-4.0"
mode: "V"
---

Real-Time Transfer (RTT) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring. 

Within `mnist_executorch/`, create the configuration file `SEGGER_RTT_Conf.h`:

```c
#ifndef SEGGER_RTT_CONF_H
#define SEGGER_RTT_CONF_H
#define SEGGER_RTT_MAX_NUM_UP_BUFFERS     (1)
#define SEGGER_RTT_MAX_NUM_DOWN_BUFFERS   (1)
#define SEGGER_RTT_BUFFER_SIZE_UP         (4096)
#define SEGGER_RTT_BUFFER_SIZE_DOWN       (16)
#define SEGGER_RTT_MODE_DEFAULT           SEGGER_RTT_MODE_NO_BLOCK_SKIP
#define SEGGER_RTT_PRINTF_BUFFER_SIZE     (256)
#endif
```
