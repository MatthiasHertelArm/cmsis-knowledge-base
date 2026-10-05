---
id: "tbx-mcuxpresso-for-nxp-devices-create-a-board-layer"
type: "concept"
domain: "project"
title: "MCUXpresso for NXP Devices: Create a Board Layer"
summary: "A software layer is a set of pre-configured software components and source files that can be reused in multiple projects. A board layer typically contains basic I/O drivers and related device and board configuration."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/MCUXpressoConfig.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/#create-a-board-layer"
license: "Apache-2.0"
mode: "V"
---

A [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/build-overview.md#software-layers) is a set of pre-configured software components and source files that can be reused in multiple projects. A board layer typically contains basic I/O drivers and related device and board configuration. MCUXpresso generates a significant part of a board layer.

The board layer is stored in a separate directory that is independent of a specific *csolution project*. To create a board layer, copy the related source files, the MCUXpresso generated files, and the configuration files of the `RTE directory` that relate to software components in the board layer.

**Example directory content of a NXP board layer**

Directory and Files               | Description
:---------------------------------|:---------------------------------------
`Board.clayer.yml`                | Defines the source files and software components of the board layer.
`MCUXpressoConfig/`               | Directory with MCUXpresso generated files.
`MCUXpressoConfig/Board.cgen.yml` | Generator import file that lists MCUXpresso generated files and options.

The `Board.clayer.yml` file defines, with the `generators:` node, options to locate the MCUXpresso generated files in the directory structure of the [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/build-overview.md#software-layers). As a board layer is used by many projects, the name of the generator import file should be explicitly specified, as shown below:

```yml
generators:
    options:
    - generator: MCUXpressoConfig
      path: ./MCUXpressoConfig              # path relative to the `*.clayer.yml` file
      name: Board                           # generator import file is named `Board.cgen.yml`.
```
