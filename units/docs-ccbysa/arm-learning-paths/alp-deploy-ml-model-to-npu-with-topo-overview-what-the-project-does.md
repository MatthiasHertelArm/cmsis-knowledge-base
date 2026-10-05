---
id: "alp-deploy-ml-model-to-npu-with-topo-overview-what-the-project-does"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Understand the architecture of the machine learning application: W"
summary: "Deploying the Topo Project starts two runtime services on the target:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview/#what-the-project-does"
license: "CC-BY-SA-4.0"
mode: "V"
---

Deploying the Topo Project starts two runtime services on the target:

- `webapp`: Web application running on the Cortex-A Linux host. It receives an image input from the user and outputs the results of the ML image classification.
- `cm33-runner`: Cortex-M33 firmware that receives the image tensor from the web application, runs the compiled MobileNetV2 ExecuTorch `.pte` program, delegates supported operators to the Ethos-U65 NPU, and runs non-delegated operators on the Cortex-M33 CPU.
