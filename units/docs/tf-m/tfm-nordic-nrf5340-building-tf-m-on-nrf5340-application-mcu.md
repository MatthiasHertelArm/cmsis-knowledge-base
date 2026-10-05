---
id: "tfm-nordic-nrf5340-building-tf-m-on-nrf5340-application-mcu"
type: "concept"
domain: "security"
title: "Nordic nRF5340: Building TF-M on nRF5340 Application MCU"
summary: "To build an S and NS application image for the nRF5340 Application MCU run the following commands:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/nordic_nrf/nrf5340dk_nrf5340_cpuapp/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nordic_nrf/nrf5340dk_nrf5340_cpuapp/.html#building-tf-m-on-nrf5340-application-mcu"
license: "BSD-3-Clause"
mode: "V"
---

To build an S and NS application image for the nRF5340 Application MCU run the
following commands:


```bash

cmake -S <TF-M base folder> -B build_spe \
        -DTFM_PLATFORM=nordic_nrf/nrf5340dk_nrf5340_cpuapp \
        -DTFM_TOOLCHAIN_FILE=../toolchain_GNUARM.cmake \
cmake --build build_spe -- install

cmake -S <Application base folder> -B build_app \
        -DCONFIG_SPE_PATH<Absolute path to TF-M base folder>/build_spe/api_ns
        -DTFM_TOOLCHAIN_FILE=cmake/toolchain_ns_GNUARM.cmake
cmake --build
```

**Note:** Currently, applications can only be built using GCC (GNU ARM Embedded toolchain).


**Note:** BL2 (MCUBoot) logging output to be available, the project needs to be built with Debug configuration (CMAKE_BUILD_TYPE=Debug).
