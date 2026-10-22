---
id: "tfm-max32657-building-tf-m"
type: "concept"
domain: "security"
title: "MAX32657: Building TF-M"
summary: "This platform port supports TF-M regression tests (Secure and Non-secure) with Isolation Level 1."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/adi/max32657/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/adi/max32657/.html#building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

This platform port supports TF-M regression tests (Secure and Non-secure)
with Isolation Level 1.

To build S and NS application, run the following commands:


**Note:** Only GNU toolchain is supported.


**Note:** Only "profile_small" predefined profile is supported.

Prepare the tf-m-tests repository inside the TF-M base folder.

```bash

cd <TF-M base folder>
git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
```
```bash

cd <TF-M base folder>/tf-m-test/tests_reg

cmake -S spe -B build_spe \
        -G"Unix Makefiles"               \
        -DTFM_PLATFORM=adi/max32657      \
        -DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
        -DTFM_TOOLCHAIN_FILE=<TF-M base folder>/trusted-firmware-m/toolchain_GNUARM.cmake \
        -DTEST_S=OFF                \
        -DTEST_NS=ON               \
        -DTFM_NS_REG_TEST=ON        \
        -DTFM_BL2_LOG_LEVEL=LOG_LEVEL_INFO  \
        -DTFM_ISOLATION_LEVEL=1
cmake --build build_spe -- install

cmake -S . -B build_test    \
        -G"Unix Makefiles"  \
        -DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns \
        -DTFM_TOOLCHAIN_FILE=cmake/toolchain_ns_GNUARM.cmake \
        -DTFM_NS_REG_TEST=ON
cmake --build build_test
```
