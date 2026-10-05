---
id: "tbx-csolution-project-format-debugger-configuration"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration"
summary: "The debugger: node specified under the target-set: in the csolution project configures the debugger."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#debugger-configuration"
license: "Apache-2.0"
mode: "V"
---

The `debugger:` node specified under the [`target-set:`](#target-set) in the *csolution project* configures the debugger.

!!! Note
    - Packs may provide a default configuration for a debugger connection to a device or board. 
    - Several settings are optional and the default settings are specific to the selected debug adapter.
    - The complete debugger settings including default values are listed in `debugger:` node of the [`*.cbuild-run.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md#run-and-debug-management).
