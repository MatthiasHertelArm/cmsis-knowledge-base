---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-understand-the-memory-configur"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Understand the memory configuration"
summary: "The Cortex-M33 has 128KB of ITCM (code) and 108KB of DTCM (data). The firmware also uses reserved DDR regions for the model and NPU working memory. The key settings are defined in CMakeLists.txt:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#understand-the-memory-configuration"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Cortex-M33 has 128KB of ITCM (code) and 108KB of DTCM (data). The firmware also uses reserved DDR regions for the model and NPU working memory. The key settings are defined in `CMakeLists.txt`:

```cmake
target_compile_definitions(${MCUX_SDK_PROJECT_NAME} PRIVATE
  ET_ARM_BAREMETAL_METHOD_ALLOCATOR_POOL_SIZE=0x6000      # 24KB method allocator
  ET_ARM_BAREMETAL_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE=0x200000  # 2MB scratch allocator
  ET_MODEL_PTE_ADDR=0xC0000000  # DDR address where U-Boot loads the .pte model
)
```

| Setting | Value | Description |
|---------|-------|-------------|
| Method allocator | 24KB (`0x6000`) | Method metadata and small model activations |
| Scratch allocator | 2MB (`0x200000`) | NPU scratch buffer (MobileNet V2 needs approximately 1.5MB) |
| Model address | `0xC0000000` | Start of the 4MB reserved DDR region |

**Note:**
The i.MX93 device tree reserves two DDR regions: `model@c0000000` (4MB for the `.pte` model) and `ethosu_region@A8000000` (128MB for NPU working memory). The NPU scratch buffer is placed at `0xA8000000` and planned buffers for large models at `0xA8200000`, both inside the 128MB ethosu_region. The Ethos-U65 accesses memory via the AXI bus and cannot reach the CM33's tightly-coupled DTCM, so all NPU buffers must be in DDR.
