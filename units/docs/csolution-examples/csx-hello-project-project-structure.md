---
id: "csx-hello-project-project-structure"
type: "concept"
domain: "project"
title: "Hello project: Project Structure"
summary: "The project is generated using the CMSIS-Toolbox and is defined in csolution format:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:Hello/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/Hello/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is generated using the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview) and is defined in [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format) format:

- [`Hello.csolution.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/Hello/./Hello.csolution.yml) lists the required packs and defines the hardware targets, build types, and supported compilers.
- [`Hello.cproject.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/Hello/./Hello.cproject.yml) defines the source files and the software components.

> [!NOTE]
> The project supports the AC6, GCC, and CLANG compilers.
