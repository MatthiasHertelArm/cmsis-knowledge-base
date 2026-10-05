---
id: "alp-introduction-to-tinyml-on-arm-2-env-setup-install-executorch"
type: "concept"
domain: "edge-ai"
title: "Introduction to TinyML on Arm using PyTorch and ExecuTorch: Install ExecuTorch: Install ExecuTorch"
summary: "From within the Python virtual environment, run the commands below to download the ExecuTorch repository and install the required packages:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/2-env-setup/#install-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

From within the Python virtual environment, run the commands below to download the ExecuTorch repository and install the required packages:

``` bash
cd $HOME
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout release/1.0
```

Run the commands below to set up the ExecuTorch internal dependencies:

```bash
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```

**Note:**
If you run into an issue of `buck` running in a stale environment, reset it by running the following instructions:

```bash
ps aux | grep buck
pkill -f buck
```


After running the commands, `executorch` should be listed upon running `pip list`:

```bash
pip list | grep executorch
```

```output
executorch             1.1.0a0+1883128
```
