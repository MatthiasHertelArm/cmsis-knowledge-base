---
id: "aig-install-guides-cmsis-toolbox-set-up-environment-variables"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox: Set up environment variables"
summary: "Exact paths will depend on the versions and locations of installed tools."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/cmsis-toolbox.md"
doc_source: "https://learn.arm.com/install-guides/cmsis-toolbox/#set-up-environment-variables"
license: "CC-BY-SA-4.0"
mode: "V"
---

Set environment variables as follows. 

**Note:**
The exact name of the `TOOLCHAIN` variables will be based on the tool and version installed. In this way, you can register multiple build tools.


| Variable                                   | Description                           | Notes                                         |
| ------------------------------------------ | ------------------------------------- | --------------------------------------------- |
| `<n>_TOOLCHAIN_<major>_<minor>_<patch>` | Path to toolchain binaries            | `<n>` = `AC6`, `GCC`, `IAR`, or `CLANG`    |
| `CMSIS_PACK_ROOT`                          | Path to CMSIS-Pack root directory     | Use `cpackget init` to initialize             |
| `PATH`                                     | Add CMSIS-Toolbox `bin` to path       | Also path to `CMake` and `Ninja` if necessary |
| `CMSIS_COMPILER_ROOT`                      | Path to CMSIS-Toolbox `etc` directory | Optional                                      |


For example:

  **Windows:**
set AC6_TOOLCHAIN_6_24_0=%ProgramFiles%/ArmCompilerforEmbedded6.24/bin
set CMSIS_PACK_ROOT=%LocalAppData%/Arm/Packs
set PATH=%PATH%;%UserProfile%/cmsis-toolbox-windows-amd64/bin
set CMSIS_COMPILER_ROOT=%UserProfile%/cmsis-toolbox-windows-amd64/etc
  
  **Linux:**
export AC6_TOOLCHAIN_6_24_0=$HOME/ArmCompilerforEmbedded6.24/bin
export CMSIS_PACK_ROOT=$HOME/packs
export PATH=$HOME/cmsis-toolbox-linux-arm64/bin:$PATH
export CMSIS_COMPILER_ROOT=$HOME/cmsis-toolbox-linux-arm64/etc
  


Exact paths will depend on the versions and locations of installed tools.
