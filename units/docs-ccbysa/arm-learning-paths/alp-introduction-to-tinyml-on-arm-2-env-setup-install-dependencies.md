---
id: "alp-introduction-to-tinyml-on-arm-2-env-setup-install-dependencies"
type: "concept"
domain: "edge-ai"
title: "Introduction to TinyML on Arm using PyTorch and ExecuTorch: Install ExecuTorch: Install dependencies"
summary: "These instructions have been tested on Ubuntu 22.04, 24.04, and on Windows Subsystem for Linux (WSL)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup/#install-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

These instructions have been tested on Ubuntu 22.04, 24.04, and on Windows Subsystem for Linux (WSL).

Python 3 is required and comes installed with Ubuntu, but some additional packages are needed:

```bash
sudo apt update
sudo apt install python-is-python3 python3-dev python3-venv gcc g++ make -y
```
