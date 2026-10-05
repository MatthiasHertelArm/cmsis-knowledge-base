---
id: "ethu-arm-cmsis-ethos-u-building-the-driver-using-cmake"
type: "concept"
domain: "edge-ai"
title: "Arm CMSIS Ethos-U: Building the Driver using CMake"
summary: "Projects that build a single-variant driver directly with CMake select the target through ETHOSU_TARGET_NPU_CONFIG, for example ethos-u55-128."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/README.md#building-the-driver-using-cmake"
license: "Apache-2.0"
mode: "V"
---

Projects that build a single-variant driver directly with CMake select the target
through `ETHOSU_TARGET_NPU_CONFIG`, for example `ethos-u55-128`.

The driver is intended to be cross-compiled for the Arm Cortex-M processor used by the target system. Configure the toolchain, processor, and Ethos-U configuration before building:

```bash
cmake -S source -B build \
  -DCMAKE_TOOLCHAIN_FILE=<toolchain> \
  -DCMAKE_SYSTEM_PROCESSOR=cortex-m<nr><features> \
  -DETHOSU_TARGET_NPU_CONFIG=ethos-u<nr>-<macs>
cmake --build build
```

For a multi-variant build, set `ETHOSU_MULTI_VARIANT=ON` instead of selecting
`ETHOSU_TARGET_NPU_CONFIG`. The build includes support for all three NPU
families. Applications use `ethosu_init_ex()` and `ethosu_reserve_driver_ex()`
to select the product and MAC configuration at run time.

When using a toolchain from the Ethos-U core platform, set `TARGET_CPU` instead of `CMAKE_SYSTEM_PROCESSOR`. See the [driver README](https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/./source/README.md) for API examples and integration requirements.
