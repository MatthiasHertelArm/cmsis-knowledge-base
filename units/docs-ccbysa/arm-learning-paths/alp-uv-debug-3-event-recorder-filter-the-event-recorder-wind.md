---
id: "alp-uv-debug-3-event-recorder-filter-the-event-recorder-wind"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Filter the Event Recorder Window"
summary: "It is possible to filter the window contents. Modify the information displayed in the Event Recorder window using the funnel icon which will open the Show Event Levels window."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#filter-the-event-recorder-window"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

It is possible to filter the window contents. Modify the information displayed in the Event Recorder window using the funnel icon which will open the **Show Event Levels** window. You can specify what elements are collected and displayed in the Event Recorder window.

1. If running, (figure: Stop) **stop** the program if necessary but stay in debug mode.
2. In the Event Recorder window, select (figure: Configure Target Event Recording) **Configure Target Event Recording**. The **Show Event Levels** window opens up:  
   (figure: Filter event levels)
3. Unselect all boxes opposite STDIO as shown above.
4. Click **OK** to close this window.
5. Click (figure: Clear) **Clear** to make it easier to see what is happening.
1. (figure: Run) **Run (F5)** the application.
7. The Event Recorder window no longer contains printf frames as shown below:  
   (figure: Filtered Event Recorder window)  
In this case, you only need to unselect the Op column. The other frames do not exist in this simple example.

#### Save Filter Settings

You can [save and recall](https://developer.arm.com/documentation/101407/latest/Debug-Commands/EventRecorder) the filter settings. In the [**Command**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Command-Window) window, execute:
```
ER SAVE path\filename
ER LOAD path\filename
```
