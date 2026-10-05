---
id: "tbx-csolution-project-format-layer"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure / `layer:`"
summary: "The layer: node is the start of a .clayer.yml file and defines a Software Layer. It can contain the following nodes:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#layer"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project File Structure_

The `layer:` node is the start of a `*.clayer.yml` file and defines a [Software Layer](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/./build-overview.md#software-layers). It can contain the following nodes:

`layer:`                                                        |          | Content
:---------------------------------------------------------------|:---------|:------------------------------------
&nbsp;&nbsp;&nbsp; [`type:`](#layer-type)                       | Optional | Layer type for combining layers; used to identify [compatible layers](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/ReferenceApplications.md#usage).
&nbsp;&nbsp;&nbsp; `description:`                               | Optional | Brief description text of the layer.
&nbsp;&nbsp;&nbsp; [`language-C:`](#language-c)                 | Optional | Set the language standard for C source file compilation.
&nbsp;&nbsp;&nbsp; [`language-CPP:`](#language-cpp)             | Optional | Set the language standard for C++ source file compilation.
&nbsp;&nbsp;&nbsp; [`optimize:`](#optimize)                     | Optional | Optimize level for code generation.
&nbsp;&nbsp;&nbsp; [`link-time-optimize:`](#link-time-optimize) | Optional | Enable optimization at linker level.
&nbsp;&nbsp;&nbsp; [`debug:`](#debug)                           | Optional | Generation of debug information.
&nbsp;&nbsp;&nbsp; [`warnings:`](#warnings)                     | Optional | Control generation of compiler diagnostics.
&nbsp;&nbsp;&nbsp; [`define:`](#define)                         | Optional | Define symbol settings for C/C++ code generation.
&nbsp;&nbsp;&nbsp; [`define-asm:`](#define-asm)                 | Optional | Define symbol settings for Assembler code generation.
&nbsp;&nbsp;&nbsp; [`undefine:`](#undefine)                     | Optional | Remove define symbol settings for code generation.
&nbsp;&nbsp;&nbsp; [`add-path:`](#add-path)                     | Optional | Additional include file paths.
&nbsp;&nbsp;&nbsp; [`del-path:`](#del-path)                     | Optional | Remove specific include file paths.
&nbsp;&nbsp;&nbsp; [`misc:`](#misc)                             | Optional | Literal tool-specific controls.
&nbsp;&nbsp;&nbsp; [`device:`](#device)                         | Optional | Specify processor core.
&nbsp;&nbsp;&nbsp; [`generators:`](#generators)                 | Optional | Control the directory structure for generator output.
&nbsp;&nbsp;&nbsp; [`packs:`](#packs)                           | Optional | Defines packs that are required for this layer.
&nbsp;&nbsp;&nbsp; [`for-device:`](#device-name-conventions)    | Optional | Device information, used for consistency check (device selection is in `*.csolution.yml`).
&nbsp;&nbsp;&nbsp; [`for-board:`](#board-name-conventions)      | Optional | Board information, used for consistency check (board selection is in `*.csolution.yml`).
&nbsp;&nbsp;&nbsp; [`connections:`](#connections)               | Optional | List of consumed and provided resources.
&nbsp;&nbsp;&nbsp; [`processor:`](#processor)                   | Optional | Processor specific settings.
&nbsp;&nbsp;&nbsp; [`linker:`](#linker)                         | Optional | Instructions for the linker.
&nbsp;&nbsp;&nbsp; [`groups:`](#groups)                         | Optional | List of source file groups along with source files.
&nbsp;&nbsp;&nbsp; [`components:`](#components)                 | Optional | List of software components used.

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
