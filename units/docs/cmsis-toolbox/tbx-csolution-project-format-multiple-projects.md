---
id: "tbx-csolution-project-format-multiple-projects"
type: "concept"
domain: "project"
title: "CSolution Project Format: Multiple Projects"
summary: "The section \"Configure Related Projects\" describes the organization of multiple projects. The file .csolution.yml describes the relationship of these projects and may also re-map target-types: and build-types: for projects using context-map:."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#multiple-projects"
license: "Apache-2.0"
mode: "V"
---

The section ["Configure Related Projects"](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#configure-related-projects) describes the
organization of multiple projects. The file `*.csolution.yml` describes the relationship of these projects and may also re-map
`target-types:` and `build-types:` for projects using [`context-map:`](#context-map).

### `projects:`

The YAML structure of the section `projects:` is:

`projects:`                                               |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
[`- project:`](#project)                                  |   Optional   | Path to the `*.cproject.yml` file.
    [`west:`](#west)                       |   Optional   | Enable West "build orchestration wrapper" for Zephyr projects.
    [`cmake:`](#cmake)                     |   Optional   | Enable native CMake project build orchestration.
    [`for-context:`](#for-context)         |   Optional   | Include project for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context) |   Optional   | Exclude project for a list of *build* and *target* types.

!!! Note
  - The nodes `project:`, `west:`, and `cmake:` are mutually exclusive in one list node. A list may contain several nodes of each type.

**Examples:**

This example uses two projects that are built in parallel using the same `build-type:` and `target-type:`.  Such a setup is typical for multi-processor systems.

```yml
  projects:
    - project: ./CM0/CM0.cproject.yml      # include project for Cortex-M0 processor
    - project: ./CM4/CM4.cproject.yml      # include project for Cortex-M4 processor
```

This example uses multiple projects but with additional controls.

```yml
  projects:
    - project: ./CM0/CM0.cproject.yml      # specify cproject.yml file
      for-context: +CM0-Addon              # build only when 'target-type: CM0-Addon' is selected

    - project: ./CM0/CM0.cproject.yml      # specify cproject.yml file
      for-context: +CM0-Addon              # specify use case

    - project: ./Debug/Debug.cproject.yml  # specify cproject.yml file
      not-for-context: .Release            # generated for any 'build-type:' except 'Release'

    - west:                                # enable west build orchestration wrapper
        app-path: ./blinky                 # specify a zephyr application path

    - cmake:                               # enable native CMake build orchestration
        source: ./native-cmake             # specify the CMake source directory
```
