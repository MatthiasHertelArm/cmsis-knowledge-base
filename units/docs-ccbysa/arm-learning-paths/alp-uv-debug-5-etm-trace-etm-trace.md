---
id: "alp-uv-debug-5-etm-trace-etm-trace"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace"
summary: "Many Armv7-M/Armv8-M devices include an Embedded Trace Macrocell (ETM) which provides instruction trace. When streaming instruction trace directly to your PC, the µVision debugger enables review of historical sequences, execution profiling, performance optimization, and code coverage analysis."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#etm-trace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many Armv7-M/Armv8-M devices include an **Embedded Trace Macrocell (ETM)** which provides instruction trace. When streaming instruction trace directly to your PC, the µVision debugger enables [review of historical sequences](#instruction-trace), [execution profiling](#execution-profiling), [performance optimization](#performance-analysis), and code [coverage analysis](#code-coverage).

#### Types of Problems that can only be found with ETM Trace

There are certain types of problems that can only be found with a quality trace, such as:

1. Pointer problems.
2. Illegal instructions and data aborts (such as misaligned writes): How I did I get to this fault vector?
3. Code overwrites – writes to Flash, unexpected writes to peripheral registers: How did I get here?
4. A corrupted stack.
5. Out of bounds data. Uninitialized variables and arrays.
6. Stack overflows: What causes the stack to grow bigger than it should?
7. Probably the most important use: an application has gone off into the weeds and you need to know what instruction caused this.
8. Communication protocol and timing issues.
1. System timing problems.
1. Profile Analysis and Code Coverage is provided. Available only with ETM trace.

#### FVPs: Configure the Target Driver Setup to use ETM Trace

The Corstone-300 FVP can be used to collect instruction trace data with a two-step approach. First, you run the simulation and collect the data. Then, you restart the simulation and load the coverage file that was created in the first step to use the data in µVision. Follow these steps to set this up in µVision:

1. Open a Windows Explorer and copy the file `MTItoCoverage.dll` from `C:\Keil_v5\ARM\VHT` to `C:\Keil_v5\ARM\FVP\Corstone-300\models\Win64_VC2017`. This file is required to extract the coverage data from a previous run.
1. In µVision, Go to (figure: Options for Target) **Project - Options for Target... (Alt+F7)** and switch to the **Debug** tab.
2. On the right-hand side, select **Models ARMv8-M Debugger** and click on **Settings**. The **Models ARMv8-M Target Driver Setup** window opens.
3. Select a coverage file (enter a name for the file and it will be generated automatically).
1. Enable **Load Coverage on Connect** and **Store Coverage on Disconnect**:
   (figure: Models ARMv8-M Target Driver Setup)
1. Click **OK** twice.

When you now start a debug session, the coverage information is recorded. When you leave the debug session, the data is written to the coverage file specified. Next time you start a debug session, the file is opened and the information is used. This method does not provide [Instruction Trace](#instruction-trace) data, so you can move directly to the [Code Coverage](#code-coverage) section.

#### Hardware: Configure the Target Driver Setup to use ETM Trace

For the following, you need to connect a [ULINKpro](https://developer.arm.com/Tools%20and%20Software/ULINKpro) debug and trace adapter to your target board using the [20-pin Cortex+ETM connector](https://developer.arm.com/documentation/kan339/latest).

1. Go to (figure: Options for Target) **Project - Options for Target... (Alt+F7)** and switch to the **Debug** tab.
1. Remove any **Initialization File** that might be present.
2. On the right-hand side, select **ULINK Pro Cortex Debugger** and click on **Settings**. The **Target Driver Setup** window opens.
3. Select the **Trace** tab:  
   (figure: Target Driver Setup Window)
4. In **Core Clock:** enter the correct core clock of your target device. This value will be used for calculating timing values.
5. If your device runs a different trace clock, you might need to unselect **Use Core Clock** and enter the correct trace clock speed. 
4. Select **Trace Enable** for SWV data trace.
4. Select **ETM Trace Enable** for ETM.
5. Set **Trace Port** to **Sync Trace Port with 4-bit Data**.
6. The last 1 million trace frames will be saved with the older ones being overwritten. If you need to save them all, select also **Unlimited Trace**. Your hard drive space will determine how many are saved. ULINKpro is a streaming trace.
10. ETM and SWV are now configured and ready to use. Click **OK** twice to return to the main μVision menu.
