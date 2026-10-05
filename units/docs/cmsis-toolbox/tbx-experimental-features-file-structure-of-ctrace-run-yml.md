---
id: "tbx-experimental-features-file-structure-of-ctrace-run-yml"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / File Structure of `*.ctrace-run.yml`"
summary: "The .ctrace-run.yml file starts with the node ctrace-run:. It is generated from .ctrace.yml, .cbuild-run.yml, and ELF/DWARF symbol information. This file is a generated artifact and should not be edited manually."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#file-structure-of-ctrace-run-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

The `*.ctrace-run.yml` file starts with the node `ctrace-run:`. It is generated from `*.ctrace.yml`, `*.cbuild-run.yml`, and ELF/DWARF symbol information. This file is a generated artifact and should not be edited manually.

`ctrace-run:`                                            |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
    `generated-by:`                       |  Optional   | Tool and version that generated the file.
    `ctrace-setup:`                       |  Optional   | Copy of [`setup`](#file-structure-of-ctraceyml) node in the `*.ctrace.yml` file.
    `ctrace-disable:`                     |**Required** | Per-processor register values that disable trace features before applying `ctrace-refs:`.
    `ctrace-refs:`                        |**Required** | List of [references](#references) in the `*.ctrace.yml` file.

The `ctrace-setup` node uses the same format as the [`setup`](#file-structure-of-ctraceyml) node in the `*.ctrace.yml` file and preserves the original user input for consumers of the `*.ctrace-run.yml` file. Consumers may read settings that do not resolve to a `ref` or register write. For example, the `ctrace` decoder uses `timestamps:clock` as a trace-formatting hint, while pyOCD reads `synchronization:sync-on-run` to control built-in trace-capture behavior.

The `ctrace-disable:` node contains register values that disable trace features before applying `ctrace-refs:`. Its `regs:` entries use the [register access format](#register-accesses). Multi-processor entries require `pname:`, while single-processor entries omit it.

`ctrace-disable:`                                       |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
`- pname:`                                              |  Optional   | Processor name.
    `regs:`                               |**Required** | Register writes that disable trace features for this processor.

The `ref:` node references the trace generation configuration in the file `*.ctrace.yml` and contains register values that represent the setup for trace sources. The `regs:` entries use the [register access format](#register-accesses). A single-core system has no `pname:` value; a multi-processor always includes a `pname:` value in the `ref:` node.

`ctrace-refs:`                                           |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
`- ref:`                                                 |**Required** | [Reference](#references) to a node in the `*.ctrace.yml` file that generated the register setup.
    `type:`                               |**Required** | Trace source type.
    `pname:`                              |  Optional   | Processor name the reference resolves to for multi-core systems.
    `stream:`                             |  Optional   | Stream ID (CoreSight ATB ID).
    `index:`                              |  Optional   | Index or list of indices of ITM channels or DWT comparators used by setting.
    `info:`                               |  Optional   | Additional information (for example alignment extension).
    `warning:`                            |  Optional   | Warning message.
    `error:`                              |  Optional   | Error message when setup cannot be completed.
    `label:`                              |  Optional   | User-defined short label for Trace Compass
    `address:`                            |  Optional   | Resolved address for the setting. May be resolved from a symbol.
    `size:`                               |  Optional   | Size, in bytes, of the capture data. May be extracted from symbol information.
    `symbol-file:`                        |  Optional   | Absolute path to the symbol file used in this reference.
    `data-type:`                          |  Optional   | Type of displayed data: `unsigned`, `signed`, or `float`. Default: `unsigned`.
    `regs:`                               |  Optional   | Register setup.

The trace source types are: `dwt`, `event`, `exception`, `itm`, `pmu`, `overflow`, `pcsample`, `global_ts`.

Each of the `info:`, `warning:`, and `error:` nodes accepts either a string or a list of strings, allowing multiple messages to be represented separately.

Multiple `ref` entries may reference the same configuration node when it generates setups for multiple streams. The combination of `ref` and `stream` identifies each generated setup.

The `data-type` in combination with `size` provides a hint for the display format. Other information required for generating CTF data can be extracted from the referenced setting node in the `ctrace-setup:` section.

`size` can be extracted from symbol information or provided in the `ctrace` file. If both are present, user input takes precedence.

The use of `index:` depends on the combination of `type:` and the setting referenced by `ref:`.

`type:` | `ref:` setting | Usage of `index:`
:-------|:----------------------|:-------------------
`dwt`   | `data:` | Number or array of DWT comparators allocated for the data-trace entry.
`dwt`   | `instructions:start:`, `instructions:stop:`, or `tracehalt:` | Number or array of DWT comparators allocated for the condition.
`itm`   | `itm:` | Number or array of enabled ITM channels.

#### Register Accesses

The `ctrace-run.yml` file contains the disabled register values and active register setup required for trace generation. It does not include enable sequences required by the Arm processor to access these registers. The debugger (pyOCD) has knowledge about architecturally defined trace components (listed in the table below) and therefore generates the right sequences, potentially with timeouts.

Trace Component | Base Address | Description
:---------------|:------------:|:------------------------------------
`ITM`           | `0xE0000000` | Instrumentation Trace Macrocell.
`DWT`           | `0xE0001000` | Data Watchpoint and Trace unit.
`PMU`           | `0xE0003000` | Performance Monitoring Unit.
`ETM`           | `0xE0041000` | Embedded Trace Macrocell.

`regs:` entries are used under both `ctrace-disable:` and `ctrace-refs:` and have the following format:

`regs:`                                                  |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
`- name:`                                                |**Required** | Symbolic name of the register.
    `value:`                              |**Required** | Value to write in this register.
    `mask:`                               | Optional    | Bit mask for value write (default: `0xFFFFFFFF`).

When applying `ctrace-disable:` writes to DWT comparators, the debugger preserves active watchpoints.

#### Example

```yml
ctrace-run:
  generated-by: pyTS v0.0
  ctrace-setup:
    synchronization:
      sync-on-run: false  # Read by pyOCD; not a register write
  ctrace-disable:
  - pname: core0
    regs:
      - name: ITM_TCR
        value: 0x00000000
        mask: 0x00000006  # Disable timestamp and synchronization generation
      - name: ITM_TER0
        value: 0x00000000  # No mask: disable all 32 ITM channels
  ctrace-refs:
  - ref: core0/itm
    pname: core0
    type: itm            # packet types
    stream: 1            # stream id
    index: 0             # ITM channel #0
    regs:
      - name: ITM_TER0
        value: 0x00000001
      - name: ITM_TPR
        value: 0x00000001
        mask: 0x0000000f
      - name: ITM_TCR
        value: 0x00010000
        mask: 0x007f0000

  - ref: data#0
    type: dwt
    stream: 1            # stream id
    error: cannot find symbol

  - ref: data#1   # symbol location
    type: dwt
    address: <symbol address>
    size: <symbol size>
    symbol-file: <symbol file used>
    data-type: unsigned
    stream: 1            # stream id
    index: [0, 1]        # allocated DWT comparators #0 and #1
    regs:
      - name: DWT_COMP0
        value: 1
        mask:  0xFF
      - name: DWT_COMP1
        value: 2

  - ref: core0/timestamps
    type: itm
    pname: core0
    stream: 1
    regs:
      - name: ITM_TCR
        value: 0x00000002
        mask: 0x00000002

  # - ref: core0/timestamps
  #   type: etm            # etm not yet supported, for demonstration purposes only
  #   pname: core0
  #   stream: 2
  #   regs:
  #     - name: TRCCONFIGR
  #       value: 0x00000010
  #       mask: 0x00000010
  #     - name: TRCCCCTLR
  #       value: 0x4
```

!!! Note
    The processor `itm` reference configures the ITM ATB stream ID. It may be generated even when no ITM channels are enabled.
