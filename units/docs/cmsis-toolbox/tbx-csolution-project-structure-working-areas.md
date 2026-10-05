---
id: "tbx-csolution-project-structure-working-areas"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / Working Areas"
summary: "The table below explains the different working area sections of an application project."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#working-areas"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

The table below explains the different working area sections of an application project.

Working Area                                                      | Access | Description
:-----------------------------------------------------------------|:------:|:------------------
[Project Area](#project-area)                                     | RW     | Contains user source code files managed by the user along with the  project files (see next item).
[Project files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/./YML-Input-Format.md#project-file-structure)     | RW     | Created by a user or an IDE to describe the application project.
Component source code                                             | RO     | Content of software packs; the location is specified by the environment variable [`CMSIS_PACK_ROOT`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/installation.md#environment-variables) or the node [`pack: path`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/./YML-Input-Format.md#pack) in project files.
[Component Configuration​](#rte-directory-structure)               | RW     | User-editable config files of software components that are copied to the RTE directory.
Generator artifacts​                                               | RO (see note) | Managed by domain-specific configuration tools such as STM32CubeMX or MCUXpresso.
[Build artifacts](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/./YML-Input-Format.md#directory-control)        | RW     | Created during the build process for example by a compiler.

!!! Note
    Some generators allow user modification of the generated files. For example, STM32CubeMX allows modification of source code between `/* USER CODE BEGIN */` and `/* USER CODE END */` and preserves this modification even when the STM32CubeMX regenerates the files.
