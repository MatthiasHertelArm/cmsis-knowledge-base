---
id: "tbx-csolution-project-format-context"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context"
summary: "A context is an environment setup for a project that is composed of:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#context"
license: "Apache-2.0"
mode: "V"
---

A [`context`](#context-name-conventions) is an environment setup for a project that is composed of:

- `project-name` that is the base name of the `*.cproject.yml` file.
- `.build-type` that defines typically build-specific settings such as for debug, release, or test.
- `+target-type` that defines typically target-specific settings such as device, board, or usage of processor features.

!!! Note
    - The [`context`](#context-name-conventions) name is used throughout the build process and is reflected in directory names. Even when there is not a fixed limit, keep identifiers short. Recommended is less than 32 characters for the [`context`](#context-name-conventions) name.
    - Blank characters (' ') in the context name are not permitted by CMake.

The section ["Configure Related Projects"](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#configure-related-projects)
explains the overall concept of  `target-types` and `build-types`. These `target-types` and `build-types` are defined in the `*.csolution.yml` that defines the overall application for a system.

The settings of the `target-types:` are processed first, followed by the settings of the `build-types:`, which potentially overwrite the `target-types:` settings.
