---
id: "tbx-create-applications-start-a-project"
type: "concept"
domain: "project"
title: "Create Applications: Start a Project"
summary: "An application is based on a device and/or board supported by a Device Family Pack (DFP) or Board Support Pack (BSP). The steps to start a project are:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CreateApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/#start-a-project"
license: "Apache-2.0"
mode: "V"
---

An application is based on a *device* and/or *board* supported by a Device Family Pack (DFP) or Board Support Pack (BSP). The steps to start a project are:

### Step 1: Install the DFP and BSP

- Use [Device search](https://www.keil.arm.com/devices/) or [Board search](https://www.keil.arm.com/boards/) available on web portals to identify the software packs required for your target.

- Download the Device Family Pack (DFP) and optionally the Board Support Pack (BSP) with [`cpackget`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-tools.md#install-public-packs). Note that a BSP is only required if you want to work with a specific board. For custom hardware, typically the DFP is sufficient.

### Step 2: Use a Template Project and add DFP and BSP

- Select a suitable generic [Template Project](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/Templates). These templates show the file structure for different types of `csolution` projects. Replace the placeholders and add the application content required for your project.

- Alternatively, refer to the DFP or BSP documentation, as some software packs provide device-specific or board-specific template projects.

- Copy the template project and open the `*.csolution.yml` file.  Add under [`packs:`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#packs) the packs identified in step (1). You may omit the version number during initial project development.

```yml
  :
  compiler: AC6
  # List the packs that define the device and/or board.
  packs:
    - pack: AnalogDevices::ADuCM320_DFP
  :
```

### Step 3: Use `csolution list` to identify the device or board

- Use `csolution list devices <name>.csolution.yml` or `csolution list boards <name>.csolution.yml` to get the device or board name.

- Enter the device or board name under [`target-types:`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#target-types). A device is typically used for custom hardware.

```yml
  :
  target-types:
    - type: ADuCM320-Board    # choose a brief name for your target hardware
    # device: MyDeviceName    # replace with your device or comment out to use a board
      board: Analog Devices::EVAL-ADuCM320EBZ     # you may omit version information
  :
```

### Step 4: Add required software components

- Most projects at least require the `CMSIS:CORE` and `Device:Startup` (or a variant) [software components](#software-components) to be present. Use `csolution list components <name>.csolution.yml` to identify the name of the startup component and add it to the file `*.cproject.yml` of your project.

- Use `csolution list components  <name>.csolution.yml` to identify additional software components from the selected packs. Use the [`components:`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#components) in the `<name>.cproject.yml` file to add new components and refer to related documentation for usage instructions. Note that you may omit vendor and version information for components as this is defined already by the packs that are selected.

```yml
  :
  components:                  # List components to use for your application
    - component: CMSIS:CORE    # The CMSIS-Core component used in most projects
    - component: Device:Startup&Baremetal
    - component: Device:Peripheral Libraries:ADC
  :
```

- Refer to [Using Components](#using-components) for more information.

- Once the referenced application source files are present, verify the project with `cbuild <name>.csolution.yml --update-rte --packs --context .Debug`. This command is suitable for a single project and for independent projects such as the UnitTest template. For Multicore and TrustZone templates, build the related application images through their target set with `cbuild <name>.csolution.yml --update-rte --packs --active <target-type>`. These commands download missing packs and copy configuration files to the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#rte-directory-structure).

### Step 5: Review and configure RTE files

- Review the configuration files in the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#rte-directory-structure) and refer to the documentation of the software components for instructions.

- [Configure Linker Scripts](#configure-linker-scripts) below explains how to setup physical memory.

- For simple projects, the default settings should be sufficient.

- The [build information file](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-CBuild-Format.md) `<name>.cbuild.Debug+<target-name>.yml` lists configuration files of components and other useful information such as links to documentation of the component.

### Step 6: Add application functionality

- Implement the application code in C/C++ source files. Use the [`groups:`](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#groups) section in `<name>.cproject.yml` to add new source files.

```yml
  :
  groups:
    - group: Source Files
      files:
        - file: main.c
        - file: MyFile1.c
  :
```

- Build the project again using the command appropriate for the selected template, as described in step (4). Repeat step (4) when you add new components that require configuration.

!!! Note
    The [Arm CMSIS Solution extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) guides you through these steps with the [`Create New Solution` workflow](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution#create-new-solution-view).
