---
id: "tbx-csolution-project-format-layer"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure / `layer:`"
summary: "The layer: node is the start of a .clayer.yml file and defines a Software Layer. It can contain the following nodes:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#layer"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project File Structure_

The `layer:` node is the start of a `*.clayer.yml` file and defines a [Software Layer](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/./build-overview.md#software-layers). It can contain the following nodes:

`layer:`                                                        |          | Content
:---------------------------------------------------------------|:---------|:------------------------------------
    [`type:`](#layer-type)                       | Optional | Layer type for combining layers; used to identify [compatible layers](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/ReferenceApplications.md#usage).
    `description:`                               | Optional | Brief description text of the layer.
    [`language-C:`](#language-c)                 | Optional | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             | Optional | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     | Optional | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) | Optional | Enable optimization at linker level.
    [`debug:`](#debug)                           | Optional | Generation of debug information.
    [`warnings:`](#warnings)                     | Optional | Control generation of compiler diagnostics.
    [`define:`](#define)                         | Optional | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 | Optional | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     | Optional | Remove define symbol settings for code generation.
    [`add-path:`](#add-path)                     | Optional | Additional include file paths.
    [`del-path:`](#del-path)                     | Optional | Remove specific include file paths.
    [`misc:`](#misc)                             | Optional | Literal tool-specific controls.
    [`device:`](#device)                         | Optional | Specify processor core.
    [`generators:`](#generators)                 | Optional | Control the directory structure for generator output.
    [`packs:`](#packs)                           | Optional | Defines packs that are required for this layer.
    [`for-device:`](#device-name-conventions)    | Optional | Device information, used for consistency check (device selection is in `*.csolution.yml`).
    [`for-board:`](#board-name-conventions)      | Optional | Board information, used for consistency check (board selection is in `*.csolution.yml`).
    [`connections:`](#connections)               | Optional | List of consumed and provided resources.
    [`processor:`](#processor)                   | Optional | Processor specific settings.
    [`linker:`](#linker)                         | Optional | Instructions for the linker.
    [`groups:`](#groups)                         | Optional | List of source file groups along with source files.
    [`components:`](#components)                 | Optional | List of software components used.

**Example:**

```yml
layer:
  type: Board
  description: Setup with Ethernet and WiFi interface
  processor:
    trustzone: secure        # set processor to secure
  components:
    - component: Startup
    - component: CMSIS CORE
  groups:
    - group: Secure Code
      files:
        - file: main_s.c
    - group: CMSE
      files:
        - file: interface.c
        - file: interface.h
        - file: tz_context.c
```
