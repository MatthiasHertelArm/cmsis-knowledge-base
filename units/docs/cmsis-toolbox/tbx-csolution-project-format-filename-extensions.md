---
id: "tbx-csolution-project-format-filename-extensions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / Filename Extensions"
summary: "The csolution Project Manager recognizes the categories of files based on the filename extension in the YAML input files as shown in the table below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#filename-extensions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

The **`csolution` Project Manager** recognizes the [categories](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileCategoryEnum) of [files](#files) based on the filename extension in the YAML input files as shown in the table below.

File Extension           | [Category](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileCategoryEnum) | Description
:--------------------------------------------|:-------------|:---------------------
`.c`, `.C`                                   | sourceC      | C source file
`.cpp`, `.c++`, `.C++`, `.cxx`, `.cc`, `.CC` | sourceCpp    | C++ source file
`.h`,`.hpp`                                  | header       | Header file
`.asm`, `.s`, `.S`                           | sourceAsm    | Assembly source file
`.ld`, `.scf`, `.sct`, `.icf`                | linkerScript | Linker Script file
`.a`, `.lib`                                 | library      | Library file
`.o`                                         | object       | Object file
`.txt`, `.md`, `.pdf`, `.htm`, `.html`       | doc          | Documentation
`.scvd`                                      | other        | [Software Component View Description](https://arm-software.github.io/CMSIS-View/latest/SCVD_Format.html) for CMSIS-View
