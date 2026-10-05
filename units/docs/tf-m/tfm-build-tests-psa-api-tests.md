---
id: "tfm-build-tests-psa-api-tests"
type: "concept"
domain: "security"
title: "Build Tests: PSA API tests"
summary: "PSA API tests from https://github.com/ARM-software/psa-arch-tests use the same mechanism for SPE extension as the regression tests above utilising CONFIG_TFM_TEST_DIR option. PSA API tests are selected by the TEST_PSA_API variable."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tests_build_instruction.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tests_build_instruction.html#psa-api-tests"
license: "BSD-3-Clause"
mode: "V"
---

PSA API tests from https://github.com/ARM-software/psa-arch-tests use the same
mechanism for SPE extension as the regression tests above utilising `CONFIG_TFM_TEST_DIR` option.
PSA API tests are selected by the TEST_PSA_API variable. Enabling both regression tests and
PSA API tests simultaneously is **not** supported.

TF-M implements a wrapper CMake for PSA API tests as well.
The PSA API test codes are located under **/tests_psa_arch** folder.

Here is a brief description of the basic flow:
Select one of the following test suites to be run.

```bash

-DTEST_PSA_API=INTERNAL_TRUSTED_STORAGE
-DTEST_PSA_API=PROTECTED_STORAGE
-DTEST_PSA_API=STORAGE
-DTEST_PSA_API=CRYPTO
-DTEST_PSA_API=INITIAL_ATTESTATION
-DTEST_PSA_API=IPC
```
Respectively for the corresponding service. For detailed information,
please refer to **PSA Certified APIs Architecture Test Suite** section [2]_
in the documentation of **psa-arch-tests** repository.

For example, to enable the PSA API tests for the Crypto service:

```bash

cd </tf-m-tests/tests_psa_arch folder>
cmake -S spe -B build_spe -DTFM_PLATFORM=arm/mps2/an521 -DCONFIG_TFM_SOURCE_PATH=<TF-M source dir>
      -DTEST_PSA_API=CRYPTO
cmake --build build_spe -- install

cmake -S . -B build_test -DCONFIG_SPE_PATH=<Absolute path to>/build_spe/api_ns
cmake --build build_test

### Reference


.. [1] [tf-m-tests](https://git.trustedfirmware.org/plugins/gitiles/TF-M/tf-m-tests/)

.. [2] [PSA Certified APIs Architecture Test Suite](https://github.com/ARM-software/psa-arch-tests/blob/v23.06_API1.5_ADAC_EAC/api-tests/dev_apis/README.md)

--------------

*Copyright (c) 2017-2024, Arm Limited. All rights reserved.*
*Copyright (c) 2022, Cypress Semiconductor Corporation. All rights reserved.*
