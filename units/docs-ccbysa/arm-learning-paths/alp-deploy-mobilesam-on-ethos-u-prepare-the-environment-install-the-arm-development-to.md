---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-install-the-arm-development-to"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Install the Arm development tools"
summary: "The Arm setup script installs the pinned GNU bare-metal toolchain, Ethos-U Vela compiler, and Corstone FVP used by the example. Read the End User License Agreements presented by the tooling before you accept them, then run:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#install-the-arm-development-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

**Note:**
Before you run the Arm setup command on macOS, install [Docker Desktop](https://learn.arm.com/install-guides/docker/docker-desktop/) and follow the [AVH FVPs on macOS install guide](https://learn.arm.com/install-guides/fvps-on-macos/). Add the FVPs-on-Mac `bin` directory to `PATH`. The wrapper runs the Linux Corstone-320 FVP in a container. Confirm that Docker is running and that `FVP_Corstone_SSE-320` resolves to the wrapper:

```bash
docker info >/dev/null
command -v FVP_Corstone_SSE-320
```


The Arm setup script installs the pinned GNU bare-metal toolchain, Ethos-U Vela compiler, and Corstone FVP used by the example. Read the End User License Agreements presented by the tooling before you accept them, then run:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```
