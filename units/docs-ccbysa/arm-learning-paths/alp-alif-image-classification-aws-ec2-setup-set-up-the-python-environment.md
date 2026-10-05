---
id: "alp-alif-image-classification-aws-ec2-setup-set-up-the-python-environment"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Set up the Python environment"
summary: "Create an isolated Python environment and install PyTorch:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#set-up-the-python-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create an isolated Python environment and install PyTorch:

```bash
python3 -m venv ~/venv_executorch
source ~/venv_executorch/bin/activate

pip install --upgrade pip setuptools wheel ninja cmake
pip install pyyaml
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pillow
```

This instance has no GPU, so the install uses CPU-only PyTorch. PyTorch is only needed for model export and ahead-of-time compilation. The actual inference runs on the microcontroller.

Verify the installation:

```bash
python - <<'PY'
import torch, torchvision
print(torch.__version__, torchvision.__version__)
PY
```

The output is similar to:

```output
2.10.0+cpu 0.25.0+cpu
```
