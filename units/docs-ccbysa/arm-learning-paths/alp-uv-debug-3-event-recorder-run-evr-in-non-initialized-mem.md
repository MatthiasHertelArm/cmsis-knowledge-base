---
id: "alp-uv-debug-3-event-recorder-run-evr-in-non-initialized-mem"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Run EVR in Non-initialized Memory"
summary: "In the Command window, you will see Warning: Event Recorder not located in uninitialized memory!. This can be safely ignored for the purpose of this tutorial."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#run-evr-in-non-initialized-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

In the [**Command**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Command-Window) window, you will see `Warning: Event Recorder not located in uninitialized memory!`. This can be safely ignored for the purpose of this tutorial.

In general, it can be important to preserve the EVR data located in the target's RAM in the event of a crash and/or reset. Creating and using non-initialized memory is implemented by modifying the scatter file. [Knowledge base article KA003868](https://developer.arm.com/documentation/ka003868/latest) explains how to modify your project to do so.
