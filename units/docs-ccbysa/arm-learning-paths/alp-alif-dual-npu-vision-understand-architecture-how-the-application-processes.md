---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-processes"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application processes each frame"
summary: "The camera and display use different MIPI D-PHY instances so they can operate at the same time. The J16 MT9M114 camera uses D-PHY 0, while the MW405 display uses D-PHY 1."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-processes-each-frame"
license: "CC-BY-SA-4.0"
mode: "V"
---

The camera and display use different MIPI D-PHY instances so they can operate at the same time. The J16 MT9M114 camera uses D-PHY 0, while the MW405 display uses D-PHY 1.

For every live frame, the application performs the following steps:

1. The MT9M114 sends 1288 x 728 RAW10 data over MIPI CSI-2.
2. The hardware ISP crops and demosaics the image into a 192 x 192 planar RGB888 buffer.
3. Zephyr maintains five video buffers so capture continues while one frame is processed.
4. The coordinator creates a 120 x 160 grayscale SSD tensor and a 224 x 224 RGB MobileNetV2 tensor.
5. The coordinator releases both persistent worker threads through separate semaphores.
6. Each worker copies its input into its prepared ExecuTorch method and submits the delegated command stream.
7. The coordinator waits for both completion semaphores, records timing, and returns the captured buffer to the ISP queue.
8. The UI compositor draws a 480 x 352 RGB565 preview, face boxes, the classification result, and rolling timing values in the 480 x 800 framebuffer.

ExecuTorch program and method construction is serialized because that setup path contains shared runtime state. After setup, each worker retains an independent immutable `Method`, allocator set, and NPU backend. Only prepared model execution runs in parallel. Camera capture, preprocessing, result fusion, and display updates remain coordinated by the Cortex-M55.
