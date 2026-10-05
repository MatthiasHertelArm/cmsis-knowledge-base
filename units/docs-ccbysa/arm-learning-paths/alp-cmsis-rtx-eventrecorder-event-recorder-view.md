---
id: "alp-cmsis-rtx-eventrecorder-event-recorder-view"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: Event recorder view"
summary: "Use the menu (View > Analysis Windows > Event Recorder) to open the viewer."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#event-recorder-view"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use the menu (`View` > `Analysis Windows` > `Event Recorder`) to open the viewer.

Note that the RTX source contains many Event Recorder annotations.

For ease of readability, click the `Filter` icon to hide these events. Ensure `STDIO` events are enabled.

(figure: Screenshot of the Event Viewer filter dialog showing event categories with STDIO enabled and RTX events disabled for easier readability#center)

Observe that printf output is in the form of the ASCII codes of the text output.

(figure: Screenshot of the Event Viewer showing STDIO events with printf output displayed as ASCII codes#center)

For this view it's better to use [EventRecorder Data](https://www.keil.com/pack/doc/compiler/EventRecorder/html/group__EventRecorder__Data.html) rather than printf statements.
