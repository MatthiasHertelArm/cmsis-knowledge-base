---
id: "tfm-nordic-nrf9161-building-tf-m-on-nrf9161"
type: "concept"
domain: "security"
title: "Nordic nRF9161: Building TF-M on nRF9161"
summary: "To build an S and NS application image for the nRF9161 run the following commands:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/nordic_nrf/nrf9161dk_nrf9161/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nordic_nrf/nrf9161dk_nrf9161/.html#building-tf-m-on-nrf9161"
license: "BSD-3-Clause"
mode: "V"
---

To build an S and NS application image for the nRF9161 run the
following commands:

```bash

cmake -S <TF-M base folder> -B build_spe \
        -DTFM_PLATFORM=nordic_nrf/nrf9161dk_nrf9161 \
        -DTFM_TOOLCHAIN_FILE=../toolchain_GNUARM.cmake \
cmake --build build_spe -- install

cmake -S <Application base folder> -B build_app \
        -DCONFIG_SPE_PATH<Absolute path to TF-M base folder>/build_spe/api_ns
        -DTFM_TOOLCHAIN_FILE=cmake/toolchain_ns_GNUARM.cmake
cmake --build
```

**Note:** Currently, applications can only be built using GCC (GNU ARM Embedded toolchain).


**Note:** For BL2 (MCUBoot) logging output to be available, the project needs to be built with Debug configuration (CMAKE_BUILD_TYPE=Debug).
