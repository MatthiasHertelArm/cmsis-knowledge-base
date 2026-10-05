---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-maintains"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application maintains cache and address visibili"
summary: "The Cortex-M55 data cache isn't coherent with the camera, display controller, or either NPU. The application follows two rules:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-maintains-cache-and-address-visibility"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Cortex-M55 data cache isn't coherent with the camera, display controller, or either NPU. The application follows two rules:

- Clean or flush CPU-written input tensors and framebuffer pixels before a device reads them.
- Invalidate captured frames and NPU-written output tensors before the CPU reads them.

The U55 and U85 also require system-visible addresses. The platform layer translates CPU-local addresses to their Alif global aliases and selects the correct AXI memory attributes for MRAM, HP DTCM, SRAM0, and SRAM1. Incorrect address translation or memory attributes can produce an NPU bus error even when the CPU can read the same bytes.
