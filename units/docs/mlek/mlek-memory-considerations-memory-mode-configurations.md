---
id: "mlek-memory-considerations-memory-mode-configurations"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Memory mode configurations"
summary: "The preceding example outlines a typical configuration for Ethos-U55 NPU, and this corresponds to the default Vela memory mode setting. Evaluation kit supports all the Ethos-U NPU memory modes:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/memory_considerations.md#memory-mode-configurations"
license: "Apache-2.0"
mode: "V"
---

The preceding example outlines a typical configuration for *Ethos-U55* NPU, and this corresponds to the default
Vela memory mode setting.
Evaluation kit supports all the *Ethos-U* NPU memory modes:

| *Ethos™-U* NPU | Default Memory Mode | Other Memory Modes supported |
|----------------|---------------------|------------------------------|
| *Ethos™-U55*   | `Shared_Sram`       | `Sram_Only`                  |
| *Ethos™-U65*   | `Dedicated_Sram`    | `Sram_Only`, `Shared_Sram`   |
| *Ethos™-U85*   | `Dedicated_Sram`    | `Sram_Only`, `Shared_Sram`   |

For further information on the default settings, please refer to: [default_vela.ini](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../scripts/vela/default_vela.ini).
To use the other supported memory modes refer to [vela.ini](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/5.2.0/ethosu/config_files/Arm/vela.ini).
For *Ethos-U55* NPU, the system SRAM can also be used to store the neural network model along with the `tensor arena`.
Vela supports optimizing the model for this configuration with its `Sram_Only` memory mode.
Although the Vela settings for this configuration suggests that only AXI0 bus is used, when compiling the model
a warning is generated, for example:

```log
vela \
  --accelerator-config=ethos-u55-128 \
  --optimise Performance \
  --config scripts/vela/vela.ini
  --memory-mode=Sram_Only
  --system-config=Ethos_U55_High_End_Embedded
  ds_cnn_clustered_int8.tflite

Info: Changing const_mem_area from Sram to OnChipFlash. This will use the same characteristics as Sram.
```

This means that the  neural network model is always placed in the flash region. In this case, timing adapters for the
AXI buses are set the same values to mimic both bandwidth and latency characteristics of a SRAM memory device.
See [Ethos-U55 NPU timing adapter default configuration](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u55_high_end.cmake).

For script snippets, please refer to: [Memory constraints](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./memory_considerations.md#memory-constraints).

> **Note:**
>
> 1. The `Shared_Sram` memory mode represents the default configuration.
> 2. The `Dedicated_Sram` memory mode is only applicable for the Arm® *Ethos™-U65* and Arm® *Ethos™-U85*.
