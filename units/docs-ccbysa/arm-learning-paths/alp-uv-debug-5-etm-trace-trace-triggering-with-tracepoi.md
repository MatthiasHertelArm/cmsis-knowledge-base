---
id: "alp-uv-debug-5-etm-trace-trace-triggering-with-tracepoi"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / Trace Triggering with Tracepoints"
summary: "The data stream capture can be controlled and filtered by using tracepoints. μVision has three types of trace trigger commands:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#trace-triggering-with-tracepoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

The data stream capture can be controlled and filtered by using tracepoints. μVision has three types of trace trigger commands:

1. [TraceRun](https://developer.arm.com/documentation/101407/latest/Debug-Commands/TraceRun--ETM-): Starts ETM trace collection when encountered.
2. [TraceSuspend](https://developer.arm.com/documentation/101407/latest/Debug-Commands/TraceSuspend--ETM-): Stops ETM trace collection when encountered. ETM tracing must have been started with **TraceRun**.
3. [TraceHalt](https://developer.arm.com/documentation/101407/latest/Debug-Commands/TraceHalt): Stops all trace data, including ETM. Trace collection can be resumed only with a STOP/RUN sequence in the µVision debugger.

They are selected from the context menu by right-clicking on a valid assembly instruction in the **Disassembly** window or a **C source line**:

(figure: Insert Trace Point)

#### How it works

When a **TraceRun** is encountered on an instruction while the program is running, ULINKpro will start collecting trace records. When a **TraceSuspend** is encountered, trace records collection will stop there. *Everything* in between these two will be collected. This includes all instructions through any branches, exceptions and interrupts. Sometimes there is some skid past the trigger point which is normal.

#### Setting Trace Triggers

Setup the current application:

1. Stop the program, but stay in debug mode.
2. In `Blinky.c`, set a breakpoint near line 46: `EventStartA(11);`.
3. (figure: Run) **Run (F5)** the application. Once it hits the breakpoint, it stops.
4. Remove the breakpoint.
5. (figure: Step into) **Step (F11)** once to enter the function `EventRecord2`.

Setup the Trace Triggers:

1. In the file `EventRecorder.c`, right click on the grey (or green) block opposite near line 1120.
7. Select **Insert Tracepoint at or near line 1120** and select **TraceRun (ETM)**. A cyan T will appear next to that line.
8. Right-click on the gray (or green) block opposite line 1136 `return ret;`.
9. Select **Insert Tracepoint at line 1136** and select **TraceSuspend (ETM)**. A cyan T will appear:  
   (figure: Tracepoints set)
10. Clear the **Trace Data** window for convenience. This is an optional step.
11. (figure: Run) **Run (F5)** the application and after a few seconds click (figure: Stop) **Stop**.
12. Filter exceptions out by selecting **ETM – Code Exec** in the **Display:** in the **Trace Data** window:  
    (figure: Display Code Exec)
13. Examine the **Trace Data** window:  
    (figure: Tracepoints)
14. In the [**Command**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Command-Window) window, enter `TL` and press "Enter" to display the two tracepoints:
    (figure: Tracepoints List)
15. Enter `TK*` in the **Command** window and press "Enter" to delete all tracepoints.

#### Trace Skid

The trace triggers use the same CoreSight hardware as the [Watchpoints](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#watchpoints). This means that it is possible a program counter skid might happen. The program might not start or stop on the exact location you set the trigger to. You might have to adjust the trigger point location to minimize this effect. This is because of the nature of the comparators in the CoreSight module and it is normal behavior.
