---
id: "alp-deploy-ml-model-to-npu-with-topo-overview-what-you-ve-learned-and-what-s"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Understand the architecture of the machine learning application: W"
summary: "You now understand that the Topo Project deploys a Cortex-A web application, a Cortex-M33 ExecuTorch runner, and Ethos-U65 NPU acceleration as one heterogeneous application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview/#what-you-ve-learned-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You now understand that the Topo Project deploys a Cortex-A web application, a Cortex-M33 ExecuTorch runner, and Ethos-U65 NPU acceleration as one heterogeneous application. You've also seen how inference uses reserved memory for the `.pte` program and input tensor, with `RPMsg` carrying commands and results between Cortex-A and Cortex-M33.

Next, you'll review the toolchains and runtime interfaces used by the Topo Project.
