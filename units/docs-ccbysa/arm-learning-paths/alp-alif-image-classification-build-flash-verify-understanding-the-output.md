---
id: "alp-alif-image-classification-build-flash-verify-understanding-the-output"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: Understanding the output"
summary: "Each line tells you something about what's happening:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#understanding-the-output"
license: "CC-BY-SA-4.0"
mode: "V"
---

Each line tells you something about what's happening:

- **"Ethos-U85 NPU initialized (polling mode)"**: The NPU driver connected to the correct peripheral (NPU_HG). "Polling mode" means NPU completion is detected by polling the status register rather than using an interrupt.
- **"Model bytes: 3835552"**: The embedded `.pte` model is 3.7 MB.
- **"Method 'forward': 1 inputs, 1 outputs, 1 planned buffers"**: The model has a single input tensor and single output tensor. ExecuTorch pre-plans one intermediate buffer.
- **"sem_take #1 count=1"** and **"sem_take #2 count=0"**: The NPU semaphore was signaled. Two semaphore takes means the NPU processed the entire model as a single command stream.
- **"Top-1 class: 283"**: ImageNet class 283 is "Persian cat". The 1000-element output vector was scanned for the highest score.
