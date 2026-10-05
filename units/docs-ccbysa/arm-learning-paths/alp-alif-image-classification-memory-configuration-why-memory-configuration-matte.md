---
id: "alp-alif-image-classification-memory-configuration-why-memory-configuration-matte"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Configure memory layout and flash settings: Why memory configuration matt"
summary: "The default Alif VS Code template divides memory equally between the two Cortex-M55 cores and allocates modest stack/heap sizes suitable for simple examples like Blinky. A MobileNetV2 model with ExecuTorch needs significantly more:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration/#why-memory-configuration-matters"
license: "CC-BY-SA-4.0"
mode: "V"
---

The default Alif VS Code template divides memory equally between the two Cortex-M55 cores and allocates modest stack/heap sizes suitable for simple examples like Blinky. A MobileNetV2 model with ExecuTorch needs significantly more:

- The embedded model is approximately 3.7 MB (stored in MRAM/flash).
- The ExecuTorch runtime, operator libraries, and application code add another 800 KB of code.
- Inference requires approximately 7.6 MB of SRAM for memory pools and intermediate tensors.

You need to reconfigure the MRAM allocation, stack/heap sizes, and linker script to fit this workload.
