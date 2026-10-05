---
id: "alp-alif-dual-npu-vision-validate-inference-check-the-startup-test"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Validate live parallel inference: Check the startup test"
summary: "The application validates the inference path before it consumes camera frames. This separates model or neural processing unit (NPU) failures from camera and image signal processor (ISP) failures."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference/#check-the-startup-test"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application validates the inference path before it consumes camera frames. This separates model or neural processing unit (NPU) failures from camera and image signal processor (ISP) failures.

After reset, the display shows the bundled Grace Hopper image. The U55 model draws one green face box. The U85 result identifies an ImageNet class such as `ACADEMIC GOWN`.

The U4 log includes model preparation and isolated preflight messages similar to:

```output
dual-et: starting parallel worker threads
dual-et: SSD persons=1 candidates=...
dual-et: frame=0 CLASS=400 ACADEMIC GOWN confidence=...%
dual-et: isolated U55 done irqs=1/0
dual-et: isolated U85 done irqs=1/1
dual-et: startup self-test passed; switching to camera in 5 seconds
```

The exact inference times and memory addresses vary between builds.
