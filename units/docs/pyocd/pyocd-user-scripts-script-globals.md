---
id: "pyocd-user-scripts-script-globals"
type: "concept"
domain: "debug"
title: "User scripts: Script globals"
summary: "A number of useful symbols are made available in the global namespace of user scripts. These include both target related objects, as well as parts of the pyOCD Python API."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/user_scripts.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/user_scripts.md#script-globals"
license: "Apache-2.0"
mode: "V"
---

A number of useful symbols are made available in the global namespace of user scripts. These include
both target related objects, as well as parts of the pyOCD Python API.

The usual Python builtins are available.

### Objects and functions

| Symbol | Description |
|--------|-------------|
| `aps` | Dictionary of CoreSight Access Port (AP) objects. The keys are the APSEL value. |
| `board` | The `Board` object. |
| `command` | Decorator for defining new commands. See [user-defined commands](#user_defined_commands) for details. |
| `debug` | Log a debug message. |
| `dp` | The CoreSight Debug Port (DP) object. |
| `error` | Output an error log. |
| `info` | Output an info-level log message. |
| `LOG` | `Logger` object for the user script. |
| `options` | The session options dictionary. |
| `probe` | The connected debug probe object. |
| `session` | The session object, which is the root of the connection object graph. |
| `target` | The `CoreSightTarget` or subclass instance representing the MCU. |
| `warning` | Log a warning. |

### Modules and classes

| Symbol | Description |
|--------|-------------|
| `BreakpointType` | Enumeration of breakpoint types. |
| `DeviceRegion` | Device-type memory region class. |
| `Error` | The base class for all pyOCD exceptions. |
| `Event` | Enumeration of notification event types. |
| `exceptions` | Module containing the exception classes. |
| `FileProgrammer` | Utility class to program files to target flash. |
| `FlashEraser` | Utility class to erase target flash. |
| `FlashLoader` | Utility class to program raw binary data to target memory. Deprecated, use `MemoryLoader` instead. |
| `FlashRegion` | Flash memory region. |
| `HaltReason` | Enumeration of halt reasons. |
| `MemoryLoader` | Utility class to program raw binary data to target memory. |
| `MemoryMap` | Class representing the device's memory map. |
| `MemoryType` | Memory region type enumeration. |
| `pyocd` | The root pyOCD module. |
| `RamRegion` | RAM memory region. |
| `ResetType` | Reset type enumeration. |
| `RomRegion` | ROM memory region. |
| `RunType` | Enumeration of types of run operations (step or run). |
| `SecurityState` | Enumeration of core security states. |
| `State` | Enumeration of target state. |
| `Target` | Base target class. |
| `TransferError` | Exception class for all transfer errors. |
| `TransferFaultError` | Exception subclass of `TransferError` for memory transfer faults. |
| `VectorCatch` | Namespace class containing bit mask constants for vector catch options. |
| `WatchpointType` | Enumeration of watchpoint types. |
