---
id: "armsw-execute-validation-project-prerequisites"
type: "concept"
domain: "rtos"
title: "Execute Validation Project: Prerequisites"
summary: "These prerequisites can be installed automatically using vcpkg:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

- [CMSIS-Toolbox 2.13.0 or later](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases)
- [Arm Virtual Hardware FVP 11.31.28 or later](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms)
- [Arm Compiler 6.24.0 or later](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded)
- [GCC Compiler 15.2.1 or later](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain)
- [IAR Compiler 9.70.4 or later](https://www.iar.com/embedded-development-tools)
- [LLVM/Clang Embedded Toolchain 22.1.0 or later](https://developer.arm.com/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded)
- [CMake 3.31.5 or later](https://cmake.org/download/)
- [Ninja 1.13.2 or later](https://github.com/ninja-build/ninja/releases)
- Python (to use `build.py` script)

These prerequisites can be installed automatically using `vcpkg`:

```Shell
 ./Project $ vcpkg activate
```

Python packages required to build and run with `build.py`:

- python-matrix-runner 1.3

These can be installed with `pip`:

```Shell
 ./Project $ pip install -r requirements.txt
```

Required CMSIS Packs:

- ARM.CMSIS
- ARM.CMSIS-RTX
- ARM.CMSIS-FreeRTOS
- ARM.Cortex_DFP

These get installed automatically if missing. One can explicitly install the packs using `cpackget` from CMSIS-Toolbox.
