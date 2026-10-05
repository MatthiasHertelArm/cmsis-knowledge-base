---
id: "ethu-vela-compare-ethos-u-configurations"
type: "concept"
domain: "edge-ai"
title: "Vela: Compare Ethos-U configurations"
summary: "Before selecting a device, use the Ethos-U reference systems in the generic Arm/vela.ini file for an initial comparison. They provide example system and memory configurations for estimating performance and memory use, but do not describe a specific production device."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md#compare-ethos-u-configurations"
license: "Apache-2.0"
mode: "V"
---

Before selecting a device, use the Ethos-U reference systems in the generic
`Arm/vela.ini` file for an initial comparison. They provide example
system and memory configurations for estimating performance and memory use, but
do not describe a specific production device. After selecting a device, repeat
the comparison with its device-specific `vela.ini` file.

Use the same ML model to test each accelerator, system configuration, and memory
mode.

> [!Tip]
> Keep the Vela version and other compiler options unchanged. Check that the same
> operations run on the NPU, and use a separate output directory for every build.

The following example comparison uses the
[`ad_large_int8.tflite` MicroNet Large INT8 anomaly-detection model](https://github.com/ARM-software/ML-zoo/blob/master/models/anomaly_detection/micronet_large/tflite_int8/ad_large_int8.tflite)
from the [Arm ML Zoo](https://github.com/ARM-software/ML-zoo) and Vela 5.1.0.
**Other memory** is `OffChipFlash` for the Ethos-U55 system and `Dram` for the
Ethos-U85 system.

To optimize for memory size, compile with `--optimise Size`:

| Accelerator | System configuration | Memory mode | SRAM | Other memory | Estimated time |
|---|---|---|---:|---:|---:|
| `ethos-u55-128` | `Ethos_U55_Deep_Embedded` | `Shared_Sram` | 136.00 KiB | 425.36 KiB | 27.816 ms |
| `ethos-u85-256` | `Ethos_U85_SYS_DRAM_High` | `Shared_Sram` | 136.00 KiB | 419.02 KiB | 1.158 ms |

To optimize for performance, compile with `--optimise Performance`:

| Accelerator | System configuration | Memory mode | SRAM | Other memory | Estimated time |
|---|---|---|---:|---:|---:|
| `ethos-u55-128` | `Ethos_U55_Deep_Embedded` | `Shared_Sram` | 390.61 KiB | 425.52 KiB | 5.806 ms |
| `ethos-u85-256` | `Ethos_U85_SYS_DRAM_High` | `Shared_Sram` | 436.77 KiB | 419.11 KiB | 0.458 ms |
