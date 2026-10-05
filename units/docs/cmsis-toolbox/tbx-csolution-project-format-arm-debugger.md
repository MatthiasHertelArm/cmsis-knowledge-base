---
id: "tbx-csolution-project-format-arm-debugger"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / Arm Debugger"
summary: "This section lists options that are specific for the Arm Debugger."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#arm-debugger"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

This section lists options that are specific for the Arm Debugger.

#### `debugger:` for Arm Debugger

debugger:                            |              | Description
:------------------------------------|:-------------|:-----------------------------------------------
    `name:`           | **Required** | Identifies the debug adapter with `<adapter>@Arm-Debugger`.
    `clock-armdbg`    |   Optional   | Debug clock speed. Possible values: auto (default), 50MHz, 33MHz, 25MHz, 20MHz, 10MHz, 5MHz, 2MHz, 1MHz, 500kHz, 200kHz, 100kHz, 50kHz, 20kHz, 10kHz, 5kHz
    `protocol-armdbg` |   Optional   | Debug protocol. Possible values: auto (default), JTAG, SWD

**Example:**

```yml
debugger:
  name: CMSIS-DAP@Arm-Debugger
  protocol-armdbg: SWD
  clock-armdbg: 5MHz
```
