---
id: "alp-tfm-tfm-configure-and-build-the-tf-m-t"
type: "concept"
domain: "core"
title: "Configure, build and run the TF-M example application: Configure and build the TF-M tests"
summary: "Activate the python environment, navigate to the test suite and set the relevant cmake variables to build TF-M and its suite of tests. The TFM_TOOLCHAIN_FILE parameter is used to select a toolchain."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tfm/tfm.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tfm/tfm/#configure-and-build-the-tf-m-tests"
license: "CC-BY-SA-4.0"
mode: "V"
---

Activate the python environment, navigate to the test suite and set the relevant `cmake` variables to build TF-M and its suite of tests. The `TFM_TOOLCHAIN_FILE` parameter is used to select a toolchain. The build is done in `Debug` mode to get progress and results displayed when they are executed. All the parameters are defined in the [Trusted Firmware-M documentation](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html#build-and-run-instructions). For example, to build with Arm GNU Compiler:

```bash
. myvenv/bin/activate

mkdir build
cmake -S tf-m-tests/tests_reg/spe -B build/tests-spe \
      -DCMAKE_BUILD_TYPE=Debug \
      -DTFM_PLATFORM=arm/mps3/corstone300/fvp \
      -DTFM_PROFILE=profile_small \
      -DTFM_TOOLCHAIN_FILE=$PWD/trusted-firmware-m/toolchain_GNUARM.cmake \
      -DCONFIG_TFM_SOURCE_PATH=$PWD/trusted-firmware-m \
      -DTEST_S=ON -DTEST_NS=ON
cmake --build build/tests-spe -- install

cmake -S tf-m-tests/tests_reg -B build/tests \
      -DCMAKE_BUILD_TYPE=Debug \
      -DCONFIG_SPE_PATH=$PWD/build/tests-spe/api_ns
cmake --build build/tests
```

Or, alternatively, for building with `armclang`, use `$PWD/../../trusted-firmware-m/toolchain_ARMCLANG.cmake` for `TFM_TOOLCHAIN_FILE`.

On a successful build, the TF-M test executables are created in the `build/tests-spe` and `build/tests` directories. This includes binary files for the `MCUBoot bootloader`, `TF-M secure firmware` and `TF-M non-secure` app. Signed variants of both the TF-M secure and non-secure images are created along with a combined signed image of both the secure and non-secure image.
