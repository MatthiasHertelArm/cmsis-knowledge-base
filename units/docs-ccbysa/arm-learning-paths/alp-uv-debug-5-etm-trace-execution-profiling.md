---
id: "alp-uv-debug-5-etm-trace-execution-profiling"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / Execution Profiling"
summary: "Execution Profiling is used to display how much time a C source line took to execute and how many times it was called. This information is provided by the ETM trace in real time while the program keeps running."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#execution-profiling"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

[**Execution Profiling**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Execution-Profiler) is used to display how much time a C source line took to execute and how many times it was called. This information is provided by the ETM trace in real time while the program keeps running.

The µVision debugger provides **Execution Profiling** with the FVP (number of calls only) or via ETM using ULINKpro.

1. (figure: Start/Stop Debug) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
2. Go to **Debug - Execution Profiling** and select **Show Time**.
3. (figure: Run) **Run (F5)** the application.
4. In the left margin of the **Disassembly** and **source code** windows various time values will be displayed.
8. Hover the cursor over a time and more information appears as in the yellow box here:  
   (figure: Execution Profiling)
9. You can also select **Debug - Execution Profiling - Show Calls** to display this information rather than the execution times in the left margin.

#### Outlining

At some places, there is an (figure: Outlining) **Outlining** sign that can be used to collapse a code section and to compress the associated source files together.

1. In `Blinky.c`, click in the **Outlining** square near the `while (1) {` loop near line 46:  
   (figure: Outlining in action)
2. The C source in the while loop is now collapsed into one line and times are added together to 8.380 us in this case.
5. Click on (figure: Expand Outlining) to expand it.

**Note:**
[Outlining](https://developer.arm.com/documentation/101407/latest/User-Interface/Edit-Menu-and-Commands/Outlining-Menu) can be useful to hide sections of code to simplify the window you are reading.
