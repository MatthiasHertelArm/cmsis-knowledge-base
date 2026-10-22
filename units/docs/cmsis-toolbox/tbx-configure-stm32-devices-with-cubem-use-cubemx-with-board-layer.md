---
id: "tbx-configure-stm32-devices-with-cubem-use-cubemx-with-board-layer"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: Use CubeMX with Board Layer"
summary: "A software layer is a set of pre-configured software components and source files that can be reused in multiple projects. A board layer typically contains basic I/O drivers and related device and board configuration."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#use-cubemx-with-board-layer"
license: "Apache-2.0"
mode: "V"
---

A [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-overview.md#software-layers) is a set of pre-configured software components and source files that can be reused in multiple projects. A board layer typically contains basic I/O drivers and related device and board configuration.

For a board layer, CubeMX can be used to generate device configuration and peripheral drivers. As a board layer uses a separate directory that is independent of a specific *csolution project*, the location of the  STM32CubeMX generated files should be specified using the [`generators:`](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/YML-Input-Format.md#generators) node in the `<board>.clayer.yml` file. This locates the CubeMX-generated files in the directory structure of the [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-overview.md#software-layers). As a board layer is used by several projects, the name of the generator import file should also be explicitly specified, as shown below:

```yml
generators:
    options:
    - generator: CubeMX
      path: ./CubeMX              # path relative to the `*.clayer.yml` file
      name: Board                 # generator import file is named `Board.cgen.yml`.
```

This configuration results in the following directory structure:

Directory and Files          | Description
:----------------------------|:---------------------------------------
`<board>.clayer.yml`           | Defines the source files and software components of the board layer.
`CubeMX/`                    | Directory with CubeMX ioc file and other generated files and folders.
`CubeMX/Board.cgen.yml`      | Generator import file that lists CubeMX-generated files and options.
`CubeMX/STM32CubeMX/`        | Directory with CubeMX generated files.
`CubeMX/STM32CubeMX/Drivers/`| Directory with driver-related source files.

Several [STM32 Board Support Packs with Generator Support](https://github.com/Open-CMSIS-Pack) contain board layers that use such a configuration. For examples, the [Nucleo-F756ZG_BSP](https://www.keil.arm.com/packs/nucleo-f756zg_bsp-keil/overview/) or [B-U585I-IOT02A_BSP](https://www.keil.arm.com/packs/b-u585i-iot02a_bsp-keil/overview/).
