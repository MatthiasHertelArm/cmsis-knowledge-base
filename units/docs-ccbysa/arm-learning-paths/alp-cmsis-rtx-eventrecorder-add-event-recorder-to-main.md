---
id: "alp-cmsis-rtx-eventrecorder-add-event-recorder-to-main"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: Add Event Recorder to main"
summary: "Add a function call to initialize the event recorder. Open main.c in the editor."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#add-event-recorder-to-main"
license: "CC-BY-SA-4.0"
mode: "V"
---

Add a function call to initialize the `event recorder`. Open `main.c` in the editor.

Include the header file:
```C
#include "EventRecorder.h"
```
Add this function call to `main()`, before `osKernelInitialize()`:
```C
	EventRecorderInitialize (EventRecordAll, 1);	// initialize and start Event Recorder
```
