---
id: "tbx-pyocd-debugger-reset"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `reset:`"
summary: "Configures the reset behavior for each core when a reset is requested."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#reset"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

Configures the reset behavior for each core when a reset is requested.

`reset:`                                          |              | Description
:-------------------------------------------------|:-------------|:------------------------------------
`- pname:`                                        |   Optional   | Identifies the processor (not required for single core system).
    `type:`                        | **Required** | Selects the reset type: `hardware`, `system`, `core`. Default: specified in DFP.

Reset Types   | Description
:-------------|:------------------------------------
`hardware`    | Use a system-wide reset via dedicated debugger reset line. Sequence: [ResetHardware](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetHardware).
`system`      | Use a system-wide reset via software mechanism. Sequence: [ResetSystem](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetSystem).
`core`        | Use a processor reset via software mechanism. Sequence: [ResetProcessor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetProcessor).

!!! Note
    The `defaultResetSequence` in DFP element [/package/devices/family/.../debug](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debug) can define a different default reset type. If no `defaultResetSequence`, the default reset type is `system`.
