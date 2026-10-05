---
id: "alp-alif-image-classification-application-code-npu-initialization"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: NPU initialization"
summary: "The Alif E8 has three NPUs, and you need to use the right one. The model was compiled for Ethos-U85, which is the NPU_HG (High-Grade) peripheral at base address 0x49042000:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#npu-initialization"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Alif E8 has three NPUs, and you need to use the right one. The model was compiled for Ethos-U85, which is the NPU_HG (High-Grade) peripheral at base address `0x49042000`:

```cpp
static int npu_init(void) {
    if (ethosu_init(&ethos_drv,
                    (void*)NPU_HG_BASE,   // Ethos-U85
                    0, 0,                  // no fast memory
                    1, 1))                 // secure, privileged
    {
        SEGGER_RTT_printf(0, "ERROR: ethosu_init failed\n");
        return -1;
    }
    return 0;
}
```

**Note:**
NPU_HP (at a different base address) is an Ethos-U55, not the U85. Using the wrong base address results in a product mismatch error from the NPU driver.
