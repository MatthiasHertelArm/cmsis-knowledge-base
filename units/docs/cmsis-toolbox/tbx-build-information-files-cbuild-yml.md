---
id: "tbx-build-information-files-cbuild-yml"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / `*.cbuild.yml`"
summary: "The <project-name>.<build-type>+<target-type>.cbuild.yml file contains all information for one context. It is structured as outlined below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#cbuild-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The `<project-name>.<build-type>+<target-type>.cbuild.yml` file contains all information for one *context*. It is structured as outlined below.

`build:`                                                      | Content
:-------------------------------------------------------------|:------------------------------------
    `generated-by:`                            | Reference to csolution tool along with version information used to generate this application.
    `context:`                                 | Project [context](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#context-name-conventions) of this build description.
    `compiler:`                                | [Compiler toolchain](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#compiler) used for code generation.
    `board:`                                   | [Board name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#board) used for this context.
    `board-pack:`                              | BSP that is defining the [Board name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#board) used for this context.
    `board-books:`                             | List board documentation as defined in the [PDSC element `<board>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_book).
    `device:`                                  | [Device name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#device) with processor core selection used in this  project context.
    `device-pack:`                             | DFP that is defining the [Device name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#device) with processor core selection used in this  project context.
    `device-books:`                            | List device documentation as defined in the [PDSC element `<device>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_book).
    `processor:`                               | List of [processor attributes](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#processor) used in this project context.
    [`packs:`](#packs)                         | List of software [packs](#packs) along with path information used to generate this project context.
    `optimize:`                                | Generic [optimize](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#optimize) level for code generation.
    `link-time-optimize:`                      | Enable [optimization at linker level](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#link-time-optimize).
    `debug:`                                   | Global control the generation of [debug](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debug) information.
    `warnings:`                                | Global control [warning](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#warnings) level for compiler diagnostics.
    `misc:`                                    | Global control of [miscellaneous](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#misc) literal tool-specific controls.
    `define:`                                  | List of global [define](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define) symbol settings.
    `add-path:`                                | List of global [include path](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-path) settings.
    `output-type:`                             | Select the [output type](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#output) (exe or lib) for this project context.
    `output-dirs:`                             | Specifies the [directories](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#output-dirs) used to generate the output files.
    `linker:`                                  | Specifies the [linker script processing](#linker) used to generate the output files.
    [`components:`](#components)               | List of software components used.
    [`apis:`](#apis)                           | List of API interfaces used.
    [`groups:`](#groups)                       | List of source file groups along with source files.
    [`constructed-files:`](#constructed-files) | List of files that are generated by RTE management of the `csolution` tool.
    [`licenses:`](#licenses)                   | List of licenses used by the various software components of this project context.

**Example:**

```yml
build:
  context: HelloWorld_cm0plus.Debug+FRDM-K32L3A6
  compiler: AC6
  device: K32L3A60VPJ1A:cm0plus
  processor:
    fpu: off
    endian: little
    trustzone: non-secure
  packs:
    - pack: ARM::CMSIS@5.9.0
      path: ${CMSIS_PACK_ROOT}/ARM/CMSIS/5.9.0
    - pack: NXP::K32L3A60_DFP@15.0.0
      path: ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0
  optimize: none
  debug: on
  misc:
    C:
      - -std=c99
      - -fno-builtin
    CPP:
      - -fno-builtin
    Link:
      - --diag_suppress 6314
      - --entry=Reset_Handler
  define:
    - CPU_K32L3A60VPJ1A_cm0plus
    - MCMGR_HANDLE_EXCEPTIONS=1
           :
    - _RTE_
  add-path:
    - ../middleware/multicore/mcmgr/src
    - RTE/Board_Support/K32L3A60VPJ1A_cm0plus
    - RTE/_HelloWorld_cm0plus.Debug_FRDM-K32L3A6
    - ${CMSIS_PACK_ROOT}/ARM/CMSIS/5.9.0/CMSIS/Core/Include
    - ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0
            :
  output-type: exe
  output-dirs:
    gendir: generated
    intdir: ../tmp/HelloWorld_cm0plus/FRDM-K32L3A6/Debug
    outdir: ../out/HelloWorld_cm0plus/FRDM-K32L3A6/Debug
    rtedir: RTE
  components:
    - component: ARM::CMSIS:CORE@5.6.0
      condition: ARMv6_7_8-M Device
      from-pack: ARM::CMSIS@5.9.0
      selected-by: ARM::CMSIS:CORE
    - component: NXP::Device:CMSIS:K32L3A60_system@1.0.0
      condition: device.K32L3A60_AND_device.K32L3A60_CMSIS
      from-pack: NXP::K32L3A60_DFP@15.0.0
      selected-by: NXP::Device:CMSIS:K32L3A60_system
      files:
        - file: ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0/system_K32L3A60_cm0plus.c
          category: sourceC
    - component: NXP::Device:SDK Drivers:clock@2.2.1
      condition: device.K32L3A60_AND_driver.common
      from-pack: NXP::K32L3A60_DFP@15.0.0
      selected-by: NXP::Device:SDK Drivers:clock
      files:
        - file: ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0/drivers/fsl_clock.c
          category: sourceC
    - component: NXP::Device:SDK Drivers:common@2.3.2
      condition: device.K32L3A60_AND_device.K32L3A60_CMSIS_AND_driver.clock
      from-pack: NXP::K32L3A60_DFP@15.0.0
      selected-by: NXP::Device:SDK Drivers:common
      files:
        - file: ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0/drivers/fsl_common.c
          category: sourceC
        - file: ${CMSIS_PACK_ROOT}/NXP/K32L3A60_DFP/15.0.0/drivers/fsl_common_arm.c
          category: sourceC
            :
  groups:
    - group: Application
      files:
        - file: ./hello_world_core1.c
          category: sourceC
        - file: ./RTE/Device/K32L3A60VPJ1A_cm0plus/K32L3A60xxx_cm0plus_flash.scf
          category: linkerScript
    - group: Middleware
      files:
        - file: ../middleware/multicore/mcmgr/src/mcmgr.c
          category: sourceC
            :
  constructed-files:
    - file: RTE/_HelloWorld_cm0plus.Debug_FRDM-K32L3A6/RTE_Components.h
      category: header
```
