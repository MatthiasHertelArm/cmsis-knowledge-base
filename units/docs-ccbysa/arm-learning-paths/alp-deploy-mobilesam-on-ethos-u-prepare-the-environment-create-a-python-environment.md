---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-create-a-python-environment"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Create a Python environment"
summary: "Create and activate a Python 3.12 virtual environment:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#create-a-python-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create and activate a Python 3.12 virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the current ExecuTorch checkout with its Ethos-U dependencies:

```bash
./install_executorch.sh --optional-dependency ethos_u
```

Using the checkout's installer keeps the Python package aligned with the example source.
