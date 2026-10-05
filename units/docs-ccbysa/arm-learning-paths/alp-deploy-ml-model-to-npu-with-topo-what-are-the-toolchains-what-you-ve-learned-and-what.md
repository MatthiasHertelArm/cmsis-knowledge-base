---
id: "alp-deploy-ml-model-to-npu-with-topo-what-are-the-toolchains-what-you-ve-learned-and-what"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Understand the toolchains used in the Topo Project: What you've le"
summary: "You now understand the major toolchains and runtime interfaces used by the Topo Project: ExecuTorch, the Cortex-M33 firmware runner, remoteproc-runtime, RPMsg, reserved memory, and the Flask web application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/what-are-the-toolchains.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/what-are-the-toolchains/#what-you-ve-learned-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You now understand the major toolchains and runtime interfaces used by the Topo Project: ExecuTorch, the Cortex-M33 firmware runner, remoteproc-runtime, RPMsg, reserved memory, and the Flask web application. You've also seen how the web application stages the `.pte` program and input data in reserved memory before sending inference commands to the Cortex-M33 firmware.

Next, you'll build the Topo Project from the base projects by adding the Compose services, build artifacts, Remoteproc Runtime metadata, and Topo parameters.
