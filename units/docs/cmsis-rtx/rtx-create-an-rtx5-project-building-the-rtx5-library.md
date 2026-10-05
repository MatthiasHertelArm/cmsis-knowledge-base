---
id: "rtx-create-an-rtx5-project-building-the-rtx5-library"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project: Building the RTX5 Library"
summary: "The CMSIS Pack contains a csolution project for building the complete set of RTX5 libraries. This project can also be used as a reference for building the RTX5 libraries using a tool-chain of your choice."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md#building-the-rtx5-library"
license: "Apache-2.0"
mode: "V"
---

The CMSIS Pack contains a csolution project for building the complete set of RTX5 libraries. This project can also be used as a reference for building the RTX5 libraries using a tool-chain of your choice.

### Build Process

The build process is managed using the following files:

- `RTX_Library.csolution.yml`: Defines the solution configuration.
- `RTX_Library.cproject.yml`: Specifies the project settings.
- `build.sh`: Script that triggers the library build process.

### Libraries Built

The following table lists the files available in the build output directory, its target
architecture with additional attributes and target toolchain.

| Library Name  | Target Architecture (attributes)     | AC6 | GCC | IAR | CLANG
|---------------|--------------------------------------|-----|-----|-----|------
| `RTX_V6M`     | Arm v6-M                             | YES | YES | YES | YES
| `RTX_V7A`     | Arm v7-A                             | YES | YES | YES | NO
| `RTX_V7M`     | Arm v7-M                             | YES | YES | YES | YES
| `RTX_V7MF`    | Arm v7-M (FP)                        | YES | YES | YES | YES
| `RTX_V8MB`    | Arm v8M Base Line                    | YES | YES | YES | YES
| `RTX_V8MBN`   | Arm v8M Base Line (non-secure)       | YES | YES | YES | YES
| `RTX_V8MM`    | Arm v8M Main Line                    | YES | YES | YES | YES
| `RTX_V8MMF`   | Arm v8M Main Line (FP)               | YES | YES | YES | YES
| `RTX_V8MMFN`  | Arm v8M Main Line (FP, non-secure)   | YES | YES | YES | YES
| `RTX_V8MMN`   | Arm v8M Main Line (non-secure)       | YES | YES | YES | YES
| `RTX_V81MM`   | Arm v8.1M Main Line                  | NO  | NO  | YES | NO
| `RTX_V81MMF`  | Arm v8.1M Main Line (FP)             | NO  | NO  | YES | NO
| `RTX_V81MMFN` | Arm v8.1M Main Line (FP, non-secure) | NO  | NO  | YES | NO
| `RTX_V81MMN`  | Arm v8.1M Main Line (non-secure)     | NO  | NO  | YES | NO

- **FP**: library built with Floating Point support
- **non-secure**: library built for TrustZone non-secure domain

All RTX5 libraries are built with debug information produced for use by a debugger.

### Optimization

The build process optimizes RTX5 libraries for size, which translates to the following per compiler
compiler options:

| Compiler | Optimization Option
|----------|--------------------
| AC6      | -Oz
| GCC      | -Os
| IAR      | -Ohz
| CLANG    | -Os

\endif
