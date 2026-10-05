---
id: "alp-alif-image-classification-build-flash-verify-build-the-project"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: Build the project"
summary: "If you prefer to build from the terminal, set the required environment variables first. The exact paths depend on where the Arm Tools Environment Manager installed the tools:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#build-the-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Option 1: Build from VS Code

- Select the **CMSIS** icon in the left sidebar.
- Select the gear icon and set **Active Target** to **E8-HP** and **Active Project** to **mv2_runner**.
- Select the **Build** (hammer) icon.

### Option 2: Build from the command line

If you prefer to build from the terminal, set the required environment variables first. The exact paths depend on where the Arm Tools Environment Manager installed the tools:

```bash
export PATH="~/.vcpkg/artifacts/2139c4c6/tools.open.cmsis.pack.cmsis.toolbox/2.12.0/bin:~/.vcpkg/artifacts/2139c4c6/compilers.arm.arm.none.eabi.gcc/13.3.1/bin:~/.vcpkg/artifacts/2139c4c6/tools.kitware.cmake/3.31.5/bin:~/.vcpkg/artifacts/2139c4c6/tools.ninja.build.ninja/1.13.2:$PATH"
export CMSIS_COMPILER_ROOT="~/.vcpkg/artifacts/2139c4c6/tools.open.cmsis.pack.cmsis.toolbox/2.12.0/etc"
export GCC_TOOLCHAIN_13_3_1="~/.vcpkg/artifacts/2139c4c6/compilers.arm.arm.none.eabi.gcc/13.3.1/bin"

cbuild alif.csolution.yml --context mv2_runner.debug+E8-HP
```

**Note:**
The `GCC_TOOLCHAIN_13_3_1` variable must include the `/bin` suffix. Without it, the build system can't find the compiler executables.


Check the output binary size:

```bash
ls -lh out/mv2_runner/E8-HP/debug/mv2_runner.bin
```

The binary should be approximately 4 MB.
