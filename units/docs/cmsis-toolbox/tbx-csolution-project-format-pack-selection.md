---
id: "tbx-csolution-project-format-pack-selection"
type: "concept"
domain: "project"
title: "CSolution Project Format: Pack Selection"
summary: "The packs: node which can be specified in the .csolution.yml file, allows you to:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#pack-selection"
license: "Apache-2.0"
mode: "V"
---

The `packs:` node which can be specified in the `*.csolution.yml` file, allows you to:

- Reduce the scope of software packs that are available for projects.
- Add specific software packs that are optional with version specifications.
- Provide a path to a local installation of a software pack that is, for example, project-specific or under development.

The  [Pack Name Conventions](#pack-name-conventions) specify the names of the software packs.
The `pack:` definition may be specific to a [`context`](#context) that specifies `target-types:` and/or `build-types:` or provides a local path to a development repository of a software pack.

!!! Note
    - By default, the **`csolution` Project Manager** only loads the latest version of the installed software packs. It is, however, possible to request specific versions using the `- pack:` node.
    - An attempt to add two different versions of the same software pack results in an error.

### `packs:`

The `packs:` node is the start of a pack selection.

`packs:`                                              | Content
:-----------------------------------------------------|:------------------------------------
    [`- pack:`](#pack)                 | Explicit pack specification (additive)

### `pack:`

The `pack:` list allows to add [specific software packs](#pack-name-conventions), optional with a version specification.

`pack:`                                                     | Content
:-----------------------------------------------------------|:------------------------------------
    `path:`                                  | Explicit path name that stores the software pack. This can be a relative path to your project workspace.
    [`for-context:`](#for-context)           | Include pack for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context)   | Exclude pack for a list of *build* and *target* types.

!!! Note
    When an explicit `path:` to the pack is specified, an explicit pack version cannot be specified as the path directly specifies the pack to include.

**Example:**

```yml
packs:                                  # start section that specifics software packs
  - pack: AWS                           # use packs from AWS
  - pack: NXP::*K32L*                   # use packs from NXP relating to K32L series (would match K32L3A60_DFP + FRDM-K32L3A6_BSP)
  - pack: ARM                           # use packs from Arm

  - pack: Keil::Arm_Compiler            # add latest version of Keil::Arm_Compiler pack
  - pack: Keil::MDK-Middleware@7.13.0   # add Keil::MDK-Middleware pack at version 7.13.0
  - pack: ARM::CMSIS-FreeRTOS@~10.4.0   # add CMSIS-FreeRTOS with version 10.4.x or higher but lower than 10.5.0
  - pack: ARM::CMSIS-FreeRTOS@^10.4.0   # add CMSIS-FreeRTOS with version 10.4.x or higher but lower than 11.0.0

  - pack: NXP::K32L3A60_DFP             # add pack for NXP device
    path: ./local/NXP/K32L3A60_DFP      # with path to the pack (local copy, repo, etc.)

  - pack: AWS::coreHTTP                 # add pack
    path: ./development/AWS/coreHTTP    # with path to development source directory
    for-context: +DevTest               # pack is only used for target-type "DevTest"
```
