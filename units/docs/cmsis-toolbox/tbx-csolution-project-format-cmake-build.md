---
id: "tbx-csolution-project-format-cmake-build"
type: "concept"
domain: "project"
title: "CSolution Project Format: CMake Build"
summary: "Enable native CMake project build orchestration and add its output images to the csolution project. This project type is supported with CMSIS-Toolbox 2.15 or higher and does not require a .cproject.yml file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#cmake-build"
license: "Apache-2.0"
mode: "V"
---

Enable native CMake project build orchestration and add its output images to the *csolution project*. This project type is supported with CMSIS-Toolbox 2.15 or higher and does not require a `*.cproject.yml` file.

### `cmake:`

Use CMake to configure and build the source directory specified in the `cmake:` node. Relative paths are based on the directory of the `*.csolution.yml` file.

The `project:`, `west:`, and `cmake:` descriptors are mutually exclusive within one `projects:` list entry. A solution may combine separate entries of all three types.

`cmake:`                                                  |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
    `source:`                              | **Required** | Path to the CMake source directory.
    `project-id:`                          |   Optional   | Project identifier used for the context name and output path (default: last sub-dir name of `source`).
    `generator:`                           |   Optional   | CMake generator to use for the build (default: `Ninja`).
    `configure:`                           |   Optional   | List of options for the CMake configure command.
    `target:`                              |   Optional   | CMake build target.
    [`images:`](#cmake-images)             |   Optional   | List of output images produced by the CMake project.
    [`device:`](#device)                   |   Optional   | Specify the processor core for execution of the generated images (used in `*.cbuild-run.yml`).

#### CMake `images:`

The `images:` node lists the output images produced by the native CMake project. Each output type can be specified only once.

Image paths are relative to the context output directory. CMSIS-Toolbox records these files as build outputs but does not define how the native CMake project creates them.

`images:`                                                 |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
`- image:`                                                | **Required** | Path to the CMake build output image.
    [`type:`](#type)                       | **Required** | Output image type: `elf`, `hex`, `bin`, or `lib`.

**Example:**

```yml
  projects:
    - cmake:
        source: ./cmake/core0
        project-id: core0
        device: :cm0_core0
        generator: Ninja
        configure:
          - -DCMAKE_BUILD_TYPE=Debug
        target: core0-target
        images:
          - image: build/core0.elf
            type: elf
          - image: build/core0.hex
            type: hex
          - image: build/core0.bin
            type: bin
```
