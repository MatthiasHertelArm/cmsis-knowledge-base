---
id: "devt-pack-generation-tool-requirements"
type: "concept"
domain: "pack"
title: "Pack Generation Tool: Requirements"
summary: "For validating and compressing pack files, the packchk and 7-zip utilities shall be in the PATH system environment variable:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packgen/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packgen/README.md#requirements"
license: "Apache-2.0"
mode: "V"
---

- CMake: <https://cmake.org/>
- Ninja: <https://ninja-build.org/>

 > **NOTE:**  Make sure the CMake project has been previously configured and
 dependencies have been installed. It is a requirement to be able to
 successfully run the CMake generation step in the current environment.

For validating and compressing pack files, the `packchk` and `7-zip` utilities
shall be in the `PATH` system environment variable:

- [packchk](https://github.com/Open-CMSIS-Pack/devtools/releases/tag/tools%2Fpackchk%2F1.4.1)
- [7-zip](https://www.7-zip.org/)
