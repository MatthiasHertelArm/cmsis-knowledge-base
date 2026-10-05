---
id: "alp-uv-debug-2-basics-watchpoints"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Use basic run/stop debug: Watchpoints"
summary: "If you put a RAM address as the expression with no value, the next read and/or write (as you selected) will cause the program to halt. This can be particularly useful in the Stack."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#watchpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

**Watchpoints** can be thought of as conditional (access) breakpoints. Most Armv7-M and Armv8-M based processors have four data comparators. Since each watchpoint uses two comparators, you can configure two of them. The **Logic Analyzer** uses the same comparators in its operations. This means in μVision you must have two variables free in the Logic Analyzer to use watchpoints. μVision supports only one watchpoint.

**Note:**
The following does not work with the FVP used in this example. Switch to a real hardware target to use watchpoints.


### Configure a Watchpoint

1. Go to **Debug - Breakpoints (Ctrl-B)** to open the **Breakpoints** window.
3. In the **Expression** box, enter g_msTicks==0x44.
4. Select both the **Read** and **Write Access**.
5. Click on **Define** and it will be accepted as shown here:  
(figure: Breakpoints Window)
6. Click on Close.
7. (figure: Run) **Run (F5)** the application.
8. When `g_msTicks` equals `0x44`, the program will halt.
9. You will see `g_msTicks` displayed with a value of 0x44 in the Watch window:  
(figure: Watch Window)
10. Delete the watchpoint by selecting **Kill All** in the **Breakpoints** window or use (figure: Kill all Breakpoints in Current Target) **Kill all Breakpoints in Current Target**.
11. Select Close.
12. Leave Debug mode.

### Use a Watchpoint in the Stack Space

If you put a RAM address as the expression with no value, the next read and/or write (as you selected) will cause the program to halt. This can be particularly useful in the Stack. Set an address at some limit and if the program reads or writes this address, the program stops.

1. In this example a watchpoint is created with address `0x2000_0008`.
2. Running the program, the first read or write will stop the processor.
3. The [**Command**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Command-Window) window shows the setting of this Watchpoint and its execution including the approximate instruction location:
(figure: Command Window)

**Notes:**
- Skid: The instruction noted will not be the instruction causing the break as it has not been executed yet. It will be noted in **Disassembly**.
- The instruction causing the break is probably a few instructions before this one in the execution stream.
- To edit a watchpoint, double-click on it in the **Breakpoints** window and its information will be dropped down into the configuration area. Clicking on **Define** will create another watchpoint. You should delete the old one by highlighting it and click on Kill Selected or use the following tip.
- The checkbox beside the expression in **Current Breakpoints:** as shown above allows you to temporarily unselect or disable a watchpoint without deleting it.
- You can create a watchpoint with a raw address and no variable value. This is useful for detecting stack overruns. Physical addresses can be entered as `*((unsigned long *)0x20000000)`. Or enter the address as shown above.
