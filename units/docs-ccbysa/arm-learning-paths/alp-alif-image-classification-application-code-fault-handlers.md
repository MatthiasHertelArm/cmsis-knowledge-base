---
id: "alp-alif-image-classification-application-code-fault-handlers"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: Fault handlers"
summary: "The fault handlers (HardFault, MemManage, BusFault) print the stacked program counter and link register to SEGGER RTT when a crash occurs."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#fault-handlers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The fault handlers (HardFault, MemManage, BusFault) print the stacked program counter and link register to SEGGER RTT when a crash occurs. This is essential for debugging on bare-metal systems where you don't have a console or operating system catching exceptions for you.

```cpp
extern "C" void Fault_Print(uint32_t *frame, uint32_t fault_type) {
    const char* names[] = {"HARDFAULT", "MEMMANAGE", "BUSFAULT"};
    SEGGER_RTT_printf(0, "*** %s ***\n", names[fault_type]);
    // ... prints CFSR, HFSR, PC, LR, R0-R3
    while (1) { __WFI(); }
}
```

If you ever see a fault message in RTT Viewer, the PC value tells you exactly which instruction caused the crash. You can cross-reference it with the `.map` file or use `arm-none-eabi-addr2line` to find the source line.
