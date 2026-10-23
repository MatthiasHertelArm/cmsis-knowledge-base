---
id: "tfm-numaker-pfm-m2351-building-tf-m"
type: "concept"
domain: "security"
title: "NuMaker-PFM-M2351: Building TF-M"
summary: "Build TF-M regression test with M2351 by following commands:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/nuvoton/m2351/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nuvoton/m2351/.html#building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

Build TF-M regression test with M2351 by following commands:

```bash

$ cd tf-m-test/tests_reg
$ cmake -S spe -B build_spe \
        -G"Unix Makefiles" \
        -DTFM_PLATFORM=nuvoton/m2351 \
        -DTFM_TOOLCHAIN_FILE=[tf-m path]/toolchain_GNUARM.cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DTEST_S=ON -DTEST_NS=ON
$ cmake --build build --parallel -- install
$ cmake -S . -B build_test \
        -G"Unix Makefiles" \
        -DCONFIG_SPE_PATH=[tf-m-tests path]/tests_reg/build_spe/api_ns \
        -DTFM_TOOLCHAIN_FILE=cmake/toolchain_ns_GNUARM.cmake \
        -DCMAKE_BUILD_TYPE=Release \
$ cmake --build build_test --parallel -- install
```
Define TEST_NS=ON or TEST_S=ON for non-secure or secure regression test.
CMAKE_BUILD_TYPE could be "Release", "RelWithDebInfo" or "Minsizerel"
Other cmake parameters should not be changed.
