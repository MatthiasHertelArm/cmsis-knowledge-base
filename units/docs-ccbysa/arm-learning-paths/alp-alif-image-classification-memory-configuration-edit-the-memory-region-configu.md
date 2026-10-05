---
id: "alp-alif-image-classification-memory-configuration-edit-the-memory-region-configu"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Configure memory layout and flash settings: Edit the memory region config"
summary: "Open device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/app_mem_regions.h."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration/#edit-the-memory-region-configuration"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open `device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/app_mem_regions.h`.

Change the following values from their defaults:

| Define | Default value | New value | Purpose |
|--------|--------------|-----------|---------|
| `APP_MRAM_HE_BASE` | `0x80000000` | `0x80580000` | Move HE core out of the way |
| `APP_MRAM_HE_SIZE` | `0x00200000` | `0x00000000` | Give HE core zero MRAM |
| `APP_MRAM_HP_BASE` | `0x80200000` | `0x80000000` | HP core starts at MRAM base |
| `APP_MRAM_HP_SIZE` | `0x00200000` | `0x00580000` | HP core gets full 5.5 MB |
| `APP_HP_STACK_SIZE` | `0x00002000` | `0x00004000` | 16 KB stack (doubled) |
| `APP_HP_HEAP_SIZE` | `0x00004000` | `0x00010000` | 64 KB heap (quadrupled) |

The default template splits MRAM 2 MB / 2 MB between the two cores. Since you're only using the HP core, you give it the entire 5.5 MB of available MRAM. The increased stack and heap accommodate ExecuTorch's initialization code, which uses more stack depth and a few small dynamic allocations.
