---
id: "tbx-reference-applications-usage"
type: "concept"
domain: "project"
title: "Reference Applications: Usage"
summary: "A Reference Application is an incomplete .csolution.yml project file that requires additional intervention."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#usage"
license: "Apache-2.0"
mode: "V"
---

A *Reference Application* is an incomplete `*.csolution.yml` project file that requires additional intervention.

The following steps explain how to compile the project:

### Step 1: Add DFP and BSP

In the `*.csolution.yml` file under the `packs:` node, add the DFP and, when available, the BSP for the selected physical or simulated target. Under `target-types:`, add the board or device represented by that target.

```yml
solution:
  cdefault:
  :
  packs:
    - pack: Keil::STM32U5xx_DFP
    - pack: Keil::B-U585I-IOT02A_BSP
  target-types:
    - type: MyBoard
      board: B-U585I-IOT02A         # name of a target board
```

### Step 2: Run `cbuild setup`

Run `cbuild setup` with the `*.csolution.yml` file. This identifies compatible layers that are part of the software packs listed in the `*.csolution.yml` file with an output similar to:

```txt
>cbuild setup xxx.csolution.yml
error csolution: undefined variables in xxx.csolution.yml:
  - $Board-Layer$
To resolve undefined variables, copy the settings from cbuild-idx.yml to csolution.yml
```

The related `*.cbuild-idx.yml` should contain information similar to this:

```yml
build-idx:
  generated-by: csolution version 2.4.0
  cdefault: cdefault.yml
  csolution: xxx.csolution.yml
  configurations:
    - target-type: B-U585I-IOT02A
      target-configurations:
        - configuration:
          variables:
            - Board-Layer: ${CMSIS_PACK_ROOT}/Keil/B-U585I-IOT02A_BSP/2.0.0/Layers/IoT/Board.clayer.yml
              description: B-U585I-IOT02A Board setup for IoT
              path: ${CMSIS_PACK_ROOT}/Keil/B-U585I-IOT02A_BSP/2.0.0/Layers/IoT
              file: Board.clayer.yml
              copy-to: .Board/U585
```

As a user, you have now two choices to work with the identified software layer:

### Refer layers in ${CMSIS_PACK_ROOT}

This is useful when there is no plan to modify the software layer, for example, in the early phase of adoption.

```yml
solution:
  cdefault:
  :
  target-types:
    - type: B-U585I-IOT02A
      board: B-U585I-IOT02A         # name of a target board
      variables:
        - Board-Layer: ${CMSIS_PACK_ROOT}/Keil/B-U585I-IOT02A_BSP/2.0.0/Layers/IoT/Board.clayer.yml
```

### Copy layers to csolution project

This allows the modification of the layer, for example, adding or removing drivers or changing device settings.

It requires these steps:

1. Copy all files from `path`, i.e. `${CMSIS_PACK_ROOT}/Keil/B-U585I-IOT02A_BSP/2.0.0/Layers/IoT` to the local csolution project directory.
2. If set, remove the R/O attribute from the copied files.
3. Under `variables:`, add the path to the `*.clayer.yml` file. Use `$SolutionDir()` as base path to make the project portable.

```yml
solution:
  cdefault:
  :
  target-types:
    - type: B-U585I-IOT02A
      board: B-U585I-IOT02A         # name of a target board
      variables:
        - Board-Layer: $SolutionDir()$/Board/B-U585I-IOT02A/Board.clayer.yml
```

!!! Note
    The copy step is executed for you by some IDEs during the *Create New Project* workflow.
