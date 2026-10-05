---
id: "tbx-build-information-files-nodes-for-project-management"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / Nodes for Project Management"
summary: "The configurations: node lists possible configurations for reference applications that have undefined variable settings."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#nodes-for-project-management"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

#### `configurations:`

The `configurations:` node lists possible configurations for [reference applications](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/ReferenceApplications.md) that have undefined variable settings.

`configurations:`                                                       | Content
:-----------------------------------------------------------------------|:------------------------------------
`- target-type:`                                                        | Name of target-type for which configurations are listed.
&nbsp;&nbsp;&nbsp;`target-configurations:`                              | List of possible configurations for the target-type.
&nbsp;&nbsp;&nbsp;- `configuration:`                                    | Possible configuration for the reference application.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`- variables:`                      | List of variable names with configuration information.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<layer-name>:`   | Layer name with a value that is the path to the `clayer.yml` file.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`description:`    | Brief [description](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#layer) text taken from `*.clayer.yml`.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`settings:`       | Usage instructions for this layer.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`- set:`          | Value of `set` and `info` taken from [`connect:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#connect) in `*.clayer.yml`.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`path:`           | Path to the directory that contains the layer (from *.PDSC file).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`file:`           | Name of the *.clayer.yml file (optional with a relative path to the directory specified with path) (from `*.PDSC` file).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`copy-to:`        | Proposed directory for the layer in the *csolution project* (from *.PDSC file).

**Example:**

```yml
  configurations:
    - target-type: B-U585I-IOT02A
      target-configurations:
        - configuration:
            - variables:
              - Board-Layer: /Users/.../Arm/Packs/Keil/B-U585I-IOT02A_BSP/2.0.0-dev0/Layers/IoT/Board.clayer.yml
                description: "Configuration including FXLS8962 sensor"

    - target-type: MyBoard
        - configuration:
            - variables:
              - Board-Layer: ./layer/board/frdmk22f/frdmk22f.clayer.yml
                description: "Configuration: Ethernet, UART, and WiFi"
                settings:
                - set: set1.select1 (connect A - set 1 select 1)
                path: ./layer/board/frdmk22f
                file: frdmk22f.clayer.yml
                copy-to: board/frdmk22f
              - Shield-Layer: ./layer/shield/agmp03/agmp03.clayer.yml
                description: "Shield with FXLS8962 and FXAS21002"
                settings:
                - set: Bus.SPI (FXLS8962 SPI Bus - Jumper configuration: I2C/SPI=SPI)
                - set: Bus.SPI (FXAS21002 SPI Bus - Jumper configuration: I2C/SPI=SPI)
                path: ./layer/board/frdmk22f
                file: frdmk22f.clayer.yml
                copy-to: board/frdmk22f
```

#### `cprojects:`

The `cprojects:` node lists all `*.cproject.yml` input files along with `*.clayer.yml` files that are used to compose the application.

