---
id: "cc-i-o-retarget-example-project-project-structure"
type: "concept"
domain: "core"
title: "I/O Retarget example project: Project Structure"
summary: "The project is generated using the CMSIS-Toolbox and is defined in csolution format:"
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_example.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_example.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is generated using the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) and
is defined in [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/) format:

- `retarget.csolution.yml` lists the required packs and defines the hardware target and build-types (along with the compiler).
- `retarget.cproject.yml` defines the source files and the software components.
