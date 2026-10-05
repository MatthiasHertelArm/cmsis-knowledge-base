---
id: "tfm-additional-build-instructions-for-notes-for-building-with-iararm"
type: "concept"
domain: "security"
title: "Additional build instructions for the IAR toolchain: Notes for building with IARARM"
summary: "IAR Embedded Workbench for ARM (EWARM) versions v9.30.1 or later are required."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tfm_build_instruction_iar.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tfm_build_instruction_iar.html#notes-for-building-with-iararm"
license: "BSD-3-Clause"
mode: "V"
---

IAR Embedded Workbench for ARM (EWARM) versions v9.30.1 or later are required.

    Currently the MUSCA_B1 target is not supported with IARARM, due to lack of testing.

    cmake needs to be version 3.21 or newer.

    For all configurations and build options some of the QCBOR tests fail due to the tests not handling
    double float NaN:s according to the Arm Runtime ABI. This should be sorted out in the future.


### Example: building TF-M for AN521 platform using IAR:


```bash

cd <TF-M base folder>
cmake -S . -B cmake_build -DTFM_PLATFORM=arm/mps2/an521 -DTFM_TOOLCHAIN_FILE=toolchain_IARARM.cmake
cmake --build cmake_build -- install
```
Alternately using traditional cmake syntax

```bash

cd <TF-M base folder>
mkdir cmake_build
cd cmake_build
cmake .. -DTFM_PLATFORM=arm/mps2/an521 -DTFM_TOOLCHAIN_FILE=../toolchain_IARARM.cmake
make install
```

### Regression Tests for the AN521 target platform


```bash

cd <TF-M base folder>
cmake -S . -B cmake_build -DTFM_PLATFORM=arm/mps2/an521 -DTFM_TOOLCHAIN_FILE=toolchain_IARARM.cmake -DTEST_S=ON -DTEST_NS=ON
cmake --build cmake_build -- install
```
Alternately using traditional cmake syntax

```bash

cd <TF-M base folder>
mkdir cmake_build
cd cmake_build
cmake .. -DTFM_PLATFORM=arm/mps2/an521 -DTFM_TOOLCHAIN_FILE=../toolchain_IARARM.cmake -DTEST_S=ON -DTEST_NS=ON
make install
```
For PSA API tests, you may need to append `-DTOOLCHAIN=INHERIT` to the build command.
--------------

*SPDX-License-Identifier: BSD-3-Clause*

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