`cprojects:`                                                       | Content
:------------------------------------------------------------------|:------------------------------------
`- cproject:`                                                      | Relative path and name of a [`*.cproject.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#project) input file.
&nbsp;&nbsp;&nbsp;`clayers:`                                       | List of [`*.clayer.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#layer) input files used by this `*.cproject.yml` file.

**Example:**

```yml
  cprojects:
    - cproject: AWS_MQTT_MutualAuth_SW_Framework/Demo.cproject.yml
      clayers:
        - clayer: AWS_MQTT_MutualAuth_SW_Framework/Socket/FreeRTOS+TCP/Socket.clayer.yml
        - clayer: AWS_MQTT_MutualAuth_SW_Framework/Socket/WiFi/Socket.clayer.yml
        - clayer: AWS_MQTT_MutualAuth_SW_Framework/Socket/VSocket/Socket.clayer.yml
             :
```

#### `cbuilds:`

The `cbuilds:` node lists all project context configurations that are generated with this build.

`cbuilds:`                                                         | Content
:------------------------------------------------------------------|:------------------------------------
`- cbuild:`                                                        | Build description file of a single context for a *.cproject.yml input file.
&nbsp;&nbsp;&nbsp; `project:`                                      | Project name.
&nbsp;&nbsp;&nbsp; `configuration:`                                | Context configuration for this build description file.
&nbsp;&nbsp;&nbsp; `errors:`                                       | Error indication.
&nbsp;&nbsp;&nbsp; `packs-missing:`                                | List of missing packs.
&nbsp;&nbsp;&nbsp; `packs-unused:`                                 | List of unused packs.
&nbsp;&nbsp;&nbsp; `messages:`                                     | List of `errors:`, `warnings:`, or `info:` messages.

**Example:**

```yml
  cbuilds:
    - cproject: AWS_MQTT_MutualAuth_SW_Framework/Demo.cproject.yml
      project: Demo
      configuration: .Debug+FVP
      errors: true
      messages:
        errors:
          - no compatible software layer found. Review the required connections of the project
        info:
          - test.cbuild-set.yml - file is already up-to-date
```

#### `select-compiler:`

If no compiler is specified in the *csolution project*, the [`cbuild setup` command](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-operation.md#details-of-the-setup-mode) lists the available compilers based on the [compiler registration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/installation.md#compiler-registration) and `select-compiler:` node in the file [`*.csolution.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#solution) or [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#cdefault).

`select-compiler:`     | Content
:----------------------|:------------------------------------
`- compiler:`          | Name (optionally with version) of the compiler toolchain; copied from the `select-compiler:` node in the *csolution project*.

#### `packs:`

The `packs:` node is the start of a pack list that is used for the project context.

`packs:`                                              | Content
:-----------------------------------------------------|:------------------------------------
`- pack:`                                             | Explicit pack specification with exact version information used.
&nbsp;&nbsp;&nbsp;`path:`                             | Path name that stores the software pack (see note).

!!! Note
    Packs that are located in the [CMSIS-Pack root directory](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/installation.md#environment-variables) are prefixed with `${CMSIS_PACK_ROOT}`.

**Example:**

```yml
  packs:
    - pack: ARM::CMSIS-FreeRTOS@10.4.6
      path: ${CMSIS_PACK_ROOT}/ARM/CMSIS-FreeRTOS/10.4.6
    - pack: ARM::CMSIS@5.9.0
      path: ${CMSIS_PACK_ROOT}/ARM/CMSIS/5.9.0
       :
    - pack: MDK-Packs::IoT_Socket@1.3.1
      path: ../IoT_Socket
```

#### `generators:`

The `generators:` node contains information for calling a generator.

`generators:`                                                       | Content
:-------------------------------------------------------------------|:------------------------------------
`- generator:`                                                      | Section for a specific generator.
&nbsp;&nbsp;&nbsp; [`path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#generators)        | Path name for storing the files generated.
&nbsp;&nbsp;&nbsp; `gdpsc:`                                         | File name of the *.GDPSC file that stores the information in `path:`.
&nbsp;&nbsp;&nbsp; `command:`                                       | Section for invoking the generator on different Host operating systems.

**Example:**

```yml
  generators:
    - generator: STM32CubeMX
      path: RTE/Device
      gpdsc: RTE/Device/STM32L475VGTx/FrameworkCubeMX.gpdsc
      command:
        win:
          file: ${CMSIS_PACK_ROOT}/Keil/STM32L4xx_DFP/2.6.1/MDK/CubeMX/STM32CubeMxLauncher.exe
          arguments:
            - STM32L475VGTx
            - ../../Release+STM32L4.cprj
            - ${CMSIS_PACK_ROOT}/Keil/STM32L4xx_DFP/2.6.1
```

#### `generator:`

`generator:`                                                   | Content
:--------------------------------------------------------------|:------------------------------------
`- id:`                                                        | Generator identifier used for this component
&nbsp;&nbsp;&nbsp; `path:`                                     | File name and path to the *.cgen.yml file that is generated.
