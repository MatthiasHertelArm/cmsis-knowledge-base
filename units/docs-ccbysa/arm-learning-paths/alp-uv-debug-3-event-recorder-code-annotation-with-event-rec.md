---
id: "alp-uv-debug-3-event-recorder-code-annotation-with-event-rec"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Code Annotation with Event Recorder"
summary: "With Event Recorder, you can also annotate your source code which can be displayed in various information windows."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#code-annotation-with-event-recorder"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

With Event Recorder, you can also annotate your source code which can be displayed in various information windows.

#### Configure Event Recorder

1. Confirm that the configuration steps in the previous section were completed.
1. To add an event, insert this function call at the top of the `while(1)` loop (around line 47):
   ```c
   EventRecord2(3, 44, counter);
   ```
3. Go to (figure: Save All) **File - Save All**.
3. Go to (figure: Build) **Project - Build Target (F7)**.
1. (figure: Build) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
5. Go to **View - Analysis Windows** and select (figure: Event Recorder) **Event Recorder** to see the event coming in.
1. (figure: Run) **Run (F5)** the application.
5. Events will start to display in the **Event Recorder** window as shown below:  
   (figure: Events shown in the Event Recorder window)
6. You can see the results of the `EventRecord2(3, 44, counter);` event.
7. `printf` frames (stdout) are also displayed with the printf data in hexadecimal form.

**Notes:**
- Hover your mouse over **Event Property** entries to gain more information.
- Stop the recording by unselecting **Enable** in the upper left corner.
- When you re-enable it, events that were collected in the background as the program ran will be displayed.
