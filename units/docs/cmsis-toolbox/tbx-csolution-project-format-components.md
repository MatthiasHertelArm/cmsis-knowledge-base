---
id: "tbx-csolution-project-format-components"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `components:`"
summary: "Add software components to a project or a software layer. Used in .cproject.yml and .clayer.yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#components"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

Add software components to a project or a software layer. Used in `*.cproject.yml` and `*.clayer.yml` files.

`components:`                                                   |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- component:`                                                  | **Required** | Name of the software component.
    [`for-context:`](#for-context)               |   Optional   | Include component for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context)       |   Optional   | Exclude component for a list of *build* and *target* types.
    [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
    [`debug:`](#debug)                           |   Optional   | Generation of debug information.
    [`warnings:`](#warnings)                     |   Optional   | Control generation of compiler diagnostics.
    [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     |   Optional   | Remove define symbol settings for code generation.
    [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
    [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
    [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
    [`instances:`](#instances)                   |   Optional   | Add multiple instances of component configuration files (default: 1)
    `build-scope:`                               |   Optional   | Control inclusion of component source files.
(default: `include` for executable builds, `exclude` for library builds)

**Example:**

```yml
  components:
    - component: ARM::CMSIS:RTOS2:FreeRTOS&Cortex-M

    - component: ARM::RTOS&FreeRTOS:Config&CMSIS RTOS2
    - component: ARM::RTOS&FreeRTOS:Core&Cortex-M
    - component: ARM::RTOS&FreeRTOS:Event Groups
    - component: ARM::RTOS&FreeRTOS:Heap&Heap_5
    - component: ARM::RTOS&FreeRTOS:Stream Buffer
    - component: ARM::RTOS&FreeRTOS:Timers

    - component: ARM::Security:mbed TLS
      define:
        - MBEDTLS_CONFIG_FILE: "aws_mbedtls_config.h"
    - component: AWS::FreeRTOS:backoffAlgorithm
    - component: AWS::FreeRTOS:coreMQTT
    - component: AWS::FreeRTOS:coreMQTT Agent
    - component: AWS::FreeRTOS:corePKCS11&Custom
      define:
        - MBEDTLS_CONFIG_FILE: "aws_mbedtls_config.h"
```

!!! Note
    The name format for a software component is described under [Name Conventions: Component Name Conventions](#component-name-conventions).
