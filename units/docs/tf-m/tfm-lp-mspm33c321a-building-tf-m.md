---
id: "tfm-lp-mspm33c321a-building-tf-m"
type: "concept"
domain: "security"
title: "LP_MSPM33C321A: Building TF-M"
summary: "Follow the generic build instructions and set -DTFM_PLATFORM=ti/LP_MSPM33C321A."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/ti/LP_MSPM33C321A/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/ti/LP_MSPM33C321A/.html#building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

Follow the generic build instructions
and set `-DTFM_PLATFORM=ti/LP_MSPM33C321A`.

First, clone tf-m-tests at the version pinned by this TF-M release:

```bash

git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
# Check the pinned version:
cat <TF-M source dir>/lib/ext/tf-m-tests/version.txt
```

### Example: regression tests (Secure and Non-Secure), Isolation Level 1


Building the Secure side:

```bash

cmake -S <tf-m-tests>/tests_reg/spe \
      -B <build_dir>/spe \
      -DTFM_PLATFORM=ti/LP_MSPM33C321A \
      -DTFM_TOOLCHAIN_FILE=<TF-M source dir>/toolchain_GNUARM.cmake \
      -DCONFIG_TFM_SOURCE_PATH=<TF-M source dir> \
      -DCROSS_COMPILE=<toolchain_path>/arm-none-eabi \
      -DCMAKE_BUILD_TYPE=Release \
      -DTEST_S=ON \
      -DTEST_NS=ON

cmake --build <build_dir>/spe --target install -- -j8
```
Building the Non-Secure side:

```bash

cmake -S <tf-m-tests>/tests_reg \
      -B <build_dir>/ns \
      -DCONFIG_SPE_PATH=<build_dir>/spe/api_ns \
      -DTFM_TOOLCHAIN_FILE=<build_dir>/spe/api_ns/cmake/toolchain_ns_GNUARM.cmake \
      -DCROSS_COMPILE=<toolchain_path>/arm-none-eabi \
      -DCMAKE_BUILD_TYPE=Release

cmake --build <build_dir>/ns -- -j8
```
