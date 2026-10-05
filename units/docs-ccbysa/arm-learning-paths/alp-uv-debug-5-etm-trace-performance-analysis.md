---
id: "alp-uv-debug-5-etm-trace-performance-analysis"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / Performance Analysis"
summary: "It is useful to optimize your code for speed. Performance Analyzer tells you how much time was spent in each function as well as the total number of total calls. A graphical display is generated for a quick reference."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#performance-analysis"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

It is useful to optimize your code for speed. [**Performance Analyzer**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Performance-Analyzer) tells you how much time was spent in each function as well as the total number of total calls. A graphical display is generated for a quick reference. If you are optimizing for speed, work first on those functions taking the longest time to execute.

The µVision debugger provides **Performance Analysis** with the FVP (number of calls only) or via ETM using ULINKpro.

1. (figure: Start/Stop Debug) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
2. (figure: Open Code Coverage Window) Go to **View - Analysis Windows** and select **Performance Analysis**:  
   (figure: Performance Analyzer Window)
4. *Do not* click on (figure: Run) **Run (F5)** yet!
4. Expand some of the module names as shown above.
5. Shown is the number of calls and percentage of total time in this short run from reset to the start of `main()`.
6. Now, (figure: Run) **Run (F5)** the application. The **Performance Analyzer** window updates in real-time:  
   (figure: Performance Analyzer Updated)

**Notes:**
- Double-click on any **Function** or **Module** name and this will be highlighted in the **Disassembly** or **source code** windows.
- Select **Show: Functions** from the pull down box and notice the difference.
- You can reset the **Performance Analyzer** window by clicking on (figure: Performance Analyzer Reset). Watch as new data is displayed in the window.
