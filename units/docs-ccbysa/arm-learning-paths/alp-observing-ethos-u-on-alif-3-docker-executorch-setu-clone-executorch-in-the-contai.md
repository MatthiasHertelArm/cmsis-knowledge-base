---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-clone-executorch-in-the-contai"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Clone ExecuTorch in the container"
summary: "Inside the Docker container, clone ExecuTorch v1.0.0:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#clone-executorch-in-the-container"
license: "CC-BY-SA-4.0"
mode: "V"
---

Inside the Docker container, clone ExecuTorch v1.0.0:

```bash
cd /home/developer
# Clone ExecuTorch
git clone https://github.com/pytorch/executorch.git
cd executorch
# Checkout stable release
git checkout v1.0.0
# Initialize submodules
git submodule sync
git submodule update --init --recursive
```

**Note:**
Submodule initialization might take 5-10 minutes depending on your connection.


Set the environment variable `ET_HOME`:

```bash
export ET_HOME=/home/developer/executorch
echo 'export ET_HOME=/home/developer/executorch' >> ~/.bashrc
```
