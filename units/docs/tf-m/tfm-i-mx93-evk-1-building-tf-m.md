---
id: "tfm-i-mx93-evk-1-building-tf-m"
type: "concept"
domain: "security"
title: "i.MX93 EVK: 1. Building TF-M"
summary: "Prepare the tf-m-tests repository inside the TF-M base folder."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/nxp/mcimx93evk/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nxp/mcimx93evk/.html#1-building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

Prepare the tf-m-tests repository inside the TF-M base folder.

```bash

cd <TF-M base folder>
git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
```
MCIMX93EVK will only support builds without secondary bootloader (BL2).
u-boot running on Cortex-A core acts as the bootloader responsible for authenticating and loading
TF-M on memory for Cortex-M core.


### 1.1 Building TF-M demo

To build S and NS application image, run the following commands:

* Build with secure binary on TCM and non secure binary on OCRAM:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake \
-S spe \
-B build_spe -DTFM_PLATFORM=nxp/mcimx93evk \
-DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
-G"Unix Makefiles" \
-DBL2=OFF
cmake --build build_spe -- install
cmake -S . \
-B build_test -G"Unix Makefiles" \
-DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```
* Build with secure and non secure binary on TCM:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe \
-B build_spe \
-DTFM_PLATFORM=nxp/mcimx93evk \
-DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m -G"Unix Makefiles" \
-DBL2=OFF \
-DNS_PARTITION_ON_OCRAM=OFF
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
-DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```

### 1.2 Building TF-M regression tests


To build the S and NS regression tests, run the following commands:

* Profile Medium:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe \
-B build_spe \
-DTFM_PLATFORM=nxp/mcimx93evk \
-DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m -G"Unix Makefiles" \
-DTFM_PROFILE=profile_medium \
-DTEST_S=ON \
-DTEST_NS=ON \
-DBL2=OFF
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
-DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```
* Profile Small:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe_small \
-DTFM_PLATFORM=nxp/mcimx93evk \
-DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
-G"Unix Makefiles" \
-DBL2=OFF \
-DTFM_PROFILE=profile_small \
-DTEST_S=ON   -DTEST_NS=ON  \
-DTEST_S_CRYPTO=ON   -DTEST_NS_CRYPTO=ON  \
-DTEST_S_ATTESTATION=OFF  \
-DTEST_S_STORAGE=OFF  \
-DTEST_S_PLATFORM=OFF  \
-DTEST_NS_ATTESTATION=OFF \
-DTEST_NS_STORAGE=OFF -DTEST_NS_PLATFORM=OFF \
-DTEST_S_PLATFORM=OFF \
-DTEST_NS_SFN_BACKEND=OFF \
-DTEST_S_SFN_BACKEND=OFF
cmake --build build_spe_small -- install
cmake -S . -B build_test_small -G"Unix Makefiles" \
-DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe_small/api_ns
cmake --build build_test_small
```
S and NS images are compiled to be loaded to TCM and OCRAM respectively.
To compile both images for TCM, please note that the combined size of S and NS binaries can't exceed
128K if being compiled for TCM. Even if the size fits in 128K, you may beed to adjust the partition
sizes in flash_layout.h.in file based on the partition sizes. In default build, regression test
binaries don't fit in the TCM.
