---
id: "alp-deploy-ml-model-to-npu-with-topo"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo"
summary: "Use Topo to build and deploy a Cortex-A web application that sends MobileNetV2 image classification requests to Cortex-M33 firmware accelerated by the Ethos-U65 NPU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Topo to build and deploy a Cortex-A web application that sends MobileNetV2 image classification requests to Cortex-M33 firmware accelerated by the Ethos-U65 NPU.

**Who is this for:** This is an introductory topic for embedded/edge software developers who want to deploy machine learning workloads to heterogeneous Arm-based Linux targets using Topo, including leveraging Arm Ethos-U NPUs.

**Learning objectives:**

- Explain how Topo deploys an application that spans Cortex-A, Cortex-M, and Ethos-U
- Deploy the topo-imx93-npu-deployment Topo Project, which operates across Cortex-A, Cortex-M, and Ethos-U, to perform image classification using an ExecuTorch MobileNetV2 model
- Describe how the project is bootstrapped from Compose services, Remoteproc Runtime metadata, and Topo parameters and follow this process yourself
- Understand how to take similar projects and create Topo Projects, including using Agent Skills

**Prerequisites:**

- A host machine (x86 or Arm) with Linux, macOS, or Windows
- An NXP FRDM i.MX 93 target board with Linux setup, accessible over SSH with root access. To do this, see [Use Linux on the NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/).
- Docker installed on the host and target. For installation steps, see [Install Docker](https://learn.arm.com/install-guides/docker/).
- At least 25 GB of free disk space on the host if you're building without cache images.
- The Device Tree Compiler (`dtc`) installed on the host.
- lscpu installed on the target (pre-installed on most Linux distributions)
- Topo installed on the host. For installation steps, see [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).
- Basic familiarity with containers, SSH, and CLI tools
- (Optional) Access to an agent, such as Codex or Claude Code

**Steps:**

1. Understand the architecture of the machine learning application
2. Understand the toolchains used in the Topo Project
3. Build the Topo Project from scratch
4. Clone and deploy the application with Topo

Time: about 60 minutes.
