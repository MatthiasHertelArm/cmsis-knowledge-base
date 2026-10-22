---
id: "tbx-csolution-project-format-debugger"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / `debugger:`"
summary: "debugger: | | Content :---------------------------------------------------------|:-------------|:------------------------------------ name: | Required | Identifies the debug adapter. : | Optional | Other debugger specific options can be used as documented below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#debugger"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

`debugger:`                                               |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
    `name:`                                | **Required** | Identifies the debug adapter.
    `*:`                                   |   Optional   | Other debugger specific options can be used as documented below.

The command `csolution list debuggers` outputs the `name:` of the supported debug adapters; using the option `--verbose` extends the list with alias names that are also accepted as `name:`  There are five different debug adapter categories:

Debug Adapter `name:`                     | Description
:-----------------------------------------|:-----------------------------------------------
[`<adapter>@pyOCD`](#pyocd)               | Debug Adapters that interface via pyOCD ([CMSIS-DAP](https://arm-software.github.io/CMSIS-DAP/latest/index.html) and ST-Link).
[`<adapter>@Arm-Debugger`](#arm-debugger) | Debug Adapters that interface via the Arm-Debugger.
[`Arm-FVP`](#arm-fvp)                     | [FVP](https://arm-software.github.io/AVH/main/simulation/html/index.html) simulation models that represent processor sub-systems.
[`Keil uVision`](#keil-uvision)           | [uVision Debugger](https://developer.arm.com/documentation/101407/0543/Debugging) that is integrated in the Keil uVision IDE. 
[`J-Link Server`](#j-link-server)         | [Segger J-Link](https://www.segger.com/products/debug-probes/j-link/) debug probes that connect using the J-Link Server.

The [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) VS Code extension uses the `debugger:` node to create entries in the files `.vscode/tasks.json` and `.vscode/launch.json` for running and debugging using the specified debug adapter. [`pyOCD`](#pyocd) supports a command-line mode that uses the [`*.cbuild-run.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md#run-and-debug-management) file which is created by the CMSIS-Toolbox.

The following sections describe the options available for the different debug adapter types.
