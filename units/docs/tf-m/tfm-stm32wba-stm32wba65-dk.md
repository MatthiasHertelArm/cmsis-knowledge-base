---
id: "tfm-stm32wba-stm32wba65-dk"
type: "concept"
domain: "security"
title: "STM32WBA: STM32WBA65_DK"
summary: "Discovery kit for IoT node with STM32WBA series https://www.st.com/en/evaluation-tools/stm32wba65i-dk1.html"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32wba65i-dk/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32wba65i-dk/.html#stm32wba65-dk"
license: "BSD-3-Clause"
mode: "V"
---

Discovery kit for IoT node with STM32WBA series
https://www.st.com/en/evaluation-tools/stm32wba65i-dk1.html


### Configuration and Build


GNUARM/ARMCLANG/IARARM compilation is available for this target.
and build the selected configuration as follow.

The build configuration for TF-M is provided to the build system using command
line arguments. Required arguments are noted below.

The following instructions build multi-core TF-M with regression test suites
in Isolation Level 1.

```bash


cd <TF-M base folder>
cd <trusted-firmware-m folder>

git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
git checkout <recommended tf-m-tests commit>

mkdir build_s && cd build_s

cmake -S /../tf-m-tests/tests_reg/spe -B . -GNinja -DTFM_PLATFORM=stm/stm32wba65i_dk
     -DTFM_TOOLCHAIN_FILE= /../toolchain_ARMCLANG.cmake
     -DCONFIG_TFM_SOURCE_PATH= /../trusted-firmware-m
     -DTFM_PSA_API=ON -DTFM_ISOLATION_LEVEL=1
     -DTEST_S=ON -DTEST_NS=ON

cmake --build -C . install -j 8

cd <trusted-firmware-m folder>
mkdir build_ns && cd build_ns
cmake -S /../trusted-firmware-m  /../tf-m-tests/tests_reg -B . -GNinja
     -DCONFIG_SPE_PATH= /../build_s/api_ns -DTFM_TOOLCHAIN_FILE= /../build_s/api_ns/cmake/toolchain_ns_ARMCLANG.cmake

cmake --build -C . -j 8
```
The following instructions build multi-core TF-M with PSA API test suite for
the attestation service in Isolation Level 1 on Linux.

```bash


cd <TF-M base folder>
cd <trusted-firmware-m folder>

git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
git checkout <recommended tf-m-tests commit>

mkdir build_s && cd build_s

cmake -S /../tf-m-tests/tests_psa_arch/spe -B . -GNinja -DTFM_PLATFORM=stm/stm32wba65i_dk
     -DTFM_TOOLCHAIN_FILE= /../toolchain_ARMCLANG.cmake
     -DCONFIG_TFM_SOURCE_PATH= /../trusted-firmware-m
     -DTFM_PSA_API=ON -DTFM_ISOLATION_LEVEL=1
     -DTEST_PSA_API=INITIAL_ATTESTATION

cmake --build -C . install -j 8

cd <trusted-firmware-m folder>
mkdir build_ns && cd build_ns
cmake -S /../trusted-firmware-m  /../tf-m-tests/tests_psa_arch -B . -GNinja
     -DCONFIG_SPE_PATH= /../build_s/api_ns -DTFM_TOOLCHAIN_FILE= /../build_s/api_ns/cmake/toolchain_ns_ARMCLANG.cmake

cmake --build -C . -j 8
```
