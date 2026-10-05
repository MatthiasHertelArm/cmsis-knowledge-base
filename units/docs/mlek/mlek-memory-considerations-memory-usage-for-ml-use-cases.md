---
id: "mlek-memory-considerations-memory-usage-for-ml-use-cases"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Memory usage for ML use-cases"
summary: "The following numbers have been obtained from Vela for the Shared_Sram memory mode, along with the SRAM and flash memory requirements for the different use-cases of the evaluation kit."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/memory_considerations.md#memory-usage-for-ml-use-cases"
license: "Apache-2.0"
mode: "V"
---

The following numbers have been obtained from Vela for the `Shared_Sram` memory mode, along with the SRAM and flash
memory requirements for the different use-cases of the evaluation kit.

> **Note:** The SRAM usage does not include memory used by the ML framework and must be topped up as explained
> under [Total SRAM used](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./memory_considerations.md#total-sram-used).

- [Keyword spotting model](https://github.com/ARM-software/ML-zoo/tree/68b5fbc77ed28e67b2efc915997ea4477c1d9d5b//models/keyword_spotting/ds_cnn_large/tflite_clustered_int8)
  requires
  - 70.7 KiB of SRAM
  - 430.7 KiB of flash memory.

- [Image classification model](https://github.com/ARM-software/ML-zoo/tree/e0aa361b03c738047b9147d1a50e3f2dcb13dbcb/models/image_classification/mobilenet_v2_1.0_224/tflite_uint8)
  requires
  - 638.6 KiB of SRAM
  - 3.1 MB of flash memory.

- [Automated speech recognition](https://github.com/ARM-software/ML-zoo/tree/1a92aa08c0de49a7304e0a7f3f59df6f4fd33ac8/models/speech_recognition/wav2letter/tflite_pruned_int8)
  requires
  - 655.16 KiB of SRAM
  - 13.42 MB of flash memory.
