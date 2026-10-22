---
id: "tfm-trusted-firmware-m-profile-medium-platform-support"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium Design: Platform support"
summary: "To enable Profile Medium on a platform, the platform specific CMake file should be added into the platform support list in top-level Profile Medium CMake config file."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium.html#platform-support"
license: "BSD-3-Clause"
mode: "V"
---

To enable Profile Medium on a platform, the platform specific CMake file should
be added into the platform support list in top-level Profile Medium CMake config
file.


### Building Profile Medium


To build Profile Medium, argument `TFM_PROFILE` in build command line should be
set to `profile_medium`.

Take AN521 as an example:

The following commands build Profile Medium without test cases on **AN521** with
build type **MinSizeRel**, built by **Armclang**.

```bash

cd <TFM root dir>
mkdir build && cd build
cmake -DTFM_PLATFORM=arm/mps2/an521 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_PROFILE=profile_medium \
      -DCMAKE_BUILD_TYPE=MinSizeRel \
      ../
cmake --build ./ -- install
```
The following commands build Profile Medium with regression test cases on
**AN521** with build type **MinSizeRel**, built by **Armclang**.

```bash

cd <TFM root dir>
mkdir build && cd build
cmake -DTFM_PLATFORM=arm/mps2/an521 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_PROFILE=profile_medium \
      -DCMAKE_BUILD_TYPE=MinSizeRel \
      -DTEST_S=ON -DTEST_NS=ON \
      ../
cmake --build ./ -- install
```

- For devices with more constrained memory and flash requirements, it is
  possible to build with either only TEST_S enabled or only TEST_NS enabled.
  This will decrease the size of the test images. Note that both test suites
  must still be run to ensure correct operation.
More details of building instructions and parameters can be found TF-M build
instruction guide [TFM-BUILD]_.
