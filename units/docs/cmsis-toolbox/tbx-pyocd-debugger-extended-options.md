---
id: "tbx-pyocd-debugger-extended-options"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options"
summary: "The section CSolution Project Format: pyOCD contains the pyOCD configuration for typical systems."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#extended-options"
license: "Apache-2.0"
mode: "V"
---

The section [CSolution Project Format: pyOCD](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-Input-Format.md#pyocd) contains the pyOCD configuration for typical systems.

Extended YAML options are required to configure specific use-cases or overwrite information that is typically provided in the [DFP](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/build-overview.md#overview-of-operation).

CMSIS-DAP based Debug Adapters implement [debug access sequences](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#pdsc_SequenceNameEnum_pg) that are configured in the [DFP for a device](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/build-overview.md#overview-of-operation).
