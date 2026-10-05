---
id: "rtx-trustzone-rtos-project-build-project-from-the-command-line"
type: "concept"
domain: "rtos"
title: "TrustZone RTOS Project: Build Project from the Command Line"
summary: "CMSIS-Toolbox provides cbuild command-line tool that builds csolution projects."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/RTOS/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/RTOS/README.md#build-project-from-the-command-line"
license: "Apache-2.0"
mode: "V"
---

[CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) provides [cbuild](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/)
command-line tool that builds `csolution` projects.

The `RTOS.csolution.yml` solution files defines `Debug` build-type and `FVP` target-type.  
To build this configuration using Arm Compiler 6 toolchain execute the following command:

```bash
cbuild RTOS.csolution.yml --packs --context .Debug+FVP --toolchain AC6
```

> **Note**  
> During the build process required packs may be downloaded (`--pack` flag).

By default the project does not specify the toolchain and one can build the project by specifying the AC6, GCC, CLANG or IAR toolchain.

Examples:

- Build with GCC

  ```sh
  cbuild RTOS.csolution.yml --packs --context .Debug+FVP --toolchain GCC
  ```

- Build with IAR

  ```sh
  cbuild RTOS.csolution.yml --packs --context .Debug+FVP --toolchain IAR
  ```
