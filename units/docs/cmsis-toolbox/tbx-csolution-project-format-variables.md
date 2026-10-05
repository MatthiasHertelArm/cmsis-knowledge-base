---
id: "tbx-csolution-project-format-variables"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context / `variables:`"
summary: "The variables: node defines key/value pairs in the .csolution.yml file. Using $<key>$ in .cproject.yml and .clayer.yml files expands to the value of the variable."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#variables"
license: "Apache-2.0"
mode: "V"
---

_Part of: Context_

The `variables:` node defines *key/value* pairs in the `*.csolution.yml` file. Using `$<key>$` in `*.cproject.yml` and `*.clayer.yml` files expands to the *value* of the variable. The variable `$<key>$` can be used in the following nodes: [`layers:`](#layers), [`define:`](#define), [`define-asm:`](#define-asm), [`add-path:`](#add-path), [`add-path-asm:`](#add-path-asm), [`misc:`](#misc), [`files:`](#files), and [`executes:`](#executes). The `<key>:` name format `<type>-Layer` is a convention that references [layer-type](#layer-type). In this case the `copied-from:` can be used to describe the original source of a layer (typically a path in a software pack).

`variables:`                         | Description
:------------------------------------|:-------------
&nbsp;&nbsp;&nbsp; `<key>:`          | `<key>:` specifies a variable name with value.
&nbsp;&nbsp;&nbsp; `copied-from:`    | Descriptive text that documents the source of a layer. 

**Example:**

With variables that are defined in the `*.csolution.yml` file, a `*.cproject.yml` file requires no modifications when new `target-types:` are introduced.  The required `layers:` could be instead specified in the `*.csolution.yml` file using a new node `variables:`.

*Example.csolution.yml*

```yml
solution:
  target-types:
    - type: NXP Board
      board: IMXRT1050-EVKB
      variables:
        - Socket-Layer: $SolutionDir()$/Socket/FreeRTOS+TCP/Socket.clayer.yml
        - Board-Layer:  $SolutionDir()$/Board/IMXRT1050-EVKB/Board.clayer.yml

    - type: ST Board
      board: B-U585I-IOT02A
      variables:
        - Socket-Layer: $SolutionDir()$/Socket/WiFi/Socket.clayer.yml
        - Board-Layer: $SolutionDir()$/Board/B-U585I-IOT02A/Board.clayer.yml
          copied-from: ${CMSIS_PACK_ROOT}/Keil/B-U585I-IOT02A_BSP/2.0.0/CMSIS/Board/
```

*Example.cproject.yml*

```yml
  layers:
    - layer: $Socket-Layer$
      type: Socket

    - layer: $Board-Layer$      # no `*.clayer.yml` specified. Compatible layers are listed
      type: Board               # layer of type `Board` is expected
```

#### Variable `west-board` 

[West Build](#west-build) uses a different schema for the [board name](#board-name-conventions). However several board names can be mapped to `west` tool. By default, the variable `$west-board$` holds the `board_name` (converted to lower-case, `-` replaced by `_`) of the current active target type as default for the [west:](#west) node. However, as some CMSIS boards names do not map, the variable `$west-board$` can be defined as shown below.

*Example.csolution.yml*

```yml
solution:
  target-types:
    - type: Alif Board
      board: Alif Semiconductor::DevKit-E7
      variables:
        - west-board: alif_e7_dk_rtss_he              # explicit west board name

    - type: ST Board
      board: STMicroelectronics::STM32H7B3I-DK        # $west-board$ set to `stm32h7b3i_dk`
```
