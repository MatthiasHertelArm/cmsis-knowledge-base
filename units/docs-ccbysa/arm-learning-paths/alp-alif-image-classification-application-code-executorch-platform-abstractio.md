---
id: "alp-alif-image-classification-application-code-executorch-platform-abstractio"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: ExecuTorch Platform Abstraction Layer"
summary: "ExecuTorch requires several platform functions to be implemented. These are thin wrappers that route logging through SEGGER RTT and use the standard library's malloc/free for the small dynamic allocations that ExecuTorch's initialization needs:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#executorch-platform-abstraction-layer"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch requires several platform functions to be implemented. These are thin wrappers that route logging through SEGGER RTT and use the standard library's `malloc`/`free` for the small dynamic allocations that ExecuTorch's initialization needs:

```cpp
extern "C" {
    void et_pal_init(void) {}
    ET_NORETURN void et_pal_abort(void) { __BKPT(0); while(1) {} }
    void et_pal_emit_log_message(...) {
        SEGGER_RTT_printf(0, "[%c] %s\n", (char)level, message);
    }
    void* et_pal_allocate(size_t size) { return malloc(size); }
    void et_pal_free(void* ptr) { free(ptr); }
}
```
