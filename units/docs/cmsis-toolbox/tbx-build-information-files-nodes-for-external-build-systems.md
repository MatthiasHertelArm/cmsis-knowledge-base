---
id: "tbx-build-information-files-nodes-for-external-build-systems"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / Nodes for External Build Systems"
summary: "The following nodes describe contexts built by external build systems."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#nodes-for-external-build-systems"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The following nodes describe contexts built by external build systems.

#### `west:`

For each west build context a node `west:` is created in *.cbuild.yml

`west:`                                                   |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `app-path:`                            | **Required** | Path to the application source directory.
&nbsp;&nbsp;&nbsp; `project-id:`                          | **Required** | Project identifier
&nbsp;&nbsp;&nbsp; `board:`                               | **Required** | Board name used for west build invocation.
&nbsp;&nbsp;&nbsp; `device:`                              |   Optional   | Specify the processor core for execution of the generated image (used in `*.cbuild-run.yml`).
&nbsp;&nbsp;&nbsp; `west-defs:`                           |   Optional   | Defines in `CMake` format. The `west-defs:` from build and target-type are added.
&nbsp;&nbsp;&nbsp; `west-opt:`                            |   Optional   | Options for the `west` tool (default: empty).

**Example:**

```yml
  west:
    project-id: hello_world
    app-path: ../../../../hello_world
    board: stm32h7b3i_dk 
    west-defs:
      - CONFIG_BUILD_OUTPUT_HEX=y
```

#### `cmake:`

For each native CMake project context a node `cmake:` is created in `*.cbuild.yml`.

`cmake:`                                                  |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `source:`                              | **Required** | Path to the CMake source directory.
&nbsp;&nbsp;&nbsp; `project-id:`                          | **Required** | Project identifier.
&nbsp;&nbsp;&nbsp; `generator:`                           |   Optional   | CMake generator used for the build.
&nbsp;&nbsp;&nbsp; `configure:`                           |   Optional   | List of options for the CMake configure command.
&nbsp;&nbsp;&nbsp; `target:`                              |   Optional   | CMake build target.
&nbsp;&nbsp;&nbsp; `images:`                              |   Optional   | List of output images produced by the CMake project.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- image:`           | **Required** | Path to the CMake build output image.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `type:`  | **Required** | Output image type: `elf`, `hex`, `bin`, or `lib`.

**Example:**

```yml
  cmake:
    project-id: core0
    source: ../../../../cmake/core0
    generator: Ninja
    configure:
      - -DCMAKE_BUILD_TYPE=Debug
    target: core0-target
    images:
      - image: build/core0.elf
        type: elf
```
