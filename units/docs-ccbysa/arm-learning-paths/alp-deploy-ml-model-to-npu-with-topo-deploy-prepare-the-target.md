---
id: "alp-deploy-ml-model-to-npu-with-topo-deploy-prepare-the-target"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Clone and deploy the application with Topo: Prepare the target"
summary: "Before deploying the Topo Project, confirm that the FRDM i.MX 93 board is reachable from your host and that it's ready for deployment:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy/#prepare-the-target"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before deploying the Topo Project, confirm that the FRDM i.MX 93 board is reachable from your host and that it's ready for deployment:

```bash
topo health --target <user>@<target-ip>
```
Replace `<target-ip>` with the IP address or hostname of your board.

Resolve any errors before continuing.

The target section includes successful checks similar to:

```output
Host
----
Topo: ✅ (topo)
SSH: ✅ (ssh)
Curl: ✅ (curl)
Container Engine: ✅ (docker)

Target
------
Destination: ssh://<target-ip>
Connectivity: ✅
Container Engine: ✅ (docker)
Remoteproc Runtime: ✅ (remoteproc-runtime)
Remoteproc Shim: ✅ (containerd-shim-remoteproc-v1)
Hardware Info: ✅ (lscpu)
Subsystem Driver (remoteproc): ✅ (imx-rproc)
```

**Note:**
If `remoteproc-runtime` is missing, install it with Topo:

```bash
topo install remoteproc-runtime --target <user>@<target-ip>
```

Run the health check again:

```bash
topo health --target <user>@<target-ip>
```
