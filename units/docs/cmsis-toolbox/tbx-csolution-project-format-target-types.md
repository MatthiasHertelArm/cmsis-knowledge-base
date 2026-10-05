---
id: "tbx-csolution-project-format-target-types"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context / `target-types:`"
summary: "The target-types: node may include toolchain options, target selection, and processor attributes:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#target-types"
license: "Apache-2.0"
mode: "V"
---

_Part of: Context_

The `target-types:` node may include [toolchain options](#toolchain-options), [target selection](#target-selection), and [processor attributes](#processor-attributes):

`target-types:`                                                 |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- type:`                                                       | **Required** | The target-type identifier that is used to create the [context](#context-name-conventions) name.
    [`compiler:`](#compiler)                     |   Optional   | Toolchain selection.
    [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
    [`debug:`](#debug)                           |   Optional   | Generation of debug information.
    [`warnings:`](#warnings)                     |   Optional   | Control Generation of debug information.
    [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     |   Optional   | Remove preprocessor (#define) symbols.
    [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
    [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
    [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
    [`board:`](#board)                           | **see Note** | Board specification.
    [`device:`](#device)                         | **see Note** | Device specification.
    [`processor:`](#processor)                   |   Optional   | Processor specific settings.
    [`context-map:`](#context-map)               |   Optional   | Use different `target-types:` for specific projects.
    [`variables:`](#variables)                   |   Optional   | Variables that can be used to define project components.
    [`memory:`](#memory)                         |   Optional   | Add additional off-chip memory available in target hardware.
    [`target-set:`](#target-set)                 |   Optional   | One or more target-set configurations for projects, images, and debugger.
    [`west-defs:`](#west-defs)                   |   Optional   | Defines in `CMake` format for the [west build](#west-build) system.

!!! Note
    Either `device:` or `board:` is required.
