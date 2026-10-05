---
id: "alp-cmsis-rtx-eventrecorder-define-the-event-recorder-buff"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: Define the Event Recorder buffer"
summary: "EventRecorder.o will use a buffer to store the generated data. This must be located in an uninitialized region of writable memory."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#define-the-event-recorder-buffer"
license: "CC-BY-SA-4.0"
mode: "V"
---

`EventRecorder.o` will use a buffer to store the generated data. This must be located in an uninitialized region of writable memory.

Edit the scatter file, creating a new execution region (after `ARM_LIB_STACK`):
```text
	EVENT_BUFFER 0x20060000 UNINIT 0x10000 {EventRecorder.o (+ZI)}
```
If you get a link-time warning:
```text
Warning: L6314W: No section matches pattern EventRecorder.o(ZI).
```
Verify that `Link-time optimization` was disabled in `C/C++ (AC6)` tab in the `Target Options` dialog.
