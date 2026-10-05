---
id: "pyocd-open-cmsis-pack-support-pyocd-s-debug-sequence-implementation"
type: "concept"
domain: "debug"
title: "Open-CMSIS-Pack support: PyOCD's debug sequence implementation"
summary: "This section documents details of the debug sequence engine provided by pyOCD, supported features, and any notable differences with other debuggers (primarily Keil MDK, which provided the first implementation and against which Packs are generally most thoroughly tested …"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/open_cmsis_pack_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/open_cmsis_pack_support.md#pyocd-s-debug-sequence-implementation"
license: "Apache-2.0"
mode: "V"
---

This section documents details of the debug sequence engine provided by pyOCD, supported features, and any notable differences with other debuggers (primarily Keil MDK, which provided the first implementation and against which Packs are generally most thoroughly tested by their authors).


### Core-specific sequences

The DFP debug sequence architecture is currently based on the fact that most debuggers only "connect" to a single CPU core chosen by the user when debugging or running a project. All debug sequences can be customized per core, and there can be separate sequences for each core.

PyOCD is somewhat different in that it connects to the device as a whole, and then debugs one or more cores after the connection is established. This more closely reflects the hardware situation.

This primarily impacts the `DebugPortSetup`, `DebugPortStart`, `DebugPortStop`, and `DebugDeviceUnlock` debug sequences that affect the entire SoC. These relate to the connect procedure for the Arm ADI DP (Debug Port) used for SWD/JTAG communications. While most sequences can be run separately for each core, these are run only once per target connection. The core-specific variant that is selected can affect the rest of the debugging session. (Technically, this is also true for debuggers that are presented as debugging a single core, in cases where a second instance of that debugger can be started to debug another core. But, the way it's presented to the user is different.)

The `primary_core` session option is used to select which core-specific version of the `DebugPort*`/`DebugDeviceUnlock` sequences is run during the target connection process. For all other sequences, the core-specific version that is run depends on which core is performing the action.


### Custom default reset sequences

The DFP specification allows the definition of custom (nonstandard) reset sequences, and these can be selected as the default reset sequence for a core. The purpose of this is to keep the standard sequences unmodified and available for user selection. Because pyOCD does not currently support a custom reset type, this DFP feature is not supported. A custom default reset sequence will be replaced with `ResetSystem` and the custom behavior not performed.


### Debug sequences and delegate functions

Effectively, debug sequences are handled as pre-defined [delegate functions]({% link _docs/user_scripts.md %}#delegate-functions). For most standard debug sequence, there is a corresponding delegate function. This means that a delegate function in a user script (or delegate class, if using the Python API) will override the corresponding debug sequence provided by the target's DFP.


### Supported debug sequences

The following standard debug sequences are supported and will by called by pyOCD. The corresponding delegate function is listed for each.

Sequence name           | Delegate function   | Description
------------------------|---------------------|------------------------------------------------------
`DebugPortSetup`        | -                   | SWJ-DP switch; reading `DPIDR`; writing `TARGETSEL`.
`DebugPortStart`        | -                   | Connect to the target debug port and power it up.
`DebugPortStop`         | -                   | Power down and disconnect from target debug port.
`DebugDeviceUnlock`     | `unlock_device`     | Ensure the device is accessible.
`DebugCoreStart`        | `start_debug_core`  | Initialize core debug.
`DebugCoreStop`         | `stop_debug_core`   | Uninitialized core debug.
`DebugCodeMemRemap`     | -                   | Remap memory to execution location. Executed before verifying memory content after flash programming. This is required to replicate a memory remap of a device bootloader (that is not executed during debug connection).
`ResetSystem`           | `will_reset`        | System-wide reset without debug domain via software mechanisms.
`ResetProcessor`        | `will_reset`        | Local processor reset without peripherals and debug domains.
`ResetHardware`         | `will_reset`        | System-wide reset without debug domain via the dedicated debugger reset line, e.g. nRST.
`ResetHardwareAssert`   | -                   | Assert a system-wide reset via the dedicated debugger reset line, e.g. nRST.
`ResetHardwareDeassert` | -                   | De-assert a system-wide reset via the dedicated debugger reset line, e.g. nRST.
`ResetCatchSet`         | `set_reset_catch`   | Configure the vector catch to stop code execution after the reset.
`ResetCatchClear`       | `clear_reset_catch` | Free hardware resources allocated by `ResetCatchSet`.
`FlashEraseSetup`       | -                   | Optional setup before flash erase for flashinfo-based regions. May call `FlashLoadAlgorithm()` to use an FLM algorithm for erase.
`FlashProgramSetup`     | -                   | Optional setup before flash program for flashinfo-based regions. May call `FlashLoadAlgorithm()` to use an FLM algorithm for programming.
`FlashInit`             | -                   | Executed before starting a flash operation.
`FlashUninit`           | -                   | Executed after a flash operation finished.
`FlashEraseSector`      | -                   | Executed to erase a flash memory sector.
`FlashEraseChip`        | -                   | Executed to erase all on-chip flash memory with target device specific erase technology.
`FlashEraseDone`        | -                   | Executed after all flash memory erase operations are finished.
`FlashProgramPage`      | -                   | Executed to program a single flash page.
`FlashProgramDone`      | -                   | Executed after all flash programming operations are finished.
`TraceStart`            | `trace_start`       | Enable target trace capture.
`TraceCapture`          | `trace_capture`     | Capture trace data.
`TraceFlush`            | `trace_flush`       | Flush trace data.
`TraceStop`             | `trace_stop`        | Disable target trace capture.

Standard debug sequences not currently supported:

Sequence name           | Description
------------------------|------------------------------------------------------
`RecoverySupportStart`  | Before step or run command to support recovery from a lost target connection.
`RecoverySupportStop`   | After step or run command in context of the `RecoverySupportStart`.
`RecoveryAcknowledge`   | Debugger acknowledge after recovering from a lost target connection.
