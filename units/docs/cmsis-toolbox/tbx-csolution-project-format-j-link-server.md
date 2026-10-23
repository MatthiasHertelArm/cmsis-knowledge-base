---
id: "tbx-csolution-project-format-j-link-server"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / J-Link Server"
summary: "This section lists options that are specific for the Segger J-Link debug probes."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#j-link-server"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

This section lists options that are specific for the [Segger J-Link](https://www.segger.com/products/debug-probes/j-link/) debug probes.

[Extended options](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/JLink-Debugger.md#extended-options) are required for rare use cases and further tailor the behavior of J-Link Server.

#### `debugger:` for J-Link Server

debugger:                                                  |              | Description
:----------------------------------------------------------|:-------------|:-----------------------------------------------
    `name:`                                 | **Required** | Identifies the debug adapter with `J-Link Server`.
    `clock:`                                |   Optional   | Debug clock speed in Hz.
    `protocol:`                             |   Optional   | Debug protocol (jtag or swd).
    [`stdio:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/JLink-Debugger.md#stdio)     |   Optional   | Extended Option: Standard I/O service configuration.
    [`trace:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/JLink-Debugger.md#trace)     |   Optional   | Extended Option: Trace configuration.
    [`connect:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/JLink-Debugger.md#connect) |   Optional   | Extended Option: Connect mode to hardware.
    [`reset:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/JLink-Debugger.md#reset)     |   Optional   | Extended Option: Reset type configuration for various cores.

**Examples:**

```yml
debugger:
  name: J-Link Server
  clock: 4000000                  # 4000 kHz
  protocol: swd
```
