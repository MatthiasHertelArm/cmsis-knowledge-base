---
id: "tfm-first-things-first-arm-toolchain-for-embedded-minimum-v20-1"
type: "concept"
domain: "security"
title: "First Things First: Arm Toolchain for Embedded (minimum v20.1.0)"
summary: "Here, we take building TF-M for AN521 platform with regression tests using GCC as an example:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/getting_started/tfm_getting_started.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/getting_started/tfm_getting_started.html#arm-toolchain-for-embedded-minimum-v20-1-0"
license: "BSD-3-Clause"
mode: "V"
---

**Note:** Not all platforms support this toolchain. Please refer to a platform documentation or check with the platform owner.


# Build AN521 regression sample


Here, we take building TF-M for AN521 platform with regression tests using GCC
as an example:


# Run AN521 regression sample


Run the sample code on SSE-200 Fast-Model, using FVP_MPS2_AEMv8M provided by
Arm Development Studio.


**Note:** Arm Development Studio is not essential to develop TF-M, you can skip this section if don't want to try on Arm develop boards.

After completing the procedure you should see the following messages on the
DAPLink UART (baud 115200 8n1)::
```
...
#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_S_PS_TEST_1XXX)...
> Executing 'TFM_S_PS_TEST_1001'
Description: 'Set interface'
TEST: TFM_S_PS_TEST_1001 - PASSED!
> Executing 'TFM_S_PS_TEST_1002'
Description: 'Set interface with create flags'
TEST: TFM_S_PS_TEST_1002 - PASSED!
> Executing 'TFM_S_PS_TEST_1003'
Description: 'Set interface with NULL data pointer'
TEST: TFM_S_PS_TEST_1003 - PASSED!
> Executing 'TFM_S_PS_TEST_1005'
Description: 'Set interface with write once UID'
TEST: TFM_S_PS_TEST_1005 - PASSED!
....

# Tool & Dependency overview


To build the TF-M firmware the following tools are needed:

   - C compiler of supported toolchains
   - CMake version 3.21 or later
   - Git
   - gmake, aka GNU Make
   - Python >=v3.11
   - [Optionally] [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)


## Dependency chain


Here are some next steps for exploring TF-M:

    - Detailed Build instructions.
    - IAR Build instructions.
    - Try other Samples and Demos.
    - Documentation generation.

--------------

*SPDX-License-Identifier: BSD-3-Clause*

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
