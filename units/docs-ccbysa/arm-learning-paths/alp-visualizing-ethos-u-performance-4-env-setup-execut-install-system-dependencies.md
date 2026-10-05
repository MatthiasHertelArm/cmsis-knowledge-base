---
id: "alp-visualizing-ethos-u-performance-4-env-setup-execut-install-system-dependencies"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Set up your ExecuTorch environment: Install system dependencies"
summary: "Run the following commands to install the dependencies:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/4-env-setup-execut.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/4-env-setup-execut/#install-system-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

**Note:**
Make sure Python 3 is installed. It comes pre-installed on most versions of Ubuntu.


These instructions have been tested on:

- Ubuntu 22.04 and 24.04
- Windows Subsystem for Linux (WSL)

Run the following commands to install the dependencies:

```bash
sudo apt update
sudo apt install python-is-python3 python3-dev python3-venv gcc g++ make -y
```
