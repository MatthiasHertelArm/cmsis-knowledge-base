---
id: "tbx-csolution-project-structure-run-and-debug-configuration"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Run and Debug Configuration"
summary: "The CMSIS-Toolbox uses the information from the DFP and BSP to simplify the debugger configuration. It generates the file <solution-name>+<target-type>.cbuild-run.yml that contains for one target of a csolution project all information for run and debug."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#run-and-debug-configuration"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Toolbox uses the information from the DFP and BSP to simplify the debugger configuration.  It generates the file `<solution-name>+<target-type>.cbuild-run.yml` that contains for one target of a *csolution project* all information for run and debug. This file is used by [pyOCD](https://pyocd.io/) and the [CMSIS Solution extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) to configure debug and programming features of the [supported debug adapters](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#debug-adapter-integration).

An application can be composed of [various project contexts](#configure-related-projects) and [additional images](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#images). In addition the [debugger](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#debugger) along with parameters are specified in the `*.csolution.yml` file using the [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-set) node.

!!! Note
    Refer to [Run and Debug Management](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#run-and-debug-management) for further details.

**Examples:**

The following example configures the ST-LINK debugger for the project  `MyProject` with build-type `Debug`:

```yml
  target-types:
    - type: MyBoard
      board: B-U585I-IOT02A                   # Board name
      target-set:
        - set:
          debugger:
            name: ST-LINK
          images:
            -  project-context: MyProject.Debug
```

A target set can combine project contexts with different build types. This allows the project being debugged to use `Debug`, while size-sensitive supporting images use `Release`.

The following example uses a CMSIS-DAP debugger with JTAG protocol and configures a multi-core application with two projects. The project `core0` uses the build-type `Debug`. The project `core1` uses the build-type `Release`.

```yml
  target-types:
    - type: Alif_AppKitE7
      board: Alif Semiconductor::AppKit-E7
      target-set:
        - set:
          debugger:
            name: CMSIS-DAP
            protocol: jtag

          images:
            - project-context: core0.Debug
            - project-context: core1.Release
```

### Using pyOCD

A *csolution project* that uses `target-set:` to configure the debugger and select the images/projects and build-types should be build using the option `--active` to select the target in the format `<target-type>[@<target-set>]`.  The `cbuild` command creates then a corresponding `*.build-run.yml` file that can be used with [pyOCD version 0.37.0](https://pyocd.io/) or higher. This `*.build-run.yml` file contains all information to [program and debug the application](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#run-and-debug-management).

**Example:**

```shell
cbuild MyApplication.csolution.yml --active MyBoard                       # build application
pyocd load --cbuild-run MyApplication+MyBoard.cbuild-run.yml              # download image to target
pyocd gdbserver --cbuild-run MyApplication+MyBoard.cbuild-run.yml         # start GDB remote server
```

### Using VS Code

With the VS Code extension [CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) version 1.54 or higher use the **Manage Solution** view to configure the debugger. You may then use the [CMSIS Debugger](https://marketplace.visualstudio.com/items?itemName=Arm.vscode-cmsis-debugger) extension for interactive debug or [pyOCD](https://pyocd.io) in command line mode.

### Device Configuration

Several DFP contain `*.dbgconf` files that configure device-specific debug and trace parameters. The CMSIS-Toolbox provides this configuration information in the `*.cbuild-run.yml` file for [debuggers with Debug Access Sequence support](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#run-and-debug-management).

The CMSIS-Toolbox creates the `.cmsis` directory in the *csolution project* directory and generates a default `*.dbgconf` file for each target, for example `.cmsis/MyApplication+MyBoard.dbgconf`. This file can be modified to reflect user settings.

An explicit user-managed `*.dbgconf` configuration file can instead be specified using the [`debugger:` node](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#debugger) in the `*.csolution.yml` file.
