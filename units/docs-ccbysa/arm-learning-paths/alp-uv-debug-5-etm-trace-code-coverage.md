---
id: "alp-uv-debug-5-etm-trace-code-coverage"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / Code Coverage"
summary: "The µVision debugger provides Code Coverage with the FVP or via ETM using ULINKpro."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#code-coverage"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

**Code Coverage** tells what assembly instructions were executed. It is important to ensure all assembly code produced by the compiler is executed and tested. You do not want a bug or an unplanned circumstance to cause a sequence of untested instructions to be executed. The result could be catastrophic. Functional safety applications require **Code Coverage** for certification.

The µVision debugger provides **Code Coverage** with the FVP or via ETM using ULINKpro.

1. (figure: Start/Stop Debug) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
1. In Blinky.c, set a breakpoint at `if (g_ledSet) {` (near line 56).
2. (figure: Run) **Run (F5)** the application. Once it hits the breakpoint, it stops. Remove the breakpoint.
3. Examine the **Disassembly** and **Blinky.c** windows. Scroll and notice the different color blocks in the left margin:  
   (figure: Code Coverage in Disassembly)  
   This is **Code Coverage** provided by ETM trace. This indicates if an instruction has been executed or not.

Color blocks indicate which assembly instructions have been executed:

(figure: Light Grey) There is no assembly instruction here.  
(figure: Dark Grey) This assembly instruction was not executed.  
(figure: Green) This assembly instruction was executed.  
(figure: Orange) A Branch is never taken.  
(figure: Cyan) A Branch is always taken.  
(figure: Breakpoint) A Breakpoint is set here.  
(figure: Next Statement) This points to the next instruction to be executed.

**Note:**
Code Coverage is visible in both the **Disassembly** and **source code** windows. Click on a line in one window and this place will be matched in the other window.


#### Code Coverage Window

A separate [**Code Coverage**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Code-Coverage) window is available that shows statistics.

(figure: Open Code Coverage Window) Go to **View - Analysis Windows** and select **Code Coverage**:  
(figure: Code Coverage Window)

#### Code Coverage Data in the Command Window

In the [**Command**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Command-Window) window, you can show Code Coverage in many ways, for example, enter `coverage \Blinky.c\main details`:  
(figure: Code Coverage in Command Window)

**Note:**
You can copy and paste the result from the **Command** window by right-clicking into it. Save the data in a convenient format.


#### Save Code Coverage Data

Code Coverage information is temporarily saved during a run and is displayed in various windows as shown. It is possible to save this information in an ASCII file for use in other programs. You can save Code Coverage data in two formats:

1. In a [.gcov](https://en.wikipedia.org/wiki/Gcov) file. In the **Command** window execute:
   ```
   COVERAGE GCOV module
   ```
   or
   ```
   COVERAGE GCOV *
   ```
2. In an ASCII file using the `log` command.  
   Send Code Coverage data to a file (the specified directory must exist):
   ```
   log > c:\cc\test.txt
   ```
   Provides the data for `log` (you can also specify a module or function):
   ```
   coverage asm
   ```
   Turn the log function off:
   ```
   log off
   ```
