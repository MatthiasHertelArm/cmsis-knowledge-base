---
id: "tbx-pyocd-debugger-connect"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `connect:`"
summary: "Configures the behavior for connecting pyOCD to the hardware target."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#connect"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

Configures the behavior for connecting pyOCD to the hardware target.

                                             |              | Description
:-------------------------------------------------|:-------------|:------------------------------------
`connect:`                                        |   Optional   | Selects the connect mode: `pre-reset`, `under-reset`, `attach` (default), `halt`.

Connect Mode  | Description
:-------------|:------------------------------------
`pre-reset`   | Apply a hardware reset before connect. Sequence: [ResetHardware](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetHardware).
`under-reset` | Asserts a hardware reset (Sequence: [ResetHardwareAssert](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetHardwareAssert)) during connect and deasserts (Sequence: [ResetHardwareDeassert](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#resetHardwareDeassert)) after core(s) are halted.
`attach`      | Do not change status of the core(s).
`halt`        | Halt core(s) after connect.
