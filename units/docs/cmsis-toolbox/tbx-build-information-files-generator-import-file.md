---
id: "tbx-build-information-files-generator-import-file"
type: "concept"
domain: "project"
title: "Build Information Files: Generator Import File"
summary: "The .cgen.yml file lists the generated csolution project part and starts with the node generator-import:. It is defined similarly to a Software Layer additional parameters, files, and components that are included in the project."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#generator-import-file"
license: "Apache-2.0"
mode: "V"
---

The `*.cgen.yml` file lists the generated *csolution project* part and starts with the node `generator-import:`. It is defined similarly to a [Software Layer](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#software-layers) additional parameters, files, and components that are included in the project.

### File Structure of `*.cgen.yml`

`generator-import:`                                                             | Content
:-------------------------------------------------------------------------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `generated-by:`                                              | Tool name that generated this file
&nbsp;&nbsp;&nbsp; [`for-device:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#device-name-conventions) | Device information, used for consistency check (device selection is in `*.csolution.yml`).
&nbsp;&nbsp;&nbsp; [`for-board:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#board-name-conventions)   | Board information, used for consistency check (board selection is in `*.csolution.yml`).
&nbsp;&nbsp;&nbsp; [`packs:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#packs)                        | Defines packs that are required for this layer.
&nbsp;&nbsp;&nbsp; [`define:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define)                      | Define symbol settings for code generation.
&nbsp;&nbsp;&nbsp; [`undefine:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#undefine)                  | Remove define symbol settings for code generation.
&nbsp;&nbsp;&nbsp; [`add-path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-path)                  | Additional include file paths.
&nbsp;&nbsp;&nbsp; [`del-path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#del-path)                  | Remove specific include file paths.
&nbsp;&nbsp;&nbsp; [`groups:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#groups)                      | List of source file groups along with source files.
&nbsp;&nbsp;&nbsp; [`components:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#components)              | List of software components used.
