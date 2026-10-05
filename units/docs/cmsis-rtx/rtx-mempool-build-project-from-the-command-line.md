---
id: "rtx-mempool-build-project-from-the-command-line"
type: "concept"
domain: "rtos"
title: "MemPool: Build Project from the Command Line"
summary: "CMSIS-Toolbox provides cbuild command-line tool that builds csolution projects."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/MemPool/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/MemPool/README.md#build-project-from-the-command-line"
license: "Apache-2.0"
mode: "V"
---

[CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) provides [cbuild](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/)
command-line tool that builds `csolution` projects.

The `MemPool.csolution.yml` solution files defines `Debug` build-type and `FVP` target-type.  
To build this configuration using Arm Compiler 6 toolchain execute the following command:

```bash
cbuild MemPool.csolution.yml --packs --context MemPool.Debug+FVP --toolchain AC6
```

> **Note**  
> During the build process required packs may be downloaded (`--pack` flag).

By default the project does not specify the toolchain and one can build the project by specifying the AC6, GCC, CLANG or IAR toolchain.

Examples:

- Build with GCC

  ```sh
  cbuild MemPool.csolution.yml --packs --context MemPool.Debug+FVP --toolchain GCC
  ```

- Build with IAR

  ```sh
  cbuild MemPool.csolution.yml --packs --context MemPool.Debug+FVP --toolchain IAR
  ```
