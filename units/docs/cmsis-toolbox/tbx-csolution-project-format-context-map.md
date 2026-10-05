---
id: "tbx-csolution-project-format-context-map"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context / `context-map:`"
summary: "The context-map: node allows for a specific project-name the remapping of target-types: and/or build-types: to a different context: which enables:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#context-map"
license: "Apache-2.0"
mode: "V"
---

_Part of: Context_

The `context-map:` node allows for a specific `project-name` the remapping of `target-types:` and/or `build-types:` to a different `context:` which enables:

- Integrating an existing `*.cproject.yml` file in a different `*.csolution.yml` file that uses different `build-types:` and/or `target-types:` for the overall application.
- Defines how different `*.cproject.yml` files of a `*.csolution.yml` are to the binary image of the final target (needs reflection in cbuild-idx.yml).

The `context-map:` node lists a remapping of the [`context-name`](#context-name-conventions) for a `project-name` and specific `target-types:` and `build-types:`.

`context-map:`                                     |              | Content
:--------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `- <context-name>`              | **Required** | Specify an alternative [`context-name`](#context-name-conventions) for a project.

For the `context-map:` it is required to specify the `<project-name>` as part of the [`context-name`](#context-name-conventions). This project will use a different `.build-type` and/or `+target-type` as applied in the [`context-name`](#context-name-conventions). This remapping of the context applies for the specific type in the `build-types:` or `target-types:` list.

**Example 1:**

This application combines two projects for a multi-processor device, but the project `HelloCM7` requires a different setting for the build-type name `Release` as this enables different settings within the `*.cproject.yml` file.

```yml
  target-types:
    - type: DualCore
      device: MyDualCoreDevice

  build-types:
    - type: Release                        # When applying build-type name 'release':
      context-map:
        - HelloCM7.flex_release            # project HelloCM7 uses build-type name "flex_release" instead of "release"

  projects:
    - project: ./CM7/HelloCM7.cproject.yml
    - project: ./CM4/HelloCM4.cproject.yml
```

**Example 2:**

The following example uses three projects: `Demo`, `TFM`, and `Boot`. The project `TFM` should always be built using the context `TFM.Release+LibMode`. For the target-type name `Board`, the Boot project requires the `+Flash` target, but any build type could be used.

```yml
  target-types:
    - type: Board                          # When applying target-type: 'Board':
      context-map:
        - TFM.Release+LibMode              # for project TFM use build-type: Release, target-type: LibMode
        - Boot+Flash                       # for project Boot use target-type: Flash
      board: B-U585I-IOT02A
    - type: FVP                            # When applying target-type: 'FVP':
      context-map:
        - context: TFM.Release+LibMode     # for project TFM use build-type: Release, target-type: LibMode
      device: ARM::SSE-300-MPS3

  projects:
    - project: ./App/Demo.cproject.yml
    - project: ./Security/TFM.cproject.yml
    - project: ./Loader/Boot.cproject.yml
```
