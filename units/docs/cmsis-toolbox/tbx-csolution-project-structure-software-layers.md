---
id: "tbx-csolution-project-structure-software-layers"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Software Layers"
summary: "Software layers collect source files and software components along with configuration files for reuse in different projects. Software Layers gives projects a better structure and simplifies:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-layers"
license: "Apache-2.0"
mode: "V"
---

Software layers collect source files and software components along with configuration files for reuse in different projects. Software Layers gives projects a better structure and simplifies:

- Development flows with evaluation boards and production hardware.
- Evaluation of middleware and hardware modules across different microcontroller boards.
- Code reuse across projects, i.e. board support for test-case deployment.
- Test-driven software development on simulation model and hardware.

**Simple Example:**

This example uses a layer to include an RTOS kernel. The file `MyProject.cproject.yml` includes the file `RTOS.clayer.yml` using the [`layers:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) node:

```yml
project:
  groups:
    - group: App
      files:
        - file: ./main.c

  components:
    - component: CMSIS:CORE
    - component: Device:Startup

  layers:
    - layer: ../Layer/RTOS.clayer.yml    # Add RTOS kernel
```

The `RTOS.clayer.yml` file defines the kernel along with configuration settings.

```yml
layer:
  description: RTX RTOS with configuration settings

  packs:
    - pack: ARM:CMSIS-RTX

  components:
    - component: CMSIS:RTOS2:Keil RTX5&Source
```

The diagram below shows two different scenarios, which are explained in the following sections.

(figure: Layer Usage)

### Target Production Hardware

Software development frequently starts on evaluation boards. Using a board layer simplifies re-targeting to  production hardware. The following `*.csolution.yml` file exemplifies the concept. A software developer starts with a board layer for the evaluation board in the folder `MyBoard`. Once the production hardware is available, this layer is copied to a different folder (i.e. `MyHardware`). As both layers are independently managed, the configuration of the `MyHardware` layer can be modified, for example, to target different devices, pin layout, or peripheral configurations.

In the `*.csolution.yml` project, the layer is defined using a [variable](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#variables). By changing the `target-type` during the build process, the software developer can continue to use the evaluation board or target the production hardware.

```yml
solution:
  cdefault:
  compiler: AC6

  target-types:
    - type: EvalBoard
      board: STMicroelectronics::B-U585I-IOT02A:Rev.C
      device: STMicroelectronics::STM32U585AIIx
      variables:
        - Board-Layer: $SolutionDir()$/MyBoard/Board.clayer.yml

    - type: ProductionHW
      device: STMicroelectronics::STM32U575AIIx    # uses a different device
      variables:
        - Board-Layer: $SolutionDir()$/MyHardware/Board.clayer.yml

  build-types:
    - type: Debug
      debug: on
      optimize: debug
    - type: Release
      debug: off
      optimize: balanced

  projects:
    - project: HID/HID.cproject.yml
```

!!! Tip
    - The [MDK-Middleware examples](https://arm-software.github.io/MDK-Middleware/latest/General/working_with_examples.html) are structured in this way. Start with a board layer that is provided in several [Board Support Packs](https://github.com/Open-CMSIS-Pack#stm32-packs-with-generator-support).
    - Another project that extends this concept to hardware shields is the [Sensor-SDK-Example](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example).

### Test Case Project

Modern software design mandates for [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) that utilize DevOps or CI principals. [Arm Fixed Virtual Platform (FVP)](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#arm-fvp) simulation models allow test automation without target hardware.

However, in some cases, tests should also be performed on physical hardware. A test case project may, therefore, contain targets for simulation and physical hardware. The *csolution project* format allows multiple test projects to be combined to validate different parts of the application.

```yml
solution:
  cdefault:
  compiler: GCC
    :                              # pack definition not shown

  target-types:
    - type: Board
      board: NUCLEO-L552ZE-Q
      variables:
        - Board-Layer: ./Board/NUCLEO-L552ZE-Q/Board.clayer.yml

    - type: FVP
      board: VHT-Corstone-300      # FVP platform (appears as a board)
      variables:
        - Board-Layer: ./Board/Corstone-300/FVP.clayer.yml

  projects:
    - project: ./TestSuite1/TestCases.cproject.yml
    - project: ./TestSuite2/TestCases.cproject.yml
    - project: ./TestSuite3/TestCases.cproject.yml
```

!!! Tip
    - Several [examples for Arm FVP simulation models](https://github.com/Arm-Examples#avh-fvp-examples) show usage of *csolution projects* in CI workflows.
    - The project [AVH-MLOps-Main](https://github.com/Arm-Examples/AVH-MLOps_Examples/tree/main/AVH-MLOps-main) is a test project that shows retargeting to different processors using a layer.
    - The project [AWS_MQTT_Demo](https://github.com/Arm-Examples/AWS_MQTT_Demo) extends this concept with retargeting of an IP communication to virtual or physical hardware.

### Configuration Settings

A software layer is a set of source files and pre-configured software components or source code that can be shared across multiple projects. To achieve this, the configuration files of a [`layer`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#layer) are stored within the directory structure of the software layer. This separate [RTE Directory Structure](#rte-directory-structure) allows that projects
can share a `layer` with common configuration settings.

!!! Note
    When using a generator, such as CubeMX or MCUxpresso, the output should be redirected as described under [Configure Generator Output](#configure-generator-output).

### Software Layers in Packs

Software layers for [*reference applications*](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/ReferenceApplications.md) may be published in software packs. For more information, refer to [Pack Creation: Layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/pack-tools.md#layers).
