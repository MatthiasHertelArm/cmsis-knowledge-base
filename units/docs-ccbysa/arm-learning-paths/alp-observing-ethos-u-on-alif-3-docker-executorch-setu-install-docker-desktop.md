---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-install-docker-desktop"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Set up a Docker development environment: Install Docker Desktop"
summary: "To train and export an MNIST model to ExecuTorch .pte format, you'll need to create a Docker environment."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#install-docker-desktop"
license: "CC-BY-SA-4.0"
mode: "V"
---

To train and export an MNIST model to ExecuTorch `.pte` format, you'll need to create a Docker environment.

**Note:**
If you're using the provided `.pte` file, skip the entire Docker setup section and proceed with [Prepare firmware artifacts](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/). Complete the Docker setup only if you want to train and export the model yourself.


Docker provides an isolated environment with all the build dependencies needed. 

Start by downloading and installing Docker Desktop. For more information, see the [Docker Desktop install guide](https://learn.arm.com/install-guides/docker/docker-desktop/).
