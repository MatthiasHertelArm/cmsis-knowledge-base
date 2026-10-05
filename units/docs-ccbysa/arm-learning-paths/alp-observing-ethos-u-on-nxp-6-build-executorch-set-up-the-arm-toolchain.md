---
id: "alp-observing-ethos-u-on-nxp-6-build-executorch-set-up-the-arm-toolchain"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build and install ExecuTorch: Set up the Arm toolchain"
summary: "Initialize the Arm-specific environment and accept the EULA:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/6-build-executorch.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/6-build-executorch/#set-up-the-arm-toolchain"
license: "CC-BY-SA-4.0"
mode: "V"
---

Initialize the Arm-specific environment and accept the EULA:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

Source the environment variables:

```bash
source ./examples/arm/ethos-u-scratch/setup_path.sh
```

**Troubleshooting:**
If `install_executorch.sh` fails, install the dependencies manually:

```bash
pip install torch torchvision
pip install --no-build-isolation .
pip install --no-build-isolation third-party/ao
```

If `buck2` hangs during the build:

```bash
ps aux | grep buck
pkill -f buck
```

To clean the build environment and start fresh:

```bash
./install_executorch.sh --clean
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```
