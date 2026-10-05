---
id: "tbx-pyocd-debugger-debug-topology"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `debug-topology:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debug-topology"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Describes the properties of the system hardware for debug functionality. The information for this node is taken from
the DFP. If the information is not provided in the `*.cbuild-run.yml` file, pyOCD will use the default values described below.

`debug-topology:`                                 |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
    `debugports:`                  |   Optional   | Describes the CoreSight debug ports of the device and its capabilities.
    `processors:`                  |   Optional   | Map of `pname` identifiers to access port IDs (mandatory for multi-processor devices).
    `trace-sinks:`                 |   Optional   | Trace sinks supported by the device.
    `swj:`                         |   Optional   | Device allows switching between Serial Wire Debug (SWD) and JTAG protocols (`true` or `false`).
    `dormant:`                     |   Optional   | Device requires the dormant state to switch debug protocols (`true` or `false`).

`debugports:`                                     |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- dpid:`                                         | **Required** | Unique ID of this debug port.
    `accessports:`                 |   Optional   | List of CoreSight access ports (APv1/APv2) (mandatory for multi-processor devices).

`accessports:`                                    |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- apid:`                                         | **Required** | Unique ID of this access port. If only `apid` is provided, access port (APv1) with index `0` will be implicitly used.
    `index:`                       |   Optional   | Index to select this access port (APv1) for a target access.
    `address:`                     |   Optional   | Address to select this access port (APv2) in its parent's address space for a target access.

!!! Note
    `index:` and `address:` cannot be specified at the same time.

`processors:`                                     |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- pname:`                                        | **Required** | Processor identifier (mandatory for multi-processor devices).
    `apid:`                        |   Optional   | Access port ID to use for this processor.
    `reset-sequence:`              |   Optional   | Name of debug sequence for reset operation (default: `ResetSystem` sequence).

`trace-sinks:`                                    |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- <trace-sink-type>:`                            | **Required** | Trace sink type: `serialwire` or `tracebuffer`.

`trace-sinks:` lists device trace sinks from the DFP [`trace`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_trace) element. `serialwire` has no value. A `tracebuffer` value is its optional PDSC `name` attribute and becomes mandatory when multiple trace buffers exist.

pyOCD uses this information to verify that a trace type is supported and that a selected named trace buffer exists.

**Default values:**

```yml
debug-topology:
  dormant: false
  swj: true
  debugports:
    - dpid: 0
      accessports:
        - apid: 0
          index: 0
  trace-sinks:
    - serialwire:
    - tracebuffer:
```

**Example:**

```yml
  debug-topology:
    dormant: true
    debugports:
      - dpid: 0
        accessports:
          - apid: 0
            address: 0x00200000
          - apid: 1
            address: 0x00300000
    processors:
      - pname: M55_HP
        apid: 0
      - pname: M55_HE
        apid: 1
    trace-sinks:
      - serialwire:
      - tracebuffer: ETF
      - tracebuffer: MTB
```
