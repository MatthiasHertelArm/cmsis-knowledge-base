---
id: "tbx-csolution-project-format-build-types"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context / `build-types:`"
summary: "The build-types: node may include toolchain options:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#build-types"
license: "Apache-2.0"
mode: "V"
---

_Part of: Context_

The `build-types:` node may include [toolchain options](#toolchain-options):

`build-types:`                                                  |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- type:`                                                       | **Required** | The build-type identifier that is used to create the [context](#context-name-conventions) name.
    [`compiler:`](#compiler)                     |   Optional   | Toolchain selection.
    [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
    [`debug:`](#debug)                           |   Optional   | Generation of debug information.
    [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     |   Optional   | Remove preprocessor (#define) symbols.
    [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
    [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
    [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
    [`context-map:`](#context-map)               |   Optional   | Use different `build-types:` for specific projects.
    [`variables:`](#variables)                   |   Optional   | Variables that can be used to define project components.
    [`west-defs:`](#west-defs)                   |   Optional   | Defines in `CMake` format for the [west build](#west-build) system.

**Example:**

```yml
target-types:
  - type: Board                  # target-type name, used in context with: +Board
    board: NUCLEO-L552ZE-Q       # board specifies indirectly also the device

  - type: Production-HW          # target-type name, used in context with: +Production-HW
    device: STM32L552RC          # specifies device

build-types:
  - type: Debug                  # build-type name, used in context with: .Debug
    optimize: none               # specifies code optimization level
    debug: debug                 # generates debug information

  - type: Test                   # build-type name, used in context with: .Test
    optimize: size
    debug: on
```

The `board:`, `device:`, and `processor:` settings are used to configure the code translation for the toolchain. These
settings are processed in the following order:

1. `board:` relates to a BSP software pack that defines board parameters, including the
   [mounted device](https://arm-software.github.io/CMSIS_5/Pack/html/pdsc_boards_pg.html#element_board_mountedDevice).
   If `board:` is not specified, a `device:` must be specified.
2. `device:` defines the target device. If `board:` is specified, the `device:` setting can be used to overwrite the
   device or specify the processor core used.
3. `processor:` overwrites default settings for code generation, such as endianness, TrustZone mode, or disabling Floating
   Point code generation.

**Examples:**

```yml
target-types:
  - type: Production-HW
    board: NUCLEO-L552ZE-Q    # hardware is similar to a board (to use related software layers)
    device: STM32L552RC       # but uses a slightly different device
    processor:
      trustzone: off          # TrustZone disabled for this project
```

```yml
target-types:
  - type: Production-HW
    board: FRDM-K32L3A6       # NXP board with K32L3A6 device
    device: :cm0plus          # use the Cortex-M0+ processor
```
