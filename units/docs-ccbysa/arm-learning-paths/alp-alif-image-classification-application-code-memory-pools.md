---
id: "alp-alif-image-classification-application-code-memory-pools"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: Memory pools"
summary: "The ExecuTorch runtime uses three memory pools, placed in SRAM using linker section attributes:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#memory-pools"
license: "CC-BY-SA-4.0"
mode: "V"
---

The ExecuTorch runtime uses three memory pools, placed in SRAM using linker section attributes:

```cpp
// SRAM0 (4 MB total)
__attribute__((section(".bss.at_sram0"), aligned(16)))
static uint8_t method_alloc_pool[1536 * 1024];       // 1.5 MB

__attribute__((section(".bss.at_sram0"), aligned(16)))
static uint8_t temp_alloc_pool[1536 * 1024];          // 1.5 MB

__attribute__((section(".bss.at_sram0"), aligned(16)))
static float input_float_buf[3 * 224 * 224];           // ~588 KB

// SRAM1 (4 MB total)
__attribute__((section(".bss.at_sram1"), aligned(16)))
static uint8_t planned_buffer_pool[4 * 1024 * 1024];  // 4 MB
```

The method allocator holds the loaded model graph. The temp allocator provides scratch memory for the Ethos-U backend (which needs approximately 1.44 MB). The planned buffer pool holds the intermediate tensors that ExecuTorch pre-plans at model load time.
