---
id: "tbx-theory-of-operation-debug-adapter-integration"
type: "concept"
domain: "project"
title: "Theory of Operation: Debug Adapter Integration"
summary: "The file debug-adapters.yml in the CMSIS-Toolbox ./etc directory contains the list of supported debug adapters. If no debugger is specified for a csolution project, the first debug adapter (\"CMSIS-DAP@pyOCD\") contained in this file will be used."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#debug-adapter-integration"
license: "Apache-2.0"
mode: "V"
---

The file `debug-adapters.yml` in the CMSIS-Toolbox `./etc` directory contains the list of supported debug adapters. If no debugger is specified for a *csolution project*, the first debug adapter ("CMSIS-DAP@pyOCD") contained in this file will be used.

The master definitions are maintained in the [Open-CMSIS-Pack Debug Adapter Registry](https://github.com/Open-CMSIS-Pack/debug-adapter-registry) and deployed with CMSIS-Toolbox. Support for a new or updated third-party debug adapter should be contributed to that registry rather than added to an application project or a local CMSIS-Toolbox installation.

 The `debug-adapters:` node in this YAML file registers the supported debug adapters with the following keys:

`debug-adapters:`                                       |            | Content
:-------------------------------------------------------|:-----------|:------------------------------------
`- name:`                                               |**Required**| `<generator-id>` referred in the `*.PDSC` file
&nbsp;&nbsp;&nbsp; `alias-name:`                        |  Optional  | List of names (in input node or BSP) that map to this debug adapter.
&nbsp;&nbsp;&nbsp; `template:`                          |  Optional  | Used only by the [VS Code CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension for configuration.
&nbsp;&nbsp;&nbsp; `gdbserver:`                         |  Optional  | Add the [`gdbserver:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#gdbserver) node in the `cbuild-run.yml` file.
&nbsp;&nbsp;&nbsp; `defaults:`                          |  Optional  | List of default options to use when not specified in the [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#target-set) node.
&nbsp;&nbsp;&nbsp; [`user-interface:`](#user-interface) |  Optional  | Defines the user interface for VS Code CMSIS Solution extension.

!!! Note
    - As the file is shared with the [VS Code CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension, also template files are references. However these template files are not part of the CMSIS-Toolbox.
    - The debugger `name: <none>` identifies no debugger configuration. With this setting, no `template:` is applied and the `.vscode` configuration files are not modified.

**Example `debug-adapters.yml`**

```yml
debug-adapters:
  - name: "CMSIS-DAP@pyOCD"
    alias-name: ["CMSIS-DAP", "DAP-Link"]     # alternative names that map to this debug adapter
    template: CMSIS-DAP-pyOCD.adapter.json    # template file
    gdbserver:                                # add gdbserver: node under debugger: in cbuild-run.yml
    defaults:                                 # default values to use when nowhere specified
      port: 3333                              # default value of first gdbserver port
      protocol: swd
      clock: 10000000

  - name: "ULINKplus"
    template: CMSIS-DAP-pyOCD.adapter.json    # template file (initially same as CMSIS-DAP@pyOCD)
    gdbserver:                                # add gdbserver: node under debugger: in cbuild-run.yml
    defaults:                                 # default values to use when nowhere specified
      port: 3333                              # default value of first gdbserver port
      protocol: swd
      clock: 10000000

  - name: "ST-Link@pyOCD"
    alias-name: ["ST-LINK"]                   # alternative names that map to this debug adapter
    template: STLink-pyOCD.adapter.json       # template file
    gdbserver:                                # add gdbserver: node under debugger: in cbuild-run.yml
    defaults:                                 # default values to use when nowhere specified
      port: 3333                              # default value of first gdbserver port
      protocol: swd
      clock: 10000000

  - name: "J-Link Server"
    template: jlink.adapter.json              # template file
    defaults:                                 # default values to use when nowhere specified
      port: 3333                              # default value of first gdbserver port
      protocol: swd
      clock: auto

  - name: "Arm-FVP"
    template: FVP.adapter.json                # template file

  - name: "Keil uVision"
    template: uVision.adapter.json            # template file
```
