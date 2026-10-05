---
id: "tbx-configure-stm32-devices-with-cubem-migration-to-cmsis-toolbox-cubemx-integr"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: Migration to CMSIS-Toolbox CubeMX Integration"
summary: "In previous CubeMX integrations a .gpdsc file is used to import the generator output. The following table compares the CMSIS-Toolbox CubeMX integration (based on .cgen.yml files) with the previous STM32CubeMX integration (based on .gpdsc files)."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#migration-to-cmsis-toolbox-cubemx-integration"
license: "Apache-2.0"
mode: "V"
---

In previous CubeMX integrations a `*.gpdsc` file is used to import the generator output. The following table compares the CMSIS-Toolbox CubeMX integration (based on `*.cgen.yml` files) with the previous STM32CubeMX integration (based on `*.gpdsc` files).

Comparison                       | CMSIS-Toolbox `*.cgen.yml` Integration           | Previous `*.gdpsc` Integration
:--------------------------------|:-------------------------------------------------|:------------------------------
IDE Support                      | [VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack), Keil uVision 5.40 or higher   | Keil uVision, [CMSIS-Pack for Eclipse](https://github.com/ARM-software/cmsis-pack-eclipse)
CLI Tools                        | [CMSIS-Toolbox 2.4.0](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/installation.md) or higher | n/a
STM32CubeMX project file         | `STM32CubeMX.ioc`                                | `STCubeGenerated.ioc`
STM32CubeMX source location      | `./STM32CubeMX/<target-type/STM32CubeMX/Src`     | `./RTE/Device/<device name>/STCubeGenerated/Src` or `./Board/<board name>/STM32CubeMX/Src`
STM32CubeMX include location     | `./STM32CubeMX/<target-type/STM32CubeMX/Inc`     | `./RTE/Device/<device name>/STCubeGenerated/Inc` or `./Board/<board name>/STM32CubeMX/Inc`
ST Firmware                      | Provided by STM32Cube Firmware Packs           | Provided by STM32*_DFP software pack
CMSIS-Driver                     | Provided by [CMSIS-Driver_STM32](https://github.com/Open-CMSIS-Pack/CMSIS-Driver_STM32) software pack     | Provided by STM32*_DFP software pack

To migrate existing projects that were using the previous STM32CubeMX integration (based on `*.gpdsc` files), use the following steps:

1. Remove all `component: Keil::Device:xxx` from the `*.cproject.yml` file.
2. Add the `component: Device:CubeMX` to the `*.cproject.yml` file.
3. Use `csolution run *.csolution.yml -g CubeMX` to initialize the directory structure.
4. Replace the file `STM32CubeMX.ioc` with the file `STCubeGenerated.ioc` from the previous project.
5. Copy the source and include files from the previous location, as they may contain user modifications.
6. Use `csolution run *.csolution.yml -g CubeMX` to generate the output from the previous STM32CubeMX project.
7. Update the configuration in STM32CubeMX:
    - In the tab `Project Manager - Project` set *Project Settings - Toolchain/IDE* to match the compiler selection in the csolution project.
    - In the tab `Project Manager - Code Generator` under *STM32Cube MCU packages and embedded software packs* select `Copy only necessary library files`.
    - Click `GENERATE CODE` to complete the migration.

### uVision - Update STM32 DFP Packs

The [Generator Integration](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-operation.md#generator-integration) of the CMSIS-Toolbox is also available with uVision version 5.40 or higher.

New `STM32*_DFP` software packs containing release information **Updated for new CMSIS-Toolbox CubeMX integration** require migration. The steps below describe the migration process of a previous CubeMX configuration.

1. In &micro;Vision open the dialog *Manage - Run-Time Environment*.

2. Remove all components from the `Device` Cclass, as CubeMX now manages the STM32 device firmware.
3. Close *Manage - Run-Time Environment* with *OK*.
4. Open the dialog *Manage - Run-Time Environment* again.
5. Select the component `Device:CubeMX` and start STM32CubeMX with the `play` button.
6. Update the configuration in STM32CubeMX:
    - In the tab `Project Manager - Project`, set *Project Settings - Toolchain/IDE* to `MDK-ARM`.
    - In the tab `Project Manager - Code Generator` under *STM32Cube MCU packages and embedded software packs* select `Copy only necessary library files`.
    - Click `GENERATE CODE` to complete the migration.

**Starting a new project** works similarly with these steps:

1. In uVision use *Project - New uVision Project* and select the STM32 device that you want to use.
   - Optional: *Project - Manage - Project items* tab *Project Info / Layer* allows to select an evaluation board under `Board`.

2. Open the dialog *Manage - Run-Time Environment*.
3. Select the component `Device:CubeMX` and start STM32CubeMX with the `play` button.
4. Create a new device configuration in STM32CubeMX:
    - Follow the instructions of STM32CubeMX and verify settings.
    - In the tab `Project Manager - Project` set *Project Settings - Toolchain/IDE* to `MDK-ARM`.
    - In the tab `Project Manager - Code Generator` under *STM32Cube MCU packages and embedded software packs* select `Copy only necessary library files`.
    - Click `GENERATE CODE` to complete the migration.
