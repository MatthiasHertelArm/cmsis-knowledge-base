---
id: "alp-deploy-ml-model-to-npu-with-topo-overview-system-architecture"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Understand the architecture of the machine learning application: S"
summary: "The deployed application spans three processing domains on the i.MX 93:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview/#system-architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

The deployed application spans three processing domains on the i.MX 93:

- Cortex-A Linux host: runs Docker, Topo-deployed containers, the Flask web app, and the Linux `remoteproc` and `RPMsg` interfaces.
- Cortex-M33 firmware domain: runs the ExecuTorch runner firmware loaded by `remoteproc-runtime`.
- Ethos-U65 NPU: accelerates delegated neural network operators from the ExecuTorch MobileNetV2 program.

The high-level data flow is:

```output
Browser
  |
  v
Flask web application on Cortex-A Linux
  |
  | writes .pte file and input tensor to reserved memory
  | sends RUN over RPMsg
  v
Cortex-M33 ExecuTorch runner firmware
  |
  | loads the .pte program from reserved memory
  | delegates supported operators
  v
Ethos-U65 NPU
  |
  v
Cortex-M33 returns classification results over RPMsg
  |
  v
Browser displays ImageNet top-1 and top-5 results
```
