---
id: "alp-training-inference-pytorch-env-setup-1-environment-setup"
type: "concept"
domain: "edge-ai"
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors: Set up your environment: Environment setup"
summary: "To get started, complete the first three sections of Introduction to TinyML on Arm using PyTorch and ExecuTorch. This setup prepares your development environment and installs the required tools. Return here after running the ./examples/arm/run.sh script in the ExecuTorch repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/env-setup-1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/env-setup-1/#environment-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

To get started, complete the first three sections of [Introduction to TinyML on Arm using PyTorch and ExecuTorch](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/). This setup prepares your development environment and installs the required tools. Return here after running the `./examples/arm/run.sh` script in the ExecuTorch repository.

If you just completed the earlier Learning Path, your virtual environment should still be active. If not, activate it:

```console
source $HOME/executorch-venv/bin/activate
```
The prompt of your terminal now has `(executorch-venv)` as a prefix to indicate the virtual environment is active.

Install Python dependencies:

```console
pip install numpy pillow torch
```

You’re now ready to create the model.
