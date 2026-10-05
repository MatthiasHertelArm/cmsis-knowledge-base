---
id: "alp-uv-debug-2-basics-watch-and-memory-windows"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Use basic run/stop debug: Watch and Memory Windows"
summary: "The Watch and Memory windows display variable values in real-time using Arm CoreSight technology. It is also possible to put or insert values into these memory locations in real-time using the Memory window while the program is running."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/2_basics/#watch-and-memory-windows"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [**Watch**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Watch-Window) and [**Memory**](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Memory-Window) windows display variable values in real-time using Arm CoreSight technology. It is also possible to `put` or insert values into these memory locations in real-time using the **Memory** window while the program is running. You can change memory in a **Watch** window if data is not changing fast.

There is a global variable `g_msTicks` located in `Blinky.c` near line 11 that you can use in the **Watch** and **Memory** windows.

### Watch Window

1. (figure: Run) **Run (F5)** the application.
2. Right click on `g_msTicks` in `Blinky.c` near line 11 and select **Add 'g_msTicks' to…** and select **Watch 1**.
3. Go to **View** in the main menu and enable **Periodic Window Update**:  
(figure: Periodic Window Update)
4. `g_msTicks` will be displayed in **Watch 1**:  
(figure: g_msTicks in Watch 1 Window)
5. The values of `g_msTicks` are updated in real-time if *Periodic Window Update* is enabled.
6. You can modify the value in a **Watch** window when the program is stopped or changing slowly. You can modify a variable in a **Memory** window anytime (see next section).

#### Add the SystemCoreClock Variable

1. Click on `<Enter expression>` twice and enter: `SystemCoreClock`
2. Right click on the `Value` and deselect **Hexadecimal Display**. 32 MHz will be displayed:  
(figure: SystemCoreClock in Watch 1 Window)

**Note:**
You do not need to stop the program execution to enter variables, raw addresses or structures in a **Watch** or **Memory** window.


### Memory Window

1. Right click on `g_msTicks` and select **Add ‘`g_msTicks` ' to…** and select **Memory 1**.
2. Note the changing value of `g_msTicks` is displaying its address in **Memory 1** as if it is a pointer. This is useful to see what address a pointer is pointing to. But this not what you want to see at this time.
3. Right click in **Memory 1** and select **Unsigned Long** to see the data field as 32-bit numbers.
4. Add an ampersand `&` in front of the variable name `g_msTicks` and press Enter. Now the physical address is shown (0x2000_0008) in this case. This physical address could change with different compilation optimizations.
5. The data contents of `g_msTicks` is displayed as shown:  
(figure: g_msTicks in Memory 1 Window)
6. Right click on the memory data value and select **Modify Memory at 0x3000000C**. Enter a value and this will be pushed into `g_msTicks`. Since `g_msTicks` is updated often, you will only see the new value displayed for a very short time.
7. (figure: Stop) **Stop** the application.

**Notes:**
- You can configure the **Watch** and **Memory** windows while the program is running in real-time without using any CPU cycles. You can change a Memory window value on-the-fly.
- [**View - Periodic Window Update**](https://developer.arm.com/documentation/101407/latest/User-Interface/View-Menu) must be selected. Otherwise variables update only when the program is stopped.


#### How It Works

μVision uses Arm CoreSight technology to read or write memory locations without using CPU cycles. Most of the time, this is non-intrusive and does not impact the program execution timings. The Armv7-M/Armv8-M are Harvard architectures. This means they have separate instruction and data buses. While the CPU is fetching instructions at full speed, there is plenty of time for the CoreSight debug module to read or write to memory without stealing any CPU cycles. This can be slightly intrusive in the unlikely event the CPU and μVision reads or writes to the same memory location at exactly the same time. Then the CPU will be stalled for one clock cycle. In practice, this use of additional CPU cycles never happens.
