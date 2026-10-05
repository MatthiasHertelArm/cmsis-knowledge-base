---
id: "alp-deploy-ml-model-to-npu-with-topo-deploy-deploy-to-the-board"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Clone and deploy the application with Topo: Deploy to the board"
summary: "You can choose to deploy from the original Topo Project, or from the project you built from scratch. If you haven't already cloned the original project, clone it now:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy/#deploy-to-the-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can choose to deploy from the original Topo Project, or from the project you built from scratch. If you haven't already cloned the original project, clone it now:

```bash
topo clone https://github.com/Arm-Examples/topo-imx93-npu-deployment.git
```

Topo prompts for optional build cache image arguments. Accept the defaults unless you have your own cache images.

**Note:**
If you build without cache images, the first build can take a long time and requires about 25 GB of free disk space. The first build involves downloading and building ExecuTorch, the Arm GNU toolchain, MCUX SDK components, RPMsg-Lite, and the Cortex-M33 runner sources. Later builds are faster when Docker can reuse local cache layers or import the configured GHCR cache layers.


Then `cd` into the correct directory:

```bash
cd topo-imx93-npu-deployment
```

Or:

```bash
cd new-topo-npu-template
```

Deploy the project to your target:

```bash
topo deploy --target <user>@<target-ip>
```

During deployment, Topo builds the required images, transfers them to the target, starts the Cortex-M33 firmware through `remoteproc-runtime`, and starts the web application.

When deployment succeeds, the output includes a successful service startup. You can also check the deployed services:

```bash
topo ps --target <user>@<target-ip>
```

The output shows a process on both the Cortex-M33 and the Linux Host, and is similar to:

```output
Image                                   Status          Processing Domain   Address
topo-imx93-npu-deployment-cm33-runner   Up 50 minutes   imx-rproc
topo-imx93-npu-deployment-webapp        Up 50 minutes   Linux Host          imx93-scorpio.cambridge.arm.com:3001, [::]:3001%
```
