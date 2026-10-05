---
id: "alp-analyze-ethos-u-models-with-mlia-2-install-and-discover-check-your-environment"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Install MLIA and discover capabilities: Check your environment"
summary: "Use Ubuntu 22.04 LTS or another compatible Linux environment with Python 3.10 or later."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover/#check-your-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Ubuntu 22.04 LTS or another compatible Linux environment with Python 3.10 or later.

Check that Git Large File Storage (LFS) is installed:

```bash
git lfs version
```

If the command fails, install Git LFS and the Python development package:

```bash
sudo apt update
sudo apt install -y git-lfs python3.10-dev
```
