---
id: "tbx-configure-stm32-devices-with-cubem-introduction"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: Introduction"
summary: "STM32CubeMX (CubeMX) is a graphical tool for configuration of an STM32 device or board. CubeMX generates C code for project and peripheral initialization, based on user settings. Depending on the device configuration, related drivers are added to the user application."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#introduction"
license: "Apache-2.0"
mode: "V"
---

[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) (CubeMX) is a graphical tool for configuration of an STM32 device or board. CubeMX generates C code for project and peripheral initialization, based on user settings. Depending on the device configuration, related drivers are added to the user application. The CMSIS-Toolbox interacts with CubeMX using the [generic interface for generators](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-operation.md#generator-integration).

The `component: Device:CubeMX` connects a *csolution project* to CubeMX. This component imports the CubeMX generated files for a selected `device:` or `board:` using the [generator import file `*.cgen.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/YML-CBuild-Format.md#generator-import-file). This file is similar to a [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-overview.md#software-layers) but managed by CubeMX and should be not modified directly.

An example project created with CubeMX can be found in [**csolution-examples/CubeMX**](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/CubeMX).

!!! Note
    - If a board is specified in the *csolution project*, CubeMX pre-configures the device peripherals with sensible settings for the evaluation board. The user may change these settings using the CubeMX dialogues.
    - If a device is specified, the user needs to configure the peripherals manually using CubeMX dialogues.
