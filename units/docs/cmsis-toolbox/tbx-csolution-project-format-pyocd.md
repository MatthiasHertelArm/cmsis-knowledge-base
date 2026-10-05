---
id: "tbx-csolution-project-format-pyocd"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / pyOCD"
summary: "This section lists the options that are specific to pyOCD that connects to CMSIS-DAP and ST-Link debug adapters. CMSIS-DAP is a standardized protocol used by many different debug adapters. All CMSIS-DAP enabled debug adapters can be accessed with name: CMSIS-DAP@pyOCD."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#pyocd"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

This section lists the options that are specific to pyOCD that connects to [CMSIS-DAP](https://arm-software.github.io/CMSIS-DAP/latest/index.html) and ST-Link debug adapters. CMSIS-DAP is a standardized protocol used by many different debug adapters. All CMSIS-DAP enabled debug adapters can be accessed with `name: CMSIS-DAP@pyOCD`. A specific debug adapter name such as `name: ULINKplus@pyOCD` provides tailored default settings and a custom configuration dialog in the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) VS Code extension.

[Extended options](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#extended-options) are required for rare use cases and further tailor the behavior of pyOCD.

#### `debugger:` for pyOCD

debugger:                                                                  |              | Description
:--------------------------------------------------------------------------|:-------------|:-----------------------------------------------
    `name:`                                                 | **Required** | Identifies the debug adapter with `<adapter>@pyOCD`.
    `clock:`                                                |   Optional   | Debug clock speed in Hz.
    `protocol:`                                             |   Optional   | Debug protocol (jtag or swd).
    `dbgconf:`                                              |   Optional   | [Configuration file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html#dbg_sqns_dbgconf) for device settings such as trace pins and option bytes.
    `start-pname:`                                          |   Optional   | Debugger connects at start to this processor.
    [`gdbserver:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#gdbserver)             |   Optional   | Extended Option: GDB Server configuration.
    [`stdio:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#stdio)                     |   Optional   | Extended Option: Standard I/O service configuration.
    [`connect:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#connect)                 |   Optional   | Extended Option: Connect mode to hardware.
    [`reset:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#reset)                     |   Optional   | Extended Option: Reset type configuration for various cores.
    [`load-setup:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#load-setup)           |   Optional   | Extended Option: Reset type and Halt configuration for Load command.
    [`rtt:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#rtt)                         |   Optional   | Extended Option: Segger RTT configuration.
    [`systemview:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#systemview)           |   Optional   | Extended Option: Segger SystemView configuration.
    [`trace:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#trace)                     |   Optional   | Extended Option: Trace configuration.
    [`device-settings:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pyOCD-Debugger.md#device-settings) |   Optional   | Extended Option: Configuration through device-specific [`<debugvars>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debugvars) settings.

**Examples:**

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  clock: 20000000               # 20 MHz
```

```yml
debugger:
  name: ULINKplus
  protocol: jtag
  clock: 10000000               # 10 MHz
  dbgconf: MyHardware.dbgconf
```
