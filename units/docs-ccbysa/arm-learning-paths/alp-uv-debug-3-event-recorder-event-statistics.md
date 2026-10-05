---
id: "alp-uv-debug-3-event-recorder-event-statistics"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Event Statistics"
summary: "You can add start and stop events to your source code to collect information about execution counts and times. If you are using a ULINKplus debug adapter, information can also include voltage, current, and total charge (Q) consumed."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#event-statistics"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

You can add start and stop events to your source code to collect information about execution counts and times. If you are using a ULINKplus debug adapter, information can also include voltage, current, and total charge (Q) consumed. Individual and aggregate times are provided in the [**Event Statistics**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Event-Recorder/Event-Statistics-Window) window. This information will be collected between the start and stop event tags including the execution of any exception handlers or program branches.

- **Start:** The basic function calls are `EventStartX(slot)` and `EventStartX(slot, v1, v2).`
- **Stop:** The basic function calla are `EventStopX(slot)` and `EventStopX(slot, v1, v2)`.
- These calls are arranged in four groups (X = A, B, C, D). v is for data value.
- Each group has 15 slots (0 to 15). Stop events for slot = 15 creates a global stop for all slots of a group.
- Examples:  
  ```c
  EventStartA(2);
  EventStopA(2);
  EventStartB(4,34, counter);
  ```

#### Set Core Clock for Timing Measurements

For correct timing information when working with real hardware, the core clock needs to be set up correctly.

1. Go to (figure: Options for Target) **Project - Options for Target... (Alt+F7)** and select the **Debug** tab.
2. Select the **Settings** icon to the right of this window.
3. Select the **Trace** tab.
4. Enter the correct **Core Clock:** value. μVision uses this setting to calculate timing values displayed in some windows.
5. Click **OK** twice to return to the main μVision menu.

**Note:**
The above is not required in simulation!


#### Add the EventStart and EventStop Events

1. If running, (figure: Stop) **stop** the program and (figure: Start/stop debug) **exit** debug mode (Ctrl+F5).
2. Add this code near line 47:  
   ```
   EventStartA(11);
   ```
3. Add this code near line 51:  
   ```
   EventStopA(11);
   ```
3. Go to (figure: Save All) **File - Save All**.
3. Go to (figure: Build) **Project - Build Target (F7)**.
1. (figure: Build) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
5. Go to **View - Analysis Windows** and select (figure: Event Statistics) **Event Statistics** to see the event coming in.
1. (figure: Run) **Run (F5)** the application.
4. The **Event Statistics** window displays timing data between the start and stop function calls:  
   (figure: Event Statistics window)
5. Event Group A is displayed, showing slot 11 as indicated.
6. The execution time statistics are displayed for minimum, maximum, and average execution times (do not differ in simulation). This makes it easy for you to determine these statistical values for locations in your sources.

This provides a good method to determine timings relative to your source code. Event Statistics is easy to configure and interpret. You can create up to 64 start/stop events.

**Notes:**
- Refer to [Event Statistics Window](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Event-Recorder/Event-Statistics-Window) for an in-depth explanation of this window.
- Refer to [Event Recorder](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Event-Recorder) to learn how to save Event Statistics information.
