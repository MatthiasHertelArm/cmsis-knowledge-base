---
id: "alp-alif-image-classification-build-flash-verify-troubleshooting"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: Troubleshooting"
summary: "If you don't see the expected output, check these common issues:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#troubleshooting"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you don't see the expected output, check these common issues:

- **RTT Viewer shows nothing**: The code starts running as soon as it's flashed. If you connect RTT Viewer too late, you might miss the output. Press the board's reset button after connecting RTT Viewer.
- **"ethosu_init failed"**: The NPU base address is wrong. Verify the code uses `NPU_HG_BASE` (0x49042000), not `NPU_HP_BASE`.
- **BusFault at a low address**: The GOT sections are missing from the linker script. Verify that `*(.got)` and `*(.got.plt)` are in the `.data.at_dtcm` section.
- **"Missing operator: cortex_m::quantize_per_tensor.out"**: `libcortex_m_ops_lib` isn't in the `--whole-archive` block. Check `mv2_runner.cproject.yml`.
- **"Memory allocation failed: 1505280B requested"**: The temp allocator pool is too small. The Ethos-U85 scratch buffer needs approximately 1.44 MB. Verify `TEMP_ALLOC_POOL_SIZE` is at least `1536 * 1024`.
- **MRAM overflow linker error**: Verify `APP_MRAM_HP_SIZE` is set to `0x00580000` in `app_mem_regions.h`.
- **"Vela bin ptr not aligned to 16 bytes"**: The model array in the header needs `__attribute__((aligned(16)))`.

This completes the setup and deployment of MobileNetV2 image classification on the Ethos-U85 NPU using ExecuTorch. The model went from PyTorch, through the Vela compiler, into a `.pte` flatbuffer embedded in firmware, and produced a correct classification result on real hardware.
