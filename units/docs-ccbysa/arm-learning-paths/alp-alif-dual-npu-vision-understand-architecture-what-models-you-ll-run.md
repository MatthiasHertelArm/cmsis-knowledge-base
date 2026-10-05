---
id: "alp-alif-dual-npu-vision-understand-architecture-what-models-you-ll-run"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: What models you'll run"
summary: "The Alif Ensemble E8 combines two Arm Cortex-M55 cores with two different Ethos-U NPUs. You'll run the workloads on the high-performance Cortex-M55 core. One model is assigned to each neural processing unit (NPU):"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#what-models-you-ll-run"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Alif Ensemble E8 combines two Arm Cortex-M55 cores with two different Ethos-U NPUs. You'll run the workloads on the high-performance Cortex-M55 core. One model is assigned to each neural processing unit (NPU):

| Workload | NPU | Input tensor | Output |
| --- | --- | --- | --- |
| SSD-Slim face detection | Ethos-U55-256 | 1 x 1 x 120 x 160 int8 grayscale | 1,118 box regressions and face and background logits |
| MobileNetV2 image classification | Ethos-U85-256 | 1 x 3 x 224 x 224 int8 RGB | 1,000 ImageNet class scores |
