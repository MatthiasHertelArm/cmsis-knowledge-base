---
id: "devt-pack-generation-tool"
type: "concept"
domain: "pack"
title: "Pack Generation Tool"
summary: "The utility packgen assists the generation of a CMSIS-Pack from CMakeLists according to the standard format by reading a manifest YAML file with metadata and running the CMake generation step to retrieve CMake targets build information, namely source …"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packgen/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packgen/README.md"
license: "Apache-2.0"
mode: "V"
---

The utility `packgen` assists the generation of a CMSIS-Pack from CMakeLists
according to the standard
[format](https://arm-software.github.io/CMSIS_5/develop/Pack/html/packFormat.html)
by reading a manifest YAML file with metadata and running the CMake generation
step to retrieve CMake targets build information, namely source files, include
paths and defines. It distributed as part of
the [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/installation.md).
