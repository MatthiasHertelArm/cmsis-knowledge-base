---
id: "alp-introduction-to-tinyml-on-arm-2-env-setup-create-a-virtual-environment"
type: "concept"
domain: "edge-ai"
title: "Introduction to TinyML on Arm using PyTorch and ExecuTorch: Install ExecuTorch: Create a virtual environment"
summary: "Create a Python virtual environment using python venv:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup/#create-a-virtual-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a Python virtual environment using `python venv`:

```console
python3 -m venv $HOME/executorch-venv
source $HOME/executorch-venv/bin/activate
```
The prompt of your terminal now has `(executorch)` as a prefix to indicate the virtual environment is active.
