---
id: "tfm-trusted-firmware-m-profile-large-d-platform-support"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Large Design: Platform support"
summary: "To enable Profile Large on a platform, the platform specific CMake file should be added into the platform support list in top-level Profile Large CMake config file."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_large.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_large.html#platform-support"
license: "BSD-3-Clause"
mode: "V"
---

To enable Profile Large on a platform, the platform specific CMake file should
be added into the platform support list in top-level Profile Large CMake config
file.


### Building Profile Large


To build Profile Large, argument `TFM_PROFILE` in build command line should be
set to `profile_large`.

Take AN521 as an example:

The following commands build Profile Large without test cases on **AN521** with
build type **MinSizeRel**, built by **Armclang**.

```bash

cd <TFM root dir>
mkdir build && cd build
cmake -DTFM_PLATFORM=arm/mps2/an521 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_PROFILE=profile_large \
      -DCMAKE_BUILD_TYPE=MinSizeRel \
      ../
cmake --build ./ -- install
```
The following commands build Profile Large with regression test cases on
**AN521** with build type **MinSizeRel**, built by **Armclang**.

```bash

cd <TFM root dir>
mkdir build && cd build
cmake -DTFM_PLATFORM=arm/mps2/an521 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_PROFILE=profile_large \
      -DCMAKE_BUILD_TYPE=MinSizeRel \
      -DTEST_S=ON -DTEST_NS=ON \
      ../
cmake --build ./ -- install
```
More details of building instructions and parameters can be found TF-M build
instruction guide [9]_.
