---
id: "rtx-trustzone-rtos-faults-project-build-project-from-the-command-line"
type: "concept"
domain: "rtos"
title: "TrustZone RTOS_Faults Project: Build Project from the Command Line"
summary: "CMSIS-Toolbox provides cbuild command-line tool that builds csolution projects."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/RTOS_Faults/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/RTOS_Faults/README.md#build-project-from-the-command-line"
license: "Apache-2.0"
mode: "V"
---

[CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) provides [cbuild](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/)
command-line tool that builds `csolution` projects.

The `RTOS_Faults.csolution.yml` solution files defines `Debug` build-type and `FVP` target-type.  
To build this configuration using Arm Compiler 6 toolchain execute the following command:

```bash
cbuild RTOS_Faults.csolution.yml --packs --context .Debug+FVP --toolchain AC6
```

> **Note**  
> During the build process required packs may be downloaded (`--pack` flag).

By default the project does not specify the toolchain and one can build the project by specifying the AC6, GCC, CLANG or IAR toolchain.

Examples:

- Build with GCC

  ```sh
  cbuild RTOS_Faults.csolution.yml --packs --context .Debug+FVP --toolchain GCC
  ```

- Build with IAR

  ```sh
  cbuild RTOS_Faults.csolution.yml --packs --context .Debug+FVP --toolchain IAR
  ```
