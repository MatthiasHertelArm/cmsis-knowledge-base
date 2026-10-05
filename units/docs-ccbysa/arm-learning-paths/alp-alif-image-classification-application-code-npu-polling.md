---
id: "alp-alif-image-classification-application-code-npu-polling"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: NPU polling"
summary: "The NPU_HG peripheral has no interrupt line routed to the M55_HP core's NVIC. The code works around this by overriding the ethosu_semaphore_take() function to poll the NPU status register directly:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#npu-polling"
license: "CC-BY-SA-4.0"
mode: "V"
---

The NPU_HG peripheral has no interrupt line routed to the M55_HP core's NVIC. The code works around this by overriding the `ethosu_semaphore_take()` function to poll the NPU status register directly:

```cpp
extern "C" int ethosu_semaphore_take(void *sem, uint64_t timeout) {
    struct ethosu_sem_t *s = (struct ethosu_sem_t *)sem;
    while (s->count == 0) {
        if (NPU_HG_STATUS & 0x2) {        // bit 1 = irq_raised
            ethosu_irq_handler(&ethos_drv);
        }
        __NOP();
    }
    s->count--;
    return 0;
}
```

The SysTick handler also polls this status register at 25 Hz as a backup path, and toggles the red LED so you can see the board is alive during inference.
