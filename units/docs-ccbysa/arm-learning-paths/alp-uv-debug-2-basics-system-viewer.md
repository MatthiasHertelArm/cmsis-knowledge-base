---
id: "alp-uv-debug-2-basics-system-viewer"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Use basic run/stop debug: System Viewer"
summary: "The System Viewer provides the ability to view certain registers of peripherals and the CPU core. In many cases, these windows are updated in real-time while your program is running. They are available only in debug mode."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#system-viewer"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [**System Viewer**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/System-Viewer) provides the ability to view certain registers of peripherals and the CPU core. In many cases, these windows are updated in real-time while your program is running. They are available only in debug mode. Go to **Peripherals - System Viewer** to open the peripheral windows. Select CPU core registers by going to **Peripherals - Core Peripherals**.

#### SysTick Timer

The example application uses the Arm Cortex-M system tick timer.

1. (figure: System Viewer) Go to **Peripherals - Core Peripherals** and then select **System Tick Timer S (SysTick)**.
2. The **SysTick Timer** window opens:  
(figure: SysTick Timer Window)
1. (figure: Run) **Run (F5)** the application.
6. While the program is running, type `0x10000` in the `SysTick -> LOAD` register and click in another register or press Enter.
7. The program execution will speed up. This is the power of Arm CoreSight debugging.
8. Replace LOAD with 0x007CFF. A (figure: Stop) **Stop** and (figure: Reset) **Reset** will also accomplish this.
9. When you are done, (figure: Stop) **Stop** the application and close the **SysTick Tick Timer (SysTick)** window.

**Notes:**
- The [documentation](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Core-Peripherals/Armv8-M-cores/Armv8-M--System-Tick-Timer) provides more information about the **System Tick Timer S (SysTick)** window.
- The window updates in real-time while your program is running.
- The `SysTick -> LOAD` register contains the reload register value. This value is set in `core_cm55.h` at line 4687:  
  ```C
  SysTick->LOAD  = (uint32_t)(ticks - 1UL);
  ```
  The value is set to 0x007CFF = dec 31,999. This is created by (32 MHz/1000)-1 = 31,999. 1000 is specified as the timer tick value. A SysTick S interrupt 15 will occur every 1 msec. Changing the reload value changes how often the SysTick interrupt 15 occurs.
- As you can modify values in the **System Viewer** while the program is running, you can make slight timing value changes instead of the usual modify, compile, program, run cycle.
- You must make sure a given peripheral register allows for and will properly react to such a change. Changing such values indiscriminately is a good way to cause serious problems that are difficult to find.
