---
id: "alp-alif-dual-npu-vision-validate-inference-what-you-ve-accomplished"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Validate live parallel inference: What you've accomplished"
summary: "You've now built, flashed, and validated a Zephyr application that drives two Ethos-U NPUs with separate persistent worker threads on one Cortex-M55. This design runs both ML workloads without adding a second microcontroller unit and its associated system power overhead."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference/#what-you-ve-accomplished"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've now built, flashed, and validated a Zephyr application that drives
two Ethos-U NPUs with separate persistent worker threads on one Cortex-M55.
This design runs both ML workloads without adding a second microcontroller unit and its
associated system power overhead.

You can now use the workflow to run ExecuTorch models for your own use cases concurrently on separate Ethos-U NPUs under Zephyr.
