---
id: "spec-debug-description-predefined-debug-access-sequences"
type: "concept"
domain: "pack"
title: "Debug Description: Predefined debug access sequences"
summary: "Debug access sequences are defined using the sequence element."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

Debug access sequences are defined using the sequence element. 

The table below lists the available predefined debug access sequences. Their default implementation is done in a development tool and gets executed by default. If PDSC file contains a user implementation of a predefined debug sequence (using `<sequence>` element) then it will override the default implementation and will be executed instead. Refer to usage_of_sequences for more information about the execution of these sequences.

For debug access sequences marked in `ItalicRed`, no default implementation  exists. When using them in debug descriptions corresponding user implementation shall be done as well. 

**Note:** Predefined debug access sequences read the System Control Space (SCS) of the processor and assume that the SCS base address is implemented as defined in the Armv6-M/Armv7-M/Armv8-M architecture reference manual.

**Note:** The **FlashInit,** **FlashUninit,** **FlashEraseSector,** **FlashEraseChip,** and **FlashProgramPage** sequences are the
sequence-based counterparts of the corresponding FLM functions. They require a corresponding
flashinfo region, which supplies the memory layout and programming parameters. **FlashEraseSetup** and
**FlashProgramSetup** can select an FLM algorithm instead of these sequences for an erase or program phase. A target may define
one or more **flashinfo** regions without implementing any flash debug sequences; in that case all such regions are ignored.
**FlashEraseDone** and **FlashProgramDone** are completion callbacks and are also executed when an FLM flash algorithm performs
the erase or program operation.



| name= | Description |
|---|---|
| debugPortSetup | Prepare the target debug port for connection; is executed before acquiring access to the debug port. May include for example an SWJ-DP switch sequence as defined in the Arm Debug Interface (ADI) Architecture Specification. **This sequence must not contain debug port/access port register and target memory accesses other than:** - **Reading the **DPIDR** debug port register to release an SWD connection from its line reset.** - **Writing the **TARGETSEL** debug port register (SWD protocol v2).** |
| debugPortStart | Connect to the target debug port and power it up; is executed after DebugPortSetup. The parent **debugport** is default debug port for this sequence. **This sequence must not contain access port register and target memory accesses.** |
| debugPortStop | Power down and disconnect from target debug port. Executed as last step during target disconnect unless another debugger connection to this port is active. The parent **debugport** is default debug port for this sequence. **This sequence must not contain access port register and target memory accesses.** |
| DebugDeviceUnlock | Check if the device is in a locked state and unlock it. Use **query** command elements for user confirmation. Executed after having powered up the debug port. See example at userDebugDeviceUnlock. |
| debugCoreStart | Initialize core debug system. Executed after having connected and powered up the default debug port for the connection. |
| debugCoreStop | Uninitialized core debug system. Executed as last step during disconnect before powering down any debug ports no longer required for concurrent connections. |
| DebugCodeMemRemap | Remap memory to execution location. Executed before verifying memory content after flash programming. This is required to replicate a memory remap of a device bootloader (that is not executed during debug connection). |
| resetSystem | Executes a system-wide reset without debug domain (or warm-reset that preserves debug connection) via software mechanisms, for example AIRCR.SYSRESETREQ. |
| resetProcessor | Executes a local processor reset without peripherals and debug domains. Uses a software mechanism (for example AIRCR.VECTRESET). |
| resetHardware |  |
| resetHardwareAssert | Assert a system-wide reset via the dedicated debugger reset line, e.g. nRST. |
| resetHardwareDeassert | De-assert a system-wide reset via the dedicated debugger reset line, e.g. nRST. |
| resetCatchSet | Executed before a target reset to configure the vector catch to stop code execution after the reset. The implementation of **ResetCatchSet** requires an implementation of **ResetCatchClear** to free any hardware resources used for stopping the core. |
| resetCatchClear | Executed after a target reset to free hardware resources allocated by **ResetCatchSet**. |
| FlashEraseSetup | Optional setup before an erase phase for a flashinfo region. The sequence can call **FlashLoadAlgorithm** to select an FLM flash algorithm for the erase phase. The debugger then uses the FLM functions instead of the corresponding flash debug sequences. If no algorithm is selected, the debugger uses the flash debug sequences. |
| FlashProgramSetup | Optional setup before a program phase for a flashinfo region. The sequence can call **FlashLoadAlgorithm** to select an FLM flash algorithm for the program phase. The debugger then uses the FLM functions instead of the corresponding flash debug sequences. If no algorithm is selected, the debugger uses the flash debug sequences. |
| FlashInit | Sequence-based counterpart of the FLM **Init** function. Executed before starting a flash operation. |
| FlashUninit | Sequence-based counterpart of the FLM **UnInit** function. Executed after a flash operation finished. |
| FlashEraseSector | Sequence-based counterpart of the FLM **EraseSector** function. Executed to erase a flash memory sector described by a flashinfo region. |
| FlashEraseChip | Sequence-based counterpart of the FLM **EraseChip** function. Executed to erase all on-chip flash memory with target device specific erase technology. If this sequence is not implemented then a debugger can use **FlashEraseSector** to erase all flash memory. |
| FlashEraseDone | Executed after all flash memory erase operations are finished, regardless of whether flash debug sequences or an FLM flash algorithm performed the operations. |
| FlashProgramPage | Sequence-based counterpart of the FLM **ProgramPage** function. Executed to program a single page described by a flashinfo region. |
| FlashProgramDone | Executed after all flash programming operations are finished, regardless of whether flash debug sequences or an FLM flash algorithm performed the operations. |
| TraceStart | Enable target trace capture. If `<sequences>` specifies **traceSetup=`legacy`** or omits the attribute, this sequence is executed before the debugger configures CoreSight trace components, e.g. after the initial target connection as well as after a system-wide reset. If `<sequences>` specifies **traceSetup=`full`**, this sequence is expected to perform all trace sink and trace data path setup required by the device, and the debugger is not expected to configure CoreSight trace components using a priori knowledge. See example at userTraceStart. |
| TraceStop | Disable target trace capture. If `<sequences>` specifies **traceSetup=`legacy`** or omits the attribute, this sequence is executed after the debugger disabled and powered down CoreSight trace components. If `<sequences>` specifies **traceSetup=`full`**, this sequence is expected to perform all trace sink and trace data path shutdown steps required by the device. |
| TraceCapture | Prepare target trace for next capture run, e.g. by enabling the trace formatter or initializing embedded trace buffer data read/write pointers. Typically executed before a debugger runs/steps the target processor. Or when manually starting a trace capture. |
| TraceFlush | Flush out remaining trace bytes. This ensures all pending data is streamed off-chip, or drained into an on-chip trace buffer before the debugger reads it. Typically executed after the target processor pauses after a run/step. Or when manually stopping a trace capture. |
| RecoverySupportStart | Executed before step or run command to support recovery from a lost target connection, e.g. after a low power mode. |
| RecoverySupportStop | Executed after step or run command in context of the **RecoverySupportStart** sequence. |
| RecoveryAcknowledge | Debugger acknowledge after recovering from a lost target connection. Can be executed independently from a **RecoverySupportStart** sequence. |




Predefined default debug access sequences
-----------------------------------------
The following sections the show the details of the predefined default debug access sequences.
