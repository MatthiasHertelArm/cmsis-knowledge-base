---
id: "alp-uv-debug-5-etm-trace-instruction-trace"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / Instruction Trace"
summary: "Instruction trace enables the review of historical data of the application execution."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#instruction-trace"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

Instruction trace enables the review of historical data of the application execution.

#### Open the Trace Data Window and Confirm Trace is Working

1. **Start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
1. (figure: Open Trace Data Window) Go to **View - Trace** and select **Trace Data**.
2. The Trace Data window will look similar to the one below if it is working correctly:  
   (figure: ETM Trace Data Window)
3. If you do not see trace frames in this window, go to **View - Trace** and select **Enable Trace Recording**.

**Notes:**
- You must stop the program to view the trace frames in the **Trace Data** window.
- All frames are executed instructions with source if available.
- The **Function** column displays the name of its function with the first instance highlighted in orange.


#### View ETM Frames starting at Reset

1. Scroll to the top of the **Trace Data** window to the first frame. This is the first instruction executed after the initial RESET sequence. In this case, it is a `LDR` instruction in the RESET_Handler function as shown below:  
   (figure: ETM Trace from Reset)
2. If you use the **Memory** window to look at location `0x04`, you will find the address of the first instruction there and this will match with that displayed in the first frame. In my case it is `0x1A00_1330 + 1 = 0x1A00_1331` (+1 says it is a [Thumb® instruction](https://developer.arm.com/documentation/ddi0210/c/Introduction/Architecture/The-Thumb-instruction-set)). The first occurrence in a function is highlighted in orange to make the start of functions easier to find.
3. Any source code associated with an instruction is displayed in the **Src Code / Trigger Addr** column.
4. If you double-click on any line, this will be highlighted in both the **Disassembly** and the relevant source window.

**Note:**
If you unselect **Run to main()** in the **Debug** tab of the (figure: Options for Target) **Options for Target...** window, no instructions will be executed when you enter debug mode. The program counter will be `0x1A00_1330`. You can run or single-step from that point and this will be recorded in the **Trace Data** window.


#### How to Find Interesting Trace Frames

Capturing all the instructions executed is possible in simulation and with ULINKpro but this might not be practical. It is not easy sorting through millions of trace frames or records looking for the ones you want. Use **Trace Filters**, **Find**, or save everything to a file and search with a different application program such as a spreadsheet.

*Trace Filters*

In the **Trace Data** window, you can select various types of frames to be displayed. The **Display:** box shows the various options available:  
(figure: Trace Data Display Filtering)

**Note:**
These filters are post collection.


#### Find a Trace Record

In the **Find a Trace Record** box, enter `bx` as shown here:  
(figure: Find a Trace Record Box)

You can select properties/columns where you want to search in the “in” box.

Select the **Find a Trace Record** icon (figure: Find a Trace Record Icon) and the following screen opens:  
(figure: Find a Trace Record Window)

Click on **Find Next** and each time it will step through the trace records highlighting each occurrence of the instruction `bx`. Or you can press "Enter" to go to the next occurrence of the search term.
