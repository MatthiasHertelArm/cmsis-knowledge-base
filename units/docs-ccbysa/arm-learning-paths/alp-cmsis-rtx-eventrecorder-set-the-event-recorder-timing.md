---
id: "alp-cmsis-rtx-eventrecorder-set-the-event-recorder-timing"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: Set the Event Recorder timing source"
summary: "Navigate the project tree to locate CMSIS-View > EventRecorderConf.h, and open this file."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#set-the-event-recorder-timing-source"
license: "CC-BY-SA-4.0"
mode: "V"
---

Navigate the project tree to locate `CMSIS-View` > `EventRecorderConf.h`, and open this file.

Click the `Configuration Wizard` tab.

Set `Event Recorder` > `Time Stamp Source` to `CMSIS-RTOS2 System Timer`, and save the file.

This change will be reflected in the source code as:

``` C
#define EVENT_TIMESTAMP_SOURCE  2
```
