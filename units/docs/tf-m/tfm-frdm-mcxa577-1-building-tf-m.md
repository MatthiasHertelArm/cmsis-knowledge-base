---
id: "tfm-frdm-mcxa577-1-building-tf-m"
type: "concept"
domain: "security"
title: "FRDM-MCXA577: 1. Building TF-M"
summary: "Prepare the tf-m-tests repository inside the TF-M base folder."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/nxp/frdmmcxa577/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nxp/frdmmcxa577/.html#1-building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

Prepare the tf-m-tests repository inside the TF-M base folder.

```bash

cd <TF-M base folder>
git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
```
There are two options for the TF-M build - with or without secondary bootloader (BL2).


### 1.1 Building TF-M demo with BL2

To build S and NS application image with BL2, run the following commands:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe \
    -DTFM_PLATFORM=nxp/frdmmcxa577 \
    -DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
    -G "Unix Makefiles" \
    -DBL2=ON \
    -DTFM_BL2_LOG_LEVEL=LOG_LEVEL_INFO
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
    -DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```

### 1.2 Building TF-M demo without BL2

To build S and NS application image without a BL2, run the following commands:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe -DTFM_PLATFORM=nxp/frdmmcxa577 \
      -DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
      -G"Unix Makefiles" \
      -DBL2=OFF
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
      -DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```

### 1.3 Building TF-M regression tests


To build the S and NS regression tests without BL2, run the following commands:

* Profile Medium:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe -DTFM_PLATFORM=nxp/frdmmcxa577 \
      -DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
      -G"Unix Makefiles" \
      -DTFM_PROFILE=profile_medium \
      -DTEST_S=ON  \
      -DTEST_NS=ON \
      -DBL2=OFF
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
      -DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```

### 1.4 Building TF-M regression tests with BL2


To build the S and NS regression tests With BL2, run the following commands:

* Profile Medium:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe -DTFM_PLATFORM=nxp/frdmmcxa577 \
      -DCONFIG_TFM_SOURCE_PATH=<TF-M base folder>/trusted-firmware-m \
      -G"Unix Makefiles" \
      -DTFM_PROFILE=profile_medium \
      -DTEST_S=ON \
      -DTEST_NS=ON \
      -DBL2=ON \
      -DTFM_BL2_LOG_LEVEL=LOG_LEVEL_INFO
cmake --build build_spe -- install
cmake -S . -B build_test -G"Unix Makefiles" \
      -DCONFIG_SPE_PATH=<TF-M base folder>/tf-m-tests/tests_reg/build_spe/api_ns
cmake --build build_test
```
* Profile Small:

```bash

cd <TF-M base folder>/tf-m-test/tests_reg
cmake -S spe -B build_spe_small -DTFM_PLATFORM=nxp/frdmmcxa577 \
    -DCONFIG_TFM_SOURCE_PATH=C:/Code/tfm-upstream/trusted-firmware-m \
    -G"Unix Makefiles"          \
    -DBL2=ON                    \
    -DTFM_PROFILE=profile_small \
    -DTEST_S=ON                 \
    -DTEST_NS=ON                \
    -DTEST_S_CRYPTO=ON          \
    -DTEST_NS_CRYPTO=ON         \
    -DTEST_S_ATTESTATION=OFF    \
    -DTEST_S_STORAGE=OFF        \
    -DTEST_S_PLATFORM=OFF       \
    -DTEST_NS_ATTESTATION=OFF   \
    -DTEST_NS_STORAGE=OFF       \
    -DTEST_NS_PLATFORM=OFF      \
    -DTEST_S_PLATFORM=OFF       \
    -DTEST_NS_SFN_BACKEND=OFF   \
    -DTEST_S_SFN_BACKEND=OFF    \
    -DTFM_BL2_LOG_LEVEL=LOG_LEVEL_INFO
cmake --build build_spe_small -- install
cmake -S . -B build_test_small -G"Unix Makefiles" \
    -DCONFIG_SPE_PATH=C:/Code/tfm-upstream/tf-m-tests/tests_reg/build_spe_small/api_ns
cmake --build build_test_small

## 2. Flashing TF-M with Segger J-Link


To install the J-Link Software and documentation pack, follow the steps below:

#. Download the appropriate package from the J-Link Software and documentation pack website
#. Depending on platform, install the package or run the installer
#. When connecting a J-Link-enabled board such as an frdmmcxa577 , a serial port should come up

Flash them with JLink as follows:

* Flash Erase:

```console

JLinkExe -device MCXA577 -if swd -speed 4000 -autoconnect 1
J-Link>exec EnableEraseAllFlashBanks
J-Link>erase
J-Link>r
```
* Flash Write:


If you built TF-M with the BL2 secondary bootloader, use the following commands:

```console

JLinkExe -device MCXA577 -if swd -speed 4000 -autoconnect 1
J-Link>r
J-Link>h
J-Link>loadfile build_spe/bin/bl2.bin 0x00
J-Link>h
J-Link>loadfile build_test/bin/tfm_s_ns_signed.bin 0x10000
J-Link>r
```
When BL2 is disabled, flash the generated hex secure and non-secure images:

```console

JLinkExe -device MCXA577 -if swd -speed 4000 -autoconnect 1
J-Link>r
J-Link>h
J-Link>loadfile build_spe/bin/tfm_s.bin 0x00
J-Link>h
J-Link>loadfile build_spe/bin/tfm_ns.bin 0x30000
J-Link>r
```
--------------

*Copyright 2025 NXP*
*SPDX-License-Identifier: BSD-3-Clause*
