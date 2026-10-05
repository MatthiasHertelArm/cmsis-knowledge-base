---
id: "cc-i-o-retarget-example-project-build-project-from-the-command-line"
type: "concept"
domain: "core"
title: "I/O Retarget example project: Build Project from the Command Line"
summary: "CMSIS-Toolbox provides cbuild command-line tool that builds csolution projects."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_example.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_example.md#build-project-from-the-command-line"
license: "Apache-2.0"
mode: "V"
---

[CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) provides [cbuild](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/)
command-line tool that builds `csolution` projects.

The `retarget.csolution.yml` solution files defines `Debug` build-type and `VHT_CM3` target-type. To build this configuration
using Arm Compiler 6 toolchain execute the following command:

```bash
cbuild retarget.csolution.yml --toolchain AC6 --packs --context retarget.Debug+VHT_CM3
```

> **Note**
>
> - During the build process required packs may be downloaded (`--pack` flag).

By default the project does not specify the toolchain and one can build the project by specifying the AC6, GCC, CLANG or IAR toolchain.
