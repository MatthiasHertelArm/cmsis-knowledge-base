---
id: "tbx-pyocd-debugger-device-settings"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `device-settings:`"
summary: "Debug and trace connection sequences are often device-specific and can be configured. This node contains a list of editable key-value pairs which are based on debug access variables defined in the device <debugvars> section in a PDSC file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#device-settings"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

!!! Note
    The `device-settings:` feature is under development. This section provides a preview.

Debug and trace connection sequences are often device-specific and can be configured. This node contains a list of editable key-value pairs which are based on debug access variables defined in the device [`<debugvars>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debugvars) section in a PDSC file.

The `device-settings:` node has higher precedence than the `dbgconf:` node, i.e. if `device-settings:` is present then an also specified [`*.dbgconf`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html#dbg_sqns_dbgconf) file is ignored.

If a `*.csolution.yml` specifies a `dbgconf:` node instead of a `device-settings:` node, then the referenced `*.dbgconf` file gets parsed and its contents is converted into a `device-settings:` node in the `*.cbuild-run.yml` file.

!!! Note
    - Settings that are not assigned under the `device-settings:` node or the referenced `*.dbgconf` file default to the values assigned in the device's [`<debugvars>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debugvars) section of the PDSC file.
    
**Example:** MySetup.csolution.yml

```yml
  debugger:
    name: ST-Link@pyOCD
    protocol: swd
    clock: 10000000
    dbgconf: .cmsis/Blinky+STM32H747I-EVAL.dbgconf
    start-pname: CM7
    gdbserver:
      - port: 3333
        pname: CM7
      - port: 3334
        pname: CM4
```

**Example:** MySetup.cbuild-run.yml generated from MySetup.csolution.yml

```yml
  debugger:
    name: ST-Link@pyOCD
    protocol: swd
    clock: 10000000
    start-pname: CM7
    gdbserver:
      - port: 3333
        pname: CM7
      - port: 3334
        pname: CM4
    device-settings:
      # DBGMCU configuration register (DBGMCU_CR)
      DbgMCU_CR: 0x00000007
      # TPIU Pin Routing (TRACECLK fixed on Pin PE2)
      TraceD0_Pin: 0x00040003  # Pin PE3
      TraceD1_Pin: 0x00040004  # Pin PE4
      TraceD2_Pin: 0x00040005  # Pin PE5
      TraceD3_Pin: 0x00040006  # Pin PE6
```
