---
id: "alp-uv-debug-2-basics-call-stack-locals-window"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Use basic run/stop debug: Call Stack + Locals Window"
summary: "The Call Stack + Locals window displays call stack contents as well as any local variables belonging to the active function. If possible, the values of the local variables will be displayed."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#call-stack-locals-window"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [**Call Stack + Locals**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Call-Stack-and-Locals-Window) window displays call stack contents as well as any local variables belonging to the active function. If possible, the values of the local variables will be displayed. If this is not possible, a message such as `<not in scope>` will be displayed. The **Call Stack + Locals** window visibility can be toggled by selecting **View - Call Stack window**.

### Call Stack Use Case

When the program is stopped, the list of stacked functions is displayed. This is when you need to know which functions have been called and are stored on the stack. This is useful to find program flow problems such as crashes. Normal functions are displayed only when they are on the stack. They are removed and added as appropriate.

1. Stop the program with the (figure: Stop) **Stop** icon. The program will probably stop in the `Delay` function.
2. Click on the **Call Stack + Locals** window in the bottom right corner of μVision.
3. Inspect the various entries in the Call Stack + Locals window as shown below in this simple example. Local variables are displayed only when they are in scope:  
   (figure: Call Stack + Locals Window)  
1. Set a breakpoint in the `while (1)` loop at line 50 on the `g_ledSet = 1;`.
5. (figure: Run) **Run (F5)** the application.
6. Shortly after, the program will stop there.
1. (figure: Step into) **Step (F11)** with Blinky.c in focus (its name in its tab is underlined).
9. Note how the variables displayed change in the **Call Stack + Locals** window.
1. (figure: Step into) **Step (F11)**  a few more times.
1. Right-click on a function and select either **Show Caller Code** or **Show Callee Code** and this will be highlighted in the **Disassembly** and **source code** windows:  
   (figure: Call Stack + Locals Window)
1. (figure: Step out) **Step Out (Ctrl+F11)** to exit a function immediately.
1. Remove the **Breakpoint** (by clicking on its red circle (figure: Breakpoint)) to continue.

**Notes:**
- You can modify a variable value in the **Call Stack & Locals** window when the program is stopped.
- This window is only valid when the processor is halted. It does not update while the program is running because locals are normally kept in a CPU register which cannot be read by the debugger while the program is running. Any local variable values are visible only when they are in scope.
- This is standard “run/stop” debugging. With Arm CoreSight debug technology you can do more. You can display global or static variables and structures updated in real-time while the program is running. No additions or changes to your code are required. They only must be converted to global or static variables so they always remain in scope.
- When Keil RTX5 is used, all threads are displayed, even if they are not running. The active thread name and its number are highlighted in green.
- Single (figure: Step into) **Step (F11)**: If you click inside a source window to bring it into focus, the program will step one source line at a time. If you click inside the **Disassembly** window to bring it into focus, it will then step one instruction at a time.
