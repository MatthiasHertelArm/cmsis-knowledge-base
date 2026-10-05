---
id: "alp-alif-image-classification-memory-configuration-what-you-ve-learned-and-what-s"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Configure memory layout and flash settings: What you've learned and what'"
summary: "You've reconfigured the memory regions to allocate the full 5.5 MB of MRAM to the HP core, modified the linker script to support GOT relocation and SRAM memory pools, and configured the Security Toolkit JSON file to boot …"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration/#what-you-ve-learned-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've reconfigured the memory regions to allocate the full 5.5 MB of MRAM to the HP core, modified the linker script to support GOT relocation and SRAM memory pools, and configured the Security Toolkit JSON file to boot the application from the correct MRAM address.

Next, you'll prepare a test image for classification by converting it to the format the model expects.
