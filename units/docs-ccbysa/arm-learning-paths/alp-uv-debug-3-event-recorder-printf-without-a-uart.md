---
id: "alp-uv-debug-3-event-recorder-printf-without-a-uart"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / printf without a UART"
summary: "μVision provides a simple printf utility using the Event Recorder. It does not require a UART and it is much faster. Text is displayed in the Debug (printf) Viewer window."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#printf-without-a-uart"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

μVision provides a simple `printf` utility using the **Event Recorder**. It does not require a UART and it is much faster. Text is displayed in the [**Debug (printf) Viewer**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Debug--printf--Viewer) window.

#### Configure Event Recorder

1. If it is running, (figure: Stop) **stop** the application and (figure: Start/Stop Debug) **exit** debug mode (Ctrl+F5).
2. (figure: Manage Run-Time Environment) Go to **Project - Manage - Run-Time Environment**.
3. Expand **Compiler** and enable **Event Recorder:DAP** and **I/O:STDOUT:EVR** as shown:
(figure: Manage Run-Time Environment Window)
5. The **Validation Output** window should be empty. If not, click on the **Resolve** button to enable other missing software components.
7. Click **OK** to close this window.
8. `retarget_io.c`, `EventRecorder.c`, and `EventRecorderConf.h` will be added to your project under the **Compiler** group in the **Project** window:  
(figure: New compiler component)
9. Right click near the top of `Blinky.c` (at line 7), choose **Insert '#include file'**, and select:
   ```c
   #include "EventRecorder.h"
   ```
10. In the `main()` function (near line 39), after `SystemCoreClockUpdate();`, add these lines:
    ```c
    EventRecorderInitialize(EventRecordAll,1);
    EventRecorderStart();
    ```

#### Use Event Recorder

Now, create a global variable named `counter` whose value will be printed on **Debug (printf) Viewer** window.

1. In Blinky.c, near line 14, declare the global variable counter:
   ```c
   uint32_t counter = 0;
   ```
2. Add these two lines after the `Delay(1000)` statement at line 46:  
   ```c
   counter++;
   if (counter > 0x0F) counter = 0;
   ```
1. Near the top of the file (around line 80), add:
   ```c
   #include "stdio.h"
   ```
2. Near line 48, after the statement `if (counter > 0x0F…`), add:
   ```c
   printf("Hello %d\n", counter);
   ```
3. Go to (figure: Save All) **File - Save All**.
3. Go to (figure: Build) **Project - Build Target (F7)**.
1. (figure: Build) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
1. (figure: Run) **Run (F5)** the application.
3. (figure: Debug (printf)) Go to **View - Serial Windows** and select **Debug (printf) Viewer**.
4. The values of counter are displayed as seen here:  
   (figure: Output in the Debug (printf) Viewer window)
5. Go to **View - Analysis Windows** and select **Event Recorder** to see information about the printf statements:  
   (figure: printf information in the Event Recorder window)
8. (figure: Stop) **Stop** the program and (figure: Start/stop debug) **exit** debug mode (Ctrl+F5).

**Notes:**
- When using real hardware, select the **::Compiler:Event Recorder:DAP** variant.
- The FVP model supports semihosting. It requires the following entry in the configuration file (already done in the example project):  
  `cpu0.semihosting-enable=1`
