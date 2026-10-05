---
id: "alp-uv-debug-5-etm-trace-in-the-weeds-example"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Advanced debug with ETM trace: ETM Trace / In-the-Weeds Example"
summary: "This part of the tutorial requires real hardware with ETM trace capabilities as the Traca Data window is not available for FVP models."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/5_etm_trace/#in-the-weeds-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: ETM Trace_

This part of the tutorial requires real hardware with ETM trace capabilities as the **Traca Data** window is not available for FVP models.

Some of the hardest problems to solve are those when a crash has occurred and you have no clue what caused this – you only know that it happened and the stack is corrupted or provides no useful clues.

Modern programs tend to be asynchronous with interrupts and RTOS thread switching plus unexpected and spurious events. Having a recording of the program flow is useful especially when a problem occurs and the consequences are not immediately visible. Another problem is detecting race conditions and determining how to fix them. ETM trace handles these problems and others easily and it is easy to use.

In this example, a hard fault occurs and the CPU ends up at `0x1A00_133A` as shown in the **Disassembly** window (note that your address might not be the same as shown here):  
(figure: Hard Fault Handler)

This is the `HardFault_Handler`. This is a branch to itself and will run this instruction forever. The trace buffer will save millions of the same branch instructions, which is not very useful.

The hard fault handler exception vector is found in the startup file of your device. Set a breakpoint by clicking on the `HardFault_Handler` and run the program. At the next hard fault event, the CPU jumps to the `HardFault_Handler` and halts processing. The difference this time is the breakpoint will stop the CPU and also the trace collection. The trace buffer will be visible and is useful to investigate and determine the cause of the crash.

#### Simulate a Hard Fault

1. Using the previous example, (figure: Start/Stop Debug) **start a Debug Session (Ctrl+F5)** to enter the µVision debugger.
2. Locate the `HardFault_Handler` in the startup_*device*.s/c file.
3. Set a breakpoint at this point. A red circle will appear.
4. In the **Command** window execute:
   ```
   g, EventRecord2
   ```
   This puts the PC at the start of this function. `EventRecord2` returns with a `POP` instruction which you will use to create a hard fault with `LR = 0`. The assembly and sources in the **Disassembly** window do not always match up and this is caused by anomalies in ELF/DWARF specification. In general, scroll downwards in this window to provide the best match.
6. Clear the **Trace Data** window by clicking on the (figure: Clear trace) clear trace icon. This helps to see what is happening.
7. In the **Register** window, double-click on the `R14 (LR)` register and set it to `'0'`. This will cause a hard fault when the processor places `LR = 0` into the PC and tries to execute the non-existent instruction at memory location `0x0`.
8. (figure: Run) **Run (F5)** the application and almost immediately it will stop on the hard fault exception branch instruction.
9. In the **Trace Data** window, you will find the `EventRecord2` function with the `POP` instruction at the end. When the function tried to return, the bogus value of LR caused a hard fault.
1. The `B` instruction at the hard fault vector was not executed because CoreSight hardware breakpoints do not execute the instruction they are set to when they stop the program. They are no-skid breakpoints.
1. (figure: Step into) **Step (F11)** once. You will now see the hard fault branch as shown in the bottom screen:  
(figure: Trace Data Window with Hard Fault Handler)

This example shows how quickly ETM trace can help debug program flow bugs.

**Note:**
Instead of setting a breakpoint on the hard fault vector, you could also right-click on it and select **Insert Tracepoint** and select **TraceHalt**. When hard fault is reached, trace collection will halt but the program will keep executing for testing and hard fault handlers.
