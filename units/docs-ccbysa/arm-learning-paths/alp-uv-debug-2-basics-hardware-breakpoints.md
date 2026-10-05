---
id: "alp-uv-debug-2-basics-hardware-breakpoints"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Use basic run/stop debug: Hardware Breakpoints"
summary: "To use hardware breakpoints in µVision follow the steps outlined below:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#hardware-breakpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

To use hardware breakpoints in µVision follow the steps outlined below:

1. (figure: Build) **Build (F7)** the example Blinky project you opened.
1. (figure: Start debug) **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
1. (figure: Run) **Run (F5)** the application.
1. Bring `Blinky.c` in focus by clicking on its tab. If it is not visible, double-click on it in the **Project** window.
3. In `Blinky.c`, scroll down to the `while (1)` loop in the `main` function near line 42 as shown here:  
(figure: Inside the while loop)
4. Note the darker grey blocks on the left of the line numbers. They indicate assembly code being present and that you can set a hardware breakpoint on these lines. You can also see these blocks in the **Disassembly** window:  
(figure: while loop Disassembly)
5. While the program is still running, click to the left of a suitable line in the `while` loop (for example at line 47) and a red circle will be created. This is a hardware breakpoint. The simulated Arm Cortex-M55 has eight hardware breakpoints. μVision will warn you if you exceed this limit.
6. The program will soon stop at the line where you have set the breakpoint on as shown below. The yellow arrow is the current program counter position. This will be the next instruction executed. The cyan arrow is a placeholder you can use to explore the relationship between a source window and the **Disassembly** window.  
(figure: Program execution stopped)
7. Add another breakpoint in `while (1)` (for example at line 50).
8. Each time you click on (figure: Run) **Run (F5)**, the program will cycle to the next breakpoint.

**Notes:**
- Sometimes the compiler will optimize out code. Breakpoints cannot be set on this code as shown by the lack of grey blocks. Setting the compiler to an optimization level of `-O0` will usually help (this is set in this example project already).
- You can set/unset hardware breakpoints with μVision while the program is running or stopped.
- Arm hardware breakpoints are no skid. They do not execute nor change the instruction they are set to.
- Your instructions in flash are not substituted or modified. Your flash contents are not changed.
- There is no intrusion to hardware or your program by Arm hardware breakpoints.


### Manage Breakpoints

1. Go to **Debug - Breakpoints (Ctrl-B)** to manage breakpoints:  
(figure: Manage Breakpoints)
2. You can temporarily unselect, delete or create breakpoints in this window. It is easier to create a breakpoint by clicking in a source file or the **Disassembly** window.
3. [Watchpoints](#watchpoints) are also created in this window.
4. Select **Kill All** to remove all breakpoints.
5. Click **Close**.
6. Continue to (figure: Run) **Run (F5)** for the next exercise.

**Note:**
For breakpoint expression examples, refer to the [Breakpoints Window](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Breakpoints-Window) documentation.
